import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CategoryPageLocators:
    # Секции фильтров
    PRICE_MIN = (By.XPATH, "//input[contains(@class, 'range-selector-input') and @name='min']")
    PRICE_MAX = (By.XPATH, "//input[contains(@class, 'range-selector-input') and @name='max']")
    BRAND_FILTER = (By.XPATH, "//label[@for='id-HP-HP']")
    TYPE_FilTER= (By.XPATH, "//label[@for='id-ноутбук-1240']")
    CPU_BRAND_FILTER = (By.XPATH, "//label[@for='id-Intel-1245']")
    CPU_LINE_FILTER = (By.XPATH, "//label[@for='id-Core-i5-2092']")
    RAM_FILTER = (By.XPATH, "//label[@for='id-8-2106']")
    SSD_FILTER = (By.XPATH, "//label[@for='id-512-Гб-6330']")
    COLOR_FILTER = (By.XPATH, "//div[contains(@class, 'Dropdown_toggle')]//span[normalize-space()='Цвет']")
    BLACK_COLOR_VALUE = (By.XPATH, "//label[@for='id-чёрный-2150']")
    PRODUCT_ITEMS = (By.XPATH, "//div[contains(@class, 'Card_wrap__')]")
    PRODUCT_TITLE = (By.XPATH, "//div[contains(@class, 'CardText_title') or contains(@class, 'CardText_link')]")


class CategoryPage(BasePage):
    def apply_price_filter(self, min_price: int, max_price: int):
        # Вводим цены с имитацией человеческого ввода
        self.enter_text_with_delay(CategoryPageLocators.PRICE_MIN, str(min_price))
        self.enter_text_with_delay(CategoryPageLocators.PRICE_MAX, str(max_price))
        print("Фильтр цена указана")
        # Прокрутка к следующему элементу
        self.scroll_down_to_element(CategoryPageLocators.TYPE_FilTER)
    def brand_filter(self):
        self.click_element(CategoryPageLocators.BRAND_FILTER)
        print("Фильтр бренд выбран")
        # Прокрутка к следующему фильтру
        self.scroll_down_to_element(CategoryPageLocators.CPU_BRAND_FILTER)
    def type_filter(self):
        self.click_element(CategoryPageLocators.TYPE_FilTER)
        print("Фильтр тип товара выбран")
        # Прокрутка к следующему фильтру
    def cpu_brand_filter(self):
        self.click_element(CategoryPageLocators.CPU_BRAND_FILTER)
        print("Фильтр Производитель CPU выбран")
        # Прокрутка к следующему фильтру
        self.scroll_down_to_element(CategoryPageLocators.CPU_LINE_FILTER)
    def line_filter(self):
        self.click_element(CategoryPageLocators.CPU_LINE_FILTER)
        print("Фильтр Линейка CPU выбран")
        # Прокрутка к следующему фильтру
        self.scroll_down_to_element(CategoryPageLocators.RAM_FILTER)
    def ram_filter(self):
        self.click_element(CategoryPageLocators.RAM_FILTER)
        print("Фильтр обьем ОЗУ выбран")
        # Прокрутка к следующему фильтру
        self.scroll_down_to_element(CategoryPageLocators.COLOR_FILTER)
    def ssd_filter(self):
        self.click_element(CategoryPageLocators.SSD_FILTER)
        print("Фильтр объем SSD выбран")
        # Прокрутка к следующему фильтру
        self.scroll_down_to_element(CategoryPageLocators.COLOR_FILTER)
    def color_filter(self):
        self.click_element(CategoryPageLocators.COLOR_FILTER)
        time.sleep(3)
        print("Фильтр цвет товара выбран")
        # Прокрутка к следующему фильтру
        self.scroll_down_to_element(CategoryPageLocators.BLACK_COLOR_VALUE)
    def blue_color(self):
        self.click_element(CategoryPageLocators.BLACK_COLOR_VALUE)
        print("Синий цвет выбран")
        # Прокрутка к следующему фильтру
        self.scroll_up_to_element()
        time.sleep(3)
        
    def verify_filtered_product_title(self, expected_keywords: list):
        # Проверяем, что выбранный товар в списке содержит все ожидаемые ключевые слова.
        product_elements = self.find_elements(CategoryPageLocators.PRODUCT_ITEMS)
        assert product_elements, "Нет товаров после применения фильтров."

        # Используем относительный поиск по локатору внутри карточки
        product_title_element = product_elements[0].find_element(
            *CategoryPageLocators.PRODUCT_TITLE
        )
        product_title = product_title_element.text.lower()

        for keyword in expected_keywords:
            assert keyword.lower() in product_title, f"Ожидалось, что '{keyword}' будет в названии: '{product_title}'"

        print(f"Проверка успешна. Найденный товар: {product_title}")
