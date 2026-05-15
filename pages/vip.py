# =====================================================
# 自動限時優惠設定（台北時區）
# =====================================================

from datetime import datetime, timedelta
import pytz

TW_TZ = pytz.timezone("Asia/Taipei")

today = datetime.now(TW_TZ)

# =====================================================
# 優惠截止時間（台北時間）
# =====================================================

discount_end = TW_TZ.localize(
    datetime(2026, 7, 31, 23, 59, 59)
)

discount_active = today <= discount_end

# =====================================================
# 最後10天倒數判定
# =====================================================

countdown_start = discount_end - timedelta(days=10)

show_countdown = (
    today >= countdown_start
    and today <= discount_end
)

# =====================================================
# 價格自動切換
# =====================================================

if discount_active:

    month_price = "NT$299"
    month_old = "NT$499"

    year_price = "NT$1999"
    year_old = "NT$3999"

    life_price = "NT$4999"
    life_old = "NT$12000"

    # =================================================
    # 倒數時間
    # =================================================

    if show_countdown:

        remain = discount_end - today

        days = remain.days
        hours = remain.seconds // 3600
        minutes = (remain.seconds % 3600) // 60
        seconds = remain.seconds % 60

        countdown_html = f"""

        <div style="
        margin-top:20px;
        background:rgba(0,0,0,0.22);
        padding:18px;
        border-radius:16px;
        border:1px solid rgba(255,255,255,0.12);
        ">

        <div style="
        font-size:1.35rem;
        font-weight:900;
        color:#fff176;
        margin-bottom:10px;
        ">

        ⏰ 限時優惠最後倒數

        </div>

        <div style="
        font-size:1.6rem;
        font-weight:900;
        color:white;
        line-height:1.8;
        text-shadow:0 2px 8px rgba(0,0,0,0.3);
        ">

        {days} 天　
        {hours} 小時　
        {minutes} 分鐘　
        {seconds} 秒

        </div>

        </div>

        """

    else:

        countdown_html = ""

    promo_html = f"""

    <br><br>

    <div style="
    background: linear-gradient(90deg,#ff9800,#ff5722);
    padding:24px;
    border-radius:20px;
    margin-top:25px;
    box-shadow:0 10px 28px rgba(0,0,0,0.28);
    border:2px solid rgba(255,255,255,0.15);
    ">

    <div style="
    font-size:1.65rem;
    font-weight:900;
    color:white;
    margin-bottom:10px;
    text-shadow:0 2px 10px rgba(0,0,0,0.35);
    ">

    🎊 慶祝 CCL-Live 平臺正式成立

    </div>

    <div style="
    font-size:1.15rem;
    font-weight:800;
    margin-bottom:16px;
    color:#fff8dc;
    line-height:1.8;
    ">

    特別推出創站限時優惠方案

    </div>

    <div style="
    font-size:1rem;
    font-weight:700;
    margin-bottom:18px;
    color:white;
    background:rgba(255,255,255,0.12);
    padding:10px 16px;
    border-radius:12px;
    display:inline-block;
    ">

    優惠期間｜115.06.01 ～ 115.07.31

    </div>

    <div style="
    color:white;
    font-size:1.05rem;
    line-height:2.2;
    margin-top:12px;
    ">

    💎 專業月費版：
    <span style="text-decoration:line-through; opacity:0.75;">
    {month_old}
    </span>
    →
    <b style="font-size:1.2rem;">
    {month_price}
    </b><br>

    🏆 年度 VIP：
    <span style="text-decoration:line-through; opacity:0.75;">
    {year_old}
    </span>
    →
    <b style="font-size:1.2rem;">
    {year_price}
    </b><br>

    🌟 終身至尊版：
    <span style="text-decoration:line-through; opacity:0.75;">
    {life_old}
    </span>
    →
    <b style="font-size:1.2rem; color:#ffe082;">
    {life_price}
    </b>

    </div>

    {countdown_html}

    <div style="
    margin-top:22px;
    font-size:0.96rem;
    color:#fff3e0;
    line-height:1.8;
    ">

    ⚡ 開站期間限定優惠，活動截止後將恢復原價。<br>
    ⚡ 現在加入即可立即享有完整會員功能與未來更新權限。

    </div>

    </div>

    """

else:

    month_price = "NT$499"
    year_price = "NT$3999"
    life_price = "NT$12000"

    promo_html = """

    <br><br>

    <div style="
    background: linear-gradient(90deg,#1e3c72,#2a5298);
    padding:22px;
    border-radius:18px;
    margin-top:25px;
    box-shadow:0 10px 28px rgba(0,0,0,0.25);
    ">

    <div style="
    font-size:1.5rem;
    font-weight:900;
    color:white;
    margin-bottom:12px;
    ">

    👑 CCL-Live 專業會員服務

    </div>

    <div style="
    color:#dbe7ff;
    line-height:2;
    font-size:1rem;
    ">

    感謝所有會員支持與使用。<br>
    平臺將持續更新更多高級功能與數據分析服務。

    </div>

    </div>

    """

# =====================================================
# 主形象區
# =====================================================

st.markdown(f"""
<div class="hero-box">

<div class="hero-title">
👑 CCL-Live 會員升級中心
</div>

<div class="hero-sub">
打造專屬於您的體育數據分析平台。<br>
升級會員後，即可享有：<br><br>

✔ 雲端保存賽事數據<br>
✔ 長期歷史分析紀錄<br>
✔ 多帳本管理系統<br>
✔ 會員專屬功能與統計工具<br>
✔ 未來 VIP 高級功能優先開放<br>
✔ 專屬身份標誌與高級權限

</div>

<div class="vip-badge">
CCL-Live Verified Membership
</div>

{promo_html}

</div>
""", unsafe_allow_html=True)

# =====================================================
# 會員方案標題
# =====================================================

st.markdown(
    '<div class="section-title">🚀 選擇您的會員方案</div>',
    unsafe_allow_html=True
)