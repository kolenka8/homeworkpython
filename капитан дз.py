#1 вариант
import datetime
def captain(lst,dat): # Функция принимает текст (записи капитана) и дату записи
    with open('note.txt','w') as file: # Создаём файл (Дневник капитана) 
        for days in range(len(lst)):
            file.writelines(["{0}:{1}{2}".format(datetime.datetime.strptime(dat,'%Y.%m.%d')+datetime.timedelta(days),lst[days],'\n')])
            # с помощью strptime создаём объект datetime из строки и с помощью timedelta запоминаем разницу между двумя датами 
captain(['Здравствуйте','Досвидания'],'2022.10.17')

#2 вариант
from datetime import timedelta, date
def captain(lst,dt): # Функция принимает текст () и дату
    a = timedelta(days=1)
    file_open = open('log.txt','w') # Создаём файл (Дневник капитана)
    for dayses in lst:
        file_open.write(str(dt) + ': ' + dayses + '\n')
        dt += a
    file_open.close()

captain(['Привет','Пока'], date(2023, 10, 17))
