from product import Product


def init_products():
    products_list: list[Product] = []

    products_list.append(Product("Shovel A", 8, 500))
    products_list.append(Product("Burner class 2", 13, 1500))
    products_list.append(Product("First aid kit, type C", 15, 800))
    products_list.append(Product("Knife multitool", 1, 1000))
    products_list.append(Product("Burner class 1", 15, 2000))
    products_list.append(Product("First aid kit, type B", 12, 600))
    products_list.append(Product("Thermal underwear", 10, 800))
    products_list.append(Product("Flashlight model 3", 2, 800))
    products_list.append(Product("Enrgetic bars", 6, 400))
    products_list.append(Product("First aid kit, type A", 10, 1000))
    products_list.append(Product("Raincoat", 4, 100))
    products_list.append(Product("Water purification tablets", 1, 500))
    products_list.append(Product("Flashlight model 1", 3, 600))
    products_list.append(Product("Burner class 3", 12, 500))
    products_list.append(Product("Flashlight model 2", 5, 200))

    return products_list


class ProductsData:
    def __init__(self):
        products_list = init_products()
        self.spaces: list[float] = []
        self.prices: list[float] = []
        self.names: list[str] = []

        for product in products_list:
            self.spaces.append(product.space)
            self.prices.append(product.price)
            self.names.append(product.name)
