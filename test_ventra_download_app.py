# Тест перехода на страницу для скачивания приложения

import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://ventrago.ru/")
    expect(page.get_by_role("banner").get_by_role("link", name="Ventra GO!")).to_be_visible()
    expect(page.get_by_role("link", name="Скачать VentraGo!").nth(1)).to_be_visible()
    page.get_by_role("link", name="Скачать VentraGo!").nth(2).click()
    expect(page.get_by_role("heading", name="Сканируйте QR код")).to_be_visible()
    expect(page.locator("#downloadAppBlock canvas")).to_be_visible()