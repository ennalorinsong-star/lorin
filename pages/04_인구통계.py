import streamlit as st
import pandas as pd
import plotly.express as px
from io import StringIO

st.set_page_config(page_title="지역구별 나이별 인구 그래프", layout="wide")
st.title("📊 지역구별 나이별 인구수 — 인터랙티브 꺾은선 그래프")

st.write("CSV 파일에 `지역구`, `나이`, `인구수` 열이 포함되어야 합니다. (영문 컬럼명도 자동 인식됩니다.)")

# 파일 업로드
uploaded = st.file_uploader("📁 CSV 파일 업로드 (예: population.csv)", type=["csv"])

# CSV 읽기 함수 (인코딩 자동 감지)
def read_csv_auto(file):
    try:
        return pd.read_csv(file, encoding="utf-8")
    except UnicodeDecodeError:
        file.seek(0)
        return pd.read_csv(file, encoding="cp949")

# 데이터 불러오기
if uploaded is not None:
    try:
        df = read_csv_auto(uploaded)
        st.success("✅ CSV 파일을 성공적으로 불러왔습니다!")
    except Exception as e:
        st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")
        st.stop()
else:
    st.info("좌측 상단의 ‘Browse files’ 버튼을 눌러 CSV 파일을 업로드하세요.")
    st.stop()

# 컬럼 자동 매핑
col_map = {}
lower_cols = {c.lower(): c for c in df.columns}

# 지역구
for cand in ["지역구", "district", "sigungu", "구"]:
    if cand in df.columns:
        col_map["district"] = cand
        break
    if cand.lower() in lower_cols:
        col_map["district"] = lower_cols[cand.lower()]
        break

# 나이
for cand in ["나이", "age", "연령"]:
    if cand in df.columns:
        col_map["age"] = cand
        break
    if cand.lower() in lower_cols:
        col_map["age"] = lower_cols[cand.lower()]
        break

# 인구수
for cand in ["인구수", "population", "pop"]:
    if cand in df.columns:
        col_map["population"] = cand
        break
    if cand.lower() in lower_cols:
        col_map["population"] = lower_cols[cand.lower()]
        break

missing = [k for k in ["district", "age", "population"] if k not in col_map]
if missing:
    st.error(f"❌ 필요한 컬럼을 찾지 못했습니다: {missing}")
    st.stop()

# 컬럼명 표준화
df = df.rename(columns={
    col_map["district"]: "district",
    col_map["age"]: "age",
    col_map["population"]: "population"
})

# 타입 변환
df["population"] = pd.to_numeric(df["population"], errors="coerce")
df["age"] = df["age"].astype(str)
df = df.dropna(subset=["district", "age", "population"])

# 숫자 나이 정렬 시도
df["age_num"] = pd.to_numeric(df["age"].str.extract(r"(\\d+)")[0], errors="coerce")
df = df.sort_values(["district", "age_num"])

# 지역구 선택
districts = df["district"].unique().tolist()
selected = st.selectbox("🏙️ 지역구 선택", options=districts)

# 선택 데이터
filtered = df[df["district"] == selected]

# 그래프
fig = px.line(
    filtered,
    x="age",
    y="population",
    markers=True,
    title=f"{selected} — 연령별 인구수 변화",
    labels={"age": "나이", "population": "인구수"},
)
fig.update_traces(mode="lines+markers", hovertemplate="%{x}세<br>인구수: %{y:,}<extra></extra>")
fig.update_layout(hovermode="x unified", margin=dict(l=40, r=40, t=60, b=40))

st.plotly_chart(fig, use_container_width=True)

# 데이터 미리보기 + 다운로드
st.markdown("---")
st.subheader("📋 데이터 미리보기")
st.dataframe(filtered)

csv = filtered.to_csv(index=False).encode("utf-8-sig")
st.download_button(
    label="💾 선택 지역구 CSV 다운로드",
    data=csv,
    file_name=f"{selected}_인구데이터.csv",
    mime="text/csv"
)
