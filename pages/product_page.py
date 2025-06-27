import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.category_page import CategoryPageLocators


class ProductPageLocators:
    PRODUCT_TITLE = (By.XPATH, "//h1[contains(@class, 'Product_title__')]")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class,'PriceBlock_price')]//span")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(),'Добавить в корзину')]")



class ProductPage(BasePage):

    def open_product_page(self):
        self.click_element(CategoryPageLocators.PRODUCT_TITLE)
        time.sleep(2)
        print("Страница продукта открыта")

    def verify_product_details(self, expected_title: str = "HP 15s-fq5025ny", expected_price: str = "52290"):
        actual_title = self.find_element(ProductPageLocators.PRODUCT_TITLE).text.strip()
        assert expected_title.lower() in actual_title.lower(), f"Ожидался заголовок '{expected_title}', но получен '{actual_title}'"

        actual_price = self.find_element(ProductPageLocators.PRODUCT_PRICE).text.strip()
        assert expected_price.replace(" ", "") in actual_price.replace(" ", ""), f"Ожидалась цена '{expected_price}', но получена '{actual_price}'"

        print(f"Проверка успешна: {actual_title}, цена: {actual_price}")

    def add_to_cart(self):
        self.click_element(ProductPageLocators.ADD_TO_CART_BUTTON)
        print("Товар добавлен в корзину")