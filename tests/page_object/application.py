from .pages import home_page as hp
from .pages import product_page as pp
from .pages import cart_page as cp


class Application:
    def __init__(self, driver):
        self.driver = driver
    
    def add_several_popular_items_to_cart(self, items_count):
        print("init home page")
        home_page = hp.HomePage(self.driver)
        print("getting home page")
        home_page.get_page()

        print("add products to cart")
        for i in range(1, items_count + 1):
            print(f"\tadd {i} random item ")
            home_page.open_random_popular_product()
            product_page = pp.ProductPage(self.driver)
            product_page.add_item_to_cart(str(i))
            print("\treturn to home page")
            home_page.get_page()
            
    def empty_cart(self):
        # home_page = hp.HomePage(self.driver)
        # print("open cart")
        # home_page.open_cart()
        cart_page = cp.CartPage(self.driver)
        cart_page.remove_all_items_from_cart()
        
    def open_cart(self):
        print("open cart")
        cart_page = cp.CartPage(self.driver)
        cart_page.get()
        
    def is_cart_empty(self):
        return not cp.CartPage(self.driver).is_items_list_displayed()