from BaseApp import BasePage
from TestPages.locators import Locators as L


class Scenario(BasePage):
    """
    Определяет методы для сценария смены региона на сайте.
    """

    def click_on_the_contacts(self):
        """
        Выполняет переход по разделу "Контакты".
        """
        self.find_element(L.region_change_page_locators.get('CONTACTS_SECTION'), do_click=True)

    def get_the_current_region(self):
        """
        Возвращает текущий регион на сайте в виде текста.
        """
        return self.find_element(L.region_change_page_locators.get('CURRENT_REGION')).text

    def get_list_of_partners(self):
        """
        Возвращает текущий список партнеров на сайте в виде элемента.
        """
        return self.find_element(L.region_change_page_locators.get('LIST_OF_PARTNERS'))

    def change_the_region(self, new_region: str):
        """
        Выполняет смену региона на new_region.
        Возвращает элемент текущего региона после ожидания смены.
        """
        self.find_element(L.region_change_page_locators.get('CURRENT_REGION'), do_click=True)
        self.find_element(L.region_change_page_locators.get(new_region.replace(' ', '_').upper()), do_click=True)
        return self.text_to_be_present_in_element(L.region_change_page_locators.get('CURRENT_REGION'), new_region)







