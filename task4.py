import requests


def ip_info() -> str:
    req = requests.get('https://ifconfig.me/')
    return req.text


if __name__ == "__main__":
    print(ip_info())
