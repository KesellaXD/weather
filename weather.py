#coding=utf-8
import urllib.request
from city import city
import json

cityname = input("你想查询那个城市的天气？\n")
citycode=""


try:
	citycode=city[cityname]
except:
	print ("not Found")

if citycode:
	try:
		url=r"http://www.weather.com.cn/data/cityinfo/"+citycode+".html"
		content=urllib.request.urlopen(url).read()#读取网页源代码
		data=json.loads(content)#使用json库将字符转化为字典
		res=data["weatherinfo"]
		str_temp=("%s :%s~%s")%(res["weather"],res["temp1"],res["temp2"])
		print(str_temp)
	except:
		print ("Not Found!!")
