import streamlit as st
import pandas as pd
import os
import pytz
import base64

# --- 1. 權威商標顯示 (確保 Logo 在最上方) ---
def get_base64_img(file_path):
    with open(file_path, "rb") as f: data = f.read()
    return base64.b64encode(data).decode()

img_path = "ccl_logo_header.jpg"
if os.path.exists(img_path):
    img_b64 = get_base64_img(img_path)
    st.markdown(f"""
        <style>
            .banner-box {{ width: 100%; text-align: center; margin-bottom: 20px; }}
            .banner-img {{ width: 90%; height: auto; display: block; margin: 0 auto; }}
        </style>
        <div class="banner-box"><img src="data:image/jpeg;base64,{img_b64}" class="banner-img"></div>
    """, unsafe_allow_html=True)

# --- 2. 頁面基本設定 ---
st.set_page_config(page_title="CCL-Live 本站歷史戰績紀錄報表", page_icon="📜", layout="wide")

# --- 3. 數據源指定 ---
ADMIN_DB = "pages/admin.csv" 

def get_admin_data():
    if os.path.exists("pages/admin.csv"): return "pages/admin.csv"
    return ADMIN_DB

# --- 4. 頂部宣傳與返回按鈕 (解決換行問題) ---
col_t, col_b = st.columns([4, 1.2])

with col_t:
    st.title("📜 本站歷史戰績紀錄報表")
    st.markdown("""
        <div style="background: rgba(30, 64, 175, 0.1); border-left: 5px solid #1e40af; padding: 15px; border-radius: 5px;">
            💎 <b>本站公告：</b>本頁面記錄為實測數據！
        </div>
    """, unsafe_allow_html=True)

with col_b:
    # 💡 關鍵修正：使用 HTML padding 確保按鈕往下移動兩行，與 Logo 保持完美間距
    st.markdown('<div style="padding-top: 45px;"></div>', unsafe_allow_html=True)
    st.link_button("🏠 回到主頁面", "/page/ccl-live.py", use_container_width=True)

st.write("") # 額外增加一行空行

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