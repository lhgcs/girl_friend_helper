#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
@Description: 
@Version: 1.0
@Autor: lhgcs
@Date: 2019-09-06 12:08:19
@LastEditors: lhgcs
@LastEditTime: 2019-09-06 12:08:31
'''

import json
from urllib import request

'''
@description: 
@param {type} 
@return: 
'''
def getHtml(url):
    page = request.urlopen(url)
    html = str(page.read(), encoding = "utf-8")
    return html

'''
@description: 
@param {type} 
@return: 
'''    
def get(id):
    id  = str(id)
    a = getHtml('http://music.163.com/api/song/lyric?os=pc&id=' + id + '&lv=-1&kv=-1&tv=-1')
    print(a)
    b = json.loads(a)
    #print b['sgc']
    if(b['sgc']):
        a = "error"
    else:
        if 'lrc' in b and 'lyric' in b:
            a = b['lrc']['lyric']
        else:
            a = "error"
    return a
    '''
    http://music.163.com/api/song/lyric?os=pc&id=2061094615&lv=-1&kv=-1&tv=-1
    {"uncollected":true,"sgc":true,"sfy":false,"qfy":false,"needDesc":true,"code":200,"briefDesc":null}
    '''

'''
@description: 
@param {type} 
@return: 
'''
def out(text):
    if(text == "error"):
        print("错误的ID！")
    else:
        text = text.split('\n')
        for i in text :
            print(i)

if __name__ == "__main__":
    i = input("请输入歌曲ID：")
    out(get(i))