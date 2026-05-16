# ================================
# CCL-Live VIP 升級中心
# pages/vip.py
# ================================

import streamlit as st
from datetime import datetime
import pytz

# ================================
# 台北時區
# ================================

taipei_tz = pytz.timezone("Asia/Taipei")
now = datetime.now(taipei_tz)

# ================================
# 優惠日期設定
# ================================

discount_start = taipei_tz.localize(
    datetime(2026, 6, 1, 0, 0, 0)
)

discount_end = taipei_tz.localize(
    datetime(2026, 7, 31, 23, 59, 59)
)

discount_active = discount_start <= now <= discount_end

# ================================
# 倒數計時
# ================================

countdown_html = ""

if discount_active:

    remaining = discount_end - now

    if remaining.days <= 10:

        total_seconds = int(remaining.total_seconds())

        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        countdown_html = f"""
        <div style="
            background:linear-gradient(90deg,#00c853,#64dd17);
            padding:14px 32px;
            border-radius:999px;
            font-size:1.05rem;
            font-weight:900;
            color:#ffffff;
            text-shadow:0 2px 8px rgba(0,0,0,0.55);
            display:inline-block;
            margin-top:20px;
            box-shadow:0 6px 18px rgba(0,0,0,0.35);
        ">
        ⏰ 限時優惠倒數：
        {days}天 {hours}小時 {minutes}分鐘 {seconds}秒
        </div>
        """

# ================================
# 頁面設定
# ================================

st.set_page_config(
    page_title="CCL-Live VIP",
    layout="wide"
)

# ================================
# CSS
# ================================

st.markdown("""
<style>

body{
    background:#f5f7fb;
}

.vip-header{
    background:linear-gradient(135deg,#0d2c75,#2450c4);
    border-radius:35px;
    padding:70px 50px;
    text-align:center;
    color:white;
    position:relative;
    overflow:hidden;
    box-shadow:0 15px 40px rgba(0,0,0,0.25);
}

.vip-header::after{
    content:'';
    position:absolute;
    width:320px;
    height:320px;
    background:rgba(255,255,255,0.06);
    border-radius:50%;
    top:-120px;
    right:-80px;
}

.vip-title{
    font-size:3.3rem;
    font-weight:900;
    margin-bottom:30px;
}

.vip-subtitle{
    font-size:1.3rem;
    margin-top:20px;
    margin-bottom:25px;
}

.vip-feature-box{
    background:rgba(255,255,255,0.08);
    border-radius:30px;
    padding:45px;
    margin-top:55px;
}

.vip-feature-title{
    color:#ffe95c;
    font-size:2rem;
    font-weight:900;
    margin-bottom:30px;
}

.feature-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:20px;
    margin-top:30px;
}

.feature-item{
    font-size:1.35rem;
    font-weight:700;
    text-align:left;
}

.plan-card{
    background:white;
    border-radius:30px;
    padding:40px;
    box-shadow:0 8px 25px rgba(0,0,0,0.12);
    min-height:700px;
}

.plan-title{
    font-size:2.8rem;
    font-weight:900;
    color:#1a2a4d;
    line-height:1.25;
}

.old-price{
    color:#888;
    font-size:1.4rem;
    text-decoration:line-through;
    margin-top:20px;
}

.new-price{
    color:#e53935;
    font-size:3.5rem;
    font-weight:900;
    margin-top:12px;
}

.save-badge{
    background:#ffe32b;
    display:inline-block;
    padding:12px 24px;
    border-radius:999px;
    font-weight:900;
    margin-top:18px;
    color:black;
}

.plan-features{
    margin-top:35px;
    font-size:1.3rem;
    line-height:2.1;
}

.upgrade-btn{
    background:#1976d2;
    color:white;
    padding:18px 36px;
    border-radius:18px;
    font-size:1.35rem;
    font-weight:900;
    text-align:center;
    margin-top:35px;
}

hr{
    margin-top:30px;
    margin-bottom:30px;
}

</style>
""", unsafe_allow_html=True)

# ================================
# 頂部
# ================================

st.markdown(f"""
<div class="vip-header">

<div class="vip-title">
⚽ CCL-Live 帳號升級中心
</div>

<div class="vip-subtitle">
🎊 為慶祝本網站成立，特別推出限時優惠方案
</div>

{countdown_html}

<div style="
margin-top:28px;
font-size:1.2rem;
font-weight:700;
color:white;
">
優惠期間｜115年6月1日 ～ 115年7月31日
</div>

<div class="vip-feature-box">

<div class="vip-feature-title">
升級會員後，即可享有
</div>

<div class="feature-grid">

<div class="feature-item">
✔ 雲端保存報表數據
</div>

<div class="feature-item">
✔ 長期歷史分析功能
</div>

<div class="feature-item">
✔ 多帳本管理系統
</div>

<div class="feature-item">
✔ 會員專屬統計工具
</div>

<div class="feature-item">
✔ VIP 專區功能優先使用權
</div>

<div class="feature-item">
✔ 未來功能永久更新支援
</div>

</div>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ================================
# 價格方案
# ================================

col1, col2, col3, col4 = st.columns(4)

# ================================
# 月費
# ================================

with col1:

    st.markdown("""
    <div class="plan-card">

    <div class="plan-title">
    月費會員
    </div>

    <div class="old-price">
    原價 NT$ 399 / 月
    </div>

    <div class="new-price">
    NT$ 299
    </div>

    <div class="save-badge">
    現省 NT$100
    </div>

    <hr>

    <div class="plan-features">
    ✓ 雲端保存報表<br>
    ✓ 模擬倉永久保存<br>
    ✓ 會員統計功能
    </div>

    <div class="upgrade-btn">
    立即升級
    </div>

    </div>
    """, unsafe_allow_html=True)

# ================================
# 季費
# ================================

with col2:

    st.markdown("""
    <div class="plan-card">

    <div class="plan-title">
    季費會員
    </div>

    <div class="old-price">
    原價 NT$ 897 / 3個月
    </div>

    <div class="new-price">
    NT$ 597
    </div>

    <div class="save-badge">
    現省 NT$300
    </div>

    <hr>

    <div class="plan-features">
    ✓ 最熱門方案<br>
    ✓ 長期分析功能<br>
    ✓ 專屬會員工具
    </div>

    <div class="upgrade-btn">
    立即升級
    </div>

    </div>
    """, unsafe_allow_html=True)

# ================================
# 年費
# ================================

with col3:

    st.markdown("""
    <div class="plan-card">

    <div class="plan-title">
    年費會員
    </div>

    <div class="old-price">
    原價 NT$ 3588 / 年
    </div>

    <div class="new-price">
    NT$ 1188
    </div>

    <div class="save-badge">
    超值優惠
    </div>

    <hr>

    <div class="plan-features">
    ✓ 高 CP 值方案<br>
    ✓ 完整 VIP 功能<br>
    ✓ 優先體驗更新
    </div>

    <div class="upgrade-btn">
    立即升級
    </div>

    </div>
    """, unsafe_allow_html=True)

# ================================
# 終身
# ================================

with col4:

    st.markdown("""
    <div class="plan-card">

    <div class="plan-title">
    終身會員
    </div>

    <div class="old-price">
    原價 NT$ 6999
    </div>

    <div class="new-price">
    NT$ 2500
    </div>

    <div class="save-badge">
    永久使用
    </div>

    <hr>

    <div class="plan-features">
    ✓ 永久免續費<br>
    ✓ 所有 VIP 功能<br>
    ✓ 未來更新永久支援
    </div>

    <div class="upgrade-btn">
    永久升級
    </div>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 底部資訊
# =========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.info("💡 綠界金流付款功能，可於後續直接串接至本頁按鈕。")

st.markdown("""

<div style="
text-align:center;
color:#777;
padding:30px;
font-size:0.95rem;
">

Copyright © 2026 CCL-Live 體育賽事管理系統

</div>

""", unsafe_allow_html=True)