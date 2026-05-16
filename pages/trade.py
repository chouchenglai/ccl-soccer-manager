import pytz
import streamlit as st
import pandas as pd
import os
import time
from datetime import datetime, timedelta, timezone

# 1. 頁面設定 (最頂端)
st.set_page_config(page_title="CCL-Live 體育賽事管理系統", page_icon="⚽", layout="wide")

# --- 基本設定 ---
DEFAULT_DB = "ccl-soccer.csv"
CHAT_DB = "ccl_chat_log.csv"
COLUMNS = ["日期", "賽事項目", "類型", "金額", "盈虧金額", "結算總分"]
CHAT_COLUMNS = ["時間", "暱稱", "內容", "標籤"]

TW_TZ = pytz.timezone('Asia/Taipei') # 設定台北時區

def get_now_time():
    # 這裡會回傳正確的台北時間字串
    return datetime.now(TW_TZ).strftime("%Y-%m-%d %H:%M")

# --- 工具 ---
def get_all_reports():
    # 這裡加上條件：排除「註冊帳本 (pending_requests.csv)」和「聊天紀錄」
    forbidden_files = [CHAT_DB, "pending_requests.csv"]
    return [f for f in os.listdir('.') if f.endswith('.csv') and f not in forbidden_files]

def ensure_files():
    if not os.path.exists(DEFAULT_DB):
        pd.DataFrame(columns=COLUMNS).to_csv(DEFAULT_DB, index=False)
    if not os.path.exists(CHAT_DB):
        pd.DataFrame(columns=CHAT_COLUMNS).to_csv(CHAT_DB, index=False, encoding='utf-8-sig')

ensure_files()

import base64  # 請確保檔案最上方有 import base64

# --- 💡 讀取並轉換圖片為 Base64 (解決路徑無法顯示問題) ---
def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

ensure_files()

import base64 # 確保最上方有這行

# 💡 定義一個萬用的圖片讀取器
def get_img_as_base64(file):
    try:
        # 這裡會嘗試讀取跟 trade.py 同一個資料夾下的 pro.png
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception as e:
        return None

ensure_files()

ensure_files()

# --- 💡 專業 CSS 樣式：打造本站專屬藍色按鈕 ---
st.markdown("""
<style>
    .vip-btn {
        background: linear-gradient(135deg, #2563eb, #0f172a); /* 本站標誌藍色漸層 */
        color: white !important;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        font-weight: bold;
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
        transition: 0.3s;
        cursor: pointer;
    }
    .vip-btn:hover {
        background: linear-gradient(135deg, #3b82f6, #1e40af);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# --- 1. 標題與專業按鈕並排區塊 ---
col_title, col_pro = st.columns([4, 1.2])

with col_pro:
    # 使用我們剛剛定義的 .vip-btn 樣式
    st.markdown(f"""
        <div style="text-align: right; padding-top: 15px;">
            <a href="/vip" target="_self" class="vip-btn">
                💎 升 級 帳 號
            </a>
        </div>
    """, unsafe_allow_html=True)

st.divider()

def load_data():
    if os.path.exists(st.session_state.current_db):
        try:
            # 自動跳過前面非 CSV 的說明文字
            df = pd.read_csv(
                        st.session_state.current_db,
                        encoding='utf-8-sig',
                        on_bad_lines='skip'
                        )

            # 如果欄位不完整，自動修復
            missing_cols = [col for col in COLUMNS if col not in df.columns]
            for col in missing_cols:
                df[col] = None

            df = df[COLUMNS]

            # 清除舊月份欄位
            if "月份" in df.columns:
                df = df.drop(columns=["月份"])

            return df

        except Exception as e:
            st.error(f"CSV 讀取失敗：{e}")
            return pd.DataFrame(columns=COLUMNS)

    return pd.DataFrame(columns=COLUMNS)

def save_data(df):
    if "月份" in df.columns: df = df.drop(columns=["月份"])
    df.to_csv(st.session_state.current_db, index=False, encoding='utf-8-sig')

def load_chat():
    if os.path.exists(CHAT_DB): return pd.read_csv(CHAT_DB)
    return pd.DataFrame(columns=CHAT_COLUMNS)

def save_chat(nickname, content):
    df = load_chat()
    new_msg = {"時間": get_now_time(), "暱稱": nickname, "內容": content, "標籤": "訪客"}
    df = pd.concat([df, pd.DataFrame([new_msg])], ignore_index=True)
    df.to_csv(CHAT_DB, index=False, encoding='utf-8-sig')
current_tw_date = datetime.now(TW_TZ).date()

# --- 初始化 ---
ensure_files()
if 'current_db' not in st.session_state: st.session_state.current_db = DEFAULT_DB
all_reports = get_all_reports()
if not all_reports: all_reports = [DEFAULT_DB]
if st.session_state.current_db not in all_reports: st.session_state.current_db = all_reports[0]

main_df = load_data()

# --- 標誌顯示區 (Base64) ---
import base64
def get_base64_img(file_path):
    with open(file_path, "rb") as f: data = f.read()
    return base64.b64encode(data).decode()

img_path = "ccl_logo_header.jpg"
if os.path.exists(img_path):
    img_b64 = get_base64_img(img_path)
    st.markdown(f"""
        <style>
            .banner-box {{ width: 90%; text-align: center; background-color: #ffffff; padding: 0px 0; margin-bottom: 20px; overflow: hidden; }}
            .banner-img {{ width: 90%; transform: scale(1.1); transform-origin: center; height: auto; display: block; margin: 0 auto; }}
        </style>
        <div class="banner-box"><img src="data:image/jpeg;base64,{img_b64}" class="banner-img"></div>
    """, unsafe_allow_html=True)

# ==========================================
# 🚀 全局討論區提醒系統 
# ==========================================

# 1. 數據準備
current_chat_data = load_chat()
new_msg_count = len(current_chat_data)

if 'last_chat_count' not in st.session_state:
    st.session_state.last_chat_count = new_msg_count

# 2. 直接在這裡抓取身分權限 (解決報錯關鍵)
check_is_admin = False
req_file = "pending_requests.csv"
if "current_db" in st.session_state and os.path.exists(req_file):
    try:
        r_df = pd.read_csv(req_file)
        curr_name = st.session_state.current_db.replace('.csv', '')
        admin_match = r_df[(r_df['申請名稱'] == curr_name) & (r_df['權限'].str.upper() == 'ADMIN')]
        if not admin_match.empty:
            check_is_admin = True
    except:
        pass

# 3. 側邊欄開關 (使用我們剛才算好的 check_is_admin)
with st.sidebar:
    st.divider()
    # 提供開關給用戶，不論是誰都能控制自己的接收狀態
    show_notif = st.toggle("接收討論區新訊息廣播", value=True)
    if check_is_admin:
        st.caption("🛡️ 管理員身分已驗證")

# 4. 提醒邏輯：管理員發言穿透 OR 用戶開啟開關
if new_msg_count > st.session_state.last_chat_count:
    latest_msg = current_chat_data.iloc[-1]
    
    sender_name = str(latest_msg['暱稱']).lower()
    is_sender_admin = sender_name in ['管理員', 'admin']
    
    if is_sender_admin or show_notif:
        # 判斷樣式
        if is_sender_admin:
            box_style = "background: linear-gradient(90deg, #1E90FF, #00008B); border-left: 10px solid #FFD700;"
            title_tag = "🔥 【管理員指令】"
        else:
            box_style = "background: linear-gradient(90deg, #1E90FF, #00BFFF); border-left: 6px solid #FFD700;"
            title_tag = "📢 新留言提醒"

        st.markdown(f"""
            <div style="{box_style} color: white; padding: 15px 20px; border-radius: 8px; 
                        margin-bottom: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); 
                        animation: slideIn 0.5s ease-out;">
                <b>{title_tag}</b><br>
                <span style="color: #FFD700; font-weight: bold;">{latest_msg['暱稱']}</span> 
                說：「{latest_msg['內容'][:30]}...」
            </div>
            <style>@keyframes slideIn {{ from {{ transform: translateY(-20px); opacity: 0; }} to {{ transform: translateY(0); opacity: 1; }} }}</style>
        """, unsafe_allow_html=True)
        
        c_notif1, c_notif2 = st.columns([2.8, 7.2])
        if c_notif1.button("🔍 立即查看", key="notif_go_v6"):
            st.session_state.last_chat_count = new_msg_count
            st.rerun()
        if c_notif2.button("🆗 我知道了", key="notif_close_v6"):
            st.session_state.last_chat_count = new_msg_count
            st.rerun()

# --- Sidebar (側邊欄) ---
with st.sidebar:

    st.header("💰 資金與統計中心")

    idx = all_reports.index(st.session_state.current_db) \
        if st.session_state.current_db in all_reports else 0

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
            f"💼 累積投入: `${total_investment:,}`"
        )

        real_profit = current_bal - total_investment

        if real_profit >= 0:
            st.success(
                f"📈 純獲利: `${real_profit:,}`"
            )
        else:
            st.error(
                f"📉 尚虧: `${abs(real_profit):,}`"
            )

        csv = main_df.to_csv(
            index=False
        ).encode('utf-8-sig')

        st.download_button(
            "📥 下載完整紀錄 (CSV)",
            data=csv,
            file_name="soccer_backup.csv"
        )

# --- 邏輯判斷與主功能 ---
if main_df.empty or main_df["結算總分"].dropna().empty:
    st.subheader("初始化報表")
    init_cap = st.number_input("起始本金", value=60000, step=1000)
    if st.button("建立"):
        row = {"日期": get_now_time(), "賽事項目": "初始", "類型": "初始", "金額": int(init_cap), "盈虧金額": 0, "結算總分": int(init_cap)}
        save_data(pd.DataFrame([row])); st.rerun()
else:
    # 核心：標籤頁定義
    st.markdown("""
    <style>
        /* 針對 Streamlit 預設標籤列的第二個按鈕 (nth-child(2)) 裡面的文字 (p) 進行樣式修改 */
        div[data-baseweb="tab-list"] button[data-baseweb="tab"]:nth-child(2) p {
            color: #1E90FF !important;      /* 替換為閃耀的藍寶石色 */
            font-weight: bold !important;   /* 強制字體加粗 */
        }
    </style>
    """, unsafe_allow_html=True)  

# ==========================================
# Tab 2: 帳號管理 (一鍵審核 + 強效防錯版)
# ==========================================
    st.write("")
    st.markdown("""
    <p style='color: black; font-weight: bold; font-size: 0.9em; margin-bottom: 5px;'>
    💡 提示：未升級帳號前，使用模擬倉操作，數據將不會被保留，升級完成過後，才能建立報表保存數據！
    </p>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("<h2 style='color:#1E90FF; font-weight:bold;'>📂 登錄帳號管理中心</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid #1E90FF; margin-top: -10px;'>", unsafe_allow_html=True)     
  
    # --- 1. 初始化檔案與欄位 ---
    req_file = "pending_requests.csv"
    req_cols = ["申請編號", "申請日期", "申請名稱", "備註事項", "審核結果", "權限"]

    if os.path.exists(req_file):
        try:
            req_df = pd.read_csv(req_file, dtype={'申請編號': str})
            if "權限" not in req_df.columns:
                req_df["權限"] = "User"
                req_df.to_csv(req_file, index=False, encoding='utf-8-sig')
        except Exception:
            req_df = pd.DataFrame(columns=req_cols)
    else:
        req_df = pd.DataFrame(columns=req_cols)

    # --- 關鍵：管理員身分識別 (不分大小寫) ---
    is_admin = False
    if "current_db" in st.session_state:
        current_active_name = st.session_state.current_db.replace('.csv', '')
        # 只要 CSV 裡的權限是 ADMIN/Admin/admin 都算通過
        admin_check = req_df[(req_df['申請名稱'] == current_active_name) & (req_df['權限'].str.upper() == 'ADMIN')]
        if not admin_check.empty:
            is_admin = True

       # --- 2. 關鍵：管理員身分識別與強制密碼校驗 ---
    is_admin = False
    is_authenticated = False 
    
    if "current_db" in st.session_state:
        current_active_name = st.session_state.current_db.replace('.csv', '')
        # 檢查是否為 Admin 帳號 (不分大小寫)
        admin_row = req_df[(req_df['申請名稱'] == current_active_name) & (req_df['權限'].str.upper() == 'ADMIN')]
        
        # 💡 只有當查詢結果不為空時，才執行後續動作
        if not admin_row.empty:
            is_admin = True
            st.warning("🔐 **偵測到管理員身分：請輸入管理員密鑰以解鎖高級功能**")
            
            # 💡 使用固定 Key 避免報錯
            admin_pwd = st.text_input("請輸入管理員密鑰", type="password", key="admin_auth_lock")
            
            # 驗證密碼
            if admin_pwd == "Caiyun1992": 
                is_authenticated = True
                st.success("🔓 驗證成功：管理操作功能已開啟。")
            elif admin_pwd != "":
                st.error("❌ 密鑰錯誤：保護模式已啟動，功能暫時鎖定。")

    # --- 3. 區塊 A：提交新帳號申請 ---
    st.subheader("提交新帳號申請", anchor=False)
    new_name = st.text_input("請輸入您要創建的帳號名稱", placeholder="例如：Visitors")
    
    # 【視覺提醒】
    st.markdown("<small style='color:red; font-weight:bold;'>⚠️ 系統提醒：名稱僅限「英文與數字」，請勿使用中文或特殊符號，以免檔案建立失敗。</small>", unsafe_allow_html=True)
    
    with st.expander("**📜 點擊展開：CCL-Soccer 用戶服務協議與免責聲明**"):
        st.info("請詳細閱讀以下條款：")
        st.write("""
        1. 本系統僅供個人賽事數據記錄使用，不具備任何投注功能。
        2. 用戶需自行承擔數據分析之風險，本平臺不保證任何獲利。
        3. 申請即表示您同意系統收集您的帳號名稱以進行權限管理。
        4. 嚴禁任何違反當地法律之行為。
        """)
        is_agree = st.checkbox("我已閱讀並同意上述全部條款")

    # 【按鈕邏輯：中文攔截防線】
    if st.button("確認送出申請"):
        # 偵測是否包含中文字元
        has_chinese = any('\u4e00' <= char <= '\u9fff' for char in new_name)
        
        if not new_name:
            st.warning("請先輸入名稱再送出。")
        elif has_chinese:
            st.error("❌ 建立失敗：報表名稱不可包含中文字，請修改為純英文或數字名稱。")[cite: 1]
        elif not is_agree:
            st.error("❌ 請先勾選「同意服務協議」方可送出申請。")
        else:
            # 通過校驗，執行建立
            new_id = f"{len(req_df) + 1:04d}"
            today_str = datetime.now(TW_TZ).strftime("%Y年%m月%d日")
            target_csv = f"{new_name}.csv" if not new_name.endswith(".csv") else new_name

            empty_df = pd.DataFrame(columns=COLUMNS)
            empty_df.to_csv(target_csv, index=False, encoding='utf-8-sig')          
             
                      
            # 更新總表 (預設權限為 User)
            new_data = {
                "申請編號": new_id, "申請日期": today_str, "申請名稱": new_name,
                "備註事項": "已簽署免責聲明", "審核結果": "⏳ 審核進行中", "權限": "User"
            }
            updated_df = pd.concat([req_df, pd.DataFrame([new_data])], ignore_index=True)
            updated_df.to_csv(req_file, index=False, encoding='utf-8-sig')
            
            st.success(f"✅ 申請已成功！編號：{new_id}")
            time.sleep(1)
            st.rerun()

    st.divider()

    # --- 4. 區塊 B：審核進度詳情 (管理員互動版) ---[cite: 1]       
    st.subheader("帳號審核進度詳情", anchor=False)
    st.caption("💡 溫馨提示：審核進度需要24～48小時才能完成，伺服器建立檔案後才能啟用服務。")
           
    if not req_df.empty:
        if is_admin:
            # 管理員視角：顯示可操作的列表
            h1, h2, h3, h4 = st.columns([1, 2, 2, 1.5])
            h1.write("**編號**")
            h2.write("**名稱**")
            h3.write("**狀態**")
            h4.write("**管理操作**")
            st.divider()

            for idx, row in req_df.iloc[::-1].iterrows():
                c1, c2, c3, c4 = st.columns([1, 2, 2, 1.5])
                c1.write(row["申請編號"])
                c2.write(row["申請名稱"])
                
                status = row["審核結果"]
                if "進行中" in status:
                    c3.warning(status)
                    # 一鍵通過按鈕[cite: 1]
                    if c4.button("✅ 通過", key=f"approve_{idx}"):
                        req_df.at[idx, "審核結果"] = "通過"
                        req_df.to_csv(req_file, index=False, encoding='utf-8-sig')
                        st.toast(f"已核准 {row['申請名稱']}！")
                        time.sleep(1)
                        st.rerun()
                else:
                    c3.success(status)
                    c4.write("---")
        else:
            # 一般用戶視角：唯讀表格
            st.dataframe(req_df.iloc[::-1], use_container_width=True, hide_index=True)
    else:
        st.info("目前尚無申請記錄。")

    st.divider()

    # --- 5. 區塊 C：已授權帳號清單 (具備密碼保護) ---
    st.subheader("已授權帳號清單", anchor=False)
    st.caption("💡 溫馨提示：點擊啟動後將跳轉至主頁，在左側欄切換帳號，選擇您的報表名稱操作。")
    
    physical_files = [f for f in os.listdir('.') if f.endswith('.csv') and f not in [req_file, CHAT_DB]]
    passed_names = req_df[req_df['審核結果'].str.contains("過關|通過|OK", na=False)]['申請名稱'].tolist()
    display_targets = [f for f in physical_files if f == DEFAULT_DB or f.replace('.csv','') in passed_names]

    if display_targets:
        for fname in display_targets:
            if fname == req_file: continue
            
            col1, col2, col3 = st.columns([2.5, 1, 1])
            
            with col1:
                st.markdown(f"📁 **{fname}**" + (" <span style='color:gray;'>(預設)</span>" if fname == DEFAULT_DB else ""), unsafe_allow_html=True)
            
            with col2:
                st.link_button("🚀 啟動", "https://www.ccl-live.tw/ccl-live", use_container_width=True)
            
            with col3:
                # 💡 只有當「是管理員」且「密鑰正確」且「不是預設檔」時，才顯示刪除按鈕
                if is_admin and is_authenticated and fname != DEFAULT_DB:
                    if st.button("🗑️ 刪除", key=f"del_file_{fname}", use_container_width=True):
                        try:
                            # 1. 物理刪除檔案
                            os.remove(fname)
                            # 2. 從申請紀錄中移除該帳號
                            req_df = req_df[req_df['申請名稱'] != fname.replace('.csv','')]
                            req_df.to_csv(req_file, index=False, encoding='utf-8-sig')
                            # 3. 提示並刷新
                            st.toast(f"✅ 檔案 {fname} 已安全移除")
                            time.sleep(0.5)
                            st.rerun()
                        except Exception as e:
                            st.error(f"刪除失敗: {e}")
    else:
        st.info("暫無已授權之清單。")

# --- 底部 ---
st.markdown("""
<div style="color: #888; font-size: 0.9em; text-align: left; padding-bottom: 20px;">
謹慎理財 信用至上<br>
Copyright © 2026 CCL-Live 體育賽事管理系統版權所有
</div>
""", unsafe_allow_html=True)