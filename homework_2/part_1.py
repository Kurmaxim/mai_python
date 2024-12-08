
try:
    with open('data.txt', 'r', encoding='utf-8') as file:
            for line in file:
                    line = line.strip()
                    try:
                        objects = line.split() 
                        if all(object.replace('.', '', 1).isdigit() for object in objects):
                            print(line)
                        else:
                            raise TypeError("В файле встретилось нечисловое значение")
                    except TypeError as e:
                         print(e)
except FileNotFoundError:
    print("Файл не найден")

