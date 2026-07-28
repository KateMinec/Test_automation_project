import time
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage
from conftest import driver

def clean_digits(text_string):
    #Оставляет в строке только цифры (убирает пробелы, руб., знаки)
    return "".join(filter(str.isdigit, text_string))


def test_komus_checkout_flow(driver):
    driver.get('https://komus.ru')

    # Инициализация страниц, передавая им драйвер из фикстуры
    login_page = LoginPage(driver)
    catalog_page = CatalogPage(driver)
    cart_page = CartPage(driver)

    # Авторизация
    login_page.login(email="kata1-9-9-7@mail.ru", password="qWZgBA!$cBYG5Wj")
    login_page.wait_for_login_modal_to_disappear()

    # Навигация по каталогу
    catalog_page.open_catalog()
    catalog_page.navigate_to_household_appliances()
    catalog_page.navigate_to_major_appliances()
    catalog_page.navigate_to_fridges()

    # Применение фильтров и сортировки
    catalog_page.apply_price_filter()
    catalog_page.scroll_by_coordinates(0, 1000)
    catalog_page.close_intro_hint_if_present()
    catalog_page.select_no_frost_and_submit()

    catalog_page.scroll_by_coordinates(0, 0)
    catalog_page.sort_by_cheapest_and_accept_cookies()

    # Выбор товара и переход в корзину
    catalog_page.scroll_by_coordinates(0, 700)
    catalog_name, catalog_price = catalog_page.get_second_product_details_and_add_to_cart()
    catalog_page.go_to_cart()

    # Даем сайту 2 секунды, чтобы страница корзины успела загрузиться
    time.sleep(2)

    # Проверки в корзине
    cart_name, cart_price, final_price = cart_page.get_cart_details()

    clean_catalog_p = clean_digits(catalog_price)
    clean_cart_p = clean_digits(cart_price)
    clean_final_p = clean_digits(final_price)

    print(f"\n[PyTest] Каталог: {clean_catalog_p} | Корзина: {clean_cart_p} | Итого: {clean_final_p}")

    assert cart_name.strip() == catalog_name.strip(), "Название товара в корзине не совпадает!"
    assert clean_cart_p == clean_catalog_p, f"Цена не совпадает! Ожидалось: {clean_catalog_p}, получено: {clean_cart_p}"
    assert clean_cart_p == clean_final_p, f"Итоговая цена ({clean_final_p}) не совпадает с ценой товара ({clean_cart_p})"

    print("Проверка в корзине пройдена успешно. Данные полностью совпадают!")

    # Переход на оформление заказа
    cart_page.proceed_to_checkout()

    # Даем сайту 2 секунды, чтобы загрузилась страница ввода данных/анкеты
    time.sleep(2)

    name_screenshot = 'checkout_page_latest.png'
    target_folder = 'C:\\Users\\Admin\\PycharmProjects\\Comus_project\\screenshots\\'

    # Сохраняем скриншот
    driver.save_screenshot(target_folder + name_screenshot)
    print(f"Скриншот успешно сохранен в: {target_folder + name_screenshot}")