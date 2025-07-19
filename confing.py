# config.py

# Telegram Bot Token'ını buraya yaz
BOT_TOKEN = "7981029346:AAHzDEJtHmZt8V0ZEt7JoT59stlKn1_4DKk"

# Telegram kullanıcı ID'n (komutları sadece bu kişi kullanabilir)
OWNER_ID = 7831759991

# CoinGecko API ayarları
DEFAULT_CURRENCY = "usd"
DEFAULT_INTERVAL = "hourly"
DEFAULT_DAYS = 2

# Sinyal eşiği ayarları
RSI_OVERSOLD = 30
RSI_OVERBOUGHT = 70
MACD_CROSS_THRESHOLD = True  # True: MACD > Signal olduğunda sinyal verir

# Mesaj gönderim aralığı (saniye cinsinden)
CHECK_INTERVAL = 1800  # 30 dakika

# Sessiz mod saat aralığı (örnek: 03:00 - 09:00 arası mesaj atmaz)
SILENT_HOURS = (3, 9)

# Coin analiz listesi başlangıçta dolu olabilir, istersen boş bırak
DEFAULT_COIN_LIST = [
    "bitcoin", "ethereum", "solana", "cardano", "dogecoin", "avalanche", "ripple",
    "polkadot", "chainlink", "litecoin", "tron", "stellar", "internet-computer"
]
