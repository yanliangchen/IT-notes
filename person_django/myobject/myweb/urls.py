from django.conf.urls import url
from . import views,vieworder

urlpatterns = [

    #前台页面
    url(r'^$', views.index,name="index"),
    url(r'^rankindex$',views.indexrank,name="indexrank"),
    url(r'^list$', views.list,name="list"),
    url(r'^detail/(?P<gid>[0-9]+)$', views.detail,name="detail"),

    #登陆注册页面的路由
    #跳转登陆页面
    url(r'^login$', views.login,name="login"),
    url(r'^dologin$',views.dologin,name="dologin"),
    url(r'^logout$',views.logout,name="logout"),
    url(r'^register$', views.register,name="register"),
    url(r'^doregister$', views.doregister,name="doregister"),

    #购物车页面
    url(r'^shopcart$', vieworder.shopcart,name="shopcart"),
    url(r'^addshopcart/(?P<sid>[0-9]+)$',vieworder.addshopcart,name="addshopcart"),
    url(r'^changeshopcart$',vieworder.changeshopcart,name="changeshopcart"),
    url(r'^delshopcart/(?P<sid>[0-9]+)$',vieworder.delshopcart,name="delshopcart"),
    url(r'^clearshopcart$',vieworder.clearshopcart,name="clearshopcart"),


    #个人中心页面路由
    url(r'^personal$', vieworder.personal,name="personal"),
    url(r'^peredit$',vieworder.peredit,name="peredit"),
    url(r'^perupdate$',vieworder.perupdate,name="perupdate"),

    #我的订单路由
    #访问订单表单页
    url(r'^myorder$', vieworder.myorder,name="myorder"),
    #订单信息确认
    url(r'^myorderaffirm$',vieworder.myorderaffirm,name="myorderaffirm"),
    #订单信息添加
    url(r'^myorderadd$',vieworder.myorderadd,name="myorderadd"),

    #我的订单
    url(r'^indent$',vieworder.indent,name="indent"),
    #取消订单
    url(r'^indentdel/(?P<oid>[0-9]+)$',vieworder.indentdel,name="indentdel"),







]
