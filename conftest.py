from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from src import WDWait

import pytest
import Config

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()

ListRes = []

# --- выполнить тесты без отображения интерфейса ---
options.add_argument("--headless")
# --- игнорировать ошибки сертификатов сайта ---
# options.add_argument("--ignore-certificate-errors")
# --- не использовать кэш страницы ---
# options.add_argument("--disable-cache")
# --- запускать браузер в режиме инкогнито ---
options.add_argument("--incognito")
# --- запускать браузер с заданным разрешением ---
options.add_argument("--window-size=1920,1080")


@pytest.fixture(scope='class')
def setup():
    driver = webdriver.Chrome(service=service, options=options)
    return driver


@pytest.fixture(scope='class')
def MainPage(setup):
    setup.get(Config.MAINPAGEURL)
    WDWait.VisibilityElement(
        setup, '//span[contains(@class, "PopupContent_close") and contains(@class, "NewsPopup_close")]').click()
    return setup


@pytest.fixture(scope='class')
def StreamPage(setup):
    setup.get(Config.STREAMPAGEURL)
    return setup


# ----------------------- настройка отображения отчета --------------------

    # print("/*/ ", vars(report))
    # print("__name__: ", dir(outcome))


def pytest_html_report_title(report):
    report.title = "VKPlay.live"


def pytest_html_results_table_header(cells):
    cells.insert(
        0, '<th class="sortable" data-column-type="idt">Test ID</th>')
    cells.insert(2, '<th>Title</th>')
    cells.insert(3, '<th>Description/Steps</th>')
    cells.insert(4, '<th>Error Message</th>')


def pytest_html_results_table_row(report, cells):
    t = report.description
    t = t.split('|')
    cells.insert(0, f'<td class="col-idt">{t[0]}</td>')
    cells.insert(2, f"<td>{t[1]}</td>")
    cells.insert(3, f"<td>{report.steps}</td>")
    cells.insert(4, f"<td>{report.error_message}</td>")


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["<p>Тут происходит магия</p>"])


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    ta = report.nodeid.split('::')[2]
    if '[' in ta:
        ta = ta.replace('[', '</br>[', 1)
    t = f'{report.nodeid.split('::')[1]}//{ta}'
    report.nodeid = t
    report.description = str(item.function.__doc__)
    report.steps = ""
    report.error_message = ""

    setattr(item, "rep_" + report.when, report)
    report.error_message = str(call.excinfo.value) if call.excinfo else ""

    if report.when == "call" and report.passed:
        step = item.rep_call.sections
        if step:
            report.steps = step[0][1].replace("\n", "</br>")
        else:
            report.steps = ""

    if report.when == "call" and report.skipped or report.failed:
        error_mes = item.rep_call.error_message
        report.error_message = error_mes.replace("\n", "</br>")
        report.error_message = f'Ошибка: </br> {
            report.error_message}'.split('Stacktrace:')[0]
        report.error_message = report.error_message.replace(' Message: ', '')
        step = item.rep_call.sections
        if step:
            report.steps = step[0][1].replace("\n", "</br>")
        else:
            report.steps = ""

    # print("__name__: ", outcome.get_result())
