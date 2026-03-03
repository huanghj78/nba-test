import streamlit as st

def inject_style():
    st.markdown("""
    <style>

    /* 整体背景 */
    .stApp {
        background: radial-gradient(circle at top left, #1a1a2e, #0e1117 60%);
        color: white;
    }

    /* 主标题 */
    h1 {
        text-align: center;
        font-size: 42px !important;
        background: linear-gradient(90deg, #ffffff, #1d428a, #c8102e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 30px;
    }

    /* 球星卡容器 */
    .player-card {
        padding: 30px;
        border-radius: 20px;
        background: linear-gradient(135deg, #1d428a, #c8102e);
        box-shadow: 0 0 25px rgba(200,16,46,0.7);
        text-align: center;
        margin-bottom: 25px;
        transition: 0.3s;
    }

    .player-card:hover {
        transform: scale(1.02);
        box-shadow: 0 0 40px rgba(200,16,46,1);
    }

    .player-name {
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .player-position {
        font-size: 18px;
        opacity: 0.8;
        margin-bottom: 10px;
    }

    .match-rate {
        font-size: 22px;
        font-weight: bold;
    }

    /* 属性条 */
    .stat-bar {
        background: #222;
        border-radius: 10px;
        margin: 6px 0;
        height: 12px;
        overflow: hidden;
    }

    .stat-fill {
        height: 12px;
        background: linear-gradient(90deg,#1d428a,#c8102e);
    }

    /* Top3 卡片 */
    .mini-card {
        padding: 15px;
        border-radius: 15px;
        background: #111;
        text-align: center;
        box-shadow: 0 0 10px rgba(255,255,255,0.1);
    }

    </style>
    """, unsafe_allow_html=True)