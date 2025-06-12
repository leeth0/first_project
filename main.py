import streamlit as st
import datetime
import random

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
        "https://images.unsplash.com/photo-1596544605919-f88b7a2ed3f1?crop=entropy&cs=tinysrgb&fit=max&ixid=MXwyMDg1fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&q=80&w=400",  # 저녁
    ],
}

# 현재 시간 기준으로 추천 이미지 결정하기
def get_image_for_time():
    # 현재 시간을 가져옵니다
    current_time = datetime.datetime.now().time()

    # 오전, 오후, 저녁 시간을 나누는 기준
    if current_time < datetime.time(12, 0):  # 오전
        period = "morning"
    elif current_time < datetime.time(18, 0):  # 오후
        period = "afternoon"
    else:  # 저녁
        period = "evening"

    # 해당 시간대에 맞는 이미지 리스트 중 하나를 랜덤으로 선택
    image_url = random.choice(images[period])
    return image_url

# 제목 표시
st.title("⏰ 현재 시간에 따른 추천 이미지 🎨")

# 추천 이미지 표시
st.write("현재 시간에 맞는 이미지를 추천해드립니다!")

# 이미지 가져오기
recommended_image_url = get_image_for_time()

# 이미지 출력
st.image(recommended_image_url, caption="추천 이미지!", use_column_width=True)

# 시간에 따른 메시지 출력
current_hour = datetime.datetime.now().hour
if current_hour < 12:
    st.write("아침입니다! ☀️ 하루를 시작하는 기분 좋은 이미지입니다!")
elif current_hour < 18:
    st.write("점심시간! 🍴 에너지를 채울 수 있는 이미지네요!")
else:
    st.write("저녁시간! 🌙 하루를 마무리하는 여유로운 시간입니다!")

# 앱 리프레시 설정: 10분마다 자동으로 새 이미지를 표시
st.autorefresh(interval=60000)  # 10분마다 리프레시
