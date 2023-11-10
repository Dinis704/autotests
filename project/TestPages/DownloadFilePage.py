from BaseApp import BasePage
from TestPages.locators import Locators as L
import re


class Scenario(BasePage):
    """
    Определяет методы для сценария скачивания файла.
    """
    def click_to_download_in_footer(self):
        """
        Выполняет переход по ссылке для скачивания файла.
        """
        self.find_element(L.download_file_page_locators.get('SBIS_DOWNLOAD_IN_FOOTER'), do_click=True)

    def get_sbis_plugin(self):
        """
        Переходит по разделу "СБИС Плагин".
        Переходит по подразделу "Windows" независимо от выбора по умолчанию.
        Возвращает список из ссылки на скачивание веб-установщика и его размера, указанного на сайте.
        """
        self.find_element(L.download_file_page_locators.get('SBIS_PLUGIN_SECTION'), do_click=True)
        self.find_element(L.download_file_page_locators.get('OS_WINDOWS_SELECT'), do_click=True)
        element = self.find_element(L.download_file_page_locators.get('SBIS_PLUGIN_DOWNLOAD_LINK'))
        link = element.get_attribute('href')
        file_size = float(re.search(r"\d+\.\d+", element.text).group())
        return [link, file_size]


