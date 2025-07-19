import requests
import statistics

def analiz_yorumla(haberler):
    """
    Gelen haber başlıklarını analiz eder, olumsuz veya olumlu olup olmadığını belirlemeye çalışır.
    Basit kurallara ve kelime filtrelerine göre çalışır.
    """
    olumlu_kelimeler = ["yükseldi", "arttı", "benimsendi", "onaylandı", "büyüme", "pozitif", "iyi haber"]
    olumsuz_kelimeler = ["düştü", "çöktü", "kapatıldı", "reddedildi", "saldırı", "kayıp", "hack"]

    olumlu = 0
    olumsuz = 0

    for haber in haberler:
        başlık = haber.lower()
        if any(kelime in başlık for kelime in olumlu_kelimeler):
            olumlu += 1
        if any(kelime in başlık for kelime in olumsuz_kelimeler):
            olumsuz += 1

    if olumlu > olumsuz:
        return "Haberler genel olarak olumlu görünüyor."
    elif olumsuz > olumlu:
        return "Haberler genel olarak olumsuz görünüyor."
    else:
        return "Haberler nötr seviyede. Net bir yön belirlenemiyor."


def rsi_hesapla(fiyatlar):
    """
    14 dönemlik RSI hesaplaması yapar.
    """
    kazançlar = []
    kayıplar = []

    for i in range(1, len(fiyatlar)):
        değişim = fiyatlar[i] - fiyatlar[i - 1]
        if değişim >= 0:
            kazançlar.append(değişim)
            kayıplar.append(0)
        else:
            kazançlar.append(0)
            kayıplar.append(-değişim)

    ort_kazanç = statistics.mean(kazançlar[-14:])
    ort_kayıp = statistics.mean(kayıplar[-14:])

    if ort_kayıp == 0:
        return 100  # aşırı alım
    rs = ort_kazanç / ort_kayıp
    rsi = 100 - (100 / (1 + rs))
    return round(rsi, 2)


def sinyal_tipi(rsi):
    """
    RSI değerine göre alım/satım sinyali döndürür.
    """
    if rsi < 30:
        return f"📈 <b>Acil Al❗️</b> RSI: {rsi}"
    elif rsi > 70:
        return f"📉 <b>Acil Sat❗️</b> RSI: {rsi}"
    else:
        return f"ℹ️ <b>İzleniyor</b> RSI: {rsi}"
