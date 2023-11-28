import os
import random
import sys

import requests
from dotenv import load_dotenv


class GasRequest:
    def __init__(self):
        load_dotenv()
        self.gas_url = os.getenv("gas_url")

    def _send_request(self, params) -> str:
        res = requests.get(self.gas_url, params=params)
        if res.status_code != 200:
            raise Exception(f"status_code: {res.status_code}")
        else:
            return res.text

    def _set_pincode(self, pincode) -> bool:
        param = {
            "app": "control_propaty",
            "command": "set",
            "key": "onetime_login",
            "value": pincode,
        }
        try:
            self._send_request(param)
            return True
        except Exception as e:
            print(e)
            return False

    def new_pincode(self) -> str:
        pincode = "".join(str(random.randrange(0, 9, 1)) for _ in range(4))
        if self._set_pincode(pincode):
            return pincode
        else:
            self._force_quit()

    def get_pincode(self) -> str:
        param = {
            "app": "control_propaty",
            "command": "get",
            "key": "onetime_login",
        }
        try:
            return self._send_request(param)
        except Exception as e:
            print(e)
            return False

    def del_pincode(self) -> bool:
        param = {
            "app": "control_propaty",
            "command": "del",
            "key": "onetime_login",
        }
        if self._send_request(param):
            return True
        else:
            print("pincode del error")
            return False

    def send_line(self, to, message) -> bool:
        param = {"app": "line_send", "to": to, "message": message}
        if self._send_request(param):
            return True
        else:
            print("line send error")
            return False

    def _force_quit(self):
        sys.exit()
