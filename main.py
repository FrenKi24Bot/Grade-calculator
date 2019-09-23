# -*- coding: utf-8 -*- 
from bs4 import  BeautifulSoup
import datetime


txt=open(r'html.txt','r')
lessons=[ # constuction: 'name of lesson',[marks],[average score]
    ['Астрономия',[],[]],
    ['Бел.лит.',[],[]],
    ['Бел.яз.',[],[]],
    ['Биология',[],[]],
    ['Всемир.ист.',[],[]],
    ['География',[],[]],
    ['ДП/МП',[],[]],
    ['Информ.',[],[]],
    ['Ист.Бел.',[],[]],
    ['Матем.',[],[]],
    ['Нем.яз.',[],[]],
    ['Обществов.',[],[]],
    ['Рус.лит.',[],[]],
    ['Рус.яз.',[],[]],
    ['Физика',[],[]],
    ['Физ.к.изд.',[],[]],
    ['Химия',[],[]],
    ['ЧЗС',[],[]]
]



b=0
quarter=[  #даты начала четвертей
    datetime.date(2019,9,2),
    datetime.date(2019,11,11),
    datetime.date(2020,1,13),
    datetime.date(2020,9,6),
] 

def define_quarter():
    for i in range(len(quarter)):
        if(datetime.date.today() > quarter[i]): # опредедяем четрветь
            n=i
    return n

def main():
    soup=BeautifulSoup(txt,'html.parser') # connect bs4

    trs=soup.findAll('tr') # find all 'tr'
    for tr in trs:    
        try:
            lesson=tr.find('span').text.replace(' ', '').replace('\n','') # take a lesson and conver them to normal
            lesson=lesson.replace(lesson[0] + lesson[1],'')
            
            mark=tr.find('strong').text # take a mark


            soup1=BeautifulSoup(str(tr.parent.parent),'html.parser') # connect another bs4 for find a date

            date=soup1.find('table', class_='db_table').get('id').replace('db_table_','') # take a date
            date=datetime.datetime.strptime(date,'%d.%m.%y')

            try:
                num=define_quarter() # take a num of a quarter
                if(date.strftime("%Y%m%d")  > quarter[num].strftime("%Y%m%d")): # сравниваем(проверяем) то, чтобы была выбрана верная четветь
                    # is okay
                    for i in range(len(lessons)):
                        if lessons[i][0]==lesson:
                            #print(mark)
                            lessons[i][1]+=mark # add mark in array with lessons
                else:
                    pass

            except Exception as err:
                print(err)
      
        except:
            pass 

    for i in range(len(lessons)):  # проверка на наличие парных оценок (8/5)
        try:    
            lessons[i][1].remove('/')
        except:
            pass    

def calculation():
    for i in range(len(lessons)):
        n=0
        for j in range(len(lessons[i][1])):
            n+=int(lessons[i][1][j]) # num(количество) of mark
        try:
            lessons[i][2]=round((n/len(lessons[i][1])), 3) # calc a averange score
        except:
            pass    
        n=0

def show():
    for i in range(len(lessons)):
        print(str(lessons[i][0])+(12-len(lessons[i][0]))*' ',str(lessons[i][1]),' ',str(lessons[i][2]))
main()
#print(lessons[4][1][2])
calculation()
show()
