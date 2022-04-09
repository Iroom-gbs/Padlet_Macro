import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

option = webdriver.ChromeOptions()
option.add_argument("headless")
driver = webdriver.Chrome("./chromedriver", chrome_options=option)

url = input("매크로를 돌릴 페이지 URL: ")


def good_macro():
    a = int(input("좋아요 수"))
    k = int(input("몇번째 글에 좋아요를 달까요?"))
    print("좋아요 다는 중...")
    for i in range(a):
        s = [chr(random.randint(97, 123)) for _ in range(5)]
        driver.get(url)
        time.sleep(0.5)
        driver.delete_cookie('ww_p')
        cookie = {'name': "ww_p", 'value': ''.join(s)}
        driver.add_cookie(cookie)
        driver.find_element(by=By.XPATH, value=f"/html/body/div[3]/div[2]/div[2]/div[{k}]/div/article/div["
                                               "1]/section/div/div/div").click()


def mk_post(*args):
    driver.get(url)
    x = "/html/body/div[3]/div[3]/div[1]/button"
    b = "/html/body/div[3]/div[4]/div/div/div/div/div[2]/div/div[1]/div[1]/textarea"
    btn = '/html/body/div[3]/div[4]/div/div/div/div/div[1]/div[2]/button'
    for i in args:
        driver.find_element(by=By.XPATH, value=x).click()
        time.sleep(1.5)
        driver.find_element(by=By.XPATH, value=b).send_keys(i)
        time.sleep(1.5)
        driver.find_element(by=By.XPATH, value=btn).click()


def mk_rand():
    n = int(input("몇개의 랜덤한 스트링을 만들까요?\n"))
    return [''.join([chr(random.randint(48, 122)) for _ in range(random.randint(1, 10))]) for __ in range(n)]


done = False
while not done:
    command = input("커맨드 입력\n")
    if command == "g":
        good_macro()
    elif command == 'm':
        inp = input("랜덤한 스트링을 입력하시려면 r을 아니면 입력할 스트링을 띄어쓰기로 구분하여 입력해주세요\n").split()
        if len(inp) == 1 and inp[0] == 'r':
            mk_post(*mk_rand())
        else:
            mk_post(*inp)
    elif command == 'q':
        print("종료합니다")
        done = True
