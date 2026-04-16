class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Market:
    def __init__(self):
        self.products = {}

    def add(self, name, price):
        self.products[name] = Product(name, price)

    def buy(self, name):
        return self.products[name].price if name in self.products else 0

    def show(self):
        for p in self.products.values():
            print(p.name, p.price)


def menu():
    m = Market()

    while True:
        print("\n1.Add 2.Buy 3.Show 0.Exit")
        c = input(">> ")

        if c == "1":
            m.add(input("Name: "), int(input("Price: ")))

        elif c == "2":
            print(m.buy(input("Name: ")))

        elif c == "3":
            m.show()

        elif c == "0":
            break


if __name__ == "__main__":
    menu()
