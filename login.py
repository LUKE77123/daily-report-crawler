import requests

# 正確的登入 API：不是 v2，是 admin/login
LOGIN_URL = "https://meta02backstageapi.tb3rdgame.net/rs7777adminapi/admin/login"

ACCOUNT = "superadmin02"     # 你的帳號
PASSWORD = "123456"          # 你的密碼
GCODE = "1478963"            # 固定的登入碼

def get_token():
    payload = {
        "account": ACCOUNT,
        "password": PASSWORD,
        "gcode": GCODE    # gcode 只能放在這支 API！
    }

    resp = requests.post(LOGIN_URL, json=payload)
    resp.raise_for_status()

    data = resp.json()

    # token 在 data["data"]["token"]
    try:
        token = data["data"]["token"]
    except Exception:
        raise Exception(f"登入成功但無法找到 token：{data}")

    return token
