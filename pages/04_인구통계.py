# Streamlit population line chart app
# 파일명: streamlit_population_app.py
# 사용법:
# 1) 같은 폴더에 population.csv 파일을 두거나 (배포 시 스토리지에 포함)
# 2) 또는 앱에서 파일 업로드로 CSV를 직접 업로드하세요.
# 실행: streamlit run streamlit_population_app.py

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="지역구별 나이별 인구 그래프", layout="wide")

st.title("지역구별 나이별 인구수 — 인터랙티브 라인 차트")
st.write("CSV 파일에 `지역구`, `나이`, `인구수` 같은 열이 있으면 자동으로 인식합니다. (영문 컬럼명도 지원)")

# --- 데이터 로딩: 같은 폴더의 population.csv 우선, 없으면 업로드 허용 ---
DEFAULT_CSV = Path("population.csv")

uploaded = None
if DEFAULT_CSV.exists():
    try:
        df = pd.read_csv(DEFAULT_CSV)
        st.info(f"로컬 파일 '{DEFAULT_CSV.name}'에서 데이터를 불러왔습니다.")
    except Exception as e:
        st.error(f"로컬 파일을 읽는 중 오류 발생: {e}")
        df = pd.DataFrame()
else:
    uploaded = st.file_uploader("CSV 파일 업로드 (예: population.csv)", type=["csv"]) 
    if uploaded is not None:
        try:
            df = pd.read_csv(uploaded)
            st.success("업로드된 파일을 불러왔습니다.")
        except Exception as e:
            st.error(f"업로드된 파일을 읽는 중 오류: {e}")
            df = pd.DataFrame()
    else:
        df = pd.DataFrame()

if df.empty:
    st.warning("데이터가 비어있습니다. 로컬에 population.csv를 넣거나 CSV를 업로드하세요.")
    st.stop()

# --- 컬럼 자동 매핑: 한/영 컬럼명 허용 ---
col_map = {}
lower_cols = {c.lower(): c for c in df.columns}

# 지역구 컬럼
for candidate in ['지역구', 'sigungu', 'district', '구', '지역']:
    if candidate in df.columns:
        col_map['district'] = candidate
        break
    if candidate.lower() in lower_cols:
        col_map['district'] = lower_cols[candidate.lower()]
        break

# 나이 컬럼
for candidate in ['나이', 'age', '연령']:
    if candidate in df.columns:
        col_map['age'] = candidate
        break
    if candidate.lower() in lower_cols:
        col_map['age'] = lower_cols[candidate.lower()]
        break

# 인구수 컬럼
for candidate in ['인구수', 'population', 'pop', 'people', '인구']:
    if candidate in df.columns:
        col_map['population'] = candidate
        break
    if candidate.lower() in lower_cols:
        col_map['population'] = lower_cols[candidate.lower()]
        break

# 필수 컬럼 체크
missing = [k for k in ['district','age','population'] if k not in col_map]
if missing:
    st.error(f"CSV에 필요한 컬럼을 찾지 못했습니다: {missing}. 컬럼명이 한글(예: 지역구, 나이, 인구수) 또는 영문(예: district, age, population)인지 확인하세요.")
    st.markdown("---\nCSV의 헤더 예시:\n- 지역구,나이,인구수\n- district,age,population")
    st.stop()

# 컬럼 표준화
df = df.rename(columns={col_map['district']: 'district', col_map['age']: 'age', col_map['population']: 'population'})

# 데이터 타입 정리
# 나이 컬럼이 '20-29' 같은 범위 문자열이라면 그대로 사용하되 정렬 위해 숫자 시도
try:
    df['age_numeric'] = pd.to_numeric(df['age'], errors='coerce')
except Exception:
    df['age_numeric'] = pd.to_numeric(df['age'].astype(str).str.extract(r"(\d+)"), errors='coerce')

# 인구수 숫자 변환
df['population'] = pd.to_numeric(df['population'], errors='coerce')

# 결측값 제거
df = df.dropna(subset=['district','age','population'])

# 정렬: 숫자형 나이 우선, 없으면 문자열 정렬
if df['age_numeric'].notna().any():
    df = df.sort_values(['district','age_numeric'])
    x_col = 'age_numeric'
    x_label = '나이'
else:
    df = df.sort_values(['district','age'])
    x_col = 'age'
    x_label = '나이'

# 사용자가 선택할 수 있는 지역구 목록
districts = df['district'].unique().tolist()
selected_district = st.selectbox("지역구 선택", options=districts)

# 필터링
filtered = df[df['district'] == selected_district].copy()
if filtered.empty:
    st.warning("선택한 지역구에 데이터가 없습니다.")
    st.stop()

# Plotly 라인 차트
fig = px.line(filtered, x=x_col, y='population', markers=True, title=f"{selected_district} — 연령별 인구수",
              labels={x_col: x_label, 'population': '인구수'})
fig.update_traces(mode='lines+markers', hovertemplate=f"%{{x}}<br>인구수: %{{y:,}}<extra></extra>")
fig.update_layout(hovermode='x unified', margin=dict(l=40,r=40,t=60,b=40))

st.plotly_chart(fig, use_container_width=True)

# 간단한 테이블과 다운로드 옵션
st.markdown("---")
st.subheader("데이터 미리보기")
st.dataframe(filtered.reset_index(drop=True))

csv = filtered.to_csv(index=False).encode('utf-8-sig')
st.download_button(label="선택 지역구 CSV 다운로드", data=csv, file_name=f"{selected_district}_age_population.csv", mime='text/csv')

# --- requirements.txt 내용 (아래 내용을 requirements.txt로 저장하세요) ---
# requirements.txt
# streamlit
# pandas
# plotly

# (원하시면 이 파일과 requirements.txt를 같이 드래그/다운로드할 수 있는 형태로 패키징해 드립니다.)
