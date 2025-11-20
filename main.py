from datetime import date
from login import get_token
from crawler import fetch_dashboard
from calculator import build_row   # 你已經寫好

print("login module loaded")
print("def get_token defined:", "get_token" in globals())

def main():
    token = get_token()  # 自動取得最新 token

    target_date = date.today().strftime("%Y-%m-%d")
    raw_json = fetch_dashboard(token, target_date)
    row = build_row(raw_json)

    print("今日報表：")
    print(row)

if __name__ == "__main__":
    main()