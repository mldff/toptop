import time

from pages.authorization import Authorization
from pages.catalog import Catalog
from pages.product_card import ProductCard
from pages.cart import Cart

email = "ssadsa.dsadsad@yandex.ru"
password = "test12345X"


def test_order(driver):
    login = Authorization(driver)
    catalog = Catalog(driver)
    product = ProductCard(driver)
    cart = Cart(driver)
    try:
        """Авторизовываемся"""
        login.sign_in(email, password)
        """Ждём, чтобы подгрузилась авторизцаия"""
        time.sleep(5)
        """Переход в каталог"""
        catalog.to_catalog()
        """Выбор фильтров"""
        catalog.select_filter()
        """Переход в карточку товара и получение инфы по товару"""
        title, price = product.buy_product()
        cart.confirm(title, price)
    except Exception as e:
        """Фиксируем ошибку и скриншот"""
        login.get_screenshot("Покупка товара", exc_info=e)
