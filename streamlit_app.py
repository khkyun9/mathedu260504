import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 배경색 설정
sns.set_theme(style="whitegrid")
try:
    plt.rc("font", family="NanumGothic")
except Exception:
    pass

# 시각화
st.header("시각화 예시")

with st.expander("Matplotlib + Seaborn 차트"):
    study_data = {
        "과목": ["미적분", "선형대수", "확률과통계", "미분방정식", "수치해석"],
        "공부시간": [8, 6, 5, 4, 3],
    }
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x="공부시간", y="과목", data=study_data, palette="Blues_d", ax=ax)
    ax.set_title("과목별 공부 시간")
    ax.set_xlabel("시간(시간)")
    ax.set_ylabel("과목")
    st.pyplot(fig)

with st.expander("Plotly 차트"):
    fig2 = px.line(
        x=["1월", "2월", "3월", "4월", "5월"],
        y=[20, 25, 30, 28, 32],
        labels={"x": "월", "y": "학습 만족도"},
        title="월별 학습 만족도 변화",
    )
    fig2.update_traces(mode="markers+lines")
    st.plotly_chart(fig2, use_container_width=True)
