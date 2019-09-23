
from smtplib import SMTP_SSL
from email.header import Header, decode_header
from email.utils import parseaddr
from email.mime.text import MIMEText
from email.parser import Parser
import poplib

import os, sys
import time
import re
import string
import traceback
import urllib.request


url ='http://www.ip.cn/'
#从邮箱内获取最近的一次ip，因为程序每五分钟执行一次，
# 所以需要确认该ip是否已经发送，没有发送才进行送。  已经发送的就不需要再发送
                                      
def  Ip_recv(name):         
    ip_address =0
    message =[]
    # pop3服务器地址
    host ="pop3.163.com"
    # 用户名
    username ="xxxxxx@163.com"
    # 密码
    password ="xxxxxxx"
    # 创建一个pop3对象，这个时候实际上已经连接上服务器了
    pp = poplib.POP3_SSL(host)
    # 设置调试模式，可以看到与服务器的交互信息
    #pp.set_debuglevel(1)
    # 向服务器发送用户名
    pp.user(username)
    # 向服务器发送密码
    pp.pass_(password)
    # 获取服务器上信件信息，返回是一个列表，
    第一项是一共有多上封邮件，第二项是共有多少字节
    ret = pp.stat()
    num=ret[0]#ret[0]总共有几封邮件
    # 取第一封邮件完整信息，在返回值里，
    是按行存储在down[1]的列表里的。down[0]是返回的状态信息
    while(ip_address is 0):
        ret= pp.list()
        hdr,lines,octet = pp.retr(num)
        try:
            for line in lines:
                message.append(line.decode('utf-8'))
                msg_content ='\r\n'.join(message)
                msg = Parser().parsestr(msg_content)
        except:
            pass
        num = num -1
        if(numis0):
            pp.quit()#退出pop
            return0
        try:
            ip_flag = (decode_str(msg.get('Subject')))#获取主题
            #print ("检查邮件...")
            if  name  in  ip_flag:#获取树莓派IP
                ip = ip_flag.split(':')#字符分割
                ip_address = ip[1]#获取ip地址
                #print("取得IP成功.")
                return  ip_address
            else:
                del message[:]
        except:
            #print("取得IP失败，请检查邮箱")
            pass
    pp.quit()


def decode_str(s):#邮件格式转换
    value, charset = decode_header(s)[0]
    if  charset:
        value = value.decode(charset)
    return  value

def get_local():
    ip_local =input("输入查询地址：1是home,2是company\n")
    ip_local=int(ip_local)
    if ip_local is 1:
        name ="RaspberryIP"#用于识别是家里的ip，还是公司的ip
    elif ip_local is 2:
        name ="CompanyIP"
    else:
        name=get_local()
    return name

if__name__ =='__main__':
    content_pre =0
    count =0
    name=get_local()#确认需要获取哪里的ip，如果单纯在树莓派上运行，
                                            #则直接把判断变成肯定就行
    print("name is %s"%name)
    while True:
        try:#伪装头，用于防止网站服务器屏蔽你的ip
            req = urllib.request.Request(url,headers= {
                        'Connection':'Keep-Alive',
                        'Accept':'text/html, application/xhtml+xml, */*',
                    'Accept-Language':'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) 
                    like Gecko'
            })
            wp = urllib.request.urlopen(req)
            content = wp.read()
            content=content.decode('utf-8','ignore')#utf-8解码
            index =  content.find("IP：")#找到ip所在地
            content=content[content.find("IP：")+1:]#抓取ip所在位置
            #print(content)
            content=content[content.find("")+6:content.find("")]#抓取ip
        except:
        #print("get ip error")
            pass
        try:
            E_mail_ip=Ip_recv(name)#从邮箱里获取邮件里已有ip
        except:
            E_mail_ip = content
        if((content_pre != content)and(E_mail_ip != content)):
        #如果新ip与已存在的老ip不一样，则发送邮件，反之不发
            count =count+1
            content_pre =content
            mail_info = {
                "from":"yyyyyyy@qq.com",                          #你发送ip的邮箱
                "to":"xxxxxxxx@163.com",                          #你接受ip的邮箱
                "hostname":"smtp.qq.com",                       
                "username":"yyyyyyyyyy@qq.com",            #你接受ip的邮箱名
                "password":"yyyyy",                                     #接受ip邮箱的密码
                "mail_subject":'%s:%s'%(name,content),    #邮件主题
                "mail_text":"%s"%content,                          #ip地址
                "mail_encoding":"utf-8"                               #编码形式
            }
            #这里使用SMTP_SSL就是默认使用465端口
            smtp = SMTP_SSL(mail_info["hostname"])
            smtp.set_debuglevel(1)
            try:
                smtp.ehlo(mail_info["hostname"])
                smtp.login(mail_info["username"], mail_info["password"])
                msg = MIMEText(mail_info["mail_text"],"plain", mail_info["mail_encoding"])
                msg["Subject"] = Header(mail_info["mail_subject"], 
                        mail_info["mail_encoding"])
                msg["from"] = mail_info["from"]
                msg["to"] = mail_info["to"]
                smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())
                smtp.quit()
                print(count)
            except:
                print("send email error")
                pass
        time.sleep(60)
#GBK，GB2312,Big5,utf-8
