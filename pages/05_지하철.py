import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# 데이터 불러오기
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("qwertyuiop.csv", encoding="cp949")
    df["사용일자"] = df["사용일자"].astype(str)
    return df

df = load_data()

st.title("🚇 2025년 10월 지하철 승하차 분석 대시보드")

# 날짜 선택
date_list = sorted(df["사용일자"].unique())
selected_date = st.selectbox("📅 날짜 선택", date_list)

# 노선 선택
line_list = sorted(df["노선명"].unique())
selected_line = st.selectbox("🚇 호선 선택", line_list)

# -------------------------------
# 데이터 필터링
# -------------------------------
filtered = df[(df["사용일자"] == selected_date) & (df["노선명"] == selected_line)].copy()

# 승하차 합계 계산
filtered["총승하차"] = filtered["승차총승객수"] + filtered["하차총승객수"]

# 상위 10개 역 추출
top10 = filtered.sort_values("총승하차", ascending=False).head(10)

# -------------------------------
# 색상 설정 (1등 빨강, 나머지 파란 → 흐려짐 그라데이션)
# -------------------------------
colors = ["red"]  # 1등은 빨강

import numpy as np

# 9개 남은 바를 파란색 그라데이션으로 생성
gradient = np.linspace(1, 0.2, len(top10) - 1)  
for g in gradient:
    colors.append(f"rgba(0, 0, 255, {g})")

# -------------------------------
# 그래프 생성
# -------------------------------
fig = px.bar(
    top10,
    x="역명",
    y="총승하차",
    title=f"{selected_date} · {selected_line} 상위 10개 역 승하차량",
)

fig.update_traces(marker_color=colors)

fig.update_layout(
    xaxis_title="역명",
    yaxis_title="총 승하차 인원",
    title_font_size=20
)

st.plotly_chart(fig, use_container_width=True)

# 데이터 미리보기
with st.expander("📄 데이터 보기"):
    st.dataframe(top10)
