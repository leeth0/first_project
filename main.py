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
    {
        "situation": "📦 재고가 과도하게 쌓였습니다. 대응 방안은?",
        "choices": [
            "A. 프로모션을 통해 재고 소진",
            "B. 생산을 일시 중단",
            "C. 새로운 유통 경로 확보"
        ],
        "outcomes": {
            "A": "재고를 빠르게 소진했지만 마진이 줄었습니다.",
            "B": "손실은 줄였지만 고객 불만이 늘었습니다.",
            "C": "새로운 매출 기회를 창출했습니다!"
        }
    },
    {
        "situation": "👥 핵심 인재가 경쟁사로 이직했습니다. 어떻게 하시겠습니까?",
        "choices": [
            "A. 보상 패키지를 강화한다",
            "B. 조직 문화를 개선한다",
            "C. 새 인재를 적극 채용한다"
        ],
        "outcomes": {
            "A": "이직률이 줄었습니다.",
            "B": "직원 만족도가 상승했습니다.",
            "C": "신선한 아이디어가 유입되었습니다!"
        }
    },
    {
        "situation": "🌍 해외 시장 진출을 고민 중입니다. 전략은?",
        "choices": [
            "A. 파트너를 통해 진출",
            "B. 직접 지사를 설립",
            "C. 먼저 시장 조사를 수행"
        ],
        "outcomes": {
            "A": "위험 분산에 성공했습니다.",
            "B": "높은 비용과 리스크가 발생했습니다.",
            "C": "보다 나은 전략 수립이 가능해졌습니다."
        }
    }
]

# 세션 상태 초기화
if "scenario_index" not in st.session_state:
    st.session_state.scenario_index = random.randint(0, len(scenarios) - 1)
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "current_choice" not in st.session_state:
    st.session_state.current_choice = None

# 다음 문제 버튼 (가장 먼저 처리)
if st.button("🔄 다음 문제 보기"):
    st.session_state.scenario_index = random.randint(0, len(scenarios) - 1)
    st.session_state.show_result = False
    st.session_state.current_choice = None

# 현재 시나리오 가져오기
scenario = scenarios[st.session_state.scenario_index]

# 상황 출력
st.subheader("📌 상황:")
st.write(scenario["situation"])

# 선택지 출력
choice = st.radio("📝 당신의 선택은?", scenario["choices"], key="radio_choice")

# 결과 확인 버튼
if st.button("결과 확인"):
    st.session_state.current_choice = choice
    st.session_state.show_result = True

# 결과 보여주기
if st.session_state.show_result and st.session_state.current_choice:
    selected_letter = st.session_state.current_choice.split(".")[0]
    result = scenario["outcomes"].get(selected_letter, "결과 없음")
    st.success(f"🧾 결과: {result}")
