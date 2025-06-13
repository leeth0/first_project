import streamlit as st
import random

st.title("🧠 비즈니스 상황 선택 게임")
st.markdown("무작위로 제시되는 경영 상황에서 올바른 결정을 내려보세요!")

# 시나리오 목록
scenarios = [
    {
        "situation": "📉 자금이 빠르게 소모되고 있습니다. 무엇을 하시겠습니까?",
        "choices": [
            "A. 일부 직원을 해고한다",
            "B. 투자 유치를 시도한다",
            "C. 기능을 줄여 비용을 줄인다"
        ],
        "outcomes": {
            "A": "비용은 줄었지만 팀 사기가 저하되었습니다.",
            "B": "운영 자금을 확보했습니다!",
            "C": "비용은 줄었지만 만족도가 하락했습니다."
        }
    },
    {
        "situation": "🧪 고객 반응이 부정적입니다. 대응은?",
        "choices": [
            "A. 출시를 연기하고 개선한다",
            "B. 마케팅으로 이미지 개선을 시도한다",
            "C. 그대로 출시한다"
        ],
        "outcomes": {
            "A": "긍정적 반응을 얻었습니다.",
            "B": "일시적 효과는 있었지만 문제는 남았습니다.",
            "C": "불만이 폭주했습니다."
        }
    },
    # 추가 시나리오 가능
]

# 세션 상태 초기화
if "scenario_index" not in st.session_state:
    st.session_state.scenario_index = random.randint(0, len(scenarios) - 1)
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "current_choice" not in st.session_state:
    st.session_state.current_choice = None

scenario = scenarios[st.session_state.scenario_index]

# 문제 출력
st.subheader("📌 상황:")
st.write(scenario["situation"])

# 선택지
choice = st.radio("📝 당신의 선택은?", scenario["choices"], key="radio_choice")

# 결과 확인
if st.button("결과 확인"):
    st.session_state.current_choice = choice
    st.session_state.show_result = True

# 결과 보여주기
if st.session_state.show_result and st.session_state.current_choice:
    selected_letter = st.session_state.current_choice.split(".")[0]
    result = scenario["outcomes"].get(selected_letter, "결과 없음")
    st.success(f"🧾 결과: {result}")

    # 다음 문제 버튼
    if st.button("🔄 다음 문제 보기"):
        st.session_state.scenario_index = random.randint(0, len(scenarios) - 1)
        st.session_state.show_result = False
        st.session_state.current_choice = None
