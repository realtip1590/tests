# Тест на наличие основных элементов на главной странице сайта (неавторизованный пользователь)

import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://ventrago.ru/")
    expect(page.get_by_role("banner").get_by_role("link", name="Ventra GO!")).to_be_visible()
    expect(page.get_by_role("link", name="Все задания", exact=True)).to_be_visible()
    expect(page.get_by_role("banner").get_by_text("Исполнителям")).to_be_visible()
    expect(page.get_by_role("banner").get_by_text("Компаниям")).to_be_visible()
    expect(page.get_by_role("banner").get_by_role("link", name="Блог")).to_be_visible()
    expect(page.locator("#titlePanelSlider").get_by_role("link", name="Подробнее")).to_be_visible()
    expect(page.get_by_role("link", name="Скачать VentraGo!").nth(4)).to_be_visible()
    expect(page.get_by_role("heading", name="Новые задания в Москве")).to_be_visible()
    expect(page.get_by_role("heading", name="Отзывы о нас")).to_be_visible()
    expect(page.get_by_role("heading", name="Варианты подработки в Москве")).to_be_visible()
    expect(page.locator("section").filter(has_text="Хотите зарабатывать здесь и сейчас? Присоединяйтесь к нашей команде! Скачать при").get_by_role("link")).to_be_visible()
    expect(page.get_by_role("link", name="Начать зарабатывать")).to_be_visible()
    expect(page.locator("#startStepsBlock").get_by_role("link", name="Скачать приложение")).to_be_visible()
    expect(page.get_by_role("link", name="Посмотреть в приложении")).to_be_visible()
    expect(page.get_by_role("heading", name="С нами безопасно!")).to_be_visible()
    expect(page.get_by_role("heading", name="Вопросы и ответы")).to_be_visible()
    expect(page.get_by_text("Подпишитесь на рассылку и получайте лучшие предложения первым! Подписываясь на р")).to_be_visible()
    expect(page.get_by_role("button", name="Заказать звонок")).to_be_visible()
    expect(page.locator("div").filter(has_text="Наш сайт использует куки. Продолжая им пользоваться, вы соглашаетесь на обработк").nth(4)).to_be_visible()
