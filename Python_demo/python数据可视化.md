# python  pyecharts  数据可视化



###  0. 安装

**摘自https://www.jianshu.com/p/b718c307a61c**

**先安装  python -m pip  install  pyecharts**  

**pyecharts 兼容 Python2 和 Python3。目前版本为 0.1.2**



### 1.  demo1 图表



```
from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.show_config()
bar.render()

//注释
add() 
主要方法，用于添加图表的数据和设置各种配置项
show_config() 
打印输出图表的所有配置项
render() 
默认将会在根目录下生成一个 render.html 的文件，支持 path 参数，设置文件保存位置，如 render(r"e:\my_first_chart.html")，文件用浏览器打开。
默认的编码类型为 UTF-8，在 Python3 中是没什么问题的，Python3 对中文的支持好很多。但是在 Python2 中，编码的处理是个很头疼的问题，暂时没能找到完美的解决方法，目前只能通过文本编辑器自己进行二次编码，我用的是 Visual Studio Code，先通过 Gbk 编码重新打开，然后再用 UTF-8 重新保存，这样用浏览器打开的话就不会出现中文乱码问题了。
基本上所有的图表类型都是这样绘制的：

chart_name = Type() 初始化具体类型图表。
add() 添加数据及配置项。
render() 生成 .html 文件。

作者：chenjiandongx
链接：https://www.jianshu.com/p/b718c307a61c
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```





### demo2 柱状图/条形图

```
from pyecharts import Bar

bar = Bar("标记线和标记点示例")
bar.add("商家A", attr, v1, mark_point=["average"])
bar.add("商家B", attr, v2, mark_line=["min", "max"])
bar.render()



//x轴和y轴交换
from pyecharts import Bar

bar = Bar("x 轴和 y 轴交换")
bar.add("商家A", attr, v1)
bar.add("商家B", attr, v2, is_convert=True)
bar.render()
```





### demo3  带有涟漪效果的动态散点图

```
from pyecharts import EffectScatter

v1 = [10, 20, 30, 40, 50, 60]
v2 = [25, 20, 15, 10, 60, 33]
es = EffectScatter("动态散点图示例")
es.add("effectScatter", v1, v2)
es.render()

作者：chenjiandongx
链接：https://www.jianshu.com/p/b718c307a61c
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```



### demo4  动态散点图各种图形示例 

```
from pyecharts import EffectScatter

v1 = [10, 20, 30, 40, 50, 60]
v2 = [25, 20, 15, 10, 60, 33]
es = EffectScatter("动态散点图示例")
es.add("effectScatter", v1, v2)
es.render()


es = EffectScatter("动态散点图各种图形示例")
es.add("冠华", [10], [10], symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")
es.add("", [20], [20], symbol_size=12, effect_scale=4.5, effect_period=4,symbol="rect")
es.add("", [30], [30], symbol_size=30, effect_scale=5.5, effect_period=5,symbol="roundRect")
es.add("", [40], [40], symbol_size=10, effect_scale=6.5, effect_brushtype='fill',symbol="diamond")
es.add("", [50], [50], symbol_size=16, effect_scale=5.5, effect_period=3,symbol="arrow")
es.add("", [60], [60], symbol_size=6, effect_scale=2.5, effect_period=3,symbol="triangle")
es.render()

```



### demo5  漏斗图

```
from pyecharts import Funnel

attr = ["冠华", "水水", "雪纺衫", "裤子", "高跟鞋", "袜子"]
attra = ["冠华1", "水水2", "雪纺衫3", "裤子4", "高跟鞋5", "袜子6"]
value = [20, 40, 60, 80, 100, 120]
funnel = Funnel("漏斗图示例")
funnel.add("商品", attr, value, is_label_show=True, label_pos="inside", label_text_color="#fff")
funnel.render()
```



### 后面的demo略，需要的时候现翻阅