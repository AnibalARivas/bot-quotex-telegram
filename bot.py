import requests

TOKEN = "8166648583:AAGRMoV0KcYmBYKK3Ds6PiJgFI4ApGyHSmE"
CHAT_ID = "762757125"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": "🤖 Bot funcionando"
}

requests.post(url, data=data)
