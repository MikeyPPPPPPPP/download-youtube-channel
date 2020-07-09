from selenium import webdriver
import requests
import time

link_file = open('OMFG .txt','w')#add the name of the channel here

SCROLL_PAUSE_TIME = 0.5


path = "C:\Program Files (x86)\chromedriver.exe"# put the path to the web driver you installed 
driver = webdriver.Chrome(path)

#driver.set_page_load_time(10)
driver.get('https://www.youtube.com/c/alexsavageomfg/videos')# add the video url of the channel

last_link = None
done = 0

elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    if 'watch' in elem.get_attribute("href"):
        last_link = len(elems)
                
#scrolls to the bottem of the page
count = 0
while done != True:
    driver.execute_script("window.scrollTo(0,Math.max(document.documentElement.scrollHeight," + "document.body.scrollHeight,document.documentElement.clientHeight));")
    time.sleep(1)
    elems = driver.find_elements_by_xpath("//a[@href]")
    print(str(len(elems)) + '    count = '+str(count))

    if len(elems) == count:
        break
    else:
        
        count = len(elems)
    for elem in elems:
        if 'watch' in elem.get_attribute("href"):
            pass
        
print('\n\nDownloading')
#gets all hrefs and only prints if watch in it
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    if 'watch' in elem.get_attribute("href"):
        link_file.write(elem.get_attribute("href"))
        link_file.write('\n')
        #print(elem.get_attribute("href"))




driver.quit()
link_file.close()
