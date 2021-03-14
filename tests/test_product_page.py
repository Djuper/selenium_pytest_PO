from pages.product_page import ProductPage
link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()
    product_page.message_should_be_present(f"{product_name} has been added to your basket.")
    product_page.message_should_be_present(f"Your basket total is now {product_price}")
