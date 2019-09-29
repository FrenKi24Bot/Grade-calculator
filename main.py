# -*- coding: utf-8 -*- 
from bs4 import  BeautifulSoup
import datetime


html=open(r'html.txt','r')


lessons=[ # constuction: 'name of lesson',[marks],[average score]
    ['',[],[],[]],
    
]


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
    soup=BeautifulSoup(html,'html.parser') # connect bs4
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
                        if (lessons[i][0]==lesson) and not(mark==''): # ищем нужный предмет
                            lessons[i][1].append(mark)
                            lessons[i][3].append(date) # добавляем инфу
                            break
                        elif(i==len(lessons)-1) and not(mark==''): # создаём если его нету
                            lessons.append([lesson,[mark],[],[date]])  
                            break          
                else:
                    pass
            except Exception as err:
                print(err)

        except:
            pass 
 


def calculation():
    for i in range(len(lessons)): # в предметах
        sum=0
        n=0
        for j in range(len(lessons[i][1])): # в оценках
            if(len(lessons[i][1][j])==3): # if 8/5 for example
                n+=2
                #print(lessons[i][1][j][0],' ',lessons[i][1][2])
                sum+=int(lessons[i][1][j][0])
                sum+=int(lessons[i][1][j][2])
            elif(len(lessons[i][1][j])==5):#10/10
                n+=2
                sum+=20   
            elif(len(lessons[i][1][j])==4):#10/8 or 8/10
                n+=2
                if(lessons[i][1][j][0]=='1' and lessons[i][1][j][1]=='0'): # if 10/x
                    sum+=10
                    sum+=int(lessons[i][1][j][3])
                    
                elif(lessons[i][1][j][2]=='1' and lessons[i][1][j][3]=='0'): # if x/10
                    sum+=10
                    sum+=int(lessons[i][1][j][0])

            else: # normal mark for example 8
                n+=1
                sum+=int(lessons[i][1][j])                   
        try:
            lessons[i][2]=round((sum/n), 3) # calc a averange score
        except:
            pass   


def sort():
    for i in range(1,len(lessons)):
        for j in range(len(lessons[i][3])):
            for k in range(len(lessons[i][3])):
                if(lessons[i][3][j]<lessons[i][3][k]):
                    lessons[i][3][j],lessons[i][3][k]=lessons[i][3][k],lessons[i][3][j]
                    lessons[i][1][j],lessons[i][1][k]=lessons[i][1][k],lessons[i][1][j]


def show():
    lessons.sort()
    print(' №  |','Предмет','    |Ср.Балл|','Оценки')
    print()
    for i in range(1,len(lessons)):
        print(' '+str(i)+(3-len(str(i)))*' '+'|',str(lessons[i][0])+(12 -len(lessons[i][0]))*' '+'|',str(lessons[i][2])+(6-len(str(lessons[i][2])))*' '+str(lessons[i][1]).replace("'",'').replace("[",'| ').replace("]",''))


main()
calculation()
sort()
show()
