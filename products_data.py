from product import Product


def init_products():
    products_list: list[Product] = []

    products_list.append(Product("Shovel", 8, 500))
    products_list.append(Product("Knife multitool", 1, 1000))
    products_list.append(Product("First aid kit", 10, 600))
    products_list.append(Product("Sleeping bag", 12, 800))
    products_list.append(Product("Thermal underwear", 15, 1500))
    products_list.append(Product("Compact Solar Panel", 15, 3000))
    products_list.append(Product("Burner", 13, 2000))
    products_list.append(Product("Ropes with carabiners", 12, 500))
    products_list.append(Product("Chemical light source", 3, 600))
    products_list.append(Product("Flashlight", 5, 200))
    products_list.append(Product("Compass", 2, 800))
    products_list.append(Product("Water purification tablets", 1, 500))
    products_list.append(Product("Food", 10, 800))
    products_list.append(Product("Raincoat", 4, 100))
    products_list.append(Product("Energetic bars", 6, 400))

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
