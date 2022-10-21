def prv_visokos(year): # Проверка на високосный год
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True
def proverka(year,month,day):
    month_31 = (1,3,5,7,8,10,12)
    month_30 = (4,6,9,11)
    if 0 < month < 13 and 0 < day < 32: #Ограничения по датам(макс дней, месяцев).
        if prv_visokos(year) == True and month == 2 and 0 < day < 30: # Если високосный год, то в феврале 29 дней
            return True
        elif (prv_visokos(year) == True and month !=2 and 0 < day < 32) :
            return True
        elif prv_visokos(year) == False and month == 2 and 0 < day < 29: # Но если год не високосный, то в феврале будет 28 дней.
            return True
        elif (month in month_31 and 0 < day < 32) or (month in month_30 and 0 < day < 31): # Проверка дней по месяцам
            return True
        else:
            return False
    else:
        return False
year = int(input("Год: "))
month = int(input("Месяц: "))
day = int(input("День: "))
print(proverka(year,month,day))
