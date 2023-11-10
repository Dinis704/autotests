from selenium.webdriver.common.by import By


class Locators:
    """
    Определяет поля - словари для сценариев, содержащие в себе локаторы на соответствующие элементы.
    """

    photo_sizes_page_locators = {
        'CONTACTS_SECTION': (By.XPATH, '//a[text()="Контакты"]'),
        'BANNER_TENSOR': (By.XPATH, '//div[starts-with(text(),"г. Ярославль")]/preceding-sibling::a'),
        'BLOCK_IN_TENSOR': (By.XPATH, '//p[contains(text(), "Сила в людях")]'),
        'ABOUT_IN_TENSOR': (By.XPATH, '//p[contains(text(), "Сила в людях")]/'
                                      'following-sibling::p/a[contains(text(), "Подробнее")]'),
        'TENSOR_ABOUT_SECTION': (By.XPATH, '//h2[text()="Работаем"]'),
        'SECTION_WITH_PHOTO': (By.XPATH, '//img[contains(@class, "tensor_ru-About__block3-image")]'),
    }

    region_change_page_locators = {
        'CONTACTS_SECTION': (By.XPATH, '//a[text()="Контакты"]'),
        'CURRENT_REGION': (By.XPATH, '//span[contains(@class, "sbis_ru-Region-Chooser__text")]'),
        'LIST_OF_PARTNERS': (By.XPATH, '//div[contains(@class, "sbisru-Contacts-List__col")]'),
        'КАМЧАТСКИЙ_КРАЙ': (By.XPATH, '//span[contains(@title, "Камчатский край")]')
    }

    download_file_page_locators = {
        'SBIS_DOWNLOAD_IN_FOOTER': (By.XPATH, '//div[contains(@class, "sbisru-Footer__container")]'
                                              '//a[contains(text(),"Скачать СБИС")]'),
        'SBIS_PLUGIN_SECTION': (By.XPATH, '//div[contains(text(), "СБИС Плагин") and '
                                          '@class="controls-TabButton__caption"]'),
        'OS_WINDOWS_SELECT': (By.XPATH, '//div[@name="TabButtons"]//span[text()="Windows"]'),
        'SBIS_PLUGIN_DOWNLOAD_LINK': (By.XPATH, '//h3[contains(text(), "Веб-установщик")]/'
                                                'parent::div/following-sibling::div//a')
    }
