import streamlit as st

st.set_page_config(
    page_title="CCL-Live",
    page_icon="⚽",
    layout="wide"
)

# ======================
# CSS
# ======================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.big-title {
    font-size: 68px;
    font-weight: 900;
    color: white;
    text-align: center;
}

.sub-title {
    font-size: 26px;
    color: #dbeafe;
    text-align: center;
}

.hero-box {
    background: linear-gradient(135deg,#0f172a,#1d4ed8);
    padding: 70px 50px;
    border-radius: 30px;
    margin-top: 20px;
    margin-bottom: 40px;
}

.feature-box {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.footer {
    text-align:center;
    color:#888;
    margin-top:60px;
}

</style>
""", unsafe_allow_html=True)

# ======================
# HERO
# ======================

st.markdown("""
<div class="hero-box">

<div class="big-title">
⚽ CCL-Live
</div>

<br>

<div class="sub-title">
全球體育模擬交易與賽事分析平台
</div>

</div>
""", unsafe_allow_html=True)

# ======================
# 平台介紹
# ======================

st.markdown("## 🔥 平台核心功能")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="feature-box">
    <h3>💰 模擬交易</h3>
    <p>
    自動結算盈虧，<br>
    即時更新總資金。
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="feature-box">
    <h3>📈 統計圖表</h3>
    <p>
    自動生成資金曲線圖，<br>
    分析歷史表現。
    </p>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="feature-box">
    <h3>💬 討論區</h3>
    <p>
    即時交流討論，<br>
    免費分享熱門賽事。
    </p>
    </div>
    """, unsafe_allow_html=True)

# ======================
# 第二區
# ======================

col4, col5, col6 = st.columns(3)

with col4:

    st.markdown("""
    <div class="feature-box">
    <h3>📋 歷史紀錄</h3>
    <p>
    完整保存每場賽事，<br>
    方便後期回測。
    </p>
    </div>
    """, unsafe_allow_html=True)

with col5:

    st.markdown("""
    <div class="feature-box">
    <h3>⚽ 即時比分</h3>
    <p>
    同步全球足球賽事，<br>
    即時查看動態。
    </p>
    </div>
    """, unsafe_allow_html=True)

with col6:

    st.markdown("""
    <div class="feature-box">
    <h3>🧠 AI分析</h3>
    <p>
    未來將加入 AI 預測、<br>
    勝率分析系統。
    </p>
    </div>
    """, unsafe_allow_html=True)

# ======================
# 進入平台
# ======================

st.write("")
st.write("")

if st.button("🚀 立即進入正式平台"):

    st.switch_page("pages/ccl-live.py")

# ======================
# Footer
# ======================

st.markdown("""
<div class="footer">

CCL-Live 體育賽事管理系統 © 2026

<br>

www.ccl-live.tw

</div>
""", unsafe_allow_html=True)