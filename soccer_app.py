import streamlit as st

st.set_page_config(
    page_title="CCL-Live 體育賽事管理系統",
    page_icon="⚽",
    layout="wide"
)

# =========================
# CSS 美化
# =========================
st.markdown("""
<style>

.main {
    background:#f5f7fb;
}

.hero {
    background: linear-gradient(135deg,#0f172a,#1e3a8a);
    border-radius:30px;
    padding:60px;
    color:white;
    text-align:center;
    margin-bottom:40px;
    box-shadow:0 10px 30px rgba(0,0,0,0.2);
}

.hero-title {
    font-size:72px;
    font-weight:900;
    margin-bottom:20px;
}

.hero-sub {
    font-size:28px;
    color:#dbeafe;
    margin-bottom:40px;
}

.hero-btn {
    display:inline-block;
    background:white;
    color:#1d4ed8;
    padding:18px 40px;
    border-radius:18px;
    text-decoration:none;
    font-size:24px;
    font-weight:bold;
}

.section-title {
    font-size:42px;
    font-weight:900;
    margin-top:50px;
    margin-bottom:30px;
    color:#0f172a;
}

.grid {
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:25px;
}

.card {
    background:white;
    border-radius:22px;
    padding:30px;
    box-shadow:0 4px 18px rgba(0,0,0,0.08);
    transition:0.3s;
}
""", unsafe_allow_html=True)