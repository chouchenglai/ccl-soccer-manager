import streamlit as st
import streamlit.components.v1 as components

# 1. 頁面基礎設定
st.set_page_config(page_title="網站維護中 - CCL-Soccer", page_icon="⚙️", layout="centered")

# 2. 隱藏所有 Streamlit 預設組件 (選單、註腳、頂部導覽)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        background: transparent;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 嵌入美化過的維護 HTML 頁面
components.html("""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>網站維護中 - CCL-Soccer</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            text-align: center;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(15px);
            padding: 60px 40px;
            border-radius: 30px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.3);
            border: 1px solid rgba(255, 255, 255, 0.2);
            max-width: 600px;
            width: 90%;
        }
        .logo {
            font-size: 56pt;
            font-weight: 900;
            color: #00d2ff;
            text-shadow: 0 0 30px rgba(0, 210, 255, 0.6);
            margin-bottom: 5px;
            letter-spacing: 5px;
        }
        .subtitle {
            font-size: 14pt;
            color: #bdc3c7;
            margin-bottom: 30px;
            letter-spacing: 2px;
            font-weight: 300;
        }
        .illustration {
            margin: 40px 0;
        }
        svg {
            width: 140px;
            height: 140px;
            fill: #00d2ff;
            filter: drop-shadow(0 0 10px rgba(0,210,255,0.4));
            animation: rotate 6s linear infinite;
        }
        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        h1 {
            font-size: 26pt;
            margin-bottom: 20px;
            font-weight: 700;
        }
        p {
            font-size: 13pt;
            line-height: 1.8;
            color: #ecf0f1;
            font-weight: 300;
        }
        .status-badge {
            display: inline-block;
            background: #e67e22;
            color: #fff;
            padding: 8px 25px;
            border-radius: 50px;
            font-size: 11pt;
            font-weight: bold;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(230,126,34,0.4);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">CCL</div>
        <div class="subtitle">SOCCER SYSTEM</div>
        
        <div class="illustration">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.07-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.13,5.91,7.62,6.29L5.23,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.72,8.87 c-0.11,0.21-0.06,0.47,0.12,0.61l2.03,1.58C4.82,11.36,4.8,11.68,4.8,12c0,0.33,0.02,0.64,0.07,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.44-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.11-0.21,0.06-0.47-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/>
            </svg>
        </div>

        <div class="status-badge">SYSTEM MAINTENANCE</div>
        <h1>網站維護進行中</h1>
        <p>
            為了提供更優質的賽事管理體驗，<br>
            CCL-Soccer 正在進行系統優化與數據維護。<br>
            目前暫時關閉運作，請稍後再回來查看。呵呵！！！
        </p>
        <p style="margin-top: 40px; font-size: 10pt; color: #bdc3c7;">
            © 2026 CCL-Soccer | 專業足球數據管理系統
        </p>
    </div>
</body>
</html>
""", height=1000, scrolling=False)
