from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Определяет базовые методы для работы с WebDriver
    """

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, do_click=False, timeout=10):
        """
        Находит элемент по локатору locator,ожидая его появления на странице в течение времени timeout(в секундах).
        Если do_click=True, вызывается метод try_to_click для элемента после явного ожидания,
        когда элемент станет кликабельным.
        Возвращает найденный элемент.
        """
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator),
                                                      message=f'Невозможно найти элемент по локатору {locator}')
        if do_click:
            element = wait.until(EC.element_to_be_clickable(locator),
                                                      message=f'Элемент по локатору {locator} не кликабельный')
            self.try_to_click(element)
        return element

    def find_elements(self, locator, timeout=10):
        """
        Находит все элементы по локатору locator на странице,ожидая их появления на
        странице в течение времени timeout(в секундах).
        Возвращает список найденных элементов.
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Невозможно найти элементы по локатору {locator}')

    def text_to_be_present_in_element(self, element, text, timeout=10):
        """
        Ожидает присутсвия в элементе element текста text в течение времени timeout(в секундах).
        Возвращает данный элемент.
        """
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(element, text),
                                                      message=f'В элементе {element} отсутствует текст {text}')

    def try_to_click(self, element):
        """
        Выполняет клик по элементу element методом класса WebDriver.
        Если клик выполнить не удалось, запускается скрипт на JavaScript для выполнения клика по элементу.
        """
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script('arguments[0].click();', element)

    def go_to_site(self, url):
        """
        Выполняет переход сайт по адресу url в браузере.
        """
        self.driver.get(url)
