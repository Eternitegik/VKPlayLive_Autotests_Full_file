import pytest
import Config

from src import WDWait, AdditionalFunctions

AuthorizedPassed = False


class TestAuthorized:

    def test_authorized(self, MainPage):
        '''301 | Проверка авторизации'''

        global AuthorizedPassed

        WDWait.VisibilityElement(
            MainPage, '//div[contains(@class, "TopMenuRightUnAuthorized_signIn")]', 'Кнопка авторизации не найдена').click()

        tabs = MainPage.window_handles
        MainPage.switch_to.window(tabs[1])

        login = WDWait.VisibilityElement(
            MainPage, '//input[@name="login"]', 'Не найдено поле для логина')

        login.send_keys(Config.USERLOGIN)

        passw = WDWait.VisibilityElement(
            MainPage, '//input[@name="password"]', 'Не найдено поле для пароля')

        passw.send_keys(Config.USERPASSWORD)

        WDWait.VisibilityElement(
            MainPage, '//button[@type="submit"]', 'Не найдена кнопка для авторизации').click()

        MainPage.switch_to.window(tabs[0])

        user_name = WDWait.VisibilityElement(
            MainPage, '//div[contains(@class, "ProfileMenu_name")]', 'Не найдено поле для имени')

        assert Config.USERNAME in user_name.text, 'Имя не соответствует шаблону'

        AuthorizedPassed = True

        AdditionalFunctions.SaveCookies(MainPage)

    @pytest.mark.parametrize(
        ('u_id', 'u_text', 'u_url', 'u_xpath'),
        [
            (1, 'Профиль VK Play', 'https://profile.vkplay.ru/profile/', 'a'),
            (2, 'Настройки профиля', 'https://account.vkplay.ru/profile/userinfo/', 'a'),
            (3, 'Настройки профиля Live', '/app/settings/edit', 'a'),
            # (6, 'Управление сообществом', '/app/settings/edit', 'a'), только у стримера, тест для профиля который не стримил
            (4, 'Бокс кампании', '/app/box/campaigns', 'a'),
            (5, 'Служба поддержки', 'https://support.vkplay.ru/vkp_live', 'a'),
            (1, 'Мой канал', '', 'span'),
            (2, 'Студия', '', 'span'),
        ]
    )
    def test_profileMenu_dropdown(self, MainPage, u_id, u_text, u_url, u_xpath):
        '''302 | Проверка блока с меню профиля после авторизации'''

        if AuthorizedPassed == False:
            pytest.skip("Не пройдена авторизация")
        print("- Открытие блока")
        u_btn = WDWait.VisibilityElement(
            MainPage, '//div[contains(@class, "TopMenuRightAuthorized")]', 'Не найдена кнопка открытия меню пользователя')
        u_btn.click()
        print(f"- Поиск кнопки {u_text}")
        a_buttons = WDWait.VisibilityElement(
            MainPage, f'(//{u_xpath}[contains(@class, "ProfileMenuList_link")])[{u_id}]', f'Не найдена кнопка {u_text}')
        print(f"- Поиск элемента в кнопке для текста {u_text}")
        a_buttons_text = WDWait.VisibilityElement(
            MainPage, f'(//{u_xpath}[contains(@class, "ProfileMenuList_link")]//div[contains(@class, "ProfileMenuItem_item")])[{u_id}]', 'Не найден элемент с текстом у кнопки')

        print(f'- Проверка кнопки "{u_text}"')
        assert u_text in a_buttons_text.text, 'Неправильный текст кнопки'
        if u_xpath == 'a':
            assert u_url in a_buttons.get_property(
                'href'), 'Неправильный url для кнопки'

        u_btn.click()
