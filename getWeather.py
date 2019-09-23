#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@Description: 获取天气（可获取未来15天和昨天的信息）
@Version: 1.0
@Autor: lhgcs
@Date: 2019-09-16 17:02:58
@LastEditors: lhgcs
@LastEditTime: 2019-09-16 18:05:40
'''

'''
接口说明：
https://www.sojson.com/blog/305.html
http://www.sojson.com/api/weather.html

请求接口：
http://t.weather.sojson.com/api/weather/city/+city_code
返回json
'''

import sys
import json
import urllib.request


'''
@description: 获取天气
@param {type} 城市编码
@return: 
'''
def get_weater(city_code=101030100):
    try:
        url = "http://t.weather.sojson.com/api/weather/city/{}".format(city_code)
        page = urllib.request.urlopen(url, timeout=5)
        # bytes 转 str
        jsonStr = page.read().decode("utf-8")
        # json 解析
        jsonData = json.loads(jsonStr)
        # 正确返回
        if 200 == jsonData["status"]:
            
            print("城市编码：", jsonData["cityInfo"]["citykey"])
            print("城市：",    jsonData["cityInfo"]["city"])
            print("日期：",    jsonData["data"]["forecast"][0]["ymd"], jsonData["data"]["forecast"][0]["week"])
            print("天气：",    jsonData["data"]["forecast"][0]["type"])
            print("建议：",    jsonData["data"]["ganmao"])
            print("PM25：",    jsonData["data"]["pm25"])
            print("最低温度：", jsonData["data"]["forecast"][0]["low"])
            print("最高温度：", jsonData["data"]["forecast"][0]["high"])
            
        else:
            # 错误信息
            print("error: ", jsonData["message"])
    except Exception as e:
        print(e)
    finally:
        return None


if __name__ == "__main__":
    get_weater()