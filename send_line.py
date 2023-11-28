# 2022/06/22 gas python_hub deploy version 19

import requests


def send_line(gas_url, to, message):
    param = {"app": "line_send", "to": to, "message": message}
    res = requests.get(gas_url, params=param)
    return res.text
