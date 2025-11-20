import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import schedule
import time

account=input('请输入账号')
password=input('请输入密码')
receiver=input('请输入收件人账号')

#天气爬虫函数
def weather_spider():
    headers={'user-agent':'Mozilla/5.0(WindowsNT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    url='http://www.weather.com.cn/weather/101230708.shtml'
    res=requests.get(url,headers=hea
    ers)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    temperature= soup.find(class_='tem')
    weather= soup.find(class_='wea')
    tem=temperature.text
    wea=weather.text
    return tem,wea

def send_email(tem,wea):
    #连接服务器
    mailhost='smtp.qq.com'
    qqmail=smtplib.SMTP()
    qqmail.connect(maihost,25)
    #通过账号和密码登录邮箱
    qqmail.login(account,password)
    #正文
    content='亲爱的，今天天气是'+tem+wea
    message=MIMEText(content,'plain','utf-8')
    #主题
    subject='今日天气预报'
    MIMEText['Subject']=Header(subject,'utf-8')
    #发送
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    #退出
    qqmail.quit()

def job():
    print('开始一次任务')
    tem,weather = weather_spider()
    send_email(tem,weather)
    print('任务完成')

schedule.every().day.at("07:30").do(job) 
while True:
    schedule.run_pending()
    time.sleep(1)
