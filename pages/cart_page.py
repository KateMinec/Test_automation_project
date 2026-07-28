from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CartPage(BasePage):
    # ЛОКАТОРЫ
    CART_PRODUCT_NAME = (By.XPATH, "//span[contains(@class, 'product-title')]")
    CART_PRODUCT_PRICE = (By.XPATH, "(//span[contains(@class, 'v-product-price__value')])[1]")
    CART_FINAL_PRICE = (By.XPATH, "//div[@class='order-summary-total-cost__text order-summary-total-cost__text--value qa-total-sum gtm-cart-total']")
    CHECKOUT_BTN = (By.XPATH, "//button[contains(., 'Оформить заказ') or contains(@class, 'checkout')]")

    # МЕТОДЫ
    def get_cart_details(self):
        cart_name = self.wait_for_presence(self.CART_PRODUCT_NAME).text
        cart_price = self.wait_for_presence(self.CART_PRODUCT_PRICE).text
        final_price = self.wait_for_presence(self.CART_FINAL_PRICE).text
        return cart_name, cart_price, final_price

    def proceed_to_checkout(self):
        self.wait_for_clickable(self.CHECKOUT_BTN).click()
        print("Кнопка 'Оформить заказ' успешно нажата.")