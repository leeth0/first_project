import streamlit as st
import random

st.title("🧠 비즈니스 상황 선택 게임")
st.markdown("무작위로 제시되는 경영 상황에서 올바른 결정을 내려보세요!")

# 시나리오 목록
scenarios = [
    {
        "situation": "📉 당신의 스타트업이 예상보다 빠르게 자금을 소모하고 있습니다. 무엇을 하시겠습니까?",
        "choices": [
            "A. 인건비를 줄이기 위해 일부 직원을 해고한다",
            "B. 투자자를 찾아 추가 자금을 유치한다",
            "C. 제품 기능을 줄여 유지비를 줄인다"
        ],
        "outcomes": {
            "A": "단기적 비용 절감에는 성공했지만 팀 사기가 저하되었습니다.",
            "B": "투자 유치에 성공하며 운영 자금을 확보했습니다!",
            "C": "비용은 줄었지만 사용자 만족도도 하락했습니다."
        }
    },
    {
        "situation": "🧪 신제품 출시를 앞두고 고객 반응이 부정적입니다. 어떻게 대응하시겠습니까?",
        "choices": [
            "A. 제품을 다시 설계해 출시를 연기한다",
            "B. 마케팅으로 긍정적인 이미지 형성을 시도한다",
            "C. 피드백을 무시하고 그대로 출시한다"
        ],
        "outcomes": {
            "A": "출시는 늦어졌지만 더 나은 제품으로 긍정적인 반응을 얻었습니다.",
            "B": "초기 반응은 좋아졌지만 제품 자체 문제는 여전했습니다.",
            "C": "출시 후 불만이 폭주하며 평점이 급락했습니다."
        }
    },
    {
        "situation": "📦 경쟁사가 비슷한 제품을 훨씬 저렴하게 출시했습니다. 대응 전략은?",
        "choices": [
            "A. 가격을 맞춰 경쟁한다",
            "B. 우리만의 고급 이미지로 차별화한다",
            "C. 파트너십을 맺어 고객을 확보한다"
        ],
        "outcomes": {
            "A": "일정 고객을 유지했지만 이익률이 감소했습니다.",
            "B": "충성 고객은 유지했지만 신규 고객 유입은 어려웠습니다.",
            "C": "협업으로 고객층이 확장되며 돌파구를 찾았습니다!"
        }
    },
    {
        "situation": "🚀 예상보다 빠르게 성장하고 있어 시스템이 과부하 상태입니다. 어떻게 하시겠습니까?",
        "choices": [
            "A. 서버 증설 및 자동화 시스템에 투자한다",
            "B. 신규 고객 접수를 일시 중단한다",
            "C. 가격을 올려 수요를 줄인다"
        ],
        "outcomes": {
            "A": "초기 비용이 들었지만 장기적 안정성 확보에 성공했습니다.",
            "B": "불만은 있었지만 서비스 품질을 유지했습니다.",
            "C": "수요는 줄었지만 고가 고객층이 남았습니다."
        }
    },
    {
        "situation": "😡 직원들 사이에 갈등이 커지고 있어 업무 효율이 떨어지고 있습니다. 당신의 선택은?",
        "choices": [
            "A. 강력한 인사조치를 단행한다",
            "B. 중재자를 통해 갈등을 해결한다",
            "C. 갈등 팀을 프로젝트에서 제외한다"
        ],
        "outcomes": {
            "A": "긴장감은 생겼지만 팀 질서는 회복되었습니다.",
            "B": "협력적인 분위기가 조성되며 업무 효율이 회복되었습니다!",
            "C": "일시적으로 문제를 피했지만 인력 부족이 생겼습니다."
        }
    }
]

# 세션 상태에서 시나리오 고정
if "selected_scenario" not in st.session_state:
    st.session_state.selected_scenario = random.choice(scenarios)

scenario = st.session_state.selected_scenario

# 상황 출력
st.subheader("📌 상황:")
st.write(scenario["situation"])

# 선택지 보여주기
choice = st.radio("📝 당신의 선택은?", scenario["choices"])

# 결과 확인 버튼
if st.button("결과 확인"):
    selected_letter = choice.split(".")[0]
    result = scenario["outcomes"].get(selected_letter, "결과 없음")
    st.markdown("🧾 **결과:**")
    st.success(result)

    # 결과 본 뒤 다음 문제를 보고 싶을 경우
    if st.button("다음 문제 보기"):
        st.session_state.selected_scenario = random.choice(scenarios)
        st.experimental_rerun()
