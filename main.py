import streamlit as st
import numpy as np
import pandas as pd

st.title("💼 가상 창업 시뮬레이션 게임")

st.markdown("초기 자본금과 업종을 선택하고, 마케팅 전략과 가격 정책을 정해 수익을 극대화해보세요!")

# Step 1: 업종 선택
business_type = st.selectbox("업종을 선택하세요", ["카페", "온라인 쇼핑몰", "앱 서비스"])

# Step 2: 초기 자본금 설정
capital = st.slider("초기 자본금 (만원)", 100, 1000, 500, 50)

# Step 3: 가격 전략
price_level = st.selectbox("제품 가격 전략", ["저가", "중간", "고가"])

# Step 4: 마케팅 투자
marketing = st.slider("마케팅 예산 비율 (%)", 0, 50, 20)

# Simulation logic
base_demand = {"카페": 100, "온라인 쇼핑몰": 150, "앱 서비스": 200}[business_type]
price_multiplier = {"저가": 0.8, "중간": 1.0, "고가": 1.2}[price_level]
marketing_effect = marketing / 100

# 시뮬레이션
customers = int(base_demand * (1 + marketing_effect) * (1 if price_level == "중간" else (1.2 if price_level == "저가" else 0.8)))
revenue = customers * price_multiplier * 1.0  # 단위 가격
costs = capital * 0.3 + marketing * 10
profit = revenue - costs

st.metric("예상 고객 수", customers)
st.metric("예상 매출", f"{revenue:.0f}만원")
st.metric("예상 비용", f"{costs:.0f}만원")
st.metric("예상 이익", f"{profit:.0f}만원")

if profit > 0:
    st.success("수익을 낼 수 있는 비즈니스 모델입니다!")
else:
    st.error("적자가 예상됩니다. 전략을 조정해보세요.")
