import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="오늘의 나를 위한 한마디 🌟", page_icon="💬", layout="centered")

# 스타일 적용
st.markdown(
    """
    <style>
    .big-font {
        font-size: 36px !important;
        font-weight: bold;
        color: #6A5ACD;
        text-shadow: 2px 2px 10px rgba(106, 90, 205, 0.5);
        text-align: center;
    }
    .message-box {
        border: 3px solid #FFD700;
        background: #FFF8DC;
        border
