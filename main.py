import streamlit as st
import requests
import json

# OpenWeatherMap API 키와 URL
API_KEY = "여기에_당신의_API_키_입력"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# 페이지 설정
st.set_page_config(page_title="오늘의 날씨 & 응원 한마디", page_icon="🌞", layout="centered")

# 함수: 날씨 API에서 데이터 가져오기
def get_weather(city):
    # API 요청 URL 만들기
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric&lang=kr"
    response = requests.get(url)

    # 응답 데이터 처리
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["main"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return weather, temperature, description
    else:
        return None, None, None

# 날씨에 맞는 응원 메시지 반환 함수
def get_encouragement(weather):
    if weather == "Clear":
        return "맑은 날씨! 오늘도 기운차게 하루를 시작하세요! 🌞"
    elif weather == "Clouds":
