#pytest test case
import pytest
from base_pages.login_page import LoginPage
from test_data.login_data import login_test_data

@pytest.mark.parametrize("username,password,expected",login_test_data)
def test_login(browser,username,password,expected):
    page=LoginPage(browser)
    page.open()
    page.login(username,password)
    if expected:
        assert "/profile" in page.get_current_url()
    else:
        assert "/login" in page.get_current_url()
