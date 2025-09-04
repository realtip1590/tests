# Тест входа в личный кабинет

import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("https://ventrago.ru/")
    expect(page.get_by_role("button", name="Войти")).to_be_visible()
    page.get_by_role("button", name="Войти").click()
    expect(page.get_by_role("heading", name="Вход для исполнителя")).to_be_visible()
    page.get_by_role("button", name="Вход").click()
    page.get_by_role("button", name="Далее").click()
    expect(page.get_by_role("heading", name="Вход для исполнителя")).to_be_visible()
    page.locator("input[type=\"tel\"]").click()
    page.locator("input[type=\"tel\"]").fill("+7 (923) 769-8800")
    page.get_by_role("group").filter(has_text="Нажимая на кнопку, вы даете согласие на обработку персональных данных").locator("span").click()
    page.get_by_role("group").filter(has_text="Я ознакомлен(-а) с правилами сервиса").locator("span").click()
    page.get_by_role("button", name="Далее").click()
    expect(page.get_by_role("heading", name="Введите код")).to_be_visible()
    page.locator("input[type=\"tel\"]").click()

    # На тестовой среде необходимо задать переменную с кодом для авторизации

    page.locator("input[type=\"tel\"]").fill("978409")
    page.get_by_role("button", name="Подтвердить").click()
    expect(page.get_by_role("heading", name="Мои данные")).to_be_visible()
    expect(page.locator("[id=\"__nuxt\"] div").filter(has_text="Загрузите паспорт").nth(4)).to_be_visible()
    expect(page.get_by_role("heading", name="Основное")).to_be_visible()
    expect(page.get_by_role("link", name="Мои данные")).to_be_visible()
    expect(page.get_by_role("link", name="Паспорт")).to_be_visible()
    expect(page.get_by_role("heading", name="Адрес Ваш адрес поможет нам предлагать ближайшие к вам задания")).to_be_visible()
    expect(page.get_by_role("button", name="Выйти из аккаунта")).to_be_visible()
