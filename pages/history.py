import streamlit as st
import pandas as pd
import os
import pytz

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

# --- 1. 頁面基本設定 ---
st.set_page_config(page_title=" CCL-Live 本站歷史戰績紀錄報表", page_icon="📜", layout="wide")
  
# --- 2. 數據源指定 (指定的路徑) ---
# 💡 這裡鎖定讀取您的 admin.csv，作為本站展示樣板
ADMIN_DB = "pages/admin.csv" 

def get_admin_data():
    # 邏輯：如果在 pages 資料夾內執行，直接找 admin.csv；如果在根目錄執行，找 pages/admin.csv
    if os.path.exists("admin.csv"):
        return "admin.csv"
    return ADMIN_DB

    st.write("")
    st.write("")

col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 返回首頁"):
        st.switch_page("pages/soccer_app.py")

with col2:
    if st.button("🎯 返回主平台"):
        st.switch_page("pages/ccl-live.py")

# --- 3. 標誌藍 CSS 樣式 ---
st.markdown("""
<style>
    .vip-btn {
        background: linear-gradient(135deg, #1e40af, #0f172a);
        color: white !important;
        padding: 8px 20px;
        text-align: center;
        text-decoration: none !important;
        display: inline-block;
        font-size: 14px;
        font-weight: bold;
        border-radius: 50px;
        transition: 0.3s;
    }
    .promotion-box {
        background: rgba(30, 64, 175, 0.1);
        border-left: 5px solid #1e40af;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. 頂部宣傳標題 ---
col_t, col_b = st.columns([4, 1.2])
with col_t:
    st.title("📜 本站歷史戰績紀錄報表")
    st.markdown('<div class="promotion-box">💎 <b>本站公告：</b>本頁面記錄為實測數據！</div>', unsafe_allow_html=True)

    st.write("")
    st.write("")

# --- 5. 數據顯示邏輯 (含千分位與顏色設定) ---
target_path = get_admin_data()

if os.path.exists(target_path):
    try:
        df = pd.read_csv(target_path)
        if not df.empty:
            # 數據處理：反轉順序
            display_df = df.iloc[::-1].copy()
            
            # 💡 修正三：顏色顯示邏輯 (正數綠色、負數紅色)
            def style_profit(val):
                if isinstance(val, (int, float)):
                    color = 'green' if val > 0 else 'red' if val < 0 else 'black'
                    return f'color: {color}; font-weight: bold;'
                return ''

            # 套用樣式
            styled_df = display_df.style.applymap(style_profit, subset=['盈虧金額'])

            st.write("### 📝 完整賽事歷史記錄")
            # 💡 修正二：加入 column_config 實現千分位小分位
            st.dataframe(
                styled_df,
                use_container_width=True,
                height=450,
                column_config={
                    "日期": st.column_config.TextColumn("📅 日期"),
                    "金額": st.column_config.NumberColumn("💰 金額", format="%d"),
                    "盈虧金額": st.column_config.NumberColumn("📈 盈虧", format="%d"),
                    "結算總分": st.column_config.NumberColumn("🏆 總分", format="%d")
                }
            )
            
            # 自動統計勝率
            if "盈虧金額" in df.columns:
                wins = len(df[df["盈虧金額"] > 0])
                total = len(df)
                win_rate = (wins / total) * 100 if total > 0 else 0
                st.metric("目前實測勝率", f"{win_rate:.1f}%", delta=f"{wins} 勝 / {total} 場")

        else:
            st.info("目前暫無數據。")
    except Exception as e:
        st.error(f"數據解析出錯：{e}")
else:
    st.warning(f"找不到路徑：{target_path}")

st.divider()
st.caption("CCL-Live 系統自動同步 admin.csv 樣板")