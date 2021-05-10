from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/lastsearch2.nhn'
html = urlopen(URL)
soup = BeautifulSoup(html,'lxml')
popsearch_table= soup.find_all('table',{"class":"type_5" })
number = soup.find_all('td',{'class':'number'})
# print(number)
# print(len(number))=300 종목 30개 각각 항목 10개

ranking = soup.find_all('td', {'class':'no'})
ranking_list = []
name = soup.find_all('a', {'class':'tltle'})
# print(name)
# print(len(name))
title = []

for no in ranking:
    ranking_list.append(no.get_text())
# print(ranking_list)
for n in name:
    title.append(n.get_text())
# print(title)

#순위 종목명 검색비율 현재가 등락률(이하 항목) 수집해야함

popsearch_list = [] #이 리스트에 종목별로 원소 만들기. 각 원소는 또 리스트인데 거기에 순위~등락률이 원소로 존재함
for i in range (0,30):
    a = []
    a.append(ranking_list[i])#순위
    a.append(title[i])
    a.append(number[10*i].get_text().strip()) #검색비율
    a.append(number[1 +10*i].get_text().strip()) #현재가
    a.append(number[3 + 10 * i].get_text().strip()) #등락률
    popsearch_list.append(a)

# print(popsearch_list)

rank = int(input('검색하려는 종목의 순위(1~30)를 입력하세요 > '))
print(rank,'위',title[i-1],'의','검색비율은',popsearch_list[i-1][2],',','현재가는',popsearch_list[i-1][3],',','등락률은',popsearch_list[i-1][4],'입니다.')