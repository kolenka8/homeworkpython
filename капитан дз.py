import datetime
def captain(lst,dat): # Функция принимает текст (записи капитана) и дату записи
    with open('note.txt','w') as file: # Создаём файл (Дневник капитана) 
        for days in range(len(lst)):
            file.writelines(["{0}:{1}{2}".format(datetime.datetime.strptime(dat,'%Y.%m.%d')+datetime.timedelta(days),lst[days],'\n')])
            # с помощью strptime создаём объект datetime из строки и с помощью timedelta запоминаем разницу между двумя датами 
captain(['Здравствуйте','Досвидания'],'2022.10.17')
