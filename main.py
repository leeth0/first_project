import streamlit as st
import datetime
import random
import time

# 페이지 설정
st.set_page_config(page_title="시간에 따른 추천 이미지", page_icon="⏰", layout="centered")

# 이미지 리스트 (추천할 이미지들의 URL을 넣습니다)
images = {
    "morning": [
        "https://images.unsplash.com/photo-1533668306272-3be87cd6d86f?crop=entropy&cs=tinysrgb&fit=max&ixid=MXwyMDg1fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&q=80&w=400",  # 아침
    ],
    "afternoon": [
        "https://images.unsplash.com/photo-1601695309743-967f72d20002?crop=entropy&cs=tinysrgb&fit=max&ixid=MnwzNjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&q=80&w=400",  # 점심
    ],
    "evening": [
        "https://images.unsplash.com/photo-1596544605919-f88b7a2ed3f1?crop=entropy&cs=tinysrgb&fit=max&ixid=MXwyMDg1fDB8MHxwaG90by1wYWdlfHx8f
