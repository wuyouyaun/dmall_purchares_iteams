import requests
from case.DF_project.df_testlogin import DF_Login
import os

from nb_log import LogManager
from nb_log_config import LOG_PATH

logger = LogManager("api").get_logger_and_add_handlers(is_add_stream_handler=True,
                                                       log_filename="api.log",
                                                       log_path=LOG_PATH
                                                        )


def insert_source_group(s):
    '''
    新增二级课组
    :param s:
    :return:
    '''
    url = "https://testware-partner.dmall.com.hk/purchase/insert"
    headers = {
        "Referer": "https://testpartner.dmall.com.hk/",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarymtihAXjI7bkLcUsc"


               }
    body = {
        "name": "柬埔寨货架04",
        "code": "JPZ-01",
        "status": "1",
        "parenId": "753911",
        "localeInfo": '{"en_US":"{}"}',
        "level" : 2
        }

    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r


def get_query_ware(s):
    '''
    商品管理列表查询
    :param s:
    :return:
    '''
    url = "https://testware-partner.dmall.com.hk//waremanager/queryware"
    headers = {
        "Referer": "https://testpartner.dmall.com.hk/",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarymtihAXjI7bkLcUsc"
               }
    body={
            "rfIds": "",
            "skuIds": "",
            "itemNums": "",
            "sapTitle": ""
            }

    r=s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def add_commmodity(s):
    '''
    新增商品
    :param s:
    :return:
    '''
    url = "https://testware-partner.dmall.com.hk//wareInfo/addOrUpdate/add"
    headers = {
        "Origin": "https://testpartner.dmall.com.hk",
        "Referer": "https://testpartner.dmall.com.hk/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
               }
    body = {
            'wareStr':
                   '{"wareId":null,"rfId":"柬埔寨商家-01","wareType":"PTSP","specType":"0","venderId":10039,"basicInfo":{"sapTitle":"柬埔寨-香蕉","produceArea":"深圳","thirdCatId":"11341","weight":"0","matkl":"001","mwskz":"0.17","mwskzName":"1","unit":"EA","estiamteType":"1001","brandId":"28741","storageType":"1","wareLife":"","purchaseReceiveRadio":"","warningShelfLife":"","factorySite":"","telephone":"","canFillManufactureDate":"0","eattingType":"","materialDetail":"","specQty":"","specUnit":"","manufacturer":"","chine":"吨"},"multiWareInfo":[],"warePackageInfo":[{"warePackageUnit":"EA","warePackageRatio":1,"warePackageName":"吨"}],"wareItemNumInfo":[{"packageUnit":"EA","ratio":1,"wareItemNumEAN":"柬埔寨商家-01","wareItemNumMain":1}],"delMultiWareInfoIds":[],"delWarePackageInfoIds":[],"delWareItemNumInfoIds":[],"localeInfo":"{\'en_US\':\'{}\'}"}'
                }

    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.json())
    print(s.cookies)
    return r.json()


def select_commodity_info(s):
    '''
    查询商品信息接口
    :param s:  rfId(商品商家编码)  , venderId(商家id)
    :return:
    '''
    url = "https://testware-partner.dmall.com.hk//wareInfo/selectOne"
    headers = {
        "Referer": "https://testpartner.dmall.com.hk/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
               }
    body = {
            "rfId": 666660,
            "venderId": 10039

            }
    r=s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def update_commodity_info(s):
    '''
    修改商品信息
    :return:
    '''
    url="https://testware-partner.dmall.com.hk//wareInfo/addOrUpdate/update"
    headers = {
        "Referer": "https://testpartner.dmall.com.hk/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
               }
    body={

        "wareStr": '{"wareId":100822302,"rfId":"666660","wareType":"PTSP","specType":0,"venderId":10039,'
                  '"basicInfo":{"sapTitle":"柬埔寨商品123","produceArea":"深圳","thirdCatId":11341,'
                  '"weight":0,"matkl":"001","mwskz":"0.17","mwskzName":"1","unit":"EA","estiamteType":"1001",'
                  '"brandId":28741,"storageType":1,"wareLife":null,"purchaseReceiveRadio":null,"warningShelfLife":null,'
                  '"factorySite":"","telephone":"","canFillManufactureDate":0,"eattingType":"","materialDetail":"",'
                  '"specQty":"","specUnit":"","manufacturer":"","chine":"吨"},"multiWareInfo":[],'
                  '"warePackageInfo":[{"id":1364834,"warePackageUnit":"EA","warePackageRatio":1,'
                  '"warePackageWeight":null,'
                  '"warePackageLength":null,"warePackageWidth":null,"warePackageHeight":null,'
                  '"warePackageCubage":null,"warePackageName":"1"}],'
                  '"wareItemNumInfo":[{"id":21930962,"packageUnit":"EA","ratio":1,"wareItemNumEAN":"666660",'
                  '"wareItemNumMain":1}],'
                  '"delMultiWareInfoIds":[],"delWarePackageInfoIds":[],"delWareItemNumInfoIds":[],'
                  '"localeInfo":"{\'en_US\':\'{}\'}"}'}
    r=s.post(url, data=body, headers=headers, verify=False)
    print(r.json())
    logger.debug("返回日志： %s" % r.json())
    return r.json()


def query_list_shelves(s):
    '''
    货架组列表查询
    :return:
    '''
    url="https://testware-partner.dmall.com.hk/shelfgrouplevel/query/list"
    headers = {
        "Referer": "https://testpartner.dmall.com.hk/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
               }

    body={
        "pageSize": "10",
        "currentPage": "1"
        }
    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志： %s" % r.json())


def add_shelves(s):
    '''
    货架组新增
    :return:
    '''
    url = "https://testware-partner.dmall.com.hk/shelfgrouplevel/add"
    headers = {
        "Referer": "https://testpartner.dmall.com.hk/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
               }

    body = {
            "name": "柬埔寨测试03",
            "code": "code",
            "venderId": "10039",
            "purchaseCatId": "",
            "repetition": "0",
            "localeInfo": "{'en_US':'{}'}"
            }
    r=s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r.json()


def delete_shelves(s):
    """
    货架组移除
    :return:
    """
    url="https://testware-partner.dmall.com.hk/shelfgrouplevel/delete/81"
    body={
        "": ""
    }
    headers={
        "Referer": "https://testpartner.dmall.com.hk/"
        }
    r = s.post(url, headers=headers, data=body, verify=False)
    print(r.json())
    logger.debug("返回日志： %s" % r.json())
    return r.json()


def update_shelves(s):
    '''
    修改货架组信息
    :return:
    '''
    url="https://testware-partner.dmall.com.hk/shelfgrouplevel/update"
    headers = {
        "Referer": "https://testpartner.dmall.com.hk/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
               }

    body = {
            "name": "柬埔寨测试03",
            "code": "code",
            "venderId": "10039",
            "purchaseCatId": "",
            "repetition": "0",
            "localeInfo": "{'en_US':'{}'}"
            }
    r=s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志： %s"% r.json())
    return r.json()

def query_shelves(s):
    '''
    查看货架组信息
    :return:
    '''
    url="https://testware-partner.dmall.com.hk/shelfgrouplevel/query/77?_=1602776678508"
    headers={
        "Referer": "https://testpartner.dmall.com.hk/"
        }
    r=s.get(url, verify=False)
    logger.debug("返回日志： %s"% r.json())
    print(r.json())


def query_shelfgrouplevel(s):
    '''
    货架组级门店管理列表查询
    :return:
    '''
    url="https://testware-partner.dmall.com.hk/shelfgrouplevel/query/list"
    body={
            "code": "",
            "name": "",
            "purchaseCatId": "",
            "pageSize": "10",
            "currentPage": "1"
            }
    headers = {
        "Referer": "https://testpartner.dmall.com.hk/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
               }

    r=s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志： %s"% r.json())


def relate_shelfgrouplevel(s):
    '''
    关联门店
    :return:
    '''
    url = "https://testware-partner.dmall.com.hk/shelfgrouplevel/shop"
    body = {
            "id": "82",
            "code": "code",
            "name": "柬埔寨测试03",
            "venderId": "10039",
            "stores[0][code]": "107536",
            "stores[0][value]": "jpz-01    柬埔寨--门店01",
            "shops[0].id": "107536"

      }
    headers = {
        "Referer": "https://testpartner.dmall.com.hk/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
               }
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r.json()







def import_ware(s):
    '''
    货架组级--商品数据导入
    :return:
    '''

    real_path = os.path.dirname(os.path.realpath(__file__))
    print(real_path)

    cur_path = os.path.join(real_path, "shelfGroupLevelWare.xlsx")
    print(cur_path)

    url= "https://testware-partner.dmall.com.hk/shelfgrouplevel/importware"
    headers={
        "Referer": "https://testpartner.dmall.com.hk/"}
    f = {
       "file": ("shelfGroupLevelWare.xlsx", open(cur_path, "rb"), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    }

    r=s.post(url, headers=headers, files=f, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()





if __name__== "__main__":
    s = requests.session()
    DF_Login(s)
    get_query_ware(s)
    # add_commmodity(s)
    #
    # select_commodity_info(s)
    # update_commodity_info(s)
    # query_list_shelves(s)
    # add_shelves(s)
    # delete_shelves(s)
    # update_shelves(s)
    # query_shelves(s)
    # query_shelfgrouplevel(s)
    # relate_shelfgrouplevel(s)
    # import_ware(s)