import pyautogui as pag
from time import sleep
from utils import set_title
from options import OPTIONS

def set_option(option: str) -> None:
    pag.write(option)

def set_options(options):
    for option in options:
        set_option(option)
        sleep(2)
        pag.press("tab")
        pag.press("tab")

pag.press("win")
sleep(2)
pag.write("firefox")
sleep(2)
pag.press("enter")
sleep(5)
pag.write("https://web.whatsapp.com/")
sleep(2)
pag.press("enter")
sleep(60)
for _ in range(0,7):
    pag.press("tab")
pag.write("2024")
sleep(2)
pag.press("enter")
sleep(2)
for _ in range(0,25):
    pag.press("tab")
sleep(2)
pag.press("enter")
sleep(2)
for _ in range(0,5):
    pag.press("down")
pag.press("enter")

sleep(3)
pag.write(set_title())
pag.press("tab")
pag.press("tab")
sleep(2)
set_options(OPTIONS)
pag.press("tab")
pag.press("tab")
pag.press("tab")
pag.press("enter")
sleep(20)
pag.hotkey("alt", "f4")
