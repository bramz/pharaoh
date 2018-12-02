
class Items:
    def __init__(self, name, category, price, description):
        self.name = name
        self.category = category
        self.price = price
        self.description = description

    def get_name(self) -> str:
        return self.name

    def get_category(self) -> str:
        return self.category
    
    def get_price(self) -> str:
        return self.price

    def get_description(self) -> str:
        return self.description

