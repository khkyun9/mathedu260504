import streamlit as st

# 페이지 설정
st.set_page_config(page_title="자기소개", layout="centered")

# 배경색 설정
st.markdown("""
<style>
    .stApp {
        background-color: #f0f8ff;
    }
</style>
""", unsafe_allow_html=True)

# 프로필 섹션
st.title("📝 자기소개")

# 프로필 정보
col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("<h1 style='text-align: center; margin-top: 30px;'>❄️</h1>", unsafe_allow_html=True)

with col2:
    st.subheader("김하경")
    st.write("학생")

# 자기소개
st.header("소개")
st.write("""
수학과 사람이에용.
""")

# 스킬/기술
st.header("스킬")
st.write("**프로그래밍**: Python")

# 학회/활동
st.header("학회")
st.write("""
- 수학사랑 학회 (2년 활동 중)
""")

# 교육
st.header("교육")
st.write("""
- 숙명여자대학교 수학과
- 교직이수 중
""")

# 연락처
st.header("연락처")
col1, col2 = st.columns(2)
with col1:
    st.write("📧 Email: kyung24@sookmyung.ac.kr")
with col2:
    st.write("🔗 GitHub: [khkyun9](https://github.com/khkyun9)")
