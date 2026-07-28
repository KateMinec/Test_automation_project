import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации и закрытия драйвера браузера."""
    options = Options()
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    print("\nТест завершен. Оставляем браузер открытым на 5 секунд...")
    time.sleep(5)
    browser.quit()
    print("Браузер успешно закрыт.")