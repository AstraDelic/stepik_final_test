import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: webdriver.Chrome = None):
        if driver is None:
            options = Options()
            options.add_argument("--incognito")
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(options=options)
        else:
            self.driver = driver

        # self.wait = WebDriverWait(self.driver, 60)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def find_elements(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        el = self.find_element(locator)
        el.click()
        return el

    def enter_text_with_delay(self, locator, text, min_delay=0.1, max_delay=0.3):
        element = self.find_element(locator)
        element.click()  # Фокусируемся на элементе
        element.clear()  # Очищаем поле перед вводом

        actions = ActionChains(self.driver)
        for char in text:
            actions.send_keys(char).perform()
            # Случайная задержка между min_delay и max_delay
            delay = random.uniform(min_delay, max_delay)
            time.sleep(delay)

        # Небольшая пауза после завершения ввода
        time.sleep(0.5)

    def wait_for_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def scroll_up_to_element(self):
        self.driver.execute_script("window.scrollTo({ top: 0, behavior: 'smooth' });")
        # element = self.find_element(locator)
        # self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'start'});", element)

    def scroll_down_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)


    def close(self):
        self.driver.quit()
