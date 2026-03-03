import streamlit as st
import plotly.graph_objects as go

# --- 1. 页面配置 ---
st.set_page_config(page_title="NBA灵魂球星匹配", page_icon="🏀", layout="wide")

# --- 2. 注入自适应样式 ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #1d428a, #c8102e);
        color: white; border: none; width: 100%; height: 3em;
        font-size: 20px; font-weight: bold; border-radius: 10px;
    }
    .result-text { font-size: 24px; font-weight: bold; color: #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 核心数据定义 ---
def get_star_result(tag):
    stars = {
        "Curry": {
            "name": "斯蒂芬·库里 (Stephen Curry)",
            "values": [99, 92, 70, 75, 88], # 得分, 传球, 防守, 力量, 意识
            "color": "#1d428a",
            "desc": "你是【划时代的狙击手】！你用无解的三分和灵动的跑位解构了防守。只要你过半场，对手就得窒息。"
        },
        "Kobe": {
            "name": "科比·布莱恩特 (Kobe Bryant)",
            "values": [98, 80, 95, 90, 100],
            "color": "#552583",
            "desc": "你是【曼巴精神的化身】！偏执的努力、无解的单打是你的勋章。在你的字典里，从来没有'认输'二字。"
        },
        "LeBron": {
            "name": "勒布朗·詹姆斯 (LeBron James)",
            "values": [95, 98, 92, 99, 96],
            "color": "#c8102e",
            "desc": "你是【球场全能国王】！你拥有坦克般的身体和上帝视角。你是球队的绝对核心，能用一百种方式赢下比赛。"
        }
    }
    return stars[tag]

# --- 4. 绘制雷达图函数 ---
def draw_radar(data):
    categories = ['得分', '传球', '防守', '身体素质', '篮球智商']
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=data['values'], theta=categories, fill='toself',
        name=data['name'], line_color=data['color']
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False, height=450,
        margin=dict(l=80, r=80, t=20, b=20)
    )
    return fig

# --- 5. 交互界面 ---
st.title("🏀 NBA 灵魂球星匹配测试")
st.write("想知道你的球风最像哪位巨星？完成测试，生成专属战力雷达图！")

with st.sidebar:
    st.header("⚙️ 个人偏好设置")
    difficulty = st.slider("你的实战对抗强度", 1, 10, 5)
    st.info("设置会微调最终的战力值")

# 测试表单
with st.container():
    col_q1, col_q2 = st.columns(2)
    with col_q1:
        q1 = st.radio("1. 你的第一进攻选择是？", ["超远三分", "后仰跳投/突破", "冲击篮下强打"])
    with col_q2:
        q2 = st.radio("2. 关键时刻你会？", ["拉开单干，投绝杀球", "吸引包夹，助攻队友", "制造杀伤，走上罚球线"])
    
    q3 = st.select_slider("3. 你的防守投入度有多高？", options=["眼神防守", "中规中矩", "死亡缠绕"])

# 生成结果
if st.button("🚀 点击生成我的球员档案"):
    # 简单的匹配逻辑判别
    if "三分" in q1: result_tag = "Curry"
    elif "后仰" in q1 or "单干" in q2: result_tag = "Kobe"
    else: result_tag = "LeBron"
    
    data = get_star_result(result_tag)
    
    st.divider()
    
    # 结果展示区
    res_col1, res_col2 = st.columns([1, 1.2])
    
    with res_col1:
        st.markdown(f"### 匹配结果：\n<p class='result-text'>{data['name']}</p>", unsafe_allow_html=True)
        st.write(data['desc'])
        st.metric("核心能力评分 (OVR)", value=int(sum(data['values'])/5 + difficulty))
        st.success("💡 你的球风非常适合目前的快节奏小球体系！")
        
    with res_col2:
        st.plotly_chart(draw_radar(data), use_container_width=True)

    st.balloons()