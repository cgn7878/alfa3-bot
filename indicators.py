import numpy as np
import pandas as pd

def hesapla_rsi(prices, period=14):
    delta = prices.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def hesapla_ema(prices, period=12):
    return prices.ewm(span=period, adjust=False).mean()

def hesapla_macd(prices, fast=12, slow=26, signal=9):
    ema_fast = hesapla_ema(prices, fast)
    ema_slow = hesapla_ema(prices, slow)
    macd = ema_fast - ema_slow
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line

def hesapla_bollinger(prices, window=20, std_dev=2):
    sma = prices.rolling(window).mean()
    std = prices.rolling(window).std()
    upper = sma + std_dev * std
    lower = sma - std_dev * std
    return upper, sma, lower
