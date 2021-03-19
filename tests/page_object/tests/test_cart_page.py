import pytest
import time

from ..pages import home_page as hp
from ..pages import product_page as pp
from ..pages import cart_page as cp

from ..application import Application


def test_empty_cart(chrome_driver):
    app = Application(chrome_driver)
    app.add_several_popular_items_to_cart(3)
    app.open_cart()
    app.empty_cart()
    
    assert app.is_cart_empty() == True
        

    