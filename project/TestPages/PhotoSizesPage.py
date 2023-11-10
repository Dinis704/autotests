from BaseApp import BasePage
from TestPages.locators import Locators as L


class Scenario(BasePage):
    """
    Определяет методы для сценария проверки размеров фотографий на сайте.
    """

    def click_on_the_contacts(self):
        """
        Выполняет переход по разделу "Контакты".
        """
        self.find_element(L.photo_sizes_page_locators.get('CONTACTS_SECTION'), do_click=True)

    def click_on_the_banner_tensor(self):
        """
        Выполняет переход по баннеру "Тензор".
        """
        self.find_element(L.photo_sizes_page_locators.get('BANNER_TENSOR'), do_click=True)

    def check_presence_block_in_tensor(self):
        """
        Проверяет наличие блока на странице.
        Возвращает элемент с блоком.
        """
        return self.find_element(L.photo_sizes_page_locators.get('BLOCK_IN_TENSOR'))

    def click_on_about_in_tensor(self):
        """
        Выполняет переход по ссылке "Подробнее".
        """
        self.find_element(L.photo_sizes_page_locators.get('ABOUT_IN_TENSOR'), do_click=True)

    def verify_photo_sizes(self):
        """
        Проверяет одинковые ли размеры фотогрфий, найденных в разделе, по высоте и ширине относительно первой фотографии.
        Возвращает True или False в зависимости от результата проверки.
        """
        self.find_element(L.photo_sizes_page_locators.get('TENSOR_ABOUT_SECTION'))
        photo_elements = self.find_elements(L.photo_sizes_page_locators.get('SECTION_WITH_PHOTO'))
        sample_height = photo_elements[0].get_attribute('height')
        sample_width = photo_elements[0].get_attribute('width')
        return all(photo_element.get_attribute('height') == sample_height and photo_element.get_attribute('width') ==
                   sample_width for photo_element in photo_elements[1:])




