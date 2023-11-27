"""
Модуль с фикстурами для UI-тестов.
"""
import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="session", autouse=True)
def create_driver_session() -> Chrome:
    """
    Фикстура создания сессии браузера Chrome и перехода на сайт reqres.in.

    Окно браузера раскрывается до полного размера.

    Браузер ждет 5 секунд, пока прогрузится элемент на странице.

    :return: driver (Chrome)
    """
    site: str = "https://reqres.in"
    driver: Chrome = webdriver.Chrome()
    driver.get(site)
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


@pytest.fixture(scope="session", autouse=True)
def quit_driver_session(create_driver_session: WebDriver) -> None:
    """
    Фикстура закрытия сессии браузера Chrome.

    :param create_driver_session: WebDriver
    :return: None
    """
    yield
    create_driver_session.quit()
