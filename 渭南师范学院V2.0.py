import requests
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
# @time   2022年5月6日18:31:05

#今天突发奇想看了一下这个脚本，结果发现在服务器上挂了将近4个月了，依旧没有挂。所以我断定贵校的维护人员肯定不怎么维护吧......
#渭南师范学院打卡V2.0版本
#**************************************更新内容******************************************
#1.优化代码结构，提高可观性，也降低了对新手及入门的兄弟集美们学习的门槛。
#2.写了个debug在里面，这样在你们加我QQ之后问我为什么报错的时候我能够更好地指出错误。
#**************************************更新内容******************************************
#作者QQ：1097123142   本脚本仅供学习，使用时问题可以加我QQ问我哦！（看到绝对会回）
#注意：请修改以下8条内容。
发件人邮箱="xxx"
发件人邮箱授权码="xxx"
收件人邮件="xxx"
#以下的内容需要抓包获得，具体操作详情：https://gitee.com/smallway/wnsfsign
User_Agent="xxx"
Referer="xxx"
Cookie="xxx"
X_REQUESTED_WITH="xxx"
Header_Pool='xxx'
#本条注释的上一条内容理论上应当是一个由大括号‘{}’括起来的内容

def main_handler(event, context):
    sender = str(发件人邮箱)
    pass_ =str(发件人邮箱授权码)
    user = str(收件人邮件)
    api="http://yqtj2.wnu.edu.cn/index.php/1/addons/fire/up/submit"
    a='{"data":{"whereis":1,"health_state":1,"family_health":1,"fever":0,"fifteen_covid":0,"village_covid":0,"temperature":"null","temp_state":1,"work":1,"back":0,"lng":"null","lat":"null","agent_up":0,"agent_user_id":"null","parent":0}}'
    getheaders ={
            "Host":"yqtj2.wnu.edu.cn",
            "content-type":"application/json",
            "Accept-Encoding":"gzip, deflate",
	        "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection":"keep-alive",
            "User-Agent":str(User_Agent),
            "Referer":str(Referer),
            "Content-Length":"2000",
            "Sec-Fetch-Site":"same-site",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Dest":"empty",
            # @author smallway
            "Cookie":str(Cookie),
            "X_REQUESTED_WITH":str(X_REQUESTED_WITH),
            "Header-Pool":str(Header_Pool),
}
    a=a.encode("utf-8")
    data=requests.post(api,headers=getheaders,data=a).json()
    #打卡成功则不发邮件，打卡失败发送邮件提醒打卡失败，需要手动打卡。
    if data['status']==200:
        print("打卡成功")
        return '打卡成功'
    elif data['message']=='该时段已经上报，无需重复上报':
        print('打卡其实成功了，只不过你打过卡了，不能打第二遍卡吧')
        return '打卡其实成功了，只不过你打过卡了，不能打第二遍卡吧'
    else:
        msg = MIMEText("打卡失败", 'plain', 'utf-8') 
        msg['From'] = formataddr(["小白", sender])  
        msg['To'] = formataddr(["Me", user])  
        msg['Subject'] = "打卡失败"  
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  
        server.login(sender, pass_)  
        server.sendmail(sender, [user, ], msg.as_string())  
        server.quit()
        print("打卡失败，错误原因："+data)
        return '打卡失败，错误原因：'+str(data)
# @author smallway
if __name__ == "__main__":
    main_handler()