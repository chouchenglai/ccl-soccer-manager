st.markdown(f"""
<style>

.hero-box{{
    background: linear-gradient(135deg,#0f172a,#2563eb);
    border-radius: 35px;
    padding: 45px;
    margin-top: 20px;
    margin-bottom: 50px;
    box-shadow: 0 10px 35px rgba(0,0,0,0.18);
}}

.hero-flex{{
    display:flex;
    align-items:center;
    justify-content:center;
    gap:50px;
    flex-wrap:wrap;
}}

.hero-logo{{
    width:380px;
    max-width:100%;
}}

.hero-right{{
    text-align:left;
}}

.hero-title{{
    font-size:82px;
    font-weight:900;
    color:white;
    line-height:1.15;
    margin-bottom:15px;
}}

.hero-sub{{
    font-size:38px;
    color:#dbeafe;
    font-weight:700;
    margin-top:15px;
}}

.hero-desc{{
    font-size:24px;
    color:white;
    margin-top:30px;
    letter-spacing:1px;
}}

.hero-desc a{{
    color:white;
    text-decoration:none;
    font-weight:bold;
    margin:0 10px;
    transition:0.3s;
}}

.hero-desc a:hover{{
    color:#facc15;
}}

</style>

<div class="hero-box">

<div class="hero-flex">

<div>
<img class="hero-logo"
src="data:image/jpg;base64,{logo_base64}">
</div>

<div class="hero-right">

<div class="hero-title">
CCL-Live
</div>

<div class="hero-sub">
體育賽事模擬交易與分析平臺
</div>

<div class="hero-desc">

<a href="#">
即時比分
</a>

｜

<a href="#">
歷史數據
</a>

｜

<a href="#">
模擬倉管理
</a>

｜

<a href="#">
交流討論
</a>

</div>

</div>

</div>

</div>
""", unsafe_allow_html=True)