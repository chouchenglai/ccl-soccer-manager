import streamlit as st

# =========================
# 頁面設定
# =========================

st.set_page_config(
    page_title="CCL-Live",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

.main {
    background:#f5f7fb;
}

/* HERO */

.hero-box{
    background:linear-gradient(135deg,#0f172a,#1d4ed8);
    border-radius:35px;
    padding:70px 50px;
    margin-top:20px;
    margin-bottom:50px;
    text-align:center;
    box-shadow:0 12px 35px rgba(0,0,0,0.18);
}

.hero-logo{
    width:100%;
    max-width:1100px;
    margin:auto;
    display:block;
    margin-bottom:35px;
}

.hero-sub{
    font-size:34px;
    color:#e0e7ff;
    margin-bottom:18px;
    font-weight:700;
}

.hero-desc{
    font-size:20px;
    color:#dbeafe;
    letter-spacing:2px;
}

/* 區塊 */

.section-title{
    font-size:42px;
    font-weight:900;
    color:#0f172a;
    margin-bottom:30px;
}

/* 卡片 */

.card-link{
    text-decoration:none;
}

.card{
    background:white;
    border-radius:24px;
    padding:35px;
    box-shadow:0 4px 18px rgba(0,0,0,0.08);
    margin-bottom:25px;
    transition:0.3s;
    min-height:240px;
}

.card:hover{
    transform:translateY(-8px);
    box-shadow:0 10px 30px rgba(0,0,0,0.14);
}

.card-title{
    font-size:26px;
    font-weight:800;
    margin-bottom:20px;
    color:#111827;
}

.card-text{
    font-size:18px;
    line-height:1.9;
    color:#374151;
}

/* 特色區 */

.feature-box{
    background:linear-gradient(135deg,#1d4ed8,#2563eb);
    border-radius:28px;
    padding:55px;
    margin-top:40px;
    margin-bottom:50px;
    color:white;
    text-align:center;
}

.feature-title{
    font-size:42px;
    font-weight:900;
    margin-bottom:20px;
}

.feature-text{
    font-size:22px;
    line-height:2;
}

/* 按鈕 */

.stButton>button{
    background:#2563eb;
    color:white;
    border:none;
    border-radius:16px;
    padding:16px 20px;
    font-size:24px;
    font-weight:bold;
    transition:0.3s;
}

.stButton>button:hover{
    background:#1d4ed8;
    transform:scale(1.03);
}

/* Footer */

.footer{
    text-align:center;
    color:#6b7280;
    margin-top:70px;
    margin-bottom:20px;
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================

st.markdown("""

<div class="hero-box">

<img class="hero-logo"
src="https://www.ccl-live.tw/logo.jpg">

<div class="hero-sub">
體育模擬交易與賽事分析平臺
</div>

<div class="hero-desc">
即時比分｜歷史數據｜模擬倉管理｜交流討論
</div>

</div>

""", unsafe_allow_html=True)

# =========================
# 平臺功能
# =========================

st.markdown("""
<div class="section-title">
🔥 平臺核心功能
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <a class="card-link" href="#">

    <div class="card">

    <div class="card-title">
    💰 模擬交易
    </div>

    <div class="card-text">
    自動結算盈虧，<br>
    即時同步總資金變化。
    </div>

    </div>

    </a>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <a class="card-link" href="#">

    <div class="card">

    <div class="card-title">
    📈 統計圖表
    </div>

    <div class="card-text">
    自動生成資金曲線圖，<br>
    分析長期操作表現。
    </div>

    </div>

    </a>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <a class="card-link" href="#">

    <div class="card">

    <div class="card-title">
    💬 討論交流
    </div>

    <div class="card-text">
    即時討論熱門賽事，<br>
    站長免費分享賽事觀點。
    </div>

    </div>

    </a>
    """, unsafe_allow_html=True)

# =========================
# 第二列
# =========================

col4, col5, col6 = st.columns(3)

with col4:

    st.markdown("""
    <div class="card">

    <div class="card-title">
    📋 歷史記錄
    </div>

    <div class="card-text">
    完整保存每場記錄，<br>
    方便後續回測分析。
    </div>

    </div>
    """, unsafe_allow_html=True)

with col5:

    st.markdown("""
    <div class="card">

    <div class="card-title">
    ⚽ 即時比分
    </div>

    <div class="card-text">
    同步全球足球賽事，<br>
    即時查看最新動態。
    </div>

    </div>
    """, unsafe_allow_html=True)

with col6:

    st.markdown("""
    <div class="card">

    <div class="card-title">
    🧠 AI 分析
    </div>

    <div class="card-text">
    未來將加入 AI 分析，<br>
    提升賽事預測效率。
    </div>

    </div>
    """, unsafe_allow_html=True)

# =========================
# 特色區
# =========================

st.markdown("""

<div class="feature-box">

<div class="feature-title">
🚀 CCL-Live 正式上線
</div>

<div class="feature-text">
體育賽事模擬交易系統正式開放使用<br>
支援模擬倉、自動結算、歷史分析與社群交流功能
</div>

</div>

""", unsafe_allow_html=True)

# =========================
# 進入平臺
# =========================

col_a, col_b, col_c = st.columns([1,2,1])

with col_b:

    if st.button("🚀 立即進入正式平臺", use_container_width=True):

        st.switch_page("pages/ccl-live.py")

# =========================
# Footer
# =========================

st.markdown("""
<div class="footer">

CCL-Live 體育賽事管理系統 © 2026

<br><br>

www.ccl-live.tw

</div>
""", unsafe_allow_html=True)