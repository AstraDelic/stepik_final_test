from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage


def test_buy_laptop(set_up):
    # Создаем экземпляр MainPage, который сам создаёт self.driver внутри BasePage
    main_page = MainPage()

    try:
        # Открываем главную страницу и переходим в категорию ноутбуков
        main_page.open_main_page()
        main_page.open_catalog()
        main_page.select_category()

        # Передаём созданный driver от main_page в category_page
        category_page = CategoryPage(main_page.driver)

        # Применяем фильтры
        category_page.apply_price_filter(30000, 60000)
        category_page.brand_filter()
        category_page.type_filter()
        category_page.cpu_brand_filter()
        category_page.line_filter()
        category_page.ram_filter()
        category_page.ssd_filter()
        category_page.color_filter()
        category_page.blue_color()
        # Вот тут идёт проверка, что первый товар соответствует фильтрам
        category_page.verify_filtered_product_title(["HP"])

        # Переходим на страницу товара
        product_page = ProductPage(main_page.driver)
        product_page.open_product_page()
        product_page.verify_product_details()
        product_page.add_to_cart()

        # Переходим на страницу корзины
        cart_page = CartPage(main_page.driver)
        cart_page.open_cart_page()
        cart_page.get_to_cart()
        cart_page.check_cart()


    finally:
        # Закрываем драйвер, если он был создан
        if hasattr(main_page, "driver"):
            main_page.driver.quit()



