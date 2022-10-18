import datetime
def captain(lst,dat):
    with open('note.txt','w') as file:
        for days in range(len(lst)):
            file.writelines(["{0}:{1}{2}".format(datetime.datetime.strptime(dat,'%Y.%m.%d')+datetime.timedelta(days),lst[days],'\n')])

captain(['Здравствуйте','Досвидания'],'2022.10.17')
