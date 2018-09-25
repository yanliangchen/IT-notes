from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from myweb.models import Types,Goods,Users,Orders,Detail
import time


#公共信息加载函数
def loadinfo():
    context={}
    context['type0list'] = Types.objects.filter(pid=0)
    return context

#个人中心
def personal(request):
	user = Users.objects.get(username=request.session['user']['username'])
	context = {'users':user}
	return render(request,'myweb/personal.html',context)

#打开会员编辑表单
def peredit(request):
	try:
		ob = Users.objects.get(username=request.session['user']['username'])
		context = {'user':ob}
		return render(request,"myweb/peredit.html",context)
	except:
		context = {'info':'没有找到要修改的信息'}
	return render(request,"myweb/info.html",context)

#执行会员编辑操作
def perupdate(request):
    try:
        ob = Users.objects.get(username=request.session['user']['username'])
        ob.name = request.POST['name']
        ob.address = request.POST['address']
        ob.username = request.POST['username']
        ob.code = request.POST['code']
        ob.sex = request.POST['sex']
        ob.email = request.POST['email']
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}
    return render(request,"myweb/info.html",context)
#购物车
def shopcart(request):
    context = loadinfo()
    if 'shoplist' not in request.session:
    	request.session['shoplist']={}
    return render(request,"myweb/shopcart.html",context)

#购物车的添加
def addshopcart(request,sid):
	#获取要放入购物车中的商品信息
    goods = Goods.objects.get(id=sid)
    shop = goods.dePosit();
    print(shop)
    shop['m'] = int(request.POST['m'])
    #从session获取购物车信息
    if 'shoplist' in request.session:
        shoplist = request.session['shoplist']
    else:
        shoplist = {}
    #判断商品是否在购物车中
    if sid in shoplist:
        #商品数量加一
        shoplist[sid]['m']+=shop['m']
    else:
        #新商品添加
        shoplist[sid]=shop

    #将购物车信息放回到session
    request.session['shoplist'] = shoplist
    return redirect(reverse('shopcart'))

#购物车数量的改变
def changeshopcart(request):
    context = loadinfo()
    shoplist = request.session['shoplist']
    shopid = request.GET['sid']
    num = int(request.GET['num'])
    if num < 1:
        num = 1
    shoplist[shopid]['m'] = num
    request.session['shoplist'] = shoplist
    return render(request,"myweb/shopcart.html",context)

#购物车的删除
def delshopcart(request,sid):
    shoplist = request.session['shoplist']
    del shoplist[sid]
    request.session['shoplist'] = shoplist
    # 跳转登录页面（url地址改变）
    return redirect(reverse('shopcart'))

#购物车的清空
def clearshopcart(request):
    shoplist = request.session['shoplist']
    
    request.session['shoplist'] = {}
    # 跳转登录页面（url地址改变）
    return redirect(reverse('shopcart'))
	
#我的订单
def myorder(request):
    #获取要结账的商品信息
    ids = request.GET['gids']
    if ids == '':
        return HttpResponse("请选择要结账的信息")
    gids = ids.split(',')
    #获取购物车中的商品信息
    shoplist = request.session['shoplist']
    #封装要结账的商品及累计总金额
    orderlist = {}
    total = 0
    for sid in gids:
        orderlist[sid] = shoplist[sid]
        total += shoplist[sid]['price']*shoplist[sid]['m']
    request.session['orderlist'] = orderlist
    request.session['total'] = total
    return render(request,"myweb/myorder.html")

#订单确认页
def myorderaffirm(request):
    request.session['user']['ordername'] = request.POST['name']
    request.session['user']['phone'] = request.POST['phone']
    request.session['user']['code'] = request.POST['code']
    request.session['user']['address'] = request.POST['address']
    return render(request,"myweb/myorderaffirm.html")

#执行订单添加
def myorderadd(request):
    # 封装订单信息，并执行添加
    orders = Orders()
    orders.uid = request.session['user']['id']
    orders.linkman = request.POST['linkman']
    orders.address = request.POST['address']
    orders.code = request.POST['code']
    orders.phone = request.POST['phone']
    orders.addtime = time.time()
    orders.total = request.session['total']
    orders.status = 0
    orders.save()
    #获取订单详情
    orderlist = request.session['orderlist']
    shoplist = request.session['shoplist']
    #遍历订单信息,添加订单信息
    for shop in orderlist.values():
        # print(shop)
        del shoplist[str(shop['id'])]
        detail = Detail()
        detail.orderid = orders.id
        detail.goodsid = shop['id']
        detail.name = shop['goods']
        detail.price = shop['price']
        detail.num = shop['m']
        detail.save()
    #删除用户存在session中的值
    del request.session['orderlist']
    del request.session['total']
    request.session['shoplist'] = shoplist
    # return HttpResponse("订单成功:订单id号:"+str(orders.id))
    return redirect(reverse('indent'))

#订单信息显示页面
def indent(request): 
    context = loadinfo()
    #从session中获取登陆者的id号,并且从订单表orders中获取当前用户的所用订单
    orders = Orders.objects.filter(uid=request.session['user']['id'])
    #遍历当前用户的所有订单属性,并获得对应的订单详情信息
    for order in orders:
        dlist = Detail.objects.filter(orderid=order.id)
        order.detail_list = dlist
        #追加1图片信息
        for detail in dlist: 
            goods = Goods.objects.get(id=detail.goodsid)
            detail.picname = goods.picname
    context['orders'] = orders
    context['dlist'] = dlist
    return render(request,"myweb/indent.html",context)

#取消订单
def indentdel(request,oid):
   
    ob = Orders.objects.get(id=oid)
    ob.status = request.POST['status']
    ob.save()   
    return redirect(reverse('indent'))



    # pass



    