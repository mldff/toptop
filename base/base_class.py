import logging
import re
import time
from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Переход на страницу"""

    def go_to_url(self, url):
        try:
            self.driver.get(url)
            current_url = self.driver.current_url
            print(current_url, url)
            assert current_url == url, logging.error(f"URL не соответсвует: {current_url} != {url}")
            logging.info(f"Переход по странице {url} - ОК")
        except TimeoutException:
            print("Не загрузилась страница. Повторяю переход...")
            self.driver.get(url)

    """Закрытие попапа с предложением о рассылке"""

    def close_popup(self, element):
        # Ожидание появления попапа, максимальное время ожидания 10 секунд
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, element))
        )

    """Клик по элементу"""

    def click_on_element(self, element, description):
        try:
            element.click()
            logging.info(f"Нажатие на '{description}' - OK")
        except Exception as e:
            self.scroll_to_element(element)
            # Повторное ожидание кликабельности элемента
            element.click()

    """Получение элемента по локатору"""

    def get_element(self, locator, timeout=10):
        # Ожидание, пока элемент станет кликабельным. Были проблемы, что не всегда получаем товар по локатору, поэтому сделал проверку до 3 раз, если не находим элемент
        attempts = 0
        max_attempts = 3

        while attempts < max_attempts:
            try:
                # Ожидание появления и кликабельности элемента
                element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator)))
                return element
            except Exception as e:
                attempts += 1
                time.sleep(5)  # Пауза перед новой попыткой

        logging.error(f"Не удалось найти кликабельный элемент {locator} после {max_attempts} попыток")
        return None

    """Ввод текста в элемент"""

    def enter_text(self, element, text, description):
        element.send_keys(text)
        logging.info(f"Ввод текста '{text}' в поле '{description}' - OK")

    """Проверка текста на странице с шаблоном"""

    def assert_text(self, word, result, description):
        assert word == result, logging.error(
            f"Текст '{word}' для '{description}' не соответствует верному значению - '{result}'"
        )
        logging.info(f"Проверка текста '{word}' для '{description}' верная - OK")

    """Создание скриншота при ошибках"""

    def get_screenshot(self, test_name, exc_info):
        """Делаем скриншот после ошибки"""
        logging.error(f"Тест - {test_name} упал с ошибкой: {exc_info}")
        now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screen = f"{now_date}_{test_name}.png"
        self.driver.save_screenshot(f"..\\screen\\{name_screen}")
        logging.info(f"Скриншот {name_screen} был добавлен в папку 'screen'")

    """Убираем ховер с элемента"""

    def hover_element(self, x, y, description):
        # В данном случае нужно, чтобы убрать всплывающее меню с хедера, которое перекрывает другие элементы
        try:
            actions = ActionChains(self.driver)
            actions.move_by_offset(x, y).perform()
            logging.info(f"Наведение '{description}' - OK")
        except Exception as e:
            logging.error(f"Ошибка при наведении '{description}': {e}")

    """Изменение ползунка для выбора цены и других фильтров"""

    def move_slider(self, element, position):
        try:
            self.driver.execute_script(f"""
                const sliderHandle = arguments[0];
                sliderHandle.style.left = '{position}'; // Пример значения, которое нужно настроить
                sliderHandle.style.transform = 'translateX(-{position})'; // Обновление трансформации
            """, element)
            logging.info(f"Положение ползунка изменено на {position}%")
        except Exception as e:
            logging.error(f"Положение позунка не изменилось. Ошибка: {e}")

    """Скролл к элементу, если не видим элемент"""

    def scroll_to_element(self, element):
        try:

            # Прокрутим к элементу
            self.driver.execute_script(f"window.scrollBy(0, 200);")

            # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except Exception as e:
            print(f"Ошибка при прокрутке к элементу: {e}")

    """Проверка карточек в корзине и удаление, если они имеются"""

    def check_and_clear_cart(self, element_xpath):
        cart_items = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, element_xpath))
        )

        if cart_items:  # Если корзина не пуста
            """Удаление всех товаров"""
            cart_items.click()
            logging.info("Все товары удалены из корзины.")
        else:
            logging.info("Корзина пуста.")

    """Парсинг цены товара"""

    def get_number(self, price):
        actual_price = re.findall(r"(\d[\d\s]*)₽", price)
        return float(actual_price[-1].strip().replace(" ", ""))
