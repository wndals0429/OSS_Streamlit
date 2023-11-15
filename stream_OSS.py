import streamlit as st

    #OSS 중간 시험 결과
OSS_Score = [80,70,55,30,3,3,1,0]

st.write("# 컴퓨터소프트웨어학부 23114522 안중민")
OSS_Score

st.bar_chart(OSS_Score)
