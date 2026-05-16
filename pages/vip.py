import streamlit as st
from datetime import datetime, timedelta
import pytz

# =====================================================
# 頁面設定
# =====================================================

st.set_page_config(
    page_title="CCL-Live VIP會員中心",
    page_icon="👑",
    layout="wide"
)

# =====================================================
# 台北時區
# =====================================================

TW_TZ = pytz.timezone("Asia/Taipei")

today = datetime.now(TW_TZ)

# =====================================================
# CSS 美化
# =====================================================

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.hero-box{
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    padding:50px;
    border-radius:28px;
    color:white;
    margin-bottom:40px;
    box-shadow:0 12px 35px rgba(0,0,0,0.35);
}

.hero-title{
    font-size:3rem;
    font-weight:900;
    margin-bottom:25px;
    text-align:center;
}

.hero-sub{
    font-size:1.1rem;
    line-height:2.1;
    text-align:center;
}

.vip-badge{
    margin-top:25px;
    text-align:center;
    font-size:1rem;
    font-weight:bold;
    color:#ffe082;
}

.section-title{
    font-size:2rem;
    font-weight:900;
    margin-bottom:30px;
    color:#1E88E5;
}

.plan-card{
    background:white;
    padding:35px;
    border-radius:22px;
    box-shadow:0 8px 22px rgba(0,0,0,0.15);
    border:2px solid #f1f1f1;
    transition:0.2s;
    min-height:650px;
}

.plan-card:hover{
    transform:translateY(-5px);
}

.plan-title{
    font-size:1.8rem;
    font-weight:900;
    margin-bottom:20px;
    text-align:center;
}

.plan-price{
    font-size:2.5rem;
    font-weight:900;
    color:#ff9800;
    text-align:center;
    margin-bottom:10px;
}

.old-price{
    text-decoration:line-through;
    color:#999;
    text-align:center;
    margin-bottom:20px;
}

.plan-desc{
    line-height:2;
    font-size:1rem;
    color:#333;
}

.bottom-tip{
    margin-top:40px;
    padding:25px;
    border-radius:20px;
    background:#f5f8ff;
    line-height:2;
    border-left:8px solid #1E88E5;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# 優惠截止設定
# =====================================================

discount_end = TW_TZ.localize(
    datetime(2026, 7, 31, 23, 59, 59)
)

discount_active = today <= discount_end

# =====================================================
# 倒數開始
# =====================================================

countdown_start = discount_end - timedelta(days=10)

show_countdown = (
    today >= countdown_start
    and today <= discount_end
)

# =====================================================
# 價格切換
# =====================================================

if discount_active:

    month_price = "NT$299"
    month_old = "NT$499"

    season_price = "NT$599"
    season_old = "NT$1499"

    year_price = "NT$1188"
    year_old = "NT$3999"

    life_price = "NT$2500"
    life_old = "NT$12000"

else:

    month_price = "NT$499"
    month_old = ""

    season_price = "NT$1499"
    season_old = ""

    year_price = "NT$3999"
    year_old = ""

    life_price = "NT$12000"
    life_old = ""

# =====================================================
# 倒數功能
# =====================================================

countdown_html = ""

if show_countdown:

    remain = discount_end - today

    days = remain.days
    hours = remain.seconds // 3600
    minutes = (remain.seconds % 3600) // 60
    seconds = remain.seconds % 60

    countdown_html = f"""

    <div style="
    margin-top:30px;
    background:#ff1744;
    padding:22px;
    border-radius:20px;
    text-align:center;
    box-shadow:0 10px 25px rgba(0,0,0,0.25);
    ">

    <div style="
    font-size:1.5rem;
    font-weight:900;
    color:white;
    margin-bottom:15px;
    ">

    ⏰ 限時優惠最後倒數

    </div>

    <div style="
    font-size:2rem;
    font-weight:900;
    color:#fff176;
    ">

    {days} 天　
    {hours} 小時　
    {minutes} 分鐘　
    {seconds} 秒

    </div>

    </div>
    """

# =====================================================
# 返回首頁
# =====================================================

col_back, col_space = st.columns([2,8])

with col_back:
    if st.button("⬅ 返回主頁"):
        st.switch_page("ccl-live.py")

# =====================================================
# 主形象區
# =====================================================

st.markdown(f"""

st.markdown(f"""

<div class="hero-box" style="
background:
linear-gradient(
135deg,
#0b1f4d 0%,
#133c8b 45%,
#1f6bff 100%
);
padding:55px;
border-radius:30px;
box-shadow:0 14px 40px rgba(0,0,0,0.35);
border:1px solid rgba(255,255,255,0.12);
position:relative;
overflow:hidden;
">

<div style="
position:absolute;
right:-60px;
top:-60px;
width:240px;
height:240px;
background:rgba(255,255,255,0.05);
border-radius:50%;
"></div>

<div style="
position:absolute;
left:-40px;
bottom:-40px;
width:180px;
height:180px;
background:rgba(0,255,170,0.08);
border-radius:50%;
"></div>

<div style="
display:flex;
align-items:center;
justify-content:center;
gap:18px;
margin-bottom:20px;
flex-wrap:wrap;
">

<div style="
font-size:4rem;
filter:drop-shadow(0 4px 10px rgba(0,0,0,0.3));
">
⚽
</div>

<div style="
font-size:3.2rem;
font-weight:900;
color:white;
text-shadow:0 4px 12px rgba(0,0,0,0.35);
">

CCL-Live 會員升級中心

</div>

</div>

<div style="
text-align:center;
font-size:1.25rem;
font-weight:700;
color:#d9f3ff;
line-height:2.1;
margin-top:25px;
">

🎊 為慶祝本網站成立，特別推出限時優惠方案

</div>

<div style="
text-align:center;
margin-top:28px;
">

<span style="
background:linear-gradient(90deg,#00c853,#64dd17);
padding:12px 28px;
border-radius:999px;
font-size:1.1rem;
font-weight:900;
color:white;
box-shadow:0 6px 18px rgba(0,0,0,0.28);
">

優惠期間｜115年6月1日 ～ 115年7月31日

</span>

</div>

<div style="
margin-top:42px;
background:rgba(255,255,255,0.08);
padding:30px;
border-radius:22px;
backdrop-filter:blur(10px);
border:1px solid rgba(255,255,255,0.1);
">

<div style="
text-align:center;
font-size:1.5rem;
font-weight:900;
color:#fff176;
margin-bottom:25px;
">

升級會員後，即可享有

</div>

<div style="
display:grid;
grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
gap:18px;
font-size:1.08rem;
font-weight:700;
line-height:2;
color:white;
">

<div>✔ 雲端保存報表數據</div>
<div>✔ 長期歷史分析功能</div>
<div>✔ 多帳本管理系統</div>
<div>✔ 會員專屬統計工具</div>
<div>✔ VIP 專屬功能優先使用權</div>
<div>✔ 未來功能永久更新支援</div>

</div>

</div>

<div style="
margin-top:35px;
text-align:center;
font-size:1rem;
font-weight:800;
color:#90caf9;
letter-spacing:1px;
">

CCL-Live Verified Membership

</div>

{countdown_html}

</div>

""", unsafe_allow_html=True)

# =====================================================
# 方案區
# =====================================================

st.markdown(
    '<div class="section-title">🚀 選擇您的會員方案</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

# =====================================================
# 月費
# =====================================================

with col1:

    st.markdown(f"""

    <div class="plan-card">

    <div class="plan-title">
    🗓 月費方案
    </div>

    <div class="plan-price">
    {month_price}
    </div>

    <div class="old-price">
    {month_old}
    </div>

    <div class="plan-desc">

    ✔ 每月自動續用<br>
    ✔ 保存個人報表數據<br>
    ✔ 雲端同步管理<br>
    ✔ 完整統計分析功能

    </div>

    </div>

    """, unsafe_allow_html=True)

# =====================================================
# 季費
# =====================================================

with col2:

    st.markdown(f"""

    <div class="plan-card">

    <div class="plan-title">
    🏆 季費方案
    </div>

    <div class="plan-price">
    {season_price}
    </div>

    <div class="old-price">
    {season_old}
    </div>

    <div class="plan-desc">

    ✔ 一次享有三個月<br>
    ✔ 平均每月更便宜<br>
    ✔ 推薦熱門方案<br>
    ✔ 適合長期使用者

    </div>

    </div>

    """, unsafe_allow_html=True)

# =====================================================
# 年費
# =====================================================

with col3:

    st.markdown(f"""

    <div class="plan-card">

    <div class="plan-title">
    💎 年費 VIP
    </div>

    <div class="plan-price">
    {year_price}
    </div>

    <div class="old-price">
    {year_old}
    </div>

    <div class="plan-desc">

    ✔ 超高 CP 值方案<br>
    ✔ 專屬會員功能<br>
    ✔ 優先開放新功能<br>
    ✔ 長期專業使用推薦

    </div>

    </div>

    """, unsafe_allow_html=True)

# =====================================================
# 終身
# =====================================================

with col4:

    st.markdown(f"""

    <div class="plan-card">

    <div class="plan-title">
    👑 終身至尊版
    </div>

    <div class="plan-price">
    {life_price}
    </div>

    <div class="old-price">
    {life_old}
    </div>

    <div class="plan-desc">

    ✔ 一次付費永久使用<br>
    ✔ 永久更新權限<br>
    ✔ 未來功能免費升級<br>
    ✔ 最高級 VIP 身分

    </div>

    </div>

    """, unsafe_allow_html=True)

# =====================================================
# 底部說明
# =====================================================

st.markdown("""

<div class="bottom-tip">

⚡ 免費版僅供測試使用，離開頁面後將不保存資料。<br><br>

⚡ 升級會員後，即可永久保存個人數據與報表內容。<br><br>

⚡ 金流付款功能後續將由綠界科技正式串接。

</div>

""", unsafe_allow_html=True)