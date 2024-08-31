import time

from base.base_class import Base
import locators.toptop_shop


class Authorization(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def sign_in(self, email, password):
        self.go_to_url("https://toptop.ru/")
        """Ждём открытия попапа с рассылкой и закрываем её"""
        self.click_on_element(self.get_element(locators.toptop_shop.popup), "Кнопку закрытия попапа")
        """Закрываем плашку с куками"""
        self.click_on_element(self.get_element(locators.toptop_shop.accept_cookies), "Кнопку принятия условий")

        """Авторизация"""
        self.click_on_element(self.get_element(locators.toptop_shop.btn_to_login), "Кнопку открытия формы авторизации")
        self.enter_text(self.get_element(locators.toptop_shop.input_email), email, "Email")
        self.enter_text(self.get_element(locators.toptop_shop.input_password), password, "Password")
        self.click_on_element(self.get_element(locators.toptop_shop.btn_sign), "Кнопку входа в аккаунт")

        time.sleep(5)
        """Проверяем авторизацию"""
        self.assert_text(self.get_element(locators.toptop_shop.btn_to_login).text, "КАБИНЕТ", "Авторизованного имени")

        """Очищаем корзины от товаров, если они имеются на аккаунте"""
        self.click_on_element(self.get_element(locators.toptop_shop.btn_header_cart), "Открытие корзины")
        self.check_and_clear_cart(locators.toptop_shop.remove_cart)
        self.click_on_element(self.get_element(locators.toptop_shop.close_cart), "Закрытие корзины")
