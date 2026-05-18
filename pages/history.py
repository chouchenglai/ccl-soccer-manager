import streamlit as st
import pandas as pd
import os
import base64

# --- 1. 頁面基本設定 ---
st.set_page_config(page_title="CCL-Live 本站歷史戰績記錄", page_icon="📜", layout="wide")

# --- 2. 標誌顯示區 ---
def get_base64_img(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f: data = f.read()
        return base64.b64encode(data).decode()
    return None

img_path = "ccl_logo_header.jpg"
img_b64 = get_base64_img(img_path)

if img_b64:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 10px;">
            <img src="data:image/jpeg;base64,{img_b64}" style="width: 90%; border-radius: 10px;">
        </div>
    """, unsafe_allow_html=True)

# --- 3. CSS 樣式 ---
st.markdown("""
<style>
    .std-btn {
        display: block; width: 100%; padding: 8px;
        background-color: #f0f2f6; color: #31333F !important;
        text-align: center; text-decoration: none !important;
        border-radius: 8px; font-weight: 500; border: 1px solid #d1d5db;
    }
    .std-btn:hover { background-color: #e5e7eb; border-color: #9ca3af; }
</style>
""", unsafe_allow_html=True)

# --- 4. 數據預讀取 ---
ADMIN_DB = "pages/admin.csv"
target_path = "admin.csv" if os.path.exists("admin.csv") else ADMIN_DB
win_rate_str, delta_str = "0%", "0 勝 / 0 場"

if os.path.exists(target_path):
    raw_df = pd.read_csv(target_path)
    if not raw_df.empty and "盈虧金額" in raw_df.columns:
        wins = len(raw_df[raw_df["盈虧金額"] > 0])
        total = len(raw_df)
        win_rate_str = f"{(wins/total*100):.1f}%"
        delta_str = f"{wins} 勝 / {total} 場"

# --- 5. 頂部區塊 (修正佈局：勝率與按鈕上下並排，並增加間距) ---
st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True)
col_t, col_b = st.columns([3.5, 1.5])

with col_t:
    st.title("📜 本站歷史戰績紀錄報表")
    st.markdown('<div style="background: rgba(30,64,175,0.1); border-left: 5px solid #1e40af; padding: 15px; border-radius: 5px;">💎 <b>本站公告：</b>本頁面記錄為實測數據！</div>', unsafe_allow_html=True)

with col_b:
    # 💡 頂部放置勝率
    win_rate_str = "0%"
delta_str = "0 勝 / 0 場"

if os.path.exists(target_path):
    raw_df = pd.read_csv(target_path)
    if not raw_df.empty and "盈虧金額" in raw_df.columns:
        wins = len(raw_df[raw_df["盈虧金額"] > 0])
        total = len(raw_df)
        win_rate_str = f"{(wins/total*100):.1f}%"
        delta_str = f"{wins} 勝 / {total} 場"
    
    # 💡 關鍵修正：在這裡精確空出一行 (25像素高度)，讓按鈕往下移動
    st.markdown('<div style="height: 25px;"></div>', unsafe_allow_html=True)
    
    # 💡 放置返回主頁按鈕
    st.markdown(f'<a href="ccl-live" target="_self" class="std-btn">🏠 返回主平臺</a>', unsafe_allow_html=True)

st.write("")

# --- 6. 數據詳細清單顯示 ---
if os.path.exists(target_path):
    df = pd.read_csv(target_path)
    if not df.empty:
        display_df = df.iloc[::-1].copy()
        
        def style_profit(val):
            if isinstance(val, (int, float)):
                if val > 0: return 'color: #28a745; font-weight: bold;'
                if val < 0: return 'color: #dc3545; font-weight: bold;'
            return ''

        styled_df = display_df.style.map(style_profit, subset=['盈虧金額']).format({
            "金額": "{:,.0f}",
            "盈虧金額": "{:+,.0f}", 
            "結算總分": "{:,.0f}"
        })

        st.write("### 📝 完整賽事歷史記錄")
        st.dataframe(styled_df, use_container_width=True, height=500)
    else:
        st.info("目前暫無數據內容。")
else:
    st.warning("數據庫檔案讀取失敗。")

st.divider()
st.caption("CCL-Live 系統自動同步 admin.csv")