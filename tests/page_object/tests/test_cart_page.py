import pytest
import time

from ..pages import home_page as hp
from ..pages import product_page as pp
from ..pages import cart_page as cp

# @pytest.mark.usefixtures("chrome_driver")
def test_empty_cart(chrome_driver):
    print("init home page")
    home_page = hp.HomePage(chrome_driver)
    print("getting home page")
    home_page.get_page() 
    
    print("add products to cart")
    for i in range(1, 2):   
        print(f"\tadd {i} random item ")                 
        home_page.open_random_popular_product()
        product_page = pp.ProductPage(chrome_driver)
        product_page.add_item_to_cart(str(i))
        print("\treturn to home page")
        home_page.get_page()
        
    print("open cart")
    home_page.open_cart()
    cart_page = cp.CartPage(chrome_driver)
    cart_page.remove_all_items_from_cart()
    
    assert cart_page.is_items_list_displayed() == False
    