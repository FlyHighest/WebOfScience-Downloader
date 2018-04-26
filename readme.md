# WebOfScience-Downloader

Download files of search results from webofscience automatically. It is useful when you have thousands of papers to download

# Packages

The following packages are used:

    PyQt5
    selenium
    
If you don't need a GUI, you may only need selenium to run downloader_func.py

I use pyinstaller to generate two Exe files, you can use them on windows.

I tested this program on win10/7(64bit) and win10(32bit)

Also, your computer should have Chrome installed and chrome web driver in system path.

Chrome version 66，chrome webdriver version2.3.7 are used during developing and testing.

# Usage

1. Install Chrome
2. Install webdriver( notice the version should match with chrome version)
3. Run the downloader



Fill 下载地址 with **a url that has search results displayed** like：
http://apps.webofknowledge.com/Search.do?product=WOS&SID=\*\*\*&search_mode=GeneralSearch&prID=\*\*\*
![image](https://note.youdao.com/yws/public/resource/31699667cabbdc1de896da3b9430250e/xmlnote/A8ABF9B607C646E7B955CAD0A9AB3AFD/865)


下载间隔: how many seconds the downloader waits after it starts to download a file. Try to increase this number if your network is not so good.

Press “开始下载” to start download.

# WebOfScience-下载器

自动下载在webofscience上检索到的文章记录。

# 运行环境
使用到的包：

    PyQt5
    selenium
    
如果你不需要界面的话，可以只使用downloader_func.py中的方法。

我用pyinstaller打包好了两个exe，在64位win10/7和32位win10上测试过。

下载器依赖于chrome浏览器和chromedriver。我在开发和测试时，使用的chrome版本是66，chromedriver版本是2.3.7。

# 使用说明

1. 安装Chrome。
2. 安装对应版本的webdriver。
3. 双击downloader.exe打开下载器。

![image](https://note.youdao.com/yws/public/resource/31699667cabbdc1de896da3b9430250e/xmlnote/46DB44E0A4644F3192D1A1A55C7791F9/856)
###### <center>下载器界面 </center>


下载器的界面非常简单，下载地址填写**已经检索到论文结果**的网页地址。比如：
http://apps.webofknowledge.com/Search.do?product=WOS&SID=\*\*\*&search_mode=GeneralSearch&prID=\*\*\*
![image](https://note.youdao.com/yws/public/resource/31699667cabbdc1de896da3b9430250e/xmlnote/A8ABF9B607C646E7B955CAD0A9AB3AFD/865)
###### <center>需要的下载地址示例 </center>

下载间隔，即文件下载后，隔几秒开始下一个文件下载，默认是3秒，可以根据网速调整，避免同时下载的文件太多，造成下载失败。

右侧的选项“全部下载”，程序后自动获取检索结果网页中，记录总数，开始从1到最后，每500条记录一个文件进行下载。如果中间有网络错误，文件下载失败，或者其他特殊需求，可以选择“单个文件”，这时必须填写起始记录号和要下载的记录数量。下载数量不可以超过500。

如果配置无误的话，点击“开始下载”之后会弹出一个chrome浏览器，程序开始自动进行操作。下载的文件保存在chrome的默认保存位置下，这个可以在浏览器的设置中配置。下载的文件会自动命名，一般为savedrecs (\*).txt。在浏览器启动后，请**不要在网页中进行任何操作**，避免影响程序寻找需要点击的位置。另外，启动下载后，系统可能会提示是否允许下载器程序访问网络，点击允许即可。

