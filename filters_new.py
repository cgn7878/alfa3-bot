# filters.py

def evaluate_signal(analysis):
    """
    RSI, MACD ve Bollinger Bands'e göre sinyal üretir.
    """
    rsi = analysis.get("rsi")
    macd = analysis.get("macd")
    signal = analysis.get("macd_signal")
    price = analysis.get("price")
    boll_upper = analysis.get("bollinger_upper")
    boll_lower = analysis.get("bollinger_lower")

    macd_cross = macd > signal
    boll_position = ""

    if price > boll_upper:
        boll_position = "overbought"
    elif price < boll_lower:
        boll_position = "oversold"
    else:
        boll_position = "normal"

    # AL sinyali koşulları
    if (
        rsi is not None and rsi < 35 and
        macd_cross and
        boll_position == "oversold"
    ):
        return "AL"

    # SAT sinyali koşulları
    if (
        rsi is not None and rsi > 65 and
        not macd_cross and
        boll_position == "overbought"
    ):
        return "SAT"

    # Kararsız
    return "TUT"
