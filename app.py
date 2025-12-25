import streamlit as st
import pandas as pd
from logic.daily_analysis import analyze_daily_stock
from logic.evaluator import evaluate_goal

st.title("Goal-Based Investment Analyzer")

amount = st.number_input("Investment Amount (₹)", min_value=1000)
target_percent = st.number_input("Target Return (%)", min_value=0.1)
days = st.number_input("Time Period (days)", min_value=1)

if st.button("Analyze"):
    required_daily = target_percent / days
    st.write(f"Required Daily Return: **{required_daily:.2f}%**")

    data = pd.read_csv("data/daily_prices.csv")

    for stock in data["stock"].unique():
        stock_df = data[data["stock"] == stock]

        avg_daily, volatility, trend = analyze_daily_stock(stock_df)
        feasible, risk = evaluate_goal(avg_daily, volatility, required_daily)

        st.markdown(f"### {stock}")
        st.write(f"Trend: {trend}")
        st.write(f"Avg Daily Return: {avg_daily:.2f}%")
        st.write(f"Volatility: {volatility:.2f}")
        st.write(f"Risk Level: {risk}")

        if feasible:
            st.success("Suitable for goal (HIGH RISK possible)")
        else:
            st.warning("Not suitable for this goal")
