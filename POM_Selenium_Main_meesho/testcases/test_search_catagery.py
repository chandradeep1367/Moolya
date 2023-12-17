import pytest

from POM_Login.search_catagery import SearchProduct


@pytest.mark.usefixtures("setup")
class SearchCategory:
    SEARCH_TEXT = 'butter'

    def test_Category(self, setup):
        search_object = SearchProduct(setup)
        search_object.search_product(self.SEARCH_TEXT)

        search_object.add_item()
        search_object.cart_item1()
        search_object.purchase_item()
        print("working")





