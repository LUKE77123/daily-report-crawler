import requests

API_URL = "https://meta02backstageapi.tb3rdgame.net/rs7777adminapi/BDT/dashboard/trans"

def fetch_dashboard(token: str, target_date: str):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "*/*",
        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Origin": "https://rsadmin.rs7777.com",
        "Referer": "https://rsadmin.rs7777.com/",
        "User-Agent": "Mozilla/5.0"
    }

    params = {
        "current": 1,
        "pageSize": 20,
        "start_date": target_date,
        "end_date": target_date,
        "lang": "zh"
    }

    resp = requests.get(API_URL, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()

