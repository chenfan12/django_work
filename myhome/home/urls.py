from django.urls import path
from.import views as bv

urlpatterns = [
    path('dianying/', bv.dianying),#显示电影信息界面
    path('pcdouban/', bv.pcdouban),#爬取豆瓣页面
    path('baidu/', bv.baidu),#动态操作百度搜索页面
    path('pcjd/', bv.pcjdshouji),#爬取京东手机方法页面
    path('jdshouji/', bv.jdshouji),#显示京东手机信息页面
]