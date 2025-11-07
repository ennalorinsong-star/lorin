import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

st.set_page_config(page_title="🌍 MBTI by Country", layout="centered")

# 제목
st.title("🌍 국가별 MBTI 비율 시각화")
st.markdown("**국가를 선택하면 그 나라의 MBTI 분포를 볼 수 있어요!**")

# 국가 선택
country_list = df["Country"].sort_values().tolist()
selected_country = st.selectbox("국가 선택", country_list, index=country_list.index("Korea") if "Korea" in country_list else 0)

# 선택한 국가 데이터 추출
country_data = df[df["Country"] == selected_country].iloc[0, 1:]
sorted_data = country_data.sort_values(ascending=False)

# 색상 설정: 1등은 빨간색, 나머지는 회색 그라데이션
colors = ["#ff4d4d"] + [f"rgba(160,160,160,{0.9 - i*0.04})" for i in range(len(sorted_data) - 1)]

# 그래프 생성
fig = go.Figure(
    data=[
        go.Bar(
            x=sorted_data.index,
            y=sorted_data.values,
            marker_color=colors,
            text=[f"{v*100:.2f}%" for v in sorted_data.values],
            textposition="outside",
        )
    ]
)

fig.update_layout(
    title=f"🇨🇳 {selected_country}의 MBTI 비율",
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    template="plotly_white",
    showlegend=False,
    margin=dict(l=30, r=30, t=60, b=30),
)

# 그래프 표시
st.plotly_chart(fig, use_container_width=True)

# 추가 정보
st.markdown("---")
st.caption("💡 데이터: countriesMBTI_16types.csv  |  시각화: Plotly + Streamlit")
