def evaluate_goal(avg_daily, volatility, required_daily):
    feasible = avg_daily >= required_daily

    if volatility < 1:
        risk = "Low"
    elif volatility < 3:
        risk = "Medium"
    elif volatility < 5:
        risk = "High"
    else:
        risk = "Extreme"

    return feasible, risk
