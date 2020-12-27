import pytest
from pages.login_page import LoginPage


@pytest.fixture(scope='function')
def open_login_page(get_driver):
    print('Opening main page')
    return LoginPage.open(get_driver)


@pytest.mark.login
@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce")])
def test_login_valid_user(username, password, open_login_page):
    login_page = open_login_page
    main_page = login_page.login(username, password)
    assert main_page.is_app_logo_displayed() is True
    # assert main_page.get_items() == []


@pytest.mark.login
def test_login_invalid_user(open_login_page):
    login_page = open_login_page
    login_page.login("standard_user", "invalid_password")
    assert login_page.get_error() == "Epic sadface: Username and password do not match any user in this service"


@pytest.mark.login
@pytest.mark.xfail("Need to delete 'TODO:delete '")
def test_login_invalid_password(open_login_page):
    login_page = open_login_page
    login_page.login("invalid_user", "secret_sauce")
    assert login_page.get_error() == "TODO:delete Epic sadface: Username and password do not match any user in this " \
                                     "service "


@pytest.mark.login
def test_login_locked_user(open_login_page):
    login_page = open_login_page
    login_page.login("locked_out_user", "secret_sauce")
    assert login_page.get_error() == "Epic sadface: Sorry, this user has been locked out."
