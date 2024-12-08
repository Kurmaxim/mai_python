# Ознакомьтесь с модулем datetime в Python. Создайте программу, которая будет использовать этот модуль для выполнения следующих задач:

# Отображение текущей даты и времени.
# Вычисление разницы между двумя датами.
# Преобразование строки в объект даты и времени.
# Убедитесь, что ваша программа работает корректно и использует функции из модуля datetime.



from datetime import datetime

DATE_FORMATS = [
        "%Y.%m.%d %H:%M:%S", 
        "%Y.%m.%d",
        "%d-%m-%Y %H:%M:%S",
        "%d-%m-%Y",
        "%d/%m/%Y %H:%M:%S", 
        "%d/%m/%Y",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",  
        "%d.%m.%Y %H:%M:%S",
        "%d.%m.%Y",
        "%m/%d/%Y %H:%M:%S",
        "%m/%d/%Y",  
        "%m-%d-%Y %H:%M:%S",
        "%m-%d-%Y"  
    ]

def print_datetime_now():
    current_time = datetime.now().time()
    current_date = datetime.now().date()
    print(f"Текущее время: {current_time}")
    print(f"Текущая дата: {current_date}")

def date_diff(date_1, date_2, type="default"):
    diff = date_1 - date_2
    if type == "default":
        return diff
    if type == "second":
        return divmod(diff.total_seconds(), 1)[0]
    if type == "minute":
        return divmod(diff.total_seconds(), 60)[0]
    if type == "hour":
        return divmod(diff.total_seconds(), 3600)[0]
    if type == "day":
        return divmod(diff.total_seconds(), 86400)[0]
    if type == "year":
        return divmod(diff.total_seconds(), 31536000)[0]
        
def date_parse(date_string):    
    for date_format in DATE_FORMATS:
        try:
            return datetime.strptime(date_string, date_format)
        except ValueError:
            continue
    return None

print_datetime_now()
print(date_parse("2015.03.02"))
print("Difference: ", date_diff(date_parse("2024.06.21 18:25:30"), date_parse("05/16/2023 08:21:10"), "day"))