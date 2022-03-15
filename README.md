# 渭南师范学院微信每日打卡

#### 介绍
渭南师范学院微信每日自动打卡（渭南高校技术转移中心）
本代码仅用于学习使用，请勿使用本代码盈利等。造成后果由使用者自负，均与作者无关。健康生活，认真打卡。作者QQ：1097123142，欢迎交流。

​	
     **所有文件以及相关代码已在文件列表上传，下载即可使用**

### 一、Fiddler 抓包工具

#### 1.安装和配置

安装包下载：Fiddler 安装包和 Fiddler 证书生成器

蓝奏云链接：https://dominic.lanzouq.com/iKszLzyh5gh

下载后解压，先双击 `FiddlerSetup.exe` 进行安装，另一个是证书生成器，暂时不用。

打开 Fiddler ，点击工具栏中的 `Tools` → `Options`

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802134532161-1627956867319.png" alt="1.1.1"  />

点击 `HTTPS` 标签，勾选框住的三项，然后点击右边的 `Actions`，选择第二项，会弹出一个弹窗，点击确定，之后点击 `OK` 完成设置

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802140021903.png" alt="1.1.2"  />

这时会发现桌面上多了一个证书文件（如下图），接下来马上会用到

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802140437482.png" alt="1.1.3"  />

打开电脑上任何一个浏览器，在这里我用的是 win10 自带的 Edge，打开设置，找到`证书管理`，实在找不到也可以直接搜索

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802140839373.png" alt="1.1.4"  />

点击`管理证书`，点击`导入`进入证书导入向导

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802141018230.png" alt="1.1.5" style="zoom:67%;" />

点击`下一页`继续

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802141144696.png" alt="1.1.6" style="zoom:67%;" />

点击`浏览`，选择要导入的文件

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802141332680.png" alt="1.1.7" style="zoom:67%;" />

在桌面找到刚刚导出的证书文件，点一下证书文件，选择`打开`

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802141716446.png" alt="1.1.8" style="zoom:67%;" />

之后一直点击`下一步`，直到完成证书导入。到这里配置工作基本完成，可以进行抓包了，刚刚导出在桌面的证书文件也可以删除

#### 2.抓包
接下来从微信电脑端打开渭南高校技术转移中心公众号，进行一次打卡，会发现 Fiddler 中显示了很多内容，我们找到yqtj2.wnu.edu.cn这一行，双击打开，在右边选择Headers标签，复制 User-Agent（设备信息）、Referer（学校信息）、cookie（身份识别码）、X_REQUESTED_WITH（X_要求）、Header-Pool（标题池）。
![1.2.1](https://gitee.com/smallway/drawing-bed/raw/master/2022-3-1510:25:511647311151399.png)
复制的内容可以发给你的工具人小伙伴，或者你的小号，总之先保留下来备用。
### 二、QQ邮箱

#### 获取授权码

用QQ邮箱发件也需要登录，不是用账号密码，而是授权码（更安全），接下来获取授权码

进入QQ邮箱网页版，进入`设置`，选择`账户`

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802152812320.png" alt="2.1.1" style="zoom:67%;" />

往下翻找到 `POP3/SMTP服务`，确保第一项是`已开启`状态，如果不是，点击后面的开启，然后选择下面的`生成授权码`

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802152944128.png" alt="2.1.2" style="zoom:67%;" />

根据提示验证后，得到授权码，和抓包步骤一样，把授权码复制保存下来备用。

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802153128652.png" alt="2.1.3" style="zoom:67%;" />


### 三、Python 代码

```
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
```

### 四、腾讯云函数

注册过程就不再赘述，注册完记得完成实名认证，这里给出腾讯云官网链接：[腾讯云(tencent.com)](https://cloud.tencent.com/)

#### 1.使用云函数

进入腾讯云先登录，搜索云函数

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802160948779.png" alt="4.1.1" style="zoom:67%;" />

管理控制台

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802161241550.png" alt="4.1.2" style="zoom:67%;" />

函数服务 → 新建

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802161459839.png" alt="4.1.3" style="zoom:67%;" />

选择从头开始，函数名称可以改一下，方便区分,名称不能为中文，运行环境选择python3.6
<img src="https://gitee.com/smallway/drawing-bed/raw/master/2022-3-1510:38:501647311930730.png" alt="4.1.4" style="zoom:67%;"/>

往下翻，函数代码选择在线编辑，把代码粘贴在这里，代码内"xxx"内容需要修改为刚才抓包抓到的内容

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210803080356200.png" alt="4.1.5" style="zoom:67%;" />

其他设置保持默认即可，然后点击完成。这样就把代码部署在腾讯云上了，可以尝试运行一下
<img src="https://gitee.com/smallway/drawing-bed/raw/master/2022-3-1510:42:281647312148226.png" alt="4.1.6" style="zoom:67%;"/>

在函数管理-函数代码中可以测试代码是否运行成功
<img src="https://gitee.com/smallway/drawing-bed/raw/master/2022-3-1510:46:481647312407367.png" alt="4.1.7" style="zoom:67%;"/>

下方的执行结果若出现“打卡成功”则代表成功打卡。若出现打卡失败，请看下方的执行日志message值若为"当前不在上报时间内"也能证明打卡成功，只不过刚才抓包的时候打过卡了，同一时间段不能进行第二次打卡对吧QAQ
<img src="https://gitee.com/smallway/drawing-bed/raw/master/2022-3-1510:49:591647312598486.png" alt="4.1.8" style="zoom:67%/;">

#### 2.定时触发

设置定时触发之后，就可以按照自己的时间定时运行一次代码，这样就解放了双手

触发管理 → 创建触发器

<img src="https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210803083310441.png" alt="4.1.7" style="zoom:67%;" />

触发周期选择自定义，这里要输入 Cron 表达式，我填的是0 30 0,12 * * * *表示每天00:30、12:30各运行一次；其他设置保持默认即可，点击提交。

教程到这里就结束了，如果需要其他时间打卡，可以直接更改 Cron表达式。
