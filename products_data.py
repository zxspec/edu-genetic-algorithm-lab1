from product import Product


def init_test_products():
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

def init_real_products():
    products_list: list[Product] = []

    products_list.append(Product("Double Bed", 1.8, 170))
    products_list.append(Product("Double Bed Mattress", 0.7, 200))
    products_list.append(Product("Bedclothes", 0.4, 200))
    products_list.append(Product("Wardrobe", 2.1, 400))
    products_list.append(Product("Height-Adjustable Desk", 0.4, 2000))
    products_list.append(Product("Adult Women's Clothing", 1.5, 1000))
    products_list.append(Product("Adult Women's Shoes", 0.5, 2000))
    products_list.append(Product("Adult Men's Clothing", 1.5, 1000))
    products_list.append(Product("Adult Men's Shoes", 0.5, 1000))
    products_list.append(Product("Kids Bed", 1.2, 120))
    products_list.append(Product("Kids Bed Mattress", 0.4, 100))
    products_list.append(Product("Kids Bedclothes", 0.3, 110))
    products_list.append(Product("Kids Wardrobe", 1.8, 125))
    products_list.append(Product("Table", 0.3, 75))
    products_list.append(Product("Kids Clothing", 1, 500))
    products_list.append(Product("Kids Shoes", 0.3, 300))
    products_list.append(Product("Kids Toys", 0.2, 250))
    products_list.append(Product("Kids Bicycle", 0.2, 120))
    products_list.append(Product("Kids Scooter", 0.2, 50))
    products_list.append(Product("Infant's Bed", 0.8, 120))
    products_list.append(Product("Infant'sBed Mattress", 0.2, 100))
    products_list.append(Product("Infant's Bedclothes", 0.2, 110))
    products_list.append(Product("Kids Chests of Drawers", 0.7, 75))
    products_list.append(Product("Infant's Clothing", 0.4, 300))
    products_list.append(Product("Floor Lamp", 0.2, 100))
    products_list.append(Product("TV", 0.2, 1200))
    products_list.append(Product("Washing Machine", 0.5, 700))
    products_list.append(Product("Vacuum Cleaner", 0.3, 100))
    products_list.append(Product("Vacuum Cleaner Robot", 0.2, 150))
    products_list.append(Product("Multicooker", 0.3, 50))
    products_list.append(Product("Kitchen Utensils", 0.1, 100))
    products_list.append(Product("Dishes", 0.6, 400))
    products_list.append(Product("Books", 0.2, 200))
    products_list.append(Product("Bathroom Furniture", 0.4, 250))
    products_list.append(Product("Winter Tiers", 1.5, 800))

    return products_list


class ProductsData:
    def __init__(self, products_list):
        # products_list = init_products()
        self.spaces: list[float] = []
        self.prices: list[float] = []
        self.names: list[str] = []

        for product in products_list:
            self.spaces.append(product.space)
            self.prices.append(product.price)
            self.names.append(product.name)
