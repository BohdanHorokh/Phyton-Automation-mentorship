import pytest
from pages.login_page import LoginPage


@pytest.fixture(scope='function')
def open_login_page(get_driver):
    print('Opening main page')
    return LoginPage.open(get_driver)


@pytest.mark.products
def test_available_products(open_login_page):
    main_page = open_login_page.login("standard_user", "secret_sauce")
    assert main_page.get_products() == ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt',
                                        'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie',
                                        'Test.allTheThings() T-Shirt (Red)']


@pytest.mark.products
def test_add_product_to_cart(open_login_page):
    main_page = open_login_page.login("standard_user", "secret_sauce")
    main_page.add_product_to_cart('Sauce Labs Onesie')
    cart_page = main_page.open_cart_page()
    assert cart_page.is_cart_contains_product('Sauce Labs Onesie') == True


@pytest.mark.products
def test_remove_product_from_cart(open_login_page):
    main_page = open_login_page.login("standard_user", "secret_sauce")
    main_page.add_product_to_cart('Sauce Labs Onesie')
    main_page.add_product_to_cart('Sauce Labs Backpack')
    main_page.remove_product_from_cart('Sauce Labs Onesie')
    cart_page = main_page.open_cart_page()
    assert cart_page.is_cart_contains_product('Sauce Labs Onesie') == False
