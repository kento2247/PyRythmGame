import os
import sys

import pygame

import timing_game as timing_game
from LineInterface import LineInterface

if __name__ == "__main__":
    pygame.init()
    line_interface = LineInterface()

    while True:
        try:
            userId, userName = line_interface.login()
            music_jp_name, combo, score = timing_game.timing_game(userName)
            message = f"ゲーム記録\n楽曲名：{music_jp_name}\n最大コンボ数：{combo}\nスコア：{score}"
            line_interface.logout(userId, message)
        except Exception as e:
            print(e)
            break
        else:
            print("game restart")

    pygame.quit()
    sys.exit()
