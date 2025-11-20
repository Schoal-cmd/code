# smtplib 用于邮件的发信动作
# email模块
import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header


# 发信方的信息：发信邮箱，QQ邮箱授权码
from_addr = input('请输入登录邮箱：')
password = input('请输入邮箱授权码：')

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
text = '''亲爱的学员，你好！
​    我是吴枫老师，能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
# 待写入csv文件的收件人数据：人名+邮箱
# 记得替换成你要发送的名字和邮箱
data = [['凌羊心', '2970223125@qq.com']]

# 写入收件人数据
with open('to_addrs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

# 读取收件人数据，并启动写信和发信流程
with open('to_addrs.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader: 
        to_addrs=row[1]
        msg = MIMEText(text,'plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addrs)
        msg['Subject'] = Header('python test')
        server = smtplib.SMTP_SSL()
        server.connect(smtp_server,465)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addrs, msg.as_string())

try:
    server.sendmail(from_addr, to_addrs, msg.as_string())
    print('恭喜，发送成功')
except:
    print('发送失败，请重试')

# 关闭服务器
server.quit()

