# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import QApplication
import sys
from ui_downloader import Ui_MainWindow    # 导入生成form.py里生成的类
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DownloadThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)
    def __init__(self,url,interval=3,start=0,total=0,parent=None):
        super(DownloadThread, self).__init__(parent)
        self.url=url
        self.interval=interval
        self.start_n=start
        self.total=total
        
    def run(self):
        if int(self.start_n)==0:
            #all downloader
            self.startdownload(self.url,self.interval)
        else: 
            #single downloader
            self.startdownload_single(self.url,int(self.start_n),int(self.total))
            
    def download_once(self,browser,start,end,first):

        #选中第5个下载选项
        if(first==True):
            elems = browser.find_elements_by_css_selector('span.select2-selection__arrow')  # Find the search box
            elems[1].click()
            elem=browser.find_element_by_css_selector('ul.select2-results__options li:nth-child(5)')
            elem.click()
        else:
            elem=browser.find_element_by_id('select2-saveToMenu-container')
            elem.click()


        elem=browser.find_element_by_id('numberOfRecordsRange')
        elem.click()

        markfrom=browser.find_element_by_id('markFrom')
        markfrom.send_keys(str(start))
        markto=browser.find_element_by_id('markTo')
        markto.send_keys(str(end))

        b=browser.find_element_by_id('select2-bib_fields-container')
        b.click()

        ul=browser.find_element_by_css_selector('ul.select2-results__options li:nth-child(1)')
        ul.click()

        b=browser.find_element_by_id('select2-saveOptions-container')
        b.click()

        ul=browser.find_element_by_css_selector('ul.select2-results__options li:nth-child(7)')
        ul.click()

        button=browser.find_element_by_css_selector('div.quickoutput-overlay-buttonset span.quickoutput-action button.primary-button')
        button.click()
        
        WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'form.quick-output-form div.quickoutput-overlay-buttonset a.quickoutput-cancel-action')))
        
        close_a=browser.find_element_by_css_selector('form.quick-output-form div.quickoutput-overlay-buttonset a.quickoutput-cancel-action')
        close_a.click()
 
    def startdownload(self,url,interval):
        browser = webdriver.Chrome()

        browser.get(url)

        totalEle=browser.find_element_by_id('trueFinalResultCount').get_attribute('innerHTML')
        first=True
        c=1
        for i in range(1,int(totalEle),500):
            if i+499<=int(totalEle):
                end=i+499
                
            else:
                end=int(totalEle)
                
            self.download_once(browser,i,end,first)
            first=False
            self.trigger.emit('正在下载第{:d}个文件: {:d} - {:d}'.format(c,i,end))

            c=c+1
            time.sleep(interval)


    def startdownload_single(self,url,start,total):
        browser = webdriver.Chrome()
        browser.get(url)

        self.download_once(browser,start,start+total-1,True)

        self.trigger.emit('正在下载第{:d}个文件: {:d} - {:d}'.format(1,start,start+total-1))
        
class Downloader(QtWidgets.QMainWindow,Ui_MainWindow):    
    def __init__(self):    
        super().__init__()    
        self.setupUi(self)
        self.allButton.setChecked(True)
        self.allButton.clicked.connect(self.allbuttonclick)
        self.singleButton.clicked.connect(self.singlebuttonclick)
        self.startButton.clicked.connect(self.startdownload)
        
    def startdownload(self):
        if self.allButton.isChecked():
            url=self.urlEdit.text()
            interval=self.intervalBox.value()
            th=DownloadThread(url,interval,parent=self)
            th.trigger.connect(self.update_message)
            th.start()
        else:
            url=self.urlEdit.text()
            start=self.startEdit.text()
            total=self.totalEdit.text()
            th=DownloadThread(url,0,start,total,parent=self)
            th.trigger.connect(self.update_message)
            th.start()
    
    def allbuttonclick(self):
        self.startEdit.setEnabled(False)
        self.totalEdit.setEnabled(False)
        
    def singlebuttonclick(self):
        self.startEdit.setEnabled(True)
        self.totalEdit.setEnabled(True)
        
    def update_message(self,msg):
        self.textBrowser.append(msg)
        
app = QApplication([])
ex = Downloader()
ex.show()
sys.exit(app.exec_())