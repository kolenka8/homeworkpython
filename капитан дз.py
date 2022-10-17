import datetime
def captain(lst,dt):
    with open('log.txt','w') as file:
        for days in range(len(lst)):
            file.writelines(["{0}:{1}{2}".format(datetime.datetime.strptime(dt,'%Y.%m.%d')+datetime.timedelta(days),lst[days],'\n')])

captain(['Привет','Пока'],'2022.10.17')