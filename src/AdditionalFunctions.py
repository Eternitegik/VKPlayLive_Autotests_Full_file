import json
import pickle
import re

AuthorizedCookiesName = 'SaveCookies/AuthorizedAllCookies'
AuthorizedTokenName = 'SaveCookies/AuthorizedToken'


# Проверка значения через регулярное выражение (Не реализовано)
def RegularAssert(pattern, url):

    # pattern = r'https://support\.vkplay\.ru/vkp_live/$'
    match = re.match(pattern, url)
    if match:
        return True
    else:
        return False


# Функция для сохранения полной куки в файл и только токена
def SaveCookies(driver):
    AuthorizedCookies = driver.get_cookies()

    for cookie in AuthorizedCookies:
        if 'accessToken' in cookie.get('value', ''):
            AuthorizedToken = json.loads(cookie['value'])['accessToken']
            break

    pickle.dump(AuthorizedCookies, open(
        AuthorizedCookiesName, "wb"))

    with open(AuthorizedTokenName, 'w') as f:
        f.write(AuthorizedToken)


def AddCookies(driver):
    for cookie in pickle.load(open(AuthorizedCookiesName, "rb")):
        driver.add_cookie(cookie)


def GetCookieToken():
    with open(AuthorizedTokenName, 'r') as f:
        return f.read()
