class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"товар {item_name} был добавлен в магазин {self.name}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"товар {item_name} был удален из магазина {self.name}")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"цена товара {item_name} была обновлена в магазине {self.name}")
        else:
            print(f"товар {item_name} не найден")

store1 = Store("Пятёрочка", "Ленина, 10")
store2 = Store("Магнит", "Ленина, 11")
store3 = Store("Метро", "Ленина, 12")

store1.add_item("хлеб", 67)
store1.add_item("шпроты", 167)
store1.add_item("водяра", 267)

store1.remove_item("хлеб")

print(store1.get_price("водяра"))

store1.update_price("шпроты", 500)