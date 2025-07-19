import random

def zayif_coin_analizi(portfoy_listesi, coin_verileri):
    """
    Portföydeki coinler içinde en zayıf performansı göstereni tespit eder.
    """
    if not portfoy_listesi:
        return None, None

    # Performansları karşılaştır
    performanslar = {}
    for coin in portfoy_listesi:
        fiyat_dizi = coin_verileri.get(coin, [])
        if len(fiyat_dizi) < 2:
            continue
        değişim = fiyat_dizi[-1] - fiyat_dizi[0]
        performanslar[coin] = değişim

    if not performanslar:
        return None, None

    zayif_coin = min(performanslar, key=performanslar.get)
    return zayif_coin, performanslar[zayif_coin]


def alternatif_coin_öner(portfoy_listesi, coin_verileri):
    """
    Portföyde olmayan coinler arasında daha iyi performanslı bir tane önerir.
    """
    alternatifler = {}
    for coin, fiyatlar in coin_verileri.items():
        if coin in portfoy_listesi:
            continue
        if len(fiyatlar) < 2:
            continue
        değişim = fiyatlar[-1] - fiyatlar[0]
        alternatifler[coin] = değişim

    if not alternatifler:
        return None

    güçlü_coin = max(alternatifler, key=alternatifler.get)
    return güçlü_coin


def gecis_mesaji(zayif_coin, güçlü_coin, zayif_kazanc, guclu_kazanc):
    """
    Kullanıcıya geçiş önerisi mesajını üretir.
    """
    return (
        f"⚠️ Portföyündeki en zayıf coin: <b>{zayif_coin.upper()}</b> ({zayif_kazanc:+.2f} USD)\n"
        f"💡 Bunun yerine <b>{güçlü_coin.upper()}</b> ({guclu_kazanc:+.2f} USD) tercih edebilirsin.\n"
        f"👉 Geçiş yapmak ister misin?\nYanıt: <b>onaylandı</b> / <b>reddedildi</b>"
    )
