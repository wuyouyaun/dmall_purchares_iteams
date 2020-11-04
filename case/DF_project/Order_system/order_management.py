import requests
import os
import json

from case.DF_project.df_testlogin import DF_Login
from nb_log import LogManager
from nb_log_config import LOG_PATH

logger = LogManager("api").get_logger_and_add_handlers(is_add_stream_handler=True,
                                                       log_filename="api.log",
                                                       log_path=LOG_PATH
                                                        )


def po_order_list(s):
    '''
    手工订退货（门店）           # 门店下单页面查询      本次订单管理-手工订退货均为（门店）
    :return:
    '''
    url = "https://testpomanage-partner.dmall.com.hk/cx/po/manual/list"
    headers = {
        "Referer": "https://testpartner.dmall.com.hk/"
            }
    body = {
        "form_data": '{"statuses":21,"clients":9,"page":1,"pageSize":20}'
    }
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志: %s" % r.json())
    return r.json()


def po_manual_template(s):
    '''
    手动订退货模板下载
    :return:
    '''
    url = "https://testpomanage-partner.dmall.com.hk/cx/po/manual/template"
    headers = {
        "Referer": "https://testpartner.dmall.com.hk/"
            }
    r = s.get(url, headers=headers)
    logger.debug("返回日志： %s" % r)
    return r


def add_po_manual(s):
    '''
    新增手工订退货（门店） 采购订单
    :return:
    '''

    url = "https://testpomanage-partner.dmall.com.hk/cx/po/manual/add"
    body = {
            "form_data": '{"shopCode":"jpz-01","bizType":0,"items":[{"goodsCode":"666660","goodsName":"柬埔寨商品123",'
                         '"quantity":"88","price":"可缺省","goodsBatchId":"","baseUnit":"","storeId":107536,'
                         '"skuId":101301591,"refundInfo":"","json":{"createId":null,"created":null,"yn":null,'
                         '"updateId":null,"modified":null,"mart":null,"_id":null,"id":null,"itemId":null,'
                         '"modelName":null,"targetQuantity":null,"reorderQuantity":null,"roundValue":null,'
                         '"stock":0,"unconfirmStock":0,"onwayStock":0,"avgSales":null,"weekAvgSales":null,'
                         '"unreceive":0,"actualUnreceive":null,"minDisplay":null,"yesterdayQty":null,'
                         '"dms":null,"minOrderQuantity":null,"actualStock":null,"reviewReason":null},'
                         '"unitTaxCost":"","amount":"1056.0000","orderNumerator":1,"realGoodsCode":"666660",'
                         '"deliveryType":2,"deliveryTypeStr":"直送","bizType":0,"shopGoods":{"shopCode":"jpz-01",'
                         '"goodsCode":"666660","storeId":107536,"skuId":101301591,"specifySupplierCode":null,'
                         '"shopName":"柬埔寨--门店01","goodsName":"柬埔寨商品123","goodsType":0,"deliveryType":2,'
                         '"supplierCode":"888880","supplierName":"柬埔寨001","orderUnit":"EA","purchaseUnit":"EA",'
                         '"outSupplierCode":"888880","outSupplierName":"柬埔寨001","minDisplay":null,"maxDisplay":null,'
                         '"storageAdd":null,"loadAdd":null,"statusCn":"1","status":15,"cateId":null,'
                         '"categoryCode0":"001",'
                         '"categoryCode1":"1001","categoryCode2":"001","baseUnit":"EA","ctrlBit":null,'
                         '"statusCode":null,'
                         '"yn":1},"supplierCode":"888880","withTaxPrice":"12","unit":"EA"}],"clients":9}'
                            }
    headers = {
        "Referer": "https://testpartner.dmall.com.hk/"

            }
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r.json()


def delete_po_manual(s):
    '''
    删除采购订单
    :return:
    '''
    ids = po_order_list(s)['data']['data'][0]['id']
    print("!!!!!!!!!!!", ids)
    body1 = {"clients": 9,"ids": [ids]}
    print("@@@@@", body1)#{'clients': 9, 'ids': 1702}#这儿有3个空格，  这里是否可以用split将空格去掉！
    body3 = str(body1)
    body11 = body3.replace(" ", "")
    print("%%%%%%%%%%%%%%%%%%", body11)#{'clients':9,'ids':1702}
    body12 = json.dumps(body11)
    print("sssssssss", body12)

    url = "https://testpomanage-partner.dmall.com.hk/cx/po/manual/delete"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "https://testpartner.dmall.com.hk/",
        "Origin": "https://testpartner.dmall.com.hk"
        }

    body = {"form_data": body12} # 去掉了空格，没有+号出现 form_data=%7B%27clients%27%3A9%2C%27ids%27%3A1702%7D
    # body = {'form_data': "{'clients': 9, 'ids': 1702}"}

    # body = {
    #     "form_data": '{"statuses":21,"clients":9,"page":1,"pageSize":20}'
    # }

    print("------------------",body)
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r.json()


if __name__ == "__main__":
    s = requests.session()
    DF_Login(s)
    add_po_manual(s)
    # delete_po_manual(s)
    # # po_order_list(s)
    #
    # po_list1 = str(po_order_list(s)['data']['data'][0]['id'])
    # print(type(po_list1))
    #
    # print(po_list1)
    # ids = str(po_order_list(s)['data']['data'][0]['id'])
    # body1 = {"clients": 9, "ids": [ids]}
    # print(body1)


    aa = {"form_data":{'clients':9,'ids':[1711]}}
    print(type(aa))
    b=json.dumps(aa)
    print(b)


























