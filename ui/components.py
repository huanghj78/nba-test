import streamlit as st
import plotly.graph_objects as go

def render_player_card(name, position, score, vector, dimensions):
    st.markdown(f"""
    <div class="player-card">
        <div class="player-position">{position}</div>
        <div class="player-name">{name}</div>
        <div class="match-rate">匹配度 {score:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🧬 属性能力值")

    for dim, val in zip(dimensions, vector):
        st.markdown(f"""
        <div>{dim} {val}</div>
        <div class="stat-bar">
            <div class="stat-fill" style="width:{val}%;"></div>
        </div>
        """, unsafe_allow_html=True)


def radar_chart(user_vec, star_vec, dimensions, star_name):
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=user_vec,
        theta=dimensions,
        fill='toself',
        name='你',
        line=dict(color='#00f5ff')
    ))

    fig.add_trace(go.Scatterpolar(
        r=star_vec,
        theta=dimensions,
        fill='toself',
        name=star_name,
        line=dict(color='#ff2e63')
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,100],
                gridcolor="rgba(255,255,255,0.1)"
            )
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        showlegend=True
    )

    st.plotly_chart(fig, use_container_width=True)


def render_top3(results):
    st.markdown("## 🏆 Top 3 匹配")

    cols = st.columns(3)
    for i in range(3):
        name, score = results[i]
        with cols[i]:
            st.markdown(f"""
            <div class="mini-card">
                <div style="font-weight:bold;">{name}</div>
                <div>{score*100:.1f}%</div>
            </div>
            """, unsafe_allow_html=True)