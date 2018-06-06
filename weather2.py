#coding:utf-8
import urllib.request
from bs4 import BeautifulSoup
from city import city




def get_weather(citycode):
    url = 'http://www.weather.com.cn/weather/'+citycode+'.shtml'
    #request = urllib.request.Request(url)
    response = urllib.request.urlopen(url)
    data = response.read()
    data = data.decode('utf-8','ignore')
    #print(data)
    soup = BeautifulSoup(data,"html.parser")
    tagDate=soup.find('ul',class_='t clearfix')
    days=tagDate.find_all('h1')
    dict={}
    weathers=[]
    tagweathers=tagDate.find_all('p',class_='wea')
    for weather in tagweathers:
        weathers.append(weather.string)
    temperatures=[]
    tagtemperatures=tagDate.find_all('p',class_='tem')
    for tagtemperature in tagtemperatures:
        try:
            temperatureHigh=tagtemperature.find('span')
        except:
            temperatureHigh=''
        temperatureLow=tagtemperature.find('i')
        try:
            temperatures.append(temperatureLow.string + '~' + temperatureHigh.string + '℃')
        except:
            temperatures.append(temperatureLow.string)
    tagwinds=tagDate.find_all('p',class_='win')
    winds=[]
    for tagwind in tagwinds:
        winds.append(tagwind.find('i').string)
    states=[]
    for i in range(0,7):
        states.append([weathers[i],temperatures[i],winds[i]])
    i=0
    for day in days:
        dict[day.string]=states[i]
        i+=1
    for day in dict:
        print(day+':')
        for state in dict[day]:
            print(state)
        print('\n')
#dates=tagDate.h1.string
#print(dates)
#tagToday=soup.find('p',class_='tem')
#print(tagToday)
#try:
    #temperatureHigh=tagToday.span.string
#except AttributeError as e:
    #temperatureHigh=tagToday.find_next('p',class_='tem').span.string
#tagAddr=soup.find('div',class_='crumbs fl')
#citys = ''
#for k in tagAddr.find_all('a'):  # 查a标签的href值
    #citys = citys + k.string
#if citys == '':
    #citys = tagAddr.string.replace('\r\n\t\t\t\t','',1)
    #citys = citys.replace('\r\n\t\t\t','',1)
    #citys = citys.replace('>','',1)
#temperatureLow = tagToday.i.string
#weather = soup.find('p', class_="wea").string
#tagWind = soup.find('p', class_="win")
#winL = tagWind.i.string
#listWeather = [citys, dates, winL, temperatureLow, temperatureHigh, weather]
#print('城市: ' + listWeather[0] + '\n')
#print('今天是:' + listWeather[1] + '\n')
#print('风级:' + listWeather[2] + '\n')
#print('最低温度:' + listWeather[3] + '\n')
#print('最高温度:' + listWeather[4] +'℃'+ '\n')
#print('天气:' + listWeather[5] + '\n')
##listWeather = [citys, dates, winL, temperatureLow, temperatureHigh, weather]
##print(listWeather)

##self.lblWeather.SetBackgroundColour((0,0,0))


cityname=input('你想查询哪个城市的天气？')
try:
    citycode=city[cityname]
    get_weather(citycode)
except:
    print('您输入的城市有误或无法查询！')

