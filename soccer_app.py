# =========================
# CCL-Live 首頁入口門面
# =========================

st.markdown("""
<style>

.hero-box{
    background: linear-gradient(135deg,#0f172a,#1e3a8a);
    padding:45px;
    border-radius:25px;
    color:white;
    margin-bottom:30px;
    box-shadow:0 0 30px rgba(0,0,0,0.25);
}

.hero-title{
    font-size:52px;
    font-weight:900;
    margin-bottom:10px;
    color:white;
}

.hero-sub{
    font-size:24px;
    color:#cbd5e1;
    margin-bottom:30px;
}

.feature-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:20px;
    margin-top:30px;
}

.feature-card{
    background:white;
    border-radius:18px;
    padding:25px;
    box-shadow:0 4px 15px rgba(0,0,0,0.08);
    transition:0.3s;
}

.feature-card:hover{
    transform:translateY(-5px);
}

.feature-title{
    font-size:24px;
    font-weight:bold;
    margin-bottom:10px;
}

.feature-text{
    color:#555;
    line-height:1.8;
}

.cta-box{
    background:linear-gradient(135deg,#2563eb,#1d4ed8);
    padding:35px;
    border-radius:20px;
    text-align:center;
    color:white;
    margin-top:40px;
}

.cta-title{
    font-size:36px;
    font-weight:900;
    margin-bottom:15px;
}

.cta-btn{
    display:inline-block;
    background:white;
    color:#2563eb;
    padding:14px 35px;
    border-radius:14px;
    font-weight:bold;
    text-decoration:none;
    font-size:20px;
}

</style>
""", unsafe_allow_html=True)

# Hero 區塊
st.markdown("""
<div class="hero-box">

<div class="hero-title">
⚽ CCL-Live
</div>

<div class="hero-sub">
全球體育賽事模擬交易平台
</div>

✅ 即時比分同步<br>
✅ 自動盈虧結算<br>
✅ 智能統計分析<br>
✅ 足球社群交流<br>

</div>
""", unsafe_allow_html=True)

# 功能卡片
st.markdown("""
<div class="feature-grid">

<div class="feature-card">
<div class="feature-title">📡 即時比分</div>
<div class="feature-text">
同步全球足球賽事資訊與即時數據。
</div>
</div>

<div class="feature-card">
<div class="feature-title">💰 模擬交易</div>
<div class="feature-text">
自動記錄下注、盈虧與總資金變化。
</div>
</div>

<div class="feature-card">
<div class="feature-title">📈 統計分析</div>
<div class="feature-text">
智能生成曲線圖與歷史回測數據。
</div>
</div>

<div class="feature-card">
<div class="feature-title">💬 社群討論</div>
<div class="feature-text">
站長免費分享熱門賽事與交流分析。
</div>
</div>

</div>
""", unsafe_allow_html=True)

# CTA 區塊
st.markdown("""
<div class="cta-box">

<div class="cta-title">
🚀 開始您的模擬交易之旅
</div>

立即體驗 CCL-Live 專業體育交易平台。

</div>
""", unsafe_allow_html=True)

st.markdown("---")