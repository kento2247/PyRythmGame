import sys

import pygame
from pygame.locals import *

import control_pincode
import send_line

# import raspi_led

# ラズパイのデフォルトだとpngファイルを読めないので以下を実行
# sudo apt-get install libsdl2-image-2.0-0
# qr_path = "/Users/tokurakento/Desktop/プログラミング基礎/functions/linebot_qr.png"

# 2022/06/23 gas python_hub deploy version 23

qr_path = ""
font_path = ""
gas_url = ""

width = 1200
height = 675
screen = 0
pygame.display.set_caption("login_qr")


def screen_init():
    global screen
    screen = pygame.display.set_mode((width, height))


def led_control(command):
    return
    if command:
        raspi_led.raspi_led_init()
        raspi_led.raspi_led_on()
    else:
        raspi_led.raspi_led_off()
        raspi_led.raspi_gpio_end()


def login_qr():
    pincode = control_pincode.control_pincode(gas_url, "set")
    screen_init()
    pygame.display.set_caption("login_qr")
    qrcode = pygame.image.load(qr_path)
    qrcode_size = height * 5 // 9
    qrcode = pygame.transform.scale(qrcode, (qrcode_size, qrcode_size))
    logo_x = width * 5 // 8
    logo_y = height * 2 // 9
    message_1 = "右のQRコードから友達追加し、"
    message_2 = "以下のPINコードを送信してください"

    screen.fill((0, 0, 0))
    screen.blit(qrcode, (logo_x, logo_y))
    font_size = height * 1 // 18
    text_font = pygame.font.Font(font_path, font_size)
    text = text_font.render(message_1, True, (255, 255, 255))
    w, h = text.get_size()
    text_h = height * 2.5 // 9
    text_h_offset = (font_size - h) // 2
    text_w_offset = (width * 10 // 16 - w) // 2
    screen.blit(text, (text_w_offset, text_h + text_h_offset))
    text = text_font.render(message_2, True, (255, 255, 255))
    w, h = text.get_size()
    text_h = height * 3.5 // 9
    text_h_offset = (font_size - h) // 2
    text_w_offset = (width * 10 // 16 - w) // 2
    screen.blit(text, (text_w_offset, text_h + text_h_offset))
    font_size = height * 2 // 9
    text_font = pygame.font.Font(None, font_size)
    text = text_font.render(pincode, True, (255, 255, 255))
    w, h = text.get_size()
    text_h = height * 5 // 9
    text_h_offset = (font_size - h) // 2
    text_w_offset = (width * 10 // 16 - w) // 2
    screen.blit(text, (text_w_offset, text_h + text_h_offset))
    pygame.display.update()
    return pincode


def logined_screen(userName):
    pygame.display.set_caption("welcome")
    font_size = height // 12
    text_font = pygame.font.Font(font_path, font_size)
    message1 = "PyGameへようこそ!"
    message2 = userName + "さん"
    text1 = text_font.render(message1, True, (255, 255, 255))
    text2 = text_font.render(message2, True, (255, 255, 255))
    w1, h1 = text1.get_size()
    w2, h2 = text2.get_size()
    h_marge = height // 300
    screen.fill((0, 0, 0))  # 画面全体を黒色に塗りつぶし
    screen.blit(text1, (width // 2 - w1 / 2, height // 2 - h1 * 2 - h_marge))
    screen.blit(text2, (width // 2 - w2 / 2, height // 2 - h1 + h_marge))
    message = "キーを押してください"
    w, h = text_font.size(message)
    text = text_font.render(message, True, (255, 255, 255))  # 描画する文字列の設定
    screen.blit(text, (width // 2 - w / 2, height // 2 + h1 * 2 - h_marge))
    pygame.display.update()  # 画面を更新
    fps_clock = pygame.time.Clock()
    led_control(1)
    while 1:
        fps_clock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:  # 終了イベント
                led_control(0)
                force_quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    led_control(0)
                    force_quit()
                else:
                    led_control(0)
                    return


def get_input():
    for event in pygame.event.get():
        if event.type == QUIT:  # 閉じるボタンが押されたら終了
            return force_quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return force_quit()


def force_quit():
    pygame.quit()  # Pygameの終了(画面閉じられる)
    control_pincode.control_pincode(gas_url, "del")
    sys.exit()


def line_login(Width, Height, Qr_path, Font_path, Gas_url):
    global width
    global height
    global qr_path
    global font_path
    global gas_url
    width, height, qr_path, font_path, gas_url = (
        Width,
        Height,
        Qr_path,
        Font_path,
        Gas_url,
    )
    pincode = login_qr()
    led_control(1)
    while 1:
        now_pincode = control_pincode.control_pincode(gas_url, "get")
        get_input()
        if now_pincode != pincode:
            userId, userName = now_pincode.split(",")
            logined_screen(userName)
            led_control(0)
            return [userId, userName]


def line_logout(userId, message):
    pygame.display.set_caption("logout")
    # screen_init()
    screen.fill((0, 0, 0))
    font_size = height * 1 // 18
    message_1 = "ログアウト処理中"
    text_font = pygame.font.Font(font_path, font_size)
    text = text_font.render(message_1, True, (255, 255, 255))
    w, h = text.get_size()
    screen.blit(text, ((width - w) // 2, (height - h) // 2))
    pygame.display.update()
    send_line.send_line(gas_url, userId, message)
    control_pincode.control_pincode(gas_url, "del")

    screen.fill((0, 0, 0))
    message = "ログアウト完了"
    w, h = text_font.size(message)
    text = text_font.render(message, True, (255, 255, 255))  # 描画する文字列の設定
    screen.blit(text, [(width - w) // 2, (height - h) // 2 - h * 2])  # 文字列の表示位置
    message = "キーを押してください"
    w, h = text_font.size(message)
    text = text_font.render(message, True, (255, 255, 255))  # 描画する文字列の設定
    screen.blit(text, [(width - w) // 2, (height - h) // 2])  # 文字列の表示位置
    pygame.display.update()  # 画面を更新
    fps_clock = pygame.time.Clock()
    led_control(1)
    while 1:
        fps_clock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:  # 終了イベント
                led_control(0)
                force_quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    led_control(0)
                    force_quit()
                else:
                    led_control(0)
                    return
