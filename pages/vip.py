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