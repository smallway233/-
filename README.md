# 渭南师范学院微信每日打卡

#### 介绍
渭南师范学院微信每日自动打卡（渭南高校技术转移中心）
本代码仅用于学习使用，请勿使用本代码盈利等。造成后果由使用者自负，均与作者无关。健康生活，认真打卡。作者QQ：1097123142，欢迎交流。
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
