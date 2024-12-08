class Buffer:
    def __init__(self):
        self.my_list = []

    def add_data(self, data):
        if len(self.my_list) < 5:
            self.my_list.append(data)
        else:
            print("Буфер переполнен.")
            self.my_list = []
            
    def get_data(self):
        if len(self.my_list) == 0:
            print("Буфер пуст.")
        else:
            print(self.my_list)


a = Buffer()

a.add_data("lol")
a.add_data("kek")
a.add_data(12313)
a.add_data("none")
a.add_data(313131)
a.add_data([123])
a.add_data(2312)
a.get_data()