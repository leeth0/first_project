import streamlit as st

st.title("🧠 비즈니스 상황 선택 게임")

st.markdown("아래 주어진 상황에 따라 의사결정을 내려보세요. 선택에 따라 결과가 달라집니다!")

situation = "당신의 회사는 신제품을 출시했지만 매출이 기대에 못 미칩니다. 어떻게 하시겠습니까?"
st.subheader("📌 상황:")
st.write(situation)

choice = st.radio("당신의 선택은?", [
    "A. 마케팅 예산을 2배로 늘린다",
    "B. 제품 가격을 인하한다",
    "C. 기능을 줄이고 가성비를 높인다"
])

if st.button("결과 확인"):
    if "마케팅" in choice:
        st.success("고객 유입이 늘어났고 매출이 증가했습니다!")
    elif "가격을 인하" in choice:
        st.warning("매출은 늘었지만 이익률이 떨어졌습니다.")
    else:
        st.info("가성비로 인한 평가는 좋지만 고객 수는 큰 변화가 없었습니다.")
