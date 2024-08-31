import time

from base.base_class import Base
import locators.toptop_shop


class Catalog(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Открытие каталога и выбор типа товара"""

    def to_catalog(self):
        self.click_on_element(self.get_element(locators.toptop_shop.btn_open_catalog), "Кнока перехода в Обувь")
        self.hover_element(0, 100, "от хедера")
        self.click_on_element(self.get_element(locators.toptop_shop.btn_to_shoes),
                              "Кнопка выбора фильта ботинок")
        self.click_on_element(self.get_element(locators.toptop_shop.btn_upper_shoes),
                              "Кнопка выбора обуви на высокой подошве")

    """Выбираем необходимые фильтры"""

    def select_filter(self):
        self.click_on_element(self.get_element(locators.toptop_shop.filter_of_size), "Открытие фильтра с размером")
        self.click_on_element(self.get_element(locators.toptop_shop.select_size), "Выбор размера")

        self.click_on_element(self.get_element(locators.toptop_shop.filter_of_style), "Открытие фильтра по стилю")
        self.click_on_element(self.get_element(locators.toptop_shop.select_style), "Выбор стиля")
        self.click_on_element(self.get_element(locators.toptop_shop.filter_of_style), "Открытие фильтра по стилю")

        self.click_on_element(self.get_element(locators.toptop_shop.filter_of_color), "Открытие фильтра по цвету")
        self.click_on_element(self.get_element(locators.toptop_shop.select_color), "Выбор цвета")

        self.click_on_element(self.get_element(locators.toptop_shop.filter_of_price), "Открытие фильтра по цене")
        self.move_slider(self.get_element(locators.toptop_shop.select_price), "51%")

        self.click_on_element(self.get_element(locators.toptop_shop.filter_of_sorted),
                              "Открытие фильтра по сортировке")
        self.click_on_element(self.get_element(locators.toptop_shop.select_sort), "Выбор сортировки")

        self.click_on_element(self.get_element(locators.toptop_shop.btn_accept), "Кнопка применить фильтр")


