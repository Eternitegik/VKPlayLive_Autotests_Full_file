from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WDTIMER = 5


def AssertVisibilityElement(driver, xpath, err=''):
    '''Проверяет виден ли пользователю элемент'''
    assert WebDriverWait(driver, WDTIMER).until(EC.visibility_of_element_located((
        'xpath', xpath)), err)


def VisibilityElement(driver, xpath, err=''):
    '''Проверяет виден ли пользователю элемент и возвращает его'''
    return WebDriverWait(driver, WDTIMER).until(EC.visibility_of_element_located((
        'xpath', xpath)), err)


def AssertVisibilityElement_s(driver, xpath, err=''):
    '''Проверяет видны ли пользователю элементы'''
    assert WebDriverWait(driver, WDTIMER).until(EC.visibility_of_all_elements_located((
        'xpath', xpath)), err)


def VisibilityElement_s(driver, xpath, err=''):
    '''Проверяет вдны ли пользователю элементы и возвращает их'''
    return WebDriverWait(driver, WDTIMER).until(EC.visibility_of_all_elements_located((
        'xpath', xpath)), err)


def AssertPresenceElement(driver, xpath, err=''):
    '''Проверяет находится ли элемент на странице'''
    assert WebDriverWait(driver, WDTIMER).until(EC.presence_of_element_located((
        'xpath', xpath)), err)


def PresenceElement(driver, xpath, err=''):
    '''Проверяет находится ли элемент на странице и возвращает его'''
    return WebDriverWait(driver, WDTIMER).until(EC.presence_of_element_located((
        'xpath', xpath)), err)


def AssertPresenceElement_s(driver, xpath, err=''):
    '''Проверяет находится ли элементы на странице'''
    assert WebDriverWait(driver, WDTIMER).until(EC.presence_of_all_elements_located((
        'xpath', xpath)), err)


def PresenceElement_s(driver, xpath, err=''):
    '''Проверяет находится ли элементы на странице и возвращает их'''
    return WebDriverWait(driver, WDTIMER).until(EC.presence_of_all_elements_located((
        'xpath', xpath)), err)
