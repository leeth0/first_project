import streamlit as st
import random

st.set_page_config(page_title="🪨✂️📄 가위바위보 게임!", page_icon="✂️", layout="centered")

st.markdown(
    """
    <style>
    .big-font {
        font-size: 48px !important;
        font-weight: bold;
        color: #FF4500;
        text-shadow: 2px 2px 5px #FFB347;
        text-align: center;
    }
    .emoji-button {
        font-size: 40px;
        padding: 20px 40px;
        margin: 10px;
        border-radius: 15px;
        background: linear-gradient(45deg, #FF6B6B, #FFD93D);
        color: white;
        border: none;
        cursor: pointer;
        box-shadow: 0 5px 15px rgba(255, 107, 107, 0.4);
        transition: all 0.3s ease;
    }
    .emoji-button:hover {
        background: linear-gradient(45deg, #FFD93D, #FF6B6B);
        transform: scale(1.1);
        box-shadow: 0 8px 25px rgba(255, 217, 61, 0.7);
    }
    .result-box {
        border: 4px solid #FF6B6B;
        background: #FFF0F0;
        border-radius: 20px;
        padding: 20px;
        margin-top: 20px;
        font-size: 24px;
        text-align: center;
        color: #D72631;
        box-shadow: 0 4px 10px rgba(215, 38, 49, 0.3);
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<p class="big-font">🪨✂️📄 가위 바위 보 게임! 📄✂️🪨</p>', unsafe_allow_html=True)
st.write("나와 컴퓨터 중 누가 이길까요? 🎲 선택하세요!")

# 선택지와 이모지 매칭
choices = {
    "🪨 바위": "rock",
    "✂️ 가위": "scissors",
    "📄 보": "paper"
}

user_choice_emoji = st.radio(
    "당신의 선택:",
    options=list(choices.keys()),
    index=0,
    label_visibility="visible",
)

if st.button("▶️ 승부 내기!"):
    user_choice = choices[user_choice_emoji]
    computer_choice = random.choice(list(choices.values()))

    # 승부 판단
    def judge(user, comp):
        if user == comp:
            return "무승부! 🤝"
        elif (user == "rock" and comp == "scissors") or \
             (user == "scissors" and comp == "paper") or \
             (user == "paper" and comp == "rock"):
            return "🎉 당신이 이겼어요! 🎉"
        else:
            return "😢 컴퓨터가 이겼어요... 😢"

    result = judge(user_choice, computer_choice)

    # 컴퓨터 선택 이모지 찾기
    comp_emoji = {v: k for k, v in choices.items()}[computer_choice]

    st.markdown(
        f"""
        <div class="result-box">
        🧑 당신: {user_choice_emoji} <br><br>
        🤖 컴퓨터: {comp_emoji} <br><br>
        <b>{result}</b>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.markdown("만든이: **ChatGPT** 🤖 | 즐거운 가위바위보 하세요! ✨")
