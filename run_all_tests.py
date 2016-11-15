import unittest
from HTMLTestRunner3 import HTMLTestRunner
import time
from email.mime.text import MIMEText
from email.header import Header
import smtplib,os


# 发送测试报告，需要配置你的邮箱账号。
def send_mail(file_new):
	mail_from='you@mail.com'
	mail_to='you@mail.com'
	f = open(file_new, 'rb')
	mail_body = f.read()
	f.close()
	msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
	msg['Subject']=u"自动化测试报告"
	smtp=smtplib.SMTP()
	smtp.connect('smtp.mail.com')
	smtp.login('you@mail.com','123')
	smtp.sendmail(mail_from,mail_to,msg.as_string())
	smtp.quit()
	print('email has send out !')


# 查找最新生成的测试报告
def get_new_file(files):
	lists = os.listdir(files)
	lists.sort(key=lambda fn: os.path.getmtime(files+"\\"+fn))
	file_ = os.path.join(files,lists[-1])
	print(file_)
	return file_


if __name__ == '__main__':
    test_app = "./mail_app" #定义测试应用
    now_time =  time.strftime("%Y_%m_%d_%H_%M_%S")
    fp = open(test_app+"/report/"+now_time+"result.html",'wb')
    runner = HTMLTestRunner(fp,
                           title="xxx测试报告",
                           description="运行环境：windows 10, firefox")
    discover = unittest.defaultTestLoader.discover(test_app+"/test_case", pattern='*_case.py')
    runner.run(discover)
    fp.close()
