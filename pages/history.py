import streamlit as st
import pandas as pd
import os
import pytz
import base64

# --- 1. 頁面基本設定 (必須放在最頂端，絕對不能動) ---
st.set_page_config(page_title="CCL-Live 本站歷史戰績紀錄報表", page_icon="📜", layout="wide")

# --- 2. 標誌顯示區 (Base64) ---
def get_base64_img(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f: data = f.read()
        return base64.b64encode(data).decode()
    return None

img_path = "ccl_logo_header.jpg"
img_b64 = get_base64_img(img_path)

if img_b64:
    st.markdown(f"""
        <style>
            .banner-box {{ width: 100%; text-align: center; margin-bottom: 10px; }}
            .banner-img {{ width: 90%; height: auto; display: block; margin: 0 auto; border-radius: 10px; }}
        </style>
        <div class="banner-box"><img src="data:image/jpeg;base64,{img_b64}" class="banner-img"></div>
    """, unsafe_allow_html=True)

# --- 3. 數據源與工具函數 ---
ADMIN_DB = "pages/admin.csv" 

def get_admin_data():
    if os.path.exists("admin.csv"): return "admin.csv"
    return ADMIN_DB

# --- 4. 頂部宣傳與返回按鈕 ---
# 使用 HTML 強制空行，解決按鈕太靠上的問題
st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)

col_t, col_b = st.columns([4, 1.2])

with col_t:
    st.title("📜 本站歷史戰績紀錄報表")
    st.markdown("""
        <div style="background: rgba(30, 64, 175, 0.1); border-left: 5px solid #1e40af; padding: 15px; border-radius: 5px;">
            💎 <b>本站公告：</b>本頁面記錄為實測數據！
        </div>
    """, unsafe_allow_html=True)

with col_b:
    # 這裡調整 padding-top 讓按鈕對齊標題下方
    st.markdown('<div style="padding-top: 50px;"></div>', unsafe_allow_html=True)
    st.link_button("🏠 回到主頁面", "ccl-live.py", use_container_width=True)

st.write("") 

# --- 5. 數據顯示邏輯 ---
target_path = get_admin_data()

if os.path.exists(target_path):
    try:
        df = pd.read_csv(target_path)
        if not df.empty:
            # 數據處理：反轉順序
            display_df = df.iloc[::-1].copy()
            
            # 💡 修正：顏色顯示邏輯 (贏綠輸紅)
            # 新版 Streamlit 建議使用 map 而非 applymap
            def style_profit(val):
                if isinstance(val, (int, float)):
                    if val > 0: return 'color: #28a745; font-weight: bold;' # 綠色
                    if val < 0: return 'color: #dc3545; font-weight: bold;' # 紅色
                return 'color: #31333F;'

            # 套用表格樣式
            styled_df = display_df.style.map(style_profit, subset=['盈虧金額'])

            st.write("### 📝 完整賽事歷史記錄")
            
            # 💡 修正：加入千分位與小分位控制
            st.dataframe(
                styled_df,
                use_container_width=True,
                height=500,
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