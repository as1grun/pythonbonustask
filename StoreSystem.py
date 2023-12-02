class InventorySystem:
    def __init__(self):
        self.inventory = []

    def add_item(self, name, amount, description):
        item = {"name": name, "amount": amount, "description": description}
        self.inventory.append(item)

    def display_inventory(self):
        for item in self.inventory:
            print(f"Name: {item['name']}, amount: {item['amount']}, Description: {item['description']}")

    def change_amount(self, name, new_amount):
        for item in self.inventory:
            if item['name'] == name:
                item['amount'] = new_amount
                print(f"amount of {name} changed to {new_amount}")
                return
        print(f"Item {name} not found in inventory")

inventory_system = InventorySystem()
inventory_system.add_item("Телефон ", 100, "Хороший телефон ")
inventory_system.add_item("Холодильник", 50, "Большой холодильник")

inventory_system.display_inventory()

inventory_system.change_amount("Телефон", 75)
inventory_system.change_amount("Nonexistent Item", 50)
