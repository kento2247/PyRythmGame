import os
import sys

import pygame
from dotenv import load_dotenv

import line_login

# import line_photo_send
# import raspi_log
import timing_game

load_dotenv()

gas_url = os.getenv("gas_url")
line_token = os.getenv("line_token")
screen_width = int(os.getenv("screen_width"))
screen_height = int(os.getenv("screen_height"))
folder_path = os.getenv("folder_path")
qr_path = os.getenv("qr_path")
font_path = os.getenv("font_path")


if __name__ == "__main__":
    pygame.init()
    while 1:
        userId, userName = line_login.line_login(
            screen_width, screen_height, qr_path, font_path, gas_url
        )

        # line_photo_send.line_photo_send(line_token, "user.png")

        music_jp_name, combo, score = timing_game.timing_game(
            folder_path, font_path, userName, screen_width, screen_height
        )
        message = f"ゲーム記録\n楽曲名：{music_jp_name}\n最大コンボ数：{combo}\nスコア：{score}"
        line_login.line_logout(userId, message)
        log_message = f"userID={userId},name={userName},title={music_jp_name},combo={combo},score={score}"
        raspi_log.raspi_log(gas_url, log_message)
    pygame.quit()
    sys.quit()
