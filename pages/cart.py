import time
from base.base_class import Base
import locators.toptop_shop


class Cart(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def confirm(self, title_shoes, price_shoes):
        time.sleep(5)
        """Фиксируем название и цену товара в корзине"""
        total_title = self.get_element(locators.toptop_shop.total_shoes_title).text
        total_price = self.get_element(locators.toptop_shop.total_shoes_price).text

        """Проверка итоговой цены и название товара"""
        self.assert_text(title_shoes, total_title,
                         "Итоговое название на странице оформления")

        self.assert_text(self.get_number(price_shoes), self.get_number(total_price),
                         "Итоговая цена на странице оформления")
