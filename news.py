import requests
import datetime

def haberleri_getir():
    try:
        url = "https://api.coingecko.com/api/v3/status_updates"
        response = requests.get(url)
        if response.status_code != 200:
            return []

        haberler = response.json().get("status_updates", [])
        filtrelenmis = []
        for haber in haberler:
            kaynak = haber.get("project", {}).get("name", "Bilinmeyen")
            içerik = haber.get("description", "")
            tarih = haber.get("created_at", "")
            try:
                tarih_obj = datetime.datetime.fromisoformat(tarih.replace("Z", "+00:00"))
            except:
                continue

            filtrelenmis.append({
                "kaynak": kaynak,
                "icerik": içerik,
                "tarih": tarih_obj
            })

        return filtrelenmis
    except Exception as e:
        return [{"kaynak": "HATA", "icerik": str(e), "tarih": datetime.datetime.now()}]
