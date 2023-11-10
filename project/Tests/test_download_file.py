from conftest import browser
from TestPages.DownloadFilePage import Scenario
from logging_config import setup_logging
import requests
import os


def test_download_file(browser):
    """
    Тестовый сценарий скачивания файла.
    """

    # Определение имени для логгера
    logger = setup_logging(test_name='test_download_file')

    # Переход на сайт
    web_navigator = Scenario(browser)
    web_navigator.go_to_site('https://sbis.ru/')

    # Получение информации о фале
    web_navigator.click_to_download_in_footer()
    link, file_size_in_text = web_navigator.get_sbis_plugin()

    # Скачивание файла в папку Tests в зависимости от того, откуда запускается тест
    response = requests.get(link)
    file_name = "plugin.exe"
    current_directory = os.getcwd()

    if not os.path.basename(current_directory) == "Tests":
        file_path = os.path.join("Tests", file_name)
    else:
        file_path = os.path.join(current_directory, file_name)

    with open(file_path, "wb") as file:
        file.write(response.content)

    # Проверка наличия скачанного файла и определение его размера в МБ
    file_name = os.path.basename(file_path)
    file_size = round(os.path.getsize(file_path) / (1024 ** 2), 2)

    assert file_name == 'plugin.exe', 'Файл не найден'
    assert file_size == file_size_in_text, 'Размер скачанного файла не совпадает с размером, указанным на сайте'

    # Запись логов
    logger.info(f'Файл успешно скачан: {file_name}')
    logger.info(f'Размер скачанного файла: {file_size} MБ')
    logger.info(f'Размер файла на сайте: {file_size_in_text} MБ\n')

    # Очистка обработчика логов
    logger.handlers.clear()



