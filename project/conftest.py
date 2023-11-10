import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    """
    Определяет фикстуру browser.
    Создает экземпляр драйвера Chrome.
    Закрывает браузер после выполнения всех тестов.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
