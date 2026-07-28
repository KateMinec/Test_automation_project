from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_visible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_presence(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_invisible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def scroll_to_element(self, element):
        from selenium.webdriver import ActionChains
        ActionChains(self.driver).scroll_to_element(element).perform()

    def scroll_by_coordinates(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def switch_to_new_window(self):
        # Метод для переключения фокуса, если корзина открывается в новой вкладке
        handles = self.driver.window_handles
        if len(handles) > 1:
            self.driver.switch_to.window(handles[-1])
            print("Фокус Selenium переключен на новую вкладку.")