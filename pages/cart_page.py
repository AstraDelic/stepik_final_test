import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class CartPageLocators:
    CART_BUTTON = (By.XPATH, "//span[@class='IconButton_text__B2OHa NavigationBar_iconButtonText__escRo' and text()='Корзина']")
    GET_TO_CART = (By.XPATH, "//a[@class='Button_button__GeQ2O Button_large__FQoDr Button_primaryBlue__Y7daK Button_fullWidth__NgObg' and text()='Перейти в корзину']")
    PRODUCT_NAME = (By.XPATH, "//a[@class='BasketItem_link__qYvgV' and @title='Ноутбук HP 15s-fq5025ny (737U0EA)']")
    PRODUCT_PRICE = (By.XPATH,"//span[@class='Price_price__m2aSe notranslate' and not(ancestor::div[contains(@class, 'TotalInfo')])]")
    TOTAL_PRICE = (By.XPATH, "//span[@class='TotalInfo_totalPrice__sTOzK Price_price__m2aSe notranslate']")

class CartPage(BasePage):

    def open_cart_page(self):
        self.click_element(CartPageLocators.CART_BUTTON)
        time.sleep(2)
        print("Открыта страница корзины")

    def get_to_cart(self):
        self.click_element(CartPageLocators.GET_TO_CART)
        time.sleep(5)
        print("Переход в корзину")

    def check_cart(self, expected_title: str = "HP 15s-fq5025ny", expected_price: str = "52290"):
        product_name = self.find_element(CartPageLocators.PRODUCT_NAME).text.strip()
        assert expected_title.lower() in product_name.lower(), f"Ожидался заголовок '{expected_title}', но получен '{product_name}'"

        product_price = self.find_element(CartPageLocators.PRODUCT_PRICE).text.strip()
        assert expected_price in product_price.replace(" ",""), f"Ожидалась цена '{expected_price}', но получена '{product_price}'"

        total_price = self.find_element(CartPageLocators.TOTAL_PRICE).text.strip()
        # Рассчитываем ожидаемую итоговую цену
        expected_total_price = str(int(expected_price) + 490)  # Итоговая цена = цена товара + 490 рублей
        assert expected_total_price in total_price.replace(" ",""), f"Ожидалась итоговая цена '{expected_total_price}', но получена '{total_price}'"

        print(f"Проверка успешна: {product_name}, цена: {product_price}, итоговая цена: {total_price}")