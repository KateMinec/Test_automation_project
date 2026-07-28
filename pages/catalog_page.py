import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from base.base_page import BasePage


class CatalogPage(BasePage):
    # Локаторы
    CATALOG_MENU_BTN = (By.XPATH, "//div[@class='catalog-menu']")
    HOUSEHOLD_LINK = (By.XPATH, "//a[contains(text(), 'Бытовая техника')]")
    CATALOG_COLUMN = (By.XPATH, "//div[@class='content-single-column']")
    MAJOR_APPLIANCES_LINK = (By.XPATH, "//a[contains(text(), 'Крупная бытовая техника')]")
    FRIDGE_LINK = (By.XPATH, "//a[contains(text(), 'Холодильники')]")

    # Фильтры
    FRIDGE_MENU_SLOT = (By.XPATH, "//div[@class='yCmsContentSlot']")
    PRICE_SLIDER = (By.XPATH, "//div[@class='facets-range-slider__bar']//span[2]")
    INTRO_SKIP_BTN = (By.XPATH, "//a[@class='introjs-skipbutton']")
    NO_FROST_CHECKBOX = (By.XPATH, "//label[contains(., 'no frost')]//input[@class='v-checkbox__field']")
    APPLY_FILTER_BTN = (By.XPATH, "//button[@class='v-button v-button--size-md v-button--primary']")

    # Сортировка
    SORT_DROPDOWN = (By.XPATH, "//button[@class='v-dropdown-toggle v-dropdown-toggle--size-md']")
    CHEAPEST_OPTION = (By.XPATH, "//li[contains(., 'Сначала дешевые')]")
    COOKIE_BTN = (By.XPATH, "//button[@class='v-button v-button--full-width v-button--size-sm v-button--dark-mode']")

    # Выбор товара (Парсинг 2-го элемента)
    PRODUCT_NAME = (By.XPATH, "(//a[contains(@class, 'product-title')])[2]")
    PRODUCT_PRICE = (By.XPATH, "(//a[contains(@class, 'v-product-pric')])[2]")
    ADD_TO_CART_BTN = (By.XPATH, "(//button[contains(@class, 'product-button-cart__control')])[2]")
    GO_TO_CART_BTN = (By.XPATH, "//a[contains(@href, '/cart/')]")

    # Методы
    def open_catalog(self):
        self.wait_for_clickable(self.CATALOG_MENU_BTN).click()
        print("Панель каталога открыта.")

    def navigate_to_household_appliances(self):
        link = self.wait_for_presence(self.HOUSEHOLD_LINK)
        self.scroll_to_element(link)
        time.sleep(1)
        link.click()
        print("Переход в раздел 'Бытовая техника' выполнен.")

    def navigate_to_major_appliances(self):
        self.wait_for_visible(self.CATALOG_COLUMN)
        link = self.wait_for_presence(self.MAJOR_APPLIANCES_LINK)
        self.scroll_to_element(link)
        time.sleep(1)
        link.click()
        print("Переход в раздел 'Крупная бытовая техника' выполнен.")

    def navigate_to_fridges(self):
        self.wait_for_presence(self.FRIDGE_LINK).click()
        print("Переход в раздел 'Холодильники' выполнен.")

    def apply_price_filter(self):
        self.wait_for_visible(self.FRIDGE_MENU_SLOT)
        slider = self.wait_for_visible(self.PRICE_SLIDER)
        ActionChains(self.driver).click_and_hold(slider).move_by_offset(-130, 0).release().perform()
        time.sleep(2)

    def close_intro_hint_if_present(self):
        try:
            print("Проверяем наличие всплывающей подсказки...")
            skip_button = self.wait_for_clickable(self.INTRO_SKIP_BTN, timeout=4)
            skip_button.click()
            print("Подсказка успешно закрыта.")
            time.sleep(1)
        except Exception:
            print("Подсказка не появилась, двигаемся дальше.")

    def select_no_frost_and_submit(self):
        self.wait_for_visible(self.NO_FROST_CHECKBOX).click()
        print("Чекбокс 'no frost' успешно выбран.")
        time.sleep(2)
        self.wait_for_visible(self.APPLY_FILTER_BTN).click()
        print("Кнопка 'Показать' успешно нажата.")
        time.sleep(2)

    def sort_by_cheapest_and_accept_cookies(self):
        self.wait_for_clickable(self.SORT_DROPDOWN).click()
        time.sleep(0.5)
        self.wait_for_clickable(self.CHEAPEST_OPTION).click()
        print("Выбран тип сортировки: от дешевых к дорогим.")
        time.sleep(3)
        self.wait_for_visible(self.COOKIE_BTN).click()
        print("Соглашение на использование cookies принято.")

    def get_second_product_details_and_add_to_cart(self):
        name = self.wait_for_presence(self.PRODUCT_NAME).text
        price = self.wait_for_presence(self.PRODUCT_PRICE).text
        print(f"\nВы выбрали товар: '{name}' по цене '{price}'")

        self.wait_for_clickable(self.ADD_TO_CART_BTN).click()
        print("Выбранный товар успешно добавлен в корзину.")
        return name, price

    def go_to_cart(self):
        self.wait_for_visible(self.GO_TO_CART_BTN).click()
        print("\nВход в корзину выполнен.")