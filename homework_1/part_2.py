log = []

class Product:
    def __init__(self, name, count, price):
        self.name = name
        self.count = count
        self.price = price

    def add_count(self, number_to_add):
        self.count = self.count + number_to_add
        log.append(f"На склад добавлено {number_to_add} единиц товара {self.name}")
    
    def reduce_count(self, number_to_reduce):
        if  number_to_reduce <= self.count:
            self.count -= number_to_reduce
            log.append(f"Снято {number_to_reduce} единиц товара {self.name}. Осталось {self.count}")
            return True
        else:
            log.append(f"Невозможно снять {number_to_reduce} единиц товара {self.name}, на складе имеется {self.count} единиц товара.")
            return False

    def cost_calculation(self):
        return self.count * self.price
    
    def __eq__(self, other):
        if isinstance(other, Product):
            return (self.name == other.name and
                    self.count == other.count and
                    self.price == other.price)
        return False


class Warehouse:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, name, count, price):
        product = Product(name, count, price)
        self.product_list.append(product)
        log.append(f"Товар добавлен на склад. Название: {name}, Количество: {count}, Стоимость: {price}")
        return product

    def del_product(self, product):
        if product in self.product_list:
            self.product_list.remove(product)
            log.append(f"Товар был удален со склада. Название: {product.name}, Количество: {product.count}, Стоимость: {product.price}")
        else:
            log.append(f"Товар не найден на складе. Название товара: {product.name}")

    def product_cost(self):
        cost = 0
        for product in self.product_list:
            cost += product.cost_calculation()
        log.append(f"Общая стоимость товаров на складе: {cost}")
        return cost
    
    def list_product(self):
        log.append("Список товаров на складе:")
        for product in self.product_list:
            log.append(f"Название: {product.name}, Количество: {product.count}, Стоимость: {product.price}")

class Seller(Warehouse):
    def __init__(self, name, warehouse):
        self.name = name
        self.warehouse = warehouse
        self.sale_list = []
    
    def sale_product(self, name, number):
        for product in self.warehouse.product_list:
            if name == product.name:
                if product.reduce_count(number):
                    self.sale_list.append({"Название": product.name, "Количество": number, "Цена": product.price})
                    log.append(f"Товар продан. Название: {product.name}, Количество: {number}, Стоимость: {product.price}")
                    return number * product.price
                else:
                    log.append(f"На складе недостаточно товара {name}, единиц товара: {product.count}")
                    return "На складе недостаточно товаров"
        log.append(f"На складе нет товара {name}")
        return "Товар не найден на складе"
    
    def sale_report(self):
        log.append(f"Отчёт о продажах")
        return self.sale_list

a = Warehouse([])
b = Seller("Вася", a)
a.add_product("Молоко", 4, 5)
a.add_product("Творог", 3, 100)
a.add_product("Вино", 22, 2)
a.del_product(Product("Молоко", 4, 5))

a.list_product()

cost = a.product_cost()

cost_add = b.sale_product("Вино", 10)

cost_add = b.sale_product("Творог", 1)

cost = a.product_cost()

print(b.sale_report())

for i in log:
    print(i)
