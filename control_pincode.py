# 2022/06/22 gas python_hub deploy version 20

import random

import requests


def control_pincode(gas_url, mode):
    param = {
        "app": "control_propaty",
        "command": mode,
        "key": "onetime_login",
    }
    if mode == "set":
        pin_code = ""
        for i in range(4):
            pin_code += str(random.randrange(0, 9, 1))
        param["value"] = pin_code
    res = requests.get(gas_url, params=param)
    return res.text
