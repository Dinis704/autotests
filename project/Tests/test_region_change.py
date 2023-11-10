from conftest import browser
from TestPages.RegionChangePage import Scenario
from logging_config import setup_logging


def test_region_change(browser):
    """
    Тестовый сценарий смены региона
    """

    # Определение имени для логгера
    logger = setup_logging(test_name='test_region_change')

    # Тестовые данные
    my_region = 'Республика Башкортостан'
    example_region = {'name': 'Камчатский край',
                      'id': '41-kamchatskij-kraj'}

    # Переход на сайт
    web_navigator = Scenario(browser)
    web_navigator.go_to_site(' https://sbis.ru/')
    web_navigator.click_on_the_contacts()

    current_region = web_navigator.get_the_current_region()
    assert current_region == my_region, f'Определился другой регион "{current_region}"'
    logger.info(f'Определился мой регион {current_region}')

    list_of_partners = web_navigator.get_list_of_partners().text
    assert list_of_partners, 'Список партнеров отсутствует'
    logger.info(f'Список партнеров есть')

    # Смена региона
    new_current_region = web_navigator.change_the_region(example_region.get('name'))

    assert current_region != new_current_region, f'Подставился регион "{current_region}", вместо "{new_current_region}"'
    logger.info(f'Подставился выбранный регион {example_region.get("name")}')

    new_list_of_partners = web_navigator.get_list_of_partners().text
    assert list_of_partners != new_list_of_partners, 'Список партнеров не изменился'
    logger.info('Список партнеров изменился')

    assert example_region.get('id') in browser.current_url, 'url не содержит информацию выбранного региона'
    assert example_region.get('name') in browser.title, 'title не содержит информацию выбранного региона'
    logger.info('url и title содержат информацию выбранного региона\n')

    # Очистка обработчика логов
    logger.handlers.clear()
