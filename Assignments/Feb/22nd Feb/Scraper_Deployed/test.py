from flask import Flask, jsonify, render_template, request
from flask_cors import CORS,cross_origin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
 
app = Flask(__name__)
app.debug = True

@app.route("/")
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route("/review",methods=['POST','GET'])
@cross_origin()
def resultsPage():
    searchstring = request.form['content'] + '/videos'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(searchstring)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 1000)")
    time.sleep(3) 

    links = driver.find_elements(By.ID, "video-title-link")
    thumbnails = driver.find_elements(By.XPATH, '//a[@id="thumbnail"]/yt-image/img')
    titles = driver.find_elements(By.ID, "video-title")
    views = driver.find_elements(By.XPATH,'//div[@id="metadata-line"]/span[1]')
    time_period = driver.find_elements(By.XPATH,'//div[@id="metadata-line"]/span[2]')

    links_list = []
    for link in links[0:5]:
        links_list.append(link.get_attribute('href'))


    thumb_list = []
    for thumb in thumbnails[0:5]:
        thumb_list.append(thumb.get_attribute('src'))


    titles_list = []
    for title in titles[0:5]:
        titles_list.append(title.text.encode("UTF-8"))


    views_list = []
    for view in views[0:5]:
        views_list.append(view.text.encode("UTF-8"))


    time_list = []
    for i in time_period[0:5]:
        time_list.append(i.text.encode("UTF-8"))

    return render_template('results.html',a=links_list, b=thumb_list, c=titles_list, d=views_list, e=time_list)




if __name__=="__main__":
    app.run()
