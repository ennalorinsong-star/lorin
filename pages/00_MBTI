import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천기", page_icon="🎓", layout="centered")

st.title("🌈 MBTI로 보는 나의 진로 추천기 💫")
st.caption("너의 MBTI를 고르면 찰떡 진로랑 어울리는 학과를 알려줄게! (๑•̀ㅂ•́)و✧")

# 1️⃣ MBTI 선택
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]
user_mbti = st.selectbox("🧠 너의 MBTI는 뭐야?", mbti_list)

# 2️⃣ 데이터 (진로 + 학과 + 성격)
career_data = {
    "INTJ": {
        "jobs": ["전략기획가", "데이터 분석가"],
        "majors": ["경영학, 산업공학", "통계학, 컴퓨터공학"],
        "traits": "계획적이고 논리적인 성격! 미래를 내다보는 분석가 타입 👓"
    },
    "INTP": {
        "jobs": ["연구원", "개발자"],
        "majors": ["물리학, 컴퓨터공학", "소프트웨어학, 수학"],
        "traits": "호기심이 많고 새로운 걸 파고드는 탐구형 두뇌 🧩"
    },
    "ENTJ": {
        "jobs": ["경영 컨설턴트", "팀 리더"],
        "majors": ["경영학, 경제학", "정치외교학, 행정학"],
        "traits": "리더십 강하고 목표 지향적인 추진력 갑 💼🔥"
    },
    "ENTP": {
        "jobs": ["창업가", "마케팅 기획자"],
        "majors": ["광고홍보학, 경영학", "디지털미디어학, 경제학"],
        "traits": "아이디어 뿜뿜 💡 말 잘하고 유머 센스 최고!"
    },
    "INFJ": {
        "jobs": ["상담사", "작가"],
        "majors": ["심리학, 교육학", "문예창작학, 철학"],
        "traits": "사람 마음을 잘 읽고, 깊이 있는 생각쟁이 🌙"
    },
    "INFP": {
        "jobs": ["예술가", "디자이너"],
        "majors": ["미술, 디자인", "문예창작학, 영상예술"],
        "traits": "감수성 풍부하고 따뜻한 감정형 로맨티스트 💕"
    },
    "ENFJ": {
        "jobs": ["교사", "HR 전문가"],
        "majors": ["교육학, 심리학", "경영학, 사회학"],
        "traits": "사람을 이끄는 리더! 따뜻한 마음으로 세상을 바꾸는 타입 🌍"
    },
    "ENFP": {
        "jobs": ["기획자", "크리에이터"],
        "majors": ["미디어커뮤니케이션, 광고홍보학", "공연예술, 콘텐츠기획"],
        "traits": "에너지 넘치고 창의력 폭발 ✨ 새로운 걸 좋아하는 자유영혼!"
    },
    "ISTJ": {
        "jobs": ["회계사", "공무원"],
        "majors": ["회계학, 법학", "행정학, 경제학"],
        "traits": "성실함의 끝판왕! 책임감 있는 현실주의자 📋"
    },
    "ISFJ": {
        "jobs": ["간호사", "사회복지사"],
        "majors": ["간호학, 사회복지학", "심리학, 아동학"],
        "traits": "따뜻하고 배려심 많은 수호천사 💗"
    },
    "ESTJ": {
        "jobs": ["프로젝트 매니저", "행정가"],
        "majors": ["경영학, 행정학", "산업공학, 경제학"],
        "traits": "체계적이고 실용적인 현실주의자! 리더십도 굿 👍"
    },
    "ESFJ": {
        "jobs": ["교사", "이벤트 플래너"],
        "majors": ["교육학, 사회학", "홍보학, 관광경영"],
        "traits": "사람 좋아하고 친절한 인기쟁이 🌸"
    },
    "ISTP": {
        "jobs": ["엔지니어", "정비사"],
        "majors": ["기계공학, 전자공학", "자동차공학, 항공정비"],
        "traits": "손재주 좋고 문제 해결 능력 쩌는 실전형 🔧"
    },
    "ISFP": {
        "jobs": ["사진작가", "패션디자이너"],
        "majors": ["디자인, 예술", "패션학, 영상미디어"],
        "traits": "감성 넘치는 예술가 타입 🎨 조용하지만 매력 터짐!"
    },
    "ESTP": {
        "jobs": ["스포츠 코치", "영업 전문가"],
        "majors": ["체육학, 스포츠과학", "경영학, 마케팅"],
        "traits": "활동적이고 즉흥적인 에너지 넘치는 타입 ⚡"
    },
    "ESFP": {
        "jobs": ["배우", "이벤트 기획자"],
        "majors": ["연극영화학, 방송연예", "홍보학, 관광학"],
        "traits": "분위기 메이커 🌟 모두를 즐겁게 하는 엔터테이너!"
    },
}

# 3️⃣ 결과 보여주기
if st.button("🎯 진로 추천받기"):
    info = career_data[user_mbti]
    st.subheader(f"🌟 {user_mbti} 유형에게 어울리는 진로 🌟")
    st.write(f"💼 **{info['jobs'][0]}**, **{info['jobs'][1]}**")
    st.write("---")
    st.subheader("🎓 관련 학과 추천")
    st.write(f"📚 {info['majors'][0]}")
    st.write(f"📚 {info['majors'][1]}")
    st.write("---")
    st.subheader("💬 이런 성격의 친구에게 딱이야!")
    st.write(info['traits'])

st.markdown("---")
st.caption("🪄 만든이: 귀염뽀짝 MBTI 진로 도우미 ver.1.0 💕")
