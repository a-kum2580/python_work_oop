class Product:
    """
    Product class with name, price, and category

    Demonstrates the use of `getters` and `setters` in a Python class.
    """

    def __init__(self, name: str, price: float, category: str) -> None:
        self.name = name
        self.price = price
        self.category = category

    @property
    def price(self) -> float:
        """Getter -> Returns the price of the product"""
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        """Setter -> Sets the price, ensuring it is non-negative"""
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._price = price

    @property
    def category(self) -> str:
        """Getter -> Returns the category of the product"""
        return self._category

    @category.setter
    def category(self, category: str) -> None:
        """Setter -> Sets the category, ensuring it's valid"""
        valid_categories = ["electronics", "clothing", "food", "furniture"]
        if category.lower() not in valid_categories:
            raise ValueError(f"Category is not valid: {category}")
        self._category = category

    def __str__(self) -> str:
        return f"Product: {self.name}, Price: UGX {self.price}, Category: {self.category.capitalize()}"


def get_product_details() -> tuple[str, float, str]:
    """Returns the name, price, and category of the product"""
    name = input("Product Name: ").strip()
    price = float(input("Price (in UGX): ").strip())
    category = input("Category: ").strip()

    return name, price, category


NAME, PRICE, CATEGORY = get_product_details()

product = Product(NAME, PRICE, CATEGORY)

print(product)
