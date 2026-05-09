import pytz
import streamlit as st
import pandas as pd
import os
import time
from datetime import datetime, timedelta, timezone

# =====================================================
# 基本設定
# =====================================================
st.set_page_config(
    page_title="CCL-Soccer 足球賽事管理系統",
    page_icon="⚽",
    layout="wide"
)

DEFAULT_DB = "ccl-soccer.csv"
CHAT_DB = "ccl_chat_log.csv"
REQ_FILE = "pending_requests.csv"

COLUMNS = [
    "日期",
    "賽事項目",
    "類型",
    "金額",
    "盈虧金額",
    "結算總分"
]

CHAT_COLUMNS = [
    "時間",
    "暱稱",
    "內容",
    "標籤"
]

TW_TZ = pytz.timezone('Asia/Taipei')

# =====================================================
# 工具函式
# =====================================================
def get_now_time():
    return datetime.now(TW_TZ).strftime("%Y-%m-%d %H:%M:%S")


def ensure_files():
    if not os.path.exists(DEFAULT_DB):
        pd.DataFrame(columns=COLUMNS).to_csv(
            DEFAULT_DB,
            index=False,
            encoding='utf-8-sig'
        )

    if not os.path.exists(CHAT_DB):
        pd.DataFrame(columns=CHAT_COLUMNS).to_csv(
            CHAT_DB,
            index=False,
            encoding='utf-8-sig'
        )

    if not os.path.exists(REQ_FILE):
        pd.DataFrame(columns=[
            "申請編號",
            "申請日期",
            "申請名稱",
            "備註事項",
            "審核結果",
            "權限"
        ]).to_csv(
            REQ_FILE,
            index=False,
            encoding='utf-8-sig'
        )


def get_all_reports():
    forbidden = [CHAT_DB, REQ_FILE]

    return [
        f for f in os.listdir('.')
        if f.endswith('.csv') and f not in forbidden
    ]


def load_data():
    db_name = st.session_state.current_db

    if os.path.exists(db_name):
        try:
            df = pd.read_csv(
                db_name,
                encoding='utf-8-sig',
                on_bad_lines='skip'
            )

            for col in COLUMNS:
                if col not in df.columns:
                    df[col] = None

            df = df[COLUMNS]

            return df

        except Exception:
            return pd.DataFrame(columns=COLUMNS)

    return pd.DataFrame(columns=COLUMNS)


def save_data(df):
    df.to_csv(
        st.session_state.current_db,
        index=False,
        encoding='utf-8-sig'
    )


def load_chat():
    if os.path.exists(CHAT_DB):
        try:
            return pd.read_csv(CHAT_DB)
        except:
            return pd.DataFrame(columns=CHAT_COLUMNS)

    return pd.DataFrame(columns=CHAT_COLUMNS)


def save_chat(nickname, content):
    chat_df = load_chat()

    row = {
        "時間": get_now_time(),
        "暱稱": nickname,
        "內容": content,
        "標籤": "訪客"
    }

    chat_df = pd.concat([
        chat_df,
        pd.DataFrame([row])
    ], ignore_index=True)

    chat_df.to_csv(
        CHAT_DB,
        index=False,
        encoding='utf-8-sig'
    )

# =====================================================
# 初始化
# =====================================================
ensure_files()

if 'current_db' not in st.session_state:
    st.session_state.current_db = DEFAULT_DB

all_reports = get_all_reports()

if not all_reports:
    all_reports = [DEFAULT_DB]

if st.session_state.current_db not in all_reports:
    st.session_state.current_db = all_reports[0]

main_df = load_data()

# =====================================================
# 自動刷新同步
# =====================================================
st.markdown(
    """
    <script>
        setTimeout(function(){
            window.location.reload();
        }, 10000);
    </script>
    """,
    unsafe_allow_html=True
)

# =====================================================
# Sidebar
# =====================================================
with st.sidebar:

    st.header("💰 資金與統計中心")

    idx = all_reports.index(st.session_state.current_db)

    selected_db = st.selectbox(
        "切換帳號",
        all_reports,
        index=idx
    )

    if selected_db != st.session_state.current_db:
        st.session_state.current_db = selected_db
        st.rerun()

    st.divider()

    if not main_df.empty:

        try:
            current_bal = int(
                pd.to_numeric(
                    main_df["結算總分"],
                    errors='coerce'
                ).dropna().iloc[-1]
            )
        except:
            current_bal = 0

        st.metric(
            "目前可用本金",
            f"${current_bal:,}"
        )

        invest_types = ['初始', '手動補倉', '補倉']

        total_investment = main_df[
            main_df['類型'].isin(invest_types)
        ]['金額'].sum()

        st.write(
            f"💼 累積投入: ${total_investment:,}"
        )

        real_profit = current_bal - total_investment

        if real_profit >= 0:
            st.success(f"📈 純獲利: ${real_profit:,}")
        else:
            st.error(f"📉 尚虧: ${abs(real_profit):,}")

# =====================================================
# 初始化本金
# =====================================================
if main_df.empty or main_df["結算總分"].dropna().empty:

    st.subheader("初始化報表")

    init_cap = st.number_input(
        "起始本金",
        value=60000,
        step=1000
    )

    if st.button("建立"):

        row = {
            "日期": get_now_time(),
            "賽事項目": "初始",
            "類型": "初始",
            "金額": int(init_cap),
            "盈虧金額": 0,
            "結算總分": int(init_cap)
        }

        save_data(pd.DataFrame([row]))
        st.rerun()

# =====================================================
# 主系統 Tabs
# =====================================================
else:

    tab1, tab2, tab_live, tab3, tab4, tab5 = st.tabs([
        "💰 下單投注",
        "📝 註冊帳號",
        "⚽ 即時比分",
        "📋 歷史記錄",
        "📊 統計圖表",
        "💬 討論區"
    ])

    # =================================================
    # TAB1
    # =================================================
    with tab1:

        st.subheader("💰 下單投注")

        try:
            balance = int(main_df["結算總分"].iloc[-1])
        except:
            balance = 0

        m_info = st.text_area(
            "賽事資訊",
            placeholder="例如：英超 阿仙奴 vs 車路士"
        )

        bet_amt = st.number_input(
            "下注金額",
            min_value=0,
            value=5000,
            step=1000
        )

        gain_amt = st.number_input(
            "盈利金額",
            min_value=0,
            value=0,
            step=1000
        )

        c1, c2 = st.columns(2)

        if c1.button("✅ 過關 (贏)"):

            row = {
                "日期": get_now_time(),
                "賽事項目": m_info,
                "類型": "贏 (+)",
                "金額": int(gain_amt),
                "盈虧金額": int(gain_amt),
                "結算總分": balance + int(gain_amt)
            }

            save_data(pd.concat([
                main_df,
                pd.DataFrame([row])
            ], ignore_index=True))

            st.rerun()

        if c2.button("❌ 未過關 (輸)"):

            row = {
                "日期": get_now_time(),
                "賽事項目": m_info,
                "類型": "輸 (-)",
                "金額": int(bet_amt),
                "盈虧金額": -int(bet_amt),
                "結算總分": balance - int(bet_amt)
            }

            save_data(pd.concat([
                main_df,
                pd.DataFrame([row])
            ], ignore_index=True))

            st.rerun()

    # =================================================
    # TAB2
    # =================================================
    with tab2:

        st.subheader("📂 登錄會員管理中心")

        req_df = pd.read_csv(
            REQ_FILE,
            encoding='utf-8-sig'
        )

        st.subheader("提交新帳號申請")

        new_name = st.text_input(
            "請輸入帳號名稱"
        )

        if st.button("確認送出申請"):

            has_chinese = any(
                '\u4e00' <= c <= '\u9fff'
                for c in new_name
            )

            if not new_name:
                st.warning("請輸入名稱")

            elif has_chinese:
                st.error("帳號不可包含中文")

            else:

                target_csv = f"{new_name}.csv"

                if not os.path.exists(target_csv):
                    pd.DataFrame(columns=COLUMNS).to_csv(
                        target_csv,
                        index=False,
                        encoding='utf-8-sig'
                    )

                new_id = f"{len(req_df)+1:04d}"

                row = {
                    "申請編號": new_id,
                    "申請日期": get_now_time(),
                    "申請名稱": new_name,
                    "備註事項": "已建立",
                    "審核結果": "通過",
                    "權限": "User"
                }

                req_df = pd.concat([
                    req_df,
                    pd.DataFrame([row])
                ], ignore_index=True)

                req_df.to_csv(
                    REQ_FILE,
                    index=False,
                    encoding='utf-8-sig'
                )

                st.success("建立成功")
                st.rerun()

        st.divider()

        st.subheader("帳號審核進度詳情")

        st.dataframe(
            req_df.iloc[::-1],
            use_container_width=True,
            hide_index=True
        )

    # =================================================
    # TAB LIVE
    # =================================================
    with tab_live:

        st.subheader("📡 即時比分同步觀看")

        st.components.v1.iframe(
            "https://live.titan007.com/indexall_big.aspx",
            height=800,
            scrolling=True
        )

    # =================================================
    # TAB3
    # =================================================
    with tab3:

        st.subheader("📋 歷史記錄")

        if not main_df.empty:
            st.dataframe(
                main_df.iloc[::-1],
                use_container_width=True
            )

    # =================================================
    # TAB4
    # =================================================
    with tab4:

        st.subheader("📊 統計圖表")

        st.line_chart(main_df["結算總分"])

    # =================================================
    # TAB5
    # =================================================
    with tab5:

        st.subheader("💬 討論區")

        if 'user_nickname' not in st.session_state:

            nickname = st.text_input("請輸入暱稱")

            if st.button("確認進入"):
                st.session_state.user_nickname = nickname
                st.rerun()

        else:

            chat_df = load_chat()

            msg = st.text_area("輸入內容")

            if st.button("送出留言"):
                save_chat(
                    st.session_state.user_nickname,
                    msg
                )
                st.rerun()

            st.divider()

            if not chat_df.empty:

                for _, row in chat_df.iloc[::-1].iterrows():

                    st.markdown(
                        f"**{row['暱稱']}**｜{row['時間']}"
                    )

                    st.write(row['內容'])

                    st.divider()

# =====================================================
# 底部
# =====================================================
st.divider()

st.markdown(
    """
    <div style='color:#888;'>
    謹慎理財 信用至