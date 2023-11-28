import os
import sys
import time

import pygame
from dotenv import load_dotenv
from pygame.locals import *

from GasRequest import GasRequest


class LineInterface:
    def __init__(self):
        load_dotenv()
        self.width = int(os.getenv("screen_width"))
        self.height = int(os.getenv("screen_height"))
        self.qr_path = os.getenv("qr_path")
        self.font_path = os.getenv("font_path")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.gas_request = GasRequest()

    def login_screen(self, pincode):
        pygame.display.set_caption("login_qr")
        qrcode = pygame.image.load(self.qr_path)
        qrcode_size = self.height * 5 // 9
        qrcode = pygame.transform.scale(qrcode, (qrcode_size, qrcode_size))
        logo_x = self.width * 5 // 8
        logo_y = self.height * 2 // 9
        message_1 = "右のQRコードから友達追加し、"
        message_2 = "以下のPINコードを送信してください"

        self.screen.fill((0, 0, 0))

        self.screen.blit(qrcode, (logo_x, logo_y))

        font_size = self.height * 1 // 18
        text_font = pygame.font.Font(self.font_path, font_size)
        text = text_font.render(message_1, True, (255, 255, 255))
        w, h = text.get_size()
        text_h = self.height * 2.5 // 9
        text_h_offset = (font_size - h) // 2
        text_w_offset = (self.width * 10 // 16 - w) // 2
        self.screen.blit(text, (text_w_offset, text_h + text_h_offset))

        text = text_font.render(message_2, True, (255, 255, 255))
        w, h = text.get_size()
        text_h = self.height * 3.5 // 9
        text_h_offset = (font_size - h) // 2
        text_w_offset = (self.width * 10 // 16 - w) // 2
        self.screen.blit(text, (text_w_offset, text_h + text_h_offset))

        font_size = self.height * 2 // 9
        text_font = pygame.font.Font(None, font_size)
        text = text_font.render(pincode, True, (255, 255, 255))
        w, h = text.get_size()
        text_h = self.height * 5 // 9
        text_h_offset = (font_size - h) // 2
        text_w_offset = (self.width * 10 // 16 - w) // 2
        self.screen.blit(text, (text_w_offset, text_h + text_h_offset))
        pygame.display.update()

    def logined_screen(self, user_name):
        pygame.display.set_caption("welcome")
        font_size = self.height // 12
        text_font = pygame.font.Font(self.font_path, font_size)
        message1 = "PyGameへようこそ!"
        message2 = f"{user_name}さん"
        text1 = text_font.render(message1, True, (255, 255, 255))
        text2 = text_font.render(message2, True, (255, 255, 255))
        w1, h1 = text1.get_size()
        w2, h2 = text2.get_size()
        h_marge = self.height // 300
        self.screen.fill((0, 0, 0))
        self.screen.blit(
            text1, (self.width // 2 - w1 / 2, self.height // 2 - h1 * 2 - h_marge)
        )
        self.screen.blit(
            text2, (self.width // 2 - w2 / 2, self.height // 2 - h1 + h_marge)
        )
        message = "キーを押してください"
        w, h = text_font.size(message)
        text = text_font.render(message, True, (255, 255, 255))
        self.screen.blit(
            text, (self.width // 2 - w / 2, self.height // 2 + h1 * 2 - h_marge)
        )
        pygame.display.update()
        fps_clock = pygame.time.Clock()
        while True:
            fps_clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.force_quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.force_quit()
                    else:
                        return

    def logout_screen(self):
        pygame.display.set_caption("logout")
        self.screen.fill((0, 0, 0))
        message_1 = "ログアウト処理中"
        font_size = self.height * 1 // 18
        text_font = pygame.font.Font(self.font_path, font_size)
        text = text_font.render(message_1, True, (255, 255, 255))
        w, h = text.get_size()
        self.screen.blit(text, ((self.width - w) // 2, (self.height - h) // 2))
        pygame.display.update()

    def logged_out_screen(self):
        pygame.display.set_caption("logout successfull")
        self.screen.fill((0, 0, 0))
        message = "ログアウト完了"
        font_size = self.height * 1 // 18
        text_font = pygame.font.Font(self.font_path, font_size)
        w, h = text_font.size(message)
        text = text_font.render(message, True, (255, 255, 255))  # 描画する文字列の設定
        self.screen.blit(
            text, [(self.width - w) // 2, (self.height - h) // 2 - h * 2]
        )  # 文字列の表示位置
        message = "キーを押してください"
        w, h = text_font.size(message)
        text = text_font.render(message, True, (255, 255, 255))  # 描画する文字列の設定
        self.screen.blit(
            text, [(self.width - w) // 2, (self.height - h) // 2]
        )  # 文字列の表示位置
        pygame.display.update()  # 画面を更新
        fps_clock = pygame.time.Clock()
        while 1:
            fps_clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:  # 終了イベント
                    self.force_quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.force_quit()
                    else:
                        return

    def get_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return self.force_quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return self.force_quit()

    def force_quit(self):
        pygame.quit()
        self.gas_request.del_pincode()
        sys.exit()

    def wait_login(self, original_pincode):
        timeout = 30 * 100
        while True:
            now_pincode = self.gas_request.get_pincode()
            if now_pincode != original_pincode:
                userId, userName = now_pincode.split(",")
                return [userId, userName]
            self.get_input()
            time.sleep(0.01)
            timeout -= 1
            if timeout <= 0:
                self.force_quit()

    def login(self):
        pincode = self.gas_request.new_pincode()
        self.login_screen(pincode)
        userId, userName = self.wait_login(pincode)
        self.logined_screen(userName)
        return [userId, userName]

    def logout(self, userId, message):
        self.logout_screen()
        self.gas_request.send_line(userId, message)
        self.gas_request.del_pincode()
        self.logged_out_screen()
        self.login()
