import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 기본 설정
st.set_page_config(
    page_title="Seoul Tourist Map",
    page_icon="🗺️",
    layout="wide"
)

# 타이틀
st.title("🗺️ 외국인들이 좋아하는 서울 관광지 TOP 10")
st.write("서울의 인기 관광지를 Folium 지도로 한눈에 볼 수 있어요! 📍")

# 관광지 데이터 (이름, 위도, 경도, 설명)
locations = [
    ("경복궁 Gyeongbokgung Palace", 37.580467, 126.976944, "조선의 정궁으로 가장 대표적인 고궁이에요."),
    ("창덕궁 Changdeokgung Palace", 37.579414, 126.991039, "유네스코 세계문화유산에 등재된 아름다운 궁궐이에요."),
    ("북촌 한옥마을 Bukchon Hanok Village", 37.582604, 126.983998, "전통 한옥이 모여 있는 인기 포토존이에요."),
    ("명동 Myeongdong", 37.563757, 126.985302, "쇼핑과 길거리 음식으로 유명한 관광 명소예요."),
    ("남산타워 N Seoul Tower", 37.551170, 126.988228, "서울의 야경을 한눈에 볼 수 있는 랜드마크예요."),
    ("동대문디자인플라자 DDP", 37.566295, 127.009415, "미래적인 디자인의 복합문화공간이에요."),
    ("인사동 Insadong", 37.574018, 126.984722, "전통 공예품과 찻집이 많은 골목거리예요."),
    ("홍대 Hongdae", 37.5563, 126.9220, "젊음과 예술, 음악이 가득한 거리예요."),
    ("이태원 Itaewon", 37.534541, 126.994673, "다양한 문화와 음식이 공존하는 글로벌 거리예요."),
    ("롯데월드타워 Lotte World Tower", 37.513068, 127.102558, "한국에서 가장 높은 초고층 전망 타워예요.")
]

# 서울 중심 좌표
center_lat, center_lon = 37.5665, 126.9780
m = folium.Map(location=[center_lat, center_lon], zoom_start=12)

# 각 관광지 마커 추가
for name, lat, lon, desc in locations:
    folium.Marker(
        [lat, lon],
        popup=f"<b>{name}</b><br>{desc}",
        tooltip=name,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# 지도 출력
st_folium(m, width=900, height=600)

st.caption("📍 자료 출처: VisitSeoul, Wikipedia, Google Maps")
