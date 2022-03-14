import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def main_handler(event, context):
    
    sender = "xxx"  # 修改1：填写发件人的邮件
    pass_ = "xxx"  # 修改2：发件人邮箱授权码
    user = "xxx"  # 修改3：收件人的邮件

    api="http://yqtj2.wnu.edu.cn/index.php/1/addons/fire/up/submit"
    a='{"data":{"whereis":1,"health_state":1,"family_health":1,"fever":0,"fifteen_covid":0,"village_covid":0,"temperature":"null","temp_state":1,"work":1,"back":0,"lng":"null","lat":"null","agent_up":0,"agent_user_id":"null","parent":0}}'
    getheaders ={
            "Host":"yqtj2.wnu.edu.cn",
            "content-type":"application/json",
            "Accept-Encoding":"gzip, deflate",
	        "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection":"keep-alive",
            "User-Agent":"xxx",#修改4
            "Referer":"xxx",  #修改5
            "Content-Length":"2000",
            "Sec-Fetch-Site":"same-site",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Dest":"empty",
            "Cookie":"xxx",#修改6
            "X_REQUESTED_WITH":"xxx",#修改7
            "Header-Pool":'xxx',#修改8
}
    a=a.encode("utf-8")
    data=requests.post(api,headers=getheaders,data=a).json()
    print(data)
    #打卡成功则不发邮件，打卡失败发送邮件提醒打卡失败，需要手动打卡。
    if data['status']==200:
        print("success")
        return '打卡成功'
    else:
        msg = MIMEText("打卡失败", 'plain', 'utf-8') 
        msg['From'] = formataddr(["小白", sender])  
        msg['To'] = formataddr(["Me", user])  
        msg['Subject'] = "打卡失败"  

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  
        server.login(sender, pass_)  
        server.sendmail(sender, [user, ], msg.as_string())  
        server.quit()  
        return '打卡失败'