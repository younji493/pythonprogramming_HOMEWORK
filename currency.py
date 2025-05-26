from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# 국가 코드 → 통화 코드 매핑
CURRENCY_MAP = {
    "US": "USD",
    "KR": "KRW",
    "JP": "JPY",
    "CN": "CNY",
    "GB": "GBP",
    "EU": "EUR",
    "TH": "THB",
    "VN": "VND"
}

def get_user_country(ip):
    try:
        # 로컬에서 테스트할 경우 127.0.0.1이기 때문에 외부 IP 요청 필요
        if ip == "127.0.0.1" or ip.startswith("192.168."):
            ip = requests.get("https://api.ipify.org").text

        res = requests.get(f"http://ip-api.com/json/{ip}")
        data = res.json()
        return data.get("countryCode", "US"), data.get("country", "United States")
    except Exception as e:
        print("[IP ERROR]", e)
        return "US", "United States"

def get_currency_code(country_code):
    return CURRENCY_MAP.get(country_code, "USD")

def convert_to_krw(amount, from_currency):
    try:
        # 소수점 이하 2자리 유지하도록 precision 설정
        res = requests.get(
            f"https://api.exchangerate.host/convert",
            params={"from": from_currency, "to": "KRW", "amount": amount, "places": 2}
        )
        data = res.json()
        return data.get("result", 0)
    except Exception as e:
        print("[CONVERT ERROR]", e)
        return 0

@app.route("/", methods=["GET", "POST"])
def index():
    user_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    country_code, country_name = get_user_country(user_ip)
    currency_code = get_currency_code(country_code)

    converted_price = None
    input_price = None
    error_message = None

    if request.method == "POST":
        try:
            input_price = float(request.form.get("price", "0"))
            if input_price <= 0:
                error_message = "금액은 0보다 커야 합니다."
            else:
                converted_price = convert_to_krw(input_price, currency_code)
        except ValueError:
            error_message = "유효한 숫자를 입력하세요."

    return render_template("index.html",
                           country=country_name,
                           currency=currency_code,
                           converted_price=converted_price,
                           input_price=input_price,
                           error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)