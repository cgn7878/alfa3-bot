import requests
import numpy as np

# CoinGecko API'den veri çekme
def veri_al(coin_id, currency="usd", gün=1):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency={currency}&days={gün}"
    try:
        return requests.get(url).json()
    except Exception as e:
        return {"hata": str(e)}

# RSI hesaplama
def rsi_hesapla(prices, periyot=14):
    gains = []
    losses = []
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        if diff >= 0:
            gains.append(diff)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(-diff)
    avg_gain = np.mean(gains[-periyot:])
    avg_loss = np.mean(losses[-periyot:])
    rs = avg_gain / avg_loss if avg_loss != 0 else 100
    rsi = 100 - (100 / (1 + rs))
    return round(rsi, 2)

# EMA hesaplama
def ema_hesapla(prices, period=9):
    prices = np.array(prices)
    weights = np.exp(np.linspace(-1., 0., period))
    weights /= weights.sum()
    a = np.convolve(prices, weights, mode='full')[:len(prices)]
    a[:period] = a[period]
    return round(a[-1], 2)

# MACD hesaplama
def macd_hesapla(prices):
    ema_12 = ema_hesapla(prices, 12)
    ema_26 = ema_hesapla(prices, 26)
    macd = ema_12 - ema_26
    return round(macd, 4)

# Bollinger Band hesaplama
def bollinger_band(prices, period=20):
    prices = np.array(prices[-period:])
    sma = np.mean(prices)
    std = np.std(prices)
    upper_band = sma + 2 * std
    lower_band = sma - 2 * std
    return round(lower_band, 2), round(upper_band, 2)

# Coin analiz sonucu (tek coin için tüm göstergeler)
def analiz_yap(coin_id):
    try:
        data = veri_al(coin_id)
        if "prices" not in data:
            return {"hata": "Veri alınamadı"}
        prices = [x[1] for x in data["prices"]]

        rsi = rsi_hesapla(prices)
        macd = macd_hesapla(prices)
        ema = ema_hesapla(prices)
        bollinger = bollinger_band(prices)

        return {
            "coin": coin_id,
            "rsi": rsi,
            "macd": macd,
            "ema": ema,
            "bollinger": bollinger
        }
    except Exception as e:
        return {"hata": str(e)}

# AL/SAT sinyali üretme (örnek)
def sinyal_uret(analiz):
    rsi = analiz["rsi"]
    macd = analiz["macd"]
    ema = analiz["ema"]
    boll = analiz["bollinger"]
    yorum = []

    if rsi < 30:
        yorum.append("RSI: <b>AŞIRI DÜŞÜK</b> (AL)")
    elif rsi > 70:
        yorum.append("RSI: <b>AŞIRI YÜKSEK</b> (SAT)")
    else:
        yorum.append(f"RSI: {rsi}")

    if macd > 0:
        yorum.append("MACD: <b>POZİTİF</b>")
    else:
        yorum.append("MACD: NEGATİF")

    yorum.append(f"EMA: {ema}")
    yorum.append(f"Bollinger: Alt={boll[0]} Üst={boll[1]}")

    return "\n".join(yorum)
