# analyzer.py

import pandas as pd
import numpy as np
import requests

def get_price_data(coin_id, vs_currency="usd", days=2, interval="hourly"):
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
        params = {
            "vs_currency": vs_currency,
            "days": days,
            "interval": interval
        }
        response = requests.get(url, params=params)
        data = response.json()
        prices = data["prices"]
        df = pd.DataFrame(prices, columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        return df
    except Exception as e:
        return None

def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(prices, fast=12, slow=26, signal=9):
    ema_fast = prices.ewm(span=fast, adjust=False).mean()
    ema_slow = prices.ewm(span=slow, adjust=False).mean()
    macd = ema_fast - ema_slow
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line

def calculate_bollinger_bands(prices, window=20):
    sma = prices.rolling(window).mean()
    std = prices.rolling(window).std()
    upper = sma + (std * 2)
    lower = sma - (std * 2)
    return upper, sma, lower

def analyze_coin(coin_id):
    df = get_price_data(coin_id)
    if df is None or df.empty:
        return None

    prices = df["price"]

    rsi = calculate_rsi(prices).iloc[-1]
    macd, signal_line = calculate_macd(prices)
    macd_value = macd.iloc[-1]
    signal_value = signal_line.iloc[-1]
    upper, sma, lower = calculate_bollinger_bands(prices)

    # Sinyal üretme
    result = {
        "rsi": round(rsi, 2),
        "macd": round(macd_value, 4),
        "macd_signal": round(signal_value, 4),
        "macd_cross": macd_value > signal_value,
        "bollinger_upper": round(upper.iloc[-1], 2),
        "bollinger_lower": round(lower.iloc[-1], 2),
        "bollinger_sma": round(sma.iloc[-1], 2),
        "price": round(prices.iloc[-1], 2)
    }

    return result
