"""
Конфигурационный файл pytest с webdriver-manager для совместимости с Selene
"""
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    """Фикстура для управления браузером"""
    # Настройка опций Chrome
    options = Options()
    options.page_load_strategy = 'eager'
    options.add_argument('--window-size=1600,1200')

    # Используем webdriver-manager для совместимости с Selene
    service = Service(ChromeDriverManager().install())

    # Конфигурация браузера
    browser.config.driver = webdriver.Chrome(service=service, options=options)
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 6.0

    yield

    # Очистка после теста
    browser.quit()