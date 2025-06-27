import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class MainPageLocators:
    catalog_button = (By.XPATH, "//button[span[text()='Каталог']]")  # Каталог
    category_button = (By.XPATH, "//div[@class='Catalog_mainCategoryName__xzGxz' and text()='Компьютеры и ноутбуки']")  # Категории
    subcategory_button = (By.XPATH, "//p[@class='CardCategory_title__K2CCX' and contains(text(), 'Ноутбуки')]")


class MainPage(BasePage):
    pass
    """Главная страница сайта Regard."""

    def open_main_page(self):
        self.open_url("https://www.regard.ru/")

    def open_catalog(self):
        self.click_element(MainPageLocators.catalog_button)

    def select_category(self):
        self.click_element(MainPageLocators.category_button)
        time.sleep(1)
        self.click_element(MainPageLocators.subcategory_button)

