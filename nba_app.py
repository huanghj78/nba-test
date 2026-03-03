import streamlit as st
import plotly.graph_objects as go
import random
import time

# --- 1. 页面配置 ---
st.set_page_config(page_title="NBA 灵魂匹配", page_icon="🏀", layout="centered")

# --- 2. 炫酷 CSS 注入 ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .scanning {
        height: 4px;
        background: linear-gradient(to right, rgba(29, 66, 138, 0), #c8102e, rgba(29, 66, 138, 0));
        position: relative;
        animation: scan 2s linear infinite;
        box-shadow: 0 0 15px #c8102e;
    }
    @keyframes scan { 0% { top: 0px; } 100% { top: 200px; } }
    .neon-box {
        padding: 20px; border-radius: 15px; background: #111;
        border: 2px solid #1d428a; text-align: center; margin-bottom: 20px;
    }
    .star-name {
        font-family: 'Arial Black', sans-serif; font-size: 40px;
        background: linear-gradient(90deg, #fff, #1d428a, #c8102e);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 50位球星数据库 ---
star_database = {
    "控球后卫 (PG)": ["斯蒂芬·库里", "魔术师约翰逊", "克里斯·保罗", "凯里·欧文", "达米安·利拉德", "拉塞尔·威斯布鲁克", "谢伊·亚历山大", "卢卡·东契奇", "特雷·杨", "约翰·斯托克顿"],
    "得分后卫 (SG)": ["科比·布莱恩特", "迈克尔·乔丹", "阿伦·艾弗森", "詹姆斯·哈登", "德文·布克", "克莱·汤普森", "雷·阿伦", "安东尼·爱德华兹", "多诺万·米切尔", "德维恩·韦德"],
    "小前锋 (SF)": ["勒布朗·詹姆斯", "凯文·杜兰特", "卡哇伊·莱昂纳德", "杰森·塔图姆", "吉米·巴特勒", "斯科蒂·皮蓬", "保罗·乔治", "卡梅隆·安东尼", "布兰登·英格拉姆", "安德鲁·维金斯"],
    "大前锋 (PF)": ["蒂姆·邓肯", "扬尼斯·阿德托昆博", "凯文·加内特", "德克·诺维茨基", "安东尼·戴维斯", "锡安·威廉姆森", "保罗·班凯罗", "德雷蒙德·格林", "小贾巴里·帕克", "卡尔·马龙"],
    "中锋 (C)": ["尼古拉·约基奇", "乔尔·恩比德", "沙奎尔·奥尼尔", "维克托·文班亚马", "切特·霍姆格伦", "巴姆·阿德巴约", "多曼塔斯·萨博尼斯", "鲁迪·戈贝尔", "卡尔·安东尼·唐斯", "帕特里克·尤因"]
}

# --- 4. 界面设计 ---
st.title("🏀 NBA 灵魂匹配 (50人深度版)")
st.write("系统将通过 10 个心理偏好维度，检索最契合你的巨星基因。")

with st.form("deep_test"):
    pos = st.selectbox("📍 预设位置 (选择你在场上的倾向)", list(star_database.keys()))
    
    ans_list = []
    questions = [
        "1. 在团队项目中，你更享受？", "2. 面对高压环境，你的本能反应是？", "3. 你最希望拥有哪种天赋？",
        "4. 你的沟通风格更倾向于？", "5. 遇到困难时，你第一反应是？", "6. 你更看重什么样的成就感？",
        "7. 在陌生的社交场合，你会？", "8. 你对'力量'的理解更倾向于？", "9. 你理想的工作方式是？",
        "10. 如果人生是一场游戏，你希望自己是？"
    ]
    options = [["A. 掌控全局", "B. 一击制胜", "C. 默默支撑"], ["A. 寻找策略", "B. 正面硬刚", "C. 稳住心态"]] * 5 # 简化示意

    for i in range(10):
        a = st.radio(questions[i], ["A. 偏向灵巧与策略", "B. 偏向爆发与主宰", "C. 偏向稳定与基石"], key=f"q{i}")
        ans_list.append(a)
    
    # 这一行是关键：定义 submitted 变量
    submitted = st.form_submit_button("🚀 开启基因扫描")

# --- 5. 结果处理 (确保在 form 之外，逻辑紧随其后) ---
if submitted:
    # 动画转场
    st.markdown("<div class='scanning'></div>", unsafe_allow_html=True)
    status = st.empty()
    bar = st.progress(0)
    for p in range(1, 101, 20):
        status.markdown(f"`⚡ 正在分析基因序列... {p}%`")
        bar.progress(p)
        time.sleep(0.3)
    status.empty()
    bar.empty()

    # 简单计算匹配索引
    a_count = sum(1 for x in ans_list if "A" in x)
    b_count = sum(1 for x in ans_list if "B" in x)
    
    candidates = star_database[pos]
    # 根据 A/B/C 的比例决定取 10 人名单中的哪一位
    if a_count >= 5: idx = random.randint(0, 3)
    elif b_count >= 5: idx = random.randint(4, 6)
    else: idx = random.randint(7, 9)
    
    target = candidates[idx]
    base_val = [random.randint(88, 99) for _ in range(5)]

    # 展示结果
    st.markdown(f"""<div class="neon-box">
        <p style='color: #888; letter-spacing: 2px;'>LEGEND DETECTED</p>
        <h1 class="star-name">{target}</h1>
    </div>""", unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1.2])
    with c1:
        st.write("### 🧬 属性报告")
        st.metric("基因同步率", f"{random.randint(94, 99)}%")
        attrs = ['意识', '侵略性', '稳定性', '技巧性', '影响力']
        for a, v in zip(attrs, base_val):
            st.write(f"**{a}**: `{v}`")

    with c2:
        fig = go.Figure(go.Scatterpolar(r=base_val, theta=['意识', '侵略性', '稳定性', '技巧性', '影响力'], fill='toself', line_color='#c8102e'))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False, paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)

    st.success("✅ 测评完成！截图分享到小红书。")