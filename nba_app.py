import streamlit as st
import time

from data.stars import STAR_POSITIONS, STAR_VECTORS, DIMENSIONS
from data.questions import QUESTIONS
from logic.scoring import calculate_user_vector, match_stars
from ui.style import inject_style
from ui.components import render_player_card, radar_chart, render_top3

st.set_page_config(page_title="NBA 灵魂匹配", page_icon="🏀")

inject_style()

st.title("🏀 NBA 灵魂匹配 50人版")

position = st.selectbox("选择你倾向的位置", list(STAR_POSITIONS.keys()))

with st.form("test"):
    answers = []
    for i, q in enumerate(QUESTIONS):
        choice = st.radio(
            q["question"],
            list(q["options"].keys()),
            format_func=lambda x: q["options"][x]["text"],
            key=i
        )
        answers.append(choice)
    submit = st.form_submit_button("开始匹配")

if submit:
    with st.spinner("正在扫描篮球基因..."):
        time.sleep(1.5)

    user_vec = calculate_user_vector(answers, QUESTIONS)
    results = match_stars(user_vec, STAR_VECTORS, position)

    best_name, best_score = results[0]
    best_vector = STAR_VECTORS[best_name]["vector"]

    render_player_card(
        best_name,
        position,
        best_score*100,
        best_vector,
        DIMENSIONS
    )

    st.subheader("📊 属性雷达对比")
    radar_chart(user_vec, best_vector, DIMENSIONS, best_name)

    render_top3(results)