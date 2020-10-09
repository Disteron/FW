
from core.driver_action import DriverAction

WEB_NAME = 'https://testing1.alytics.ru/projects'

DICT_XPATH = {
    'Логин': '//input[@name="login"]',
    'Пароль': '//input[@name="password"]',
    'Запомнить меня': '//input[@id="check2"]',
    'Войти': '//input[@value="Войти"]',
    'Добавить проект': '//a[text()="Добавить проект"]',
    'Название проекта': '//input[@class="text-input validate[required, maxSize[100]]"]',
    'Сайт': '//input[@class="text-input validate[required,custom[user_url], maxSize[100]]"]',
    'Выберите страну': '//a/span[text()="Выберите страну"]',
    'Россия': '//ul/li[text()="Россия"]',
    'Далее': '//input[@value="Далее"]',
    'Логин ЯндексДирект': '//input[@class="text-input validate[required,custom[yandex_direct_login], maxSize[100]]"]',
    'Войти[Яндекс]': '//button[@class="Button2 Button2_size_l Button2_view_action Button2_width_max Button2_type_submit"]',
    'Введите пароль': '//input[@type="password"]',
    'Все кампании аккаунта': '//input[@class="campaigns-method all-campaigns"]',
    'Логин[Google]': '//input[@aria-label="Телефон или адрес эл. почты"]',
    'Далее[Google]': '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc"]',
}


def get_xpath(name):
    return DICT_XPATH.get(name)


def test(start_browser):
    driver = start_browser
    driverObject = DriverAction(driver=driver, timeout=15)
    driverObject.go_to_web(WEB_NAME)
    driverObject.fill_field(field_xpath=get_xpath("Логин"), value="oleg.rudenko.99992@mail.ru")
    driverObject.fill_field(field_xpath=get_xpath("Пароль"), value="rvKent13")
    driverObject.click_button(xpath=get_xpath("Запомнить меня"))
    driverObject.click_button(xpath=get_xpath("Войти"))
    driverObject.click_button(xpath=get_xpath('Добавить проект'))
    driverObject.fill_field(field_xpath=get_xpath("Название проекта"), value="Alytics_Test")
    driverObject.fill_field(field_xpath=get_xpath("Сайт"), value="Test.com")
    driverObject.click_button(xpath=get_xpath("Выберите страну"))
    driverObject.click_button(xpath=get_xpath("Россия"))
    driverObject.click_button(xpath=get_xpath("Далее"))
    driverObject.fill_field(field_xpath=get_xpath("Логин ЯндексДирект"), value="alytics.test.1")
    driverObject.click_button(xpath=get_xpath("Далее"))
    driverObject.switch_window(1)
    driverObject.click_button(xpath=get_xpath("Войти[Яндекс]"))
    driverObject.fill_field(field_xpath=get_xpath("Введите пароль"), value="qwertytest123")
    driverObject.click_button(xpath=get_xpath("Войти[Яндекс]"))
    driverObject.switch_window(0)
    driverObject.click_button(xpath=get_xpath("Все кампании аккаунта"))
    driverObject.click_button(xpath=get_xpath("Далее"))
    driverObject.click_button(xpath=get_xpath("Далее"))
    driverObject.switch_window(1)
    driverObject.fill_field(field_xpath=get_xpath("Логин[Google]"), value="pelmen322228@gmail.com")
    driverObject.click_button(xpath=get_xpath("Далее[Google]"))
    ### далее гугл всю малину подпортил)
