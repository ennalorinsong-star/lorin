import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="아프리카 맛집 Top10 지도", layout="wide")

st.title("🌍 아프리카 현지 인기 맛집 Top10 지도")
st.write("Folium 기반으로 만든 인터랙티브 지도입니다.")

# 아프리카 현지인들에게 인기 있는 맛집 10곳 예시
restaurants = [
    {"name": "La Colombe", "country": "South Africa", "lat": -34.0256, "lon": 18.4107},
    {"name": "FYN Restaurant", "country": "South Africa", "lat": -33.9249, "lon": 18.4241},
    {"name": "Al Fassia", "country": "Morocco", "lat": 31.6295, "lon": -7.9811},
    {"name": "The Rock Restaurant", "country": "Tanzania (Zanzibar)", "lat": -6.1356, "lon": 39.4961},
    {"name": "Carnivore Nairobi", "country": "Kenya", "lat": -1.3191, "lon": 36.8303},
    {"name": "Meza Malonga LAB", "country": "Rwanda", "lat": -1.9501, "lon": 30.0589},
    {"name": "Abou El Sid", "country": "Egypt", "lat": 30.0444, "lon": 31.2357},
    {"name": "Santoku", "country": "Ghana", "lat": 5.6037, "lon": -0.1870},
    {"name": "Yod Abyssinia", "country": "Ethiopia", "lat": 8.9806, "lon": 38.7578},
    {"name": "Le Jardin", "country": "Morocco", "lat": 31.6349, "lon": -7.9999},
]

# 지도 생성
m = folium.Map(location=[7, 20], zoom_start=3)

# 마커 표시
for r in restaurants:
    folium.Marker(
        [r["lat"], r["lon"]],
        popup=f"{r['name']} ({r['country']})",
        tooltip=r["name"]
    ).add_to(m)

st_folium(m, width=900, height=600)

st.success("지도가 성공적으로 로드되었습니다!")
