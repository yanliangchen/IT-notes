# -*- coding: utf-8 -*-
import scrapy
import  json
import xlwt
import  random
import xlrd
from xlutils.copy import copy

__author__ = 'yanliang'
class PriceSpider(scrapy.Spider):
    name = 'price'
    allowed_domains = ['aliyun.com','alibabacloud.com']
    user_agent = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        "UCWEB7.0.2.37/28/999",
        "NOKIA5700/ UCWEB7.0.2.37/28/999",
        "Openwave/ UCWEB7.0.2.37/28/999",
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
        # iPhone 6：
        "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

    ]
    headers = {
        'User-Agent' : random.choice(user_agent),
        'Referer': 'https://cn.aliyun.com/?accounttraceid=afd39a08-0fa4-468f-ae80-7990aaaf0981',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'Keep-Alive',
    }
    cookies ={
                 'Cookie': 'ping_test=false',
                 't': '1b9683758c8857257a8d79dc1d826fcb',
                 '_tb_token_=5555ee73a786b': 'cookie2=1ed5ad2cc6db6039a0bf0d0a30327e7a',
                 'csg': '38e86df8',
                 'isg': 'BObmTWQ7gf8uTlWkOzfCeSloLlxoxyqBOxqzrtCP0onkU4ZtOVd6kcyqr4_6YCKZ',
                 'aliyun_choice': 'CN',
                 'cna': 'xyn4E48Xem4CATr2kxq99N3q',
                 'login_aliyunid_csrf': '_csrf_tk_1439136033331239',
                 'cnz': 'FfAUFDSUdhUCARqT9jp9gIjN',
                 '_hvn_login': '6',
                 'login_aliyunid': "185****4668",
                 'login_aliyunid_ticket': 'rbIr0v2arVX8XAx4wjEXf6xsB5voPmof_BNpwU_TOTNChZBoeM1KJexdfb9zhYnsN5Zos6qISCrRt7mGxbigG2Cd4fWaCmBZHIzsgdZq64XXWQgyKFeuf0vpmV*s*CT58JlM_1t$w3d6$xZKsznhF*hT0',
                 'login_aliyunid_pk': '1498804704373932',
                 'login_aliyunid_token': "6JBeNJtQxOxUTwDNxW03TH+7BRULA/wQlLY1EIspjRY=",
                 'hssid': '13gaCnpLHQpGIpf2Cq5_Fxg1',
                  'hsite':'6',
                  'aliyun_country':'CN',
                   'aliyun_site':'CN',
                   'aliyun_lang':'zh',
    }
    #first url : ecs price
    start_urls = ['https://g.alicdn.com/aliyun/ecs-price-info/2.0.6/price/download/instancePrice.json?spm=0.6883001.instance.1.fa70gEtGgEtGHW&file=instancePrice.json']
    #second url : ecs expand
    second_urls = 'https://www.alibabacloud.com/help/zh/doc-detail/25378.htm?spm=a2c63.p38356.b99.5.45ff4fbdlz7HDt'
    #third : disk price
    three_urls = 'https://g.alicdn.com/aliyun/ecs-price-info/2.0.6/price/download/diskPrice.json?spm=0.6883001.disk.1.1395dEG4dEG4IG&file=diskPrice.json'
    #foutth : tape width
    fourth_urls = 'https://g.alicdn.com/aliyun/ecs-price-info/2.0.6/price/download/bandWidthPrice.json?spm=0.6883001.band.1.7688urnAurnAgd&file=bandWidthPrice.json'
    def parse(self, response):
        json_uni = response.text
        json_dispose = json.loads(json_uni,encoding='uft-8')
        # 创建excel表格
        self.xls = xlwt.Workbook(encoding='utf-8')
        self.sht1 = self.xls.add_sheet('Sheet1')
        # 添加字段
        self.sht1.write(0, 0, '实例规格')
        self.sht1.write(0, 1, 'vCPU(GB)')
        self.sht1.write(0, 2, '内存(GB)')
        self.sht1.write(0, 3, '本地存储（GiB）*')
        self.sht1.write(0, 4, '网络带宽能力（出/入）（Gbit/s）')
        self.sht1.write(0, 5, '网络收发包能力（出/入）（万PPS）**')
        self.sht1.write(0, 6, '多队列')
        self.sht1.write(0, 7, '弹性网卡（包括一块主网卡） ** **')
        self.sht1.write(0, 13, '地区')
        self.sht1.write(0, 14, '网络')
        self.sht1.write(0, 15, '系统')
        self.sht1.write(0, 16, '优化')
        self.sht1.write(0, 17, '按量(小时)')
        self.sht1.write(0, 18, '月价(月付)')
        self.sht1.write(0, 19, '月价(年付)')
        self.sht1.write(0, 20, '月价(年付)')
        self.sht1.write(0, 21, '月价(3年付)')
        self.sht1.write(0, 22, '月价(4年付)')
        self.sht1.write(0, 23, '月价(5年付)')
        self.sht1.write(0, 8, '平均基准CPU计算性能')
        self.sht1.write(0, 9, '最大CPU积分余额')
        self.sht1.write(0, 10, 'CPU积分/小时')
        self.sht1.write(0, 11, 'GPU')
        self.sht1.write(0, 12, 'FPGA')

        data = json_dispose['pricingInfo']
        #遍历所有实例类型
        ins_region =[]
        '''
        这个是我之前的所有实例的组成的一个列表
        拿下面的去判断是否在里面  如果在里面 那么我取出索引列的索引  之后我给加上我要操作的元素的行索引
        索引都有了  就可以把数据放进去了
        '''
        self.ins_type = []
        ins_net = []
        ins_os = []
        ins_optimized = []

        for  type_ins  in  data:
            #对实例类型进行切割
            sp_ins = type_ins.split('::')
            ins_region.append(sp_ins[0])
            #这个列表我想要索引
            self.ins_type.append(sp_ins[1])
            ins_net.append(sp_ins[2])
            ins_os.append(sp_ins[3])
            ins_optimized.append(sp_ins[4])

        for auto,  ins_re in enumerate(ins_region, start=1):
            self.sht1.write(auto, 13, '{}'.format(ins_re))
        self.xls.save('./ecs_price.xls')
        #实例类型
        self.auto_list = []

        for auto, ins_type in enumerate(self.ins_type, start=1):
            self.auto_list.append(auto)
            self.sht1.write(auto, 0, '{}'.format(ins_type))
        self.xls.save('./ecs_price.xls')

        for auto, ins_net in enumerate(ins_net, start=1):
            self.sht1.write(auto, 14, '{}'.format(ins_net))
        self.xls.save('./ecs_price.xls')

        for auto, ins_os in enumerate(ins_os, start=1):
            self.sht1.write(auto, 15, '{}'.format(ins_os))
        self.xls.save('./ecs_price.xls')

        for auto, ins_optimized in enumerate(ins_optimized, start=1):
            self.sht1.write(auto, 16, '{}'.format(ins_optimized))
        self.xls.save('./ecs_price.xls')

        data = json_dispose['pricingInfo']
        price_hour_list = []
        price_months_list = []
        price_one_year_list =[]
        price_two_year_list =[]
        price_three_year_list =[]
        price_four_year_list =[]
        price_five_year_list =[]

        for k, v in data.items():
            hours = v['hours'][0]['price']
            months = v['months'][0]['price']
            one_year = v['years'][0]['price']
            two_year = v['years'][1]['price']
            three_year = v['years'][2]['price']
            four_year = v['years'][3]['price']
            five_year = v['years'][4]['price']
            price_hour_list.append(hours)
            price_months_list.append(months)
            price_one_year_list.append(one_year)
            price_two_year_list.append(two_year)
            price_three_year_list.append(three_year)
            price_four_year_list.append(four_year)
            price_five_year_list.append(five_year)
        #写的是往这里面遍历的
        for auto, price_hour in enumerate(price_hour_list, start=1):
            self.sht1.write(auto, 17, '{}'.format(price_hour))
        self.xls.save('./ecs_price.xls')

        for auto,  price_months in enumerate(price_months_list, start=1):
            self.sht1.write(auto, 18, '{}'.format(price_months))
        self.xls.save('./ecs_price.xls')

        for auto, price_one_year in enumerate(price_one_year_list, start=1):
            self.sht1.write(auto, 19, '{}'.format(price_one_year))
        self.xls.save('./ecs_price.xls')

        for auto, price_two_year in enumerate(price_two_year_list, start=1):
            self.sht1.write(auto, 20, '{}'.format(price_two_year))
        self.xls.save('./ecs_price.xls')

        for auto, price_three_year in enumerate(price_three_year_list, start=1):
            self.sht1.write(auto, 21, '{}'.format(price_three_year))
        self.xls.save('./ecs_price.xls')

        for auto, price_four_year in enumerate(price_four_year_list, start=1):
            self.sht1.write(auto, 22, '{}'.format(price_four_year))
        self.xls.save('./ecs_price.xls')

        for auto, price_five_year in enumerate(price_five_year_list, start=1):
            self.sht1.write(auto, 23, '{}'.format(price_five_year))
        self.xls.save('./ecs_price.xls')

        yield  scrapy.Request(url=self.second_urls, headers=self.headers, callback=self.parsePage, cookies=self.cookies, dont_filter=True)

    def parsePage(self,response):
        ins_type_xin = response.xpath('//tbody[@class="tbody"]/tr')
        # 每一个tr行
        self.xls = xlwt.Workbook(encoding='utf-8')
        self.sht1 = self.xls.add_sheet('Sheet1')
        old_file = './ecs_price.xls'
        oldWb = xlrd.open_workbook(old_file, formatting_info=True)
        #拷贝原始文件
        newWb = copy(oldWb)
        #原始文件中存在sheet_name=0的文件
        sheet = newWb.get_sheet(0)
        #已经存在的索引的列表
        self.already_index_list = []

        for tr in ins_type_xin:
            # 第二个网站的单个实例的内容
            tds = tr.xpath('.//td/text()').extract()
            '''
            处理数据 如果说不正确的数据却在当前字段里  显然 位置不对 所以需要给他放入到指定字段中
            1. 设置尽可能的条件让他都满足 之后目的得到一个数据 加入到指定字段进去
            2. 把这个数据去写入到别的字段（也就是列里）
            3. 只要通过条件 获取到指定的数据 下面的写入代码其实不管你写多少次数据 索引位置没变 那么多写入几次指定的数据也不存在问题
            4. 总之，通过条件获取到指定的数据，之后变量名不一样，多插入几次
            '''

            #待插入的数据有了  tds[0]为第二个网站的数据的实例类型
            #检测 tds[0] 在第二个列表里的所有元素
            ins_index_all = self.index_find(tds[0], self.ins_type)
            #把插入的数据给加入到nan_list中
            #添加进去的元素的索引组成的列表
            for  index_pos  in  ins_index_all :
                if '%' in tds[-2] :
                    # 平均基准cpu计算性能
                    cpu_average = tds[-2]
                    # 最大CPU积分余额
                    cpu_integration = tds[-3]
                    #cpu积分/小时
                    cpu_integration_hour = tds[-4]
                    #平均基准cpu计算性能
                    sheet.write(index_pos + 1, 8, '{}'.format(cpu_average))
                    #最大CPU积分余额
                    sheet.write(index_pos + 1, 9, '{}'.format(cpu_integration))
                    #CPU积分/小时
                    sheet.write(index_pos + 1, 10, '{}'.format(cpu_integration_hour))

                else:
                    #多队列正常写入
                    cpu_average_n = tds[-2]
                    sheet.write(index_pos + 1, 6, '{}'.format(cpu_average_n))
                    #网络收发包能力正常写入
                    cpu_integration_n = tds[-3]
                    sheet.write(index_pos + 1, 5, '{}'.format(cpu_integration_n))
                    #带宽能力正常写入
                    net_capability = tds[-4]
                    sheet.write(index_pos + 1, 4, '{}'.format(net_capability))

                #解决了* FPGA 的重复
                if  '* AMD ' in  tds[4] or  '* NVIDIA ' in  tds[4]:
                    ins_GPU = tds[4]
                    sheet.write(index_pos + 1, 11,'{}'.format(ins_GPU))
                elif  'GX' in  tds[4] or  'Xilinx ' in  tds[4]:
                    ins_FPGA = tds[4]
                    sheet.write(index_pos + 1, 12,'{}'.format(ins_FPGA))

                #cpu
                sheet.write(index_pos+1, 1, '{}'.format(tds[1]))  # row行，col列，data追加的数据，style数据样式
                #内存
                sheet.write(index_pos+1, 2, '{}'.format(tds[2]))
                if  '%' not in  tds[5]:
                    if tds[3] == u'无':
                        #存空
                        tds[3] = ''
                    else:
                        sheet.write(index_pos + 1, 3, '{}'.format(tds[3]))

                # 弹性网卡
                sheet.write(index_pos + 1, 7, '{}'.format(tds[-1]))
                self.already_index_list.append(index_pos)
        newWb.save('./ecs_price.xls')
        yield  scrapy.Request(url=self.three_urls,callback=self.disk_price,dont_filter=True)

    #磁盘价格
    def  disk_price(self,response):
        book = xlwt.Workbook(encoding='utf-8')
        sheet1 = book.add_sheet('Sheet 1',cell_overwrite_ok=True)
        sheet1.write(0, 0, "地区")
        sheet1.write(0, 1, "类型")
        sheet1.write(0, 2, "系统盘或数据盘")
        sheet1.write(0, 3, "按量价格(￥/1GB/小时)")
        sheet1.write(0, 4, "按量价格(￥/40GB起卖/小时)")
        sheet1.write(0, 5, "价格周(￥/1GB/周)")
        sheet1.write(0, 6, "价格周(￥/40GB起卖/周)")
        sheet1.write(0, 7, "价格月(￥/1GB/月)")
        sheet1.write(0, 8, "价格月(￥/40GB起卖/月)")
        disk_price = response.text
        disk_type_dict = json.loads(disk_price,encoding='utf-8')
        disk_type_dict = disk_type_dict['pricingInfo']
        d_region_list = []
        d_ssd_type_list = []
        sys_or_data_list= []
        '''
        : 目的 ，是为了生成插入数据的 索引
        '''
        #二级列表hours
        d_price_new_list = []
        #二级列表weeks
        d_price_new_weeks_list = []
        #二级列表months
        d_price_new_months_list = []
        #对源数据进行遍历
        for  d_type, d_price in  disk_type_dict.items():
            d_total = d_type.split('::')
            # 地区
            d_region = d_total[0]
            # 硬盘的类型是哪一种 是cloud ? 还是ssd  还是cloud  ssd
            d_ssd_type = d_total[1]
            # 数据盘or 系统盘
            s_d = d_total[2]
            d_region_list.append(d_region)
            d_ssd_type_list.append(d_ssd_type)
            sys_or_data_list.append(s_d)
            '''
            由于每个地区里的数据 有的是40起的 还有 1G的 价格 ，
            所以我要把它分开， 而且还要为插入excel表格数据进行考虑，
            那么我就要把它给做成2及列表，之后通过对应的索引的位置能进行准确的插入 ， 
            那这个时候 ，我就要考虑 ，我加入数据的先后 ，因为当我进行插入数据的时候还要判断 ，
            之后我还要保证二级列表里的每一个列表的索引都有数据 因为我要拿这个40的所在索引做判断，所以必须要让，
            这个40的所在的索引不能为空，否则判断的时候就会list   out  of  index (超出索引范围，导致报错)
            '''
            #hours
            d_price_list = []
            #weeks
            d_price_weeks_list = []
            #months
            d_price_months_list = []
            #因为有40G起/小时的，数据里周和月都有
            if  d_price['hours'][0]['value'] == '40':
                #hours
                d_price_list.append(d_price['hours'][1]['value'])
                d_price_list.append(d_price['hours'][1]['price'])
                d_price_list.append(d_price['hours'][0]['value'])
                d_price_list.append(d_price['hours'][0]['price'])
                d_price_list.append(d_price['hours'][0]['unit'])
                #weeks
                d_price_weeks_list.append(d_price['weeks'][1]['value'])
                d_price_weeks_list.append(d_price['weeks'][1]['price'])
                d_price_weeks_list.append(d_price['weeks'][0]['value'])
                d_price_weeks_list.append(d_price['weeks'][0]['price'])
                d_price_weeks_list.append(d_price['weeks'][0]['unit'])
                #months
                d_price_months_list.append(d_price['months'][1]['value'])
                d_price_months_list.append(d_price['months'][1]['price'])
                d_price_months_list.append(d_price['months'][0]['value'])
                d_price_months_list.append(d_price['months'][0]['price'])
                d_price_months_list.append(d_price['months'][0]['unit'])
            else:
                #hours
                d_price_list.append(d_price['hours'][0]['value'])
                d_price_list.append(d_price['hours'][0]['price'])
                d_price_list.append(d_price['hours'][0]['unit'])
                #weeks
                d_price_weeks_list.append(d_price['weeks'][0]['value'])
                d_price_weeks_list.append(d_price['weeks'][0]['price'])
                d_price_weeks_list.append(d_price['weeks'][0]['unit'])
                #months
                d_price_months_list.append(d_price['months'][0]['value'])
                d_price_months_list.append(d_price['months'][0]['price'])
                d_price_months_list.append(d_price['months'][0]['unit'])

            d_price_new_list.append(d_price_list)
            d_price_new_weeks_list.append(d_price_weeks_list)
            d_price_new_months_list.append(d_price_months_list)

        for  auto , d_months   in  enumerate(d_price_new_months_list,start=1):
            if  d_months[2] == '40':
                fina_month_str = (d_months[1] + u'元/' + d_months[0] + d_months[4] + u'/月').encode('utf-8')
                sheet1.write(auto,7,'{}'.format(fina_month_str))
                try:
                    fina_four_month_str = (d_months[3] + u'元' + d_months[2] + d_months[4] + u'/月').encode('utf-8')
                    sheet1.write(auto,8,'{}'.format(fina_four_month_str))
                except Exception as e:
                    print(e)
            else:
                fina_month_str = (d_months[1] + u'元' + d_months[0] + d_months[2] + u'/月').encode('utf-8')
                sheet1.write(auto, 7, '{}'.format(fina_month_str))

        for  auto, d_weeks in  enumerate(d_price_new_weeks_list,start=1):
            #周40G起的1GB 价格
            if  d_weeks[2] == '40':
                fina_week_str = (d_weeks[1] + u'元/' + d_weeks[0] + d_weeks[4] + u'/周').encode('utf-8')
                sheet1.write(auto, 5, '{}'.format(fina_week_str))
                try:
                    fina_four_week_str = (d_weeks[3] + u'元' + d_weeks[2] + d_weeks[4] + u'/周').encode('utf-8')
                    sheet1.write(auto, 6, '{}'.format(fina_four_week_str))
                except Exception as e:
                    print(e)
            else:
                fina_week_str = (d_weeks[1] + u'元' + d_weeks[0] + d_weeks[2] + u'/周').encode('utf-8')
                sheet1.write(auto, 5, '{}'.format(fina_week_str))

        #小时价格的写入
        for  auto, d_hours in  enumerate(d_price_new_list,start=1):
            if d_hours[2] == '40':
                #小时40G起的1GB 价格
                fina_hour_str = (d_hours[1] + u'元/' + d_hours[0] + d_hours[4] + u'/小时').encode('utf-8')
                sheet1.write(auto, 3, '{}'.format(fina_hour_str))
                #小时40G起的40GB 价格
                try:
                    fina_four_hour_str = (d_hours[3] + u'元/' + d_hours[2] + d_hours[4] + u'/小时').encode('utf-8')
                    sheet1.write(auto, 4, '{}'.format(fina_four_hour_str))
                except Exception as e :
                    print(e)
            else:
                #小时0.00112元1GB/小时
                fina_one_gb_str = (d_hours[1] + u'元/' +d_hours[0] + d_hours[2] + u'/小时').encode('utf-8')
                sheet1.write(auto, 3, '{}'.format(fina_one_gb_str))

        #地区/盘类型/盘/的写入
        for auto,d_r in enumerate(d_region_list, start=1):
            sheet1.write(auto, 0, "{}".format(d_r))

        for  auto,d_s in  enumerate(d_ssd_type_list,start=1):
            if  d_s == 'cloud':
                sheet1.write(auto, 1, u"{}".format(u'普通云盘'))
            elif d_s == 'cloud_ssd':
                sheet1.write(auto, 1, u"{}".format(u'SSD云盘'))
            elif d_s == 'cloud_efficiency':
                sheet1.write(auto, 1, u"{}".format(u'高效云盘'))
            elif  d_s == 'ephemeral':
                sheet1.write(auto, 1, u"{}".format(u"本地盘"))
            elif  d_s =='ephemeral_ssd':
                sheet1.write(auto, 1, u"{}".format(u"本地SSD盘"))

        for  auto, s_d in  enumerate(sys_or_data_list, start=1):
            sheet1.write(auto, 2, "{}".format(s_d))

        book.save(u'block_storage_price.xls')
        yield  scrapy.Request(url=self.fourth_urls, callback=self.tape_width_price, dont_filter=True)


    def  tape_width_price(self,response):
        book = xlwt.Workbook(encoding='utf-8')
        sheet1 = book.add_sheet('Sheet 1', cell_overwrite_ok=True)
        sheet1.write(0, 0, "地区")
        sheet1.write(0, 1, "1-5 Mbps 元/Mbps/小时")
        sheet1.write(0, 2, "6Mbps及以上 元/Mbps/小时")
        sheet1.write(0, 3, "1Mbps 元/Mbps/月")
        sheet1.write(0, 4, "2Mbps 元/Mbps/月")
        sheet1.write(0, 5, "3Mbps 元/Mbps/月")
        sheet1.write(0, 6, "4Mbps 元/Mbps/月")
        sheet1.write(0, 7, "5Mbps 元/Mbps/月")
        sheet1.write(0, 8, "6Mbps及以上 元/Mbps/月")
        sheet1.write(0, 9, "使用量线性计费 元/GB")
        tape_type_dict = json.loads(response.text, encoding='utf-8')
        tape_type_dict = tape_type_dict['pricingInfo']
        t_type_new_list = []
        for  t_type, t_price in  tape_type_dict.items():
            t_region = t_type
            t_type_list = []
            #1Mb hours
            t_type_list.append(t_region)
            t_type_list.append(t_price['hours'][0]['price'])
            t_type_list.append(t_price['hours'][0]['period'])
            #6Mb起
            t_type_list.append(t_price['hours'][1]['price'])
            t_type_list.append(t_price['hours'][1]['period'])
            #1month 取(价钱)  (MB字段)  + (多少)
            t_type_list.append(t_price['months'][0]['price'])
            t_type_list.append(t_price['months'][0]['value'])
            t_type_list.append(t_price['months'][0]['unit'])
            #2months
            t_type_list.append(t_price['months'][1]['price'])
            t_type_list.append(t_price['months'][1]['value'])
            t_type_list.append(t_price['months'][1]['unit'])
            #3months
            t_type_list.append(t_price['months'][2]['price'])
            t_type_list.append(t_price['months'][2]['value'])
            t_type_list.append(t_price['months'][2]['unit'])
            #4months
            t_type_list.append(t_price['months'][3]['price'])
            t_type_list.append(t_price['months'][3]['value'])
            t_type_list.append(t_price['months'][3]['unit'])
            #5months
            t_type_list.append(t_price['months'][4]['price'])
            t_type_list.append(t_price['months'][4]['value'])
            t_type_list.append(t_price['months'][4]['unit'])
            #6months
            t_type_list.append(t_price['months'][5]['price'])
            t_type_list.append(t_price['months'][5]['value'])
            t_type_list.append(t_price['months'][5]['unit'])
            #线性计费
            #价格  取(价钱)  (多少) (单位GB)
            t_type_list.append(t_price['traffic'][0]['price'])
            t_type_list.append(t_price['traffic'][0]['value'])
            t_type_list.append(t_price['traffic'][0]['unit'])
            t_type_new_list.append(t_type_list)

        for  auto, t_data in enumerate(t_type_new_list,start=1):
            sheet1.write(auto, 0, '{}'.format(t_data[0]))
            sheet1.write(auto, 1,' {}'.format(t_data[1]))
            sheet1.write(auto, 2, '{}'.format(t_data[3]))
            sheet1.write(auto, 3, '{}'.format(t_data[5]))
            sheet1.write(auto, 4, '{}'.format(t_data[8]))
            sheet1.write(auto, 5, '{}'.format(t_data[11]))
            sheet1.write(auto, 6, '{}'.format(t_data[14]))
            sheet1.write(auto, 7, '{}'.format(t_data[17]))
            sheet1.write(auto, 8, '{}'.format(t_data[20]))
            sheet1.write(auto, 9, '{}'.format(t_data[23]))
        book.save('./tape_width_price.xls')
        #接着爬取
        yield  scrapy.Request(url='https://www.aliyun.com/price/product?spm=5176.7921785.762131.price4.58ec4100bX3vYv#/oss/detail', callback=self.oss_price, dont_filter=True)

    def oss_price(self,response):
        pass


    def take_the_wrong(self):
        '''
        :return: 获得不存在的索引的列表
        '''
        self.st_one = set(self.auto_list)
        self.st_two = set(self.already_index_list)
        st_res = list(self.st_one - self.st_two)
        return  st_res

    #获取列表的索引
    def index_find(self,x, y):
        '''
        :param x:  type ：str
        :param y:  type : list
        :return:  index  type : list
        '''
        return [a for a in range(len(y)) if y[a] == x]



