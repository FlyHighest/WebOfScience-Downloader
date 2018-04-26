from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def download_once(browser,start,end,first):


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

    ul=browser.find_element_by_css_selector('ul.select2-results__options li:nth-child(3)')
    ul.click()

    b=browser.find_element_by_id('select2-saveOptions-container')
    b.click()

    ul=browser.find_element_by_css_selector('ul.select2-results__options li:nth-child(8)')
    ul.click()

    button=browser.find_element_by_css_selector('div.quickoutput-overlay-buttonset span.quickoutput-action button.primary-button')
    button.click()
    
    WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'form.quick-output-form div.quickoutput-overlay-buttonset a.quickoutput-cancel-action')))
    
    close_a=browser.find_element_by_css_selector('form.quick-output-form div.quickoutput-overlay-buttonset a.quickoutput-cancel-action')
    close_a.click()
    
def startdownload(downloader,url,interval):
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
            
        download_once(browser,i,end,first)
        first=False
        print('正在下载第{:d}个文件: {:d} - {:d}'.format(c,i,end))
        downloader.update_message('正在下载第{:d}个文件: {:d} - {:d}'.format(1,start,start+total-1))

        c=c+1
        time.sleep(interval)

    browser.quit()        

def startdownload_single(downloader,url,start,total):
    browser = webdriver.Chrome()
    browser.get(url)

    download_once(browser,start,start+total-1,True)

    print('正在下载第{:d}个文件: {:d} - {:d}'.format(1,start,start+total-1))
    downloader.update_message('正在下载第{:d}个文件: {:d} - {:d}'.format(1,start,start+total-1))
    browser.quit()   