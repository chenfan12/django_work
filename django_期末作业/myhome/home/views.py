from django.shortcuts import render
from django.http import HttpResponse
from . import models
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# Create your views here.

def dianying(request):
    movie = []
    movie=models.movie.objects.all()
    return render(request,'douban250.html',{'movies':movie})

def pcdouban(request):
    movie_list = []
    moviedata_list=[] 
    for i in range(0,10):
        link = 'https://movie.douban.com/top250?start=' + str(i*25)
        r = requests.get(link,timeout=10)
        soup = BeautifulSoup(r.text,"lxml")
        div_list = soup.find_all('div',class_='hd')
        div_list2 = soup.find_all('div',class_='bd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
        for each in div_list2:
            moviedata = each.p.text.strip()             
            moviedata_list.append(moviedata)
        moviedata_list.remove('豆瓣')
    for i in range(len(movie_list)):
        movie = movie_list[i]
        moviedata = moviedata_list[i]
        models.movie.objects.create(movie_name=movie,movie_data=moviedata)
    
    return render(request,'pachong.html',{'a':"豆瓣top250爬取完毕！"})

def baidu(request):
    b=[]
    a=['华为','苹果','魅族','小米']
    driver = webdriver.Chrome()
    url = "https://www.baidu.com/"
    driver.get(url)
    for i in range(len(a)):
        sousuo = driver.find_element_by_id("kw")
        sousuo.clear()
        sousuo.send_keys(a[i])
        driver.find_element_by_id("su").click()
        time.sleep(3)
        jg = driver.find_element_by_css_selector("div.nums")
        jg2 = jg.find_element_by_tag_name("span").text  
        b.append(jg2)
        driver.back()
    driver.quit()
    return render(request,'baidu.html',{'jieguo':b,'key':a})

def pcjdshouji(request):
    driver=webdriver.Chrome()
    driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8')
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    b=[]
    d=[]
    a=driver.find_elements_by_xpath('//div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]/a/em')
    c=driver.find_elements_by_xpath('//div[@class="gl-i-wrap"]/div[@class="p-price"]/strong/i')
    for i in range(len(a)):
        b.append(a[i].text)
    for i in range(len(c)):
        d.append(c[i].text)
    driver.close()
    for i in range(len(b)):
        models.phone.objects.create(phone_name=b[i],phone_price=d[i])
    return render(request,'pachong.html',{'a':'京东手机爬取完毕！'})

def jdshouji(request):
    phone = []
    phone=models.phone.objects.all()
    return render(request,'JDshouji.html',{'phones':phone})

def login12306(request):
    driver=webdriver.Chrome()
    driver.get('https://kyfw.12306.cn/otn/resources/login.html')
    time.sleep(1)
    driver.find_element_by_link_text("账号登录").click()
    username = driver.find_element_by_id("J-userName")
    username.clear()
    username.send_keys("18368767575")
    password = driver.find_element_by_id("J-password")
    password.clear()
    password.send_keys("chenfan12")
    time.sleep(5)
    driver.find_element_by_link_text("立即登录").click()
    time.sleep(5)   
    return render(request,'pachong.html',{'a':'登录成功!'})