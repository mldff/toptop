import time
from base.base_class import Base
import locators.toptop_shop


class ProductCard(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Пеоеход в карточку товара и покупка товара"""

    def buy_product(self):
        time.sleep(5)
        self.click_on_element(self.get_element(locators.toptop_shop.open_shoes), "Открытие карточки товара")

        """Фиксируем название и цену товара с карточки"""
        title_shoes = self.get_element(locators.toptop_shop.shoes_title).text
        price_shoes = self.get_element(locators.toptop_shop.shoes_price).text

        self.click_on_element(self.get_element(locators.toptop_shop.shoes_size), "Кнопка покупки в каталоге")
        self.click_on_element(self.get_element(locators.toptop_shop.btn_to_buy), "Кнопка покупки в карточке")
        self.click_on_element(self.get_element(locators.toptop_shop.popup_btn_buy),
                              "Кнопка перехода в корзину в попапе")

        return title_shoes, price_shoes

