import requests


API = "https://api.ipify.org?format=json"


def get_public_ip():
    try:
        resp = requests.get(API, timeout=5)
    except requests.exceptions.Timeout:
        return "Request Timed Out"
    except requests.exceptions.RequestException:
        return "An error occurred during the request."
    return resp.json()["ip"]


def print_public_ip():
    ip = get_public_ip()
    print(ip)
