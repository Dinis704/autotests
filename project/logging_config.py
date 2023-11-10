import logging
import os


def setup_logging(test_name):
    """
    Конфигурация логирования тестов.
    Записывает логи в log-файл с названием test_name в созданную папку logs.
    Возвращает объект для записи логов.
    """

    # Создание папки logs(если его нет) и файла для записи логов в папке Tests в зависимости от того,
    # откуда запускается тест
    current_directory = os.getcwd()

    if not os.path.basename(current_directory) == "Tests":
        log_directory = os.path.join('Tests', 'logs')
    else:
        log_directory = 'logs'

    os.makedirs(log_directory, exist_ok=True)
    log_file = os.path.join(log_directory, f'{test_name}.log')

    # Создание объекта логгера и определения минимального уровня логирования
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)

    # Конфигурации для записи логов в файл
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
