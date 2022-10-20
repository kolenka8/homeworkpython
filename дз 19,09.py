def proverka(year,month,day):
    if 0 < month < 13 and 0 < day < 32: #Ограничения по датам(макс дней, месяцев).
        if year % 4 == 0 and year % 100 !=0 or year % 400 == 0: # Проверка на високосный год
            if month == 2: # В високосном году в феврале 29 дней.
                if day < 30:
                    return True
                else:
                    return False
        elif month == 2: # Но если год не високосный, то в феврале будет 28 дней.
            if day < 29:
                return True
            else:
                return False
        elif year % 4 != 0 and month != 2: # В противном случае выводим True
            return True
    else:
        return False
year = int(input("Год: "))
month = int(input("Месяц: "))
day = int(input("День: "))
print(proverka(year,month,day))
