from conftest import browser
from TestPages.PhotoSizesPage import Scenario
from logging_config import setup_logging


def test_photo_sizes(browser):
    """
    Тестовый сценарий скачивания файла.
    """

    # Определение имени для логгера
    logger = setup_logging(test_name='test_photo_sizes')

    # Переходы на сайт
    web_navigator = Scenario(browser)
    web_navigator.go_to_site(' https://sbis.ru/')
    web_navigator.click_on_the_contacts()
    web_navigator.click_on_the_banner_tensor()

    # Переключение драйвера на вкладку с необходимым сайтом
    window_handles = browser.window_handles
    browser.switch_to.window(window_handles[-1])

    assert web_navigator.check_presence_block_in_tensor(), 'Блок "Сила в людях" отсутствует'
    logger.info('Блок "Сила в людях" присутствует')

    web_navigator.click_on_about_in_tensor()
    assert browser.current_url == 'https://tensor.ru/about', ' Сайт https://tensor.ru/about не открылся'
    logger.info('Сайт https://tensor.ru/about открылся')

    assert web_navigator.verify_photo_sizes(), 'Фотографии в блоке имеют разные высоту и ширину'
    logger.info('Фотографии в блоке имеют одинаковую высоту и ширину\n')

    # Очистка обработчика логов
    logger.handlers.clear()




