# coding:utf-8
import requests
from case.DF_project.df_testlogin import DF_Login
import os

from nb_log import LogManager
from nb_log_config import LOG_PATH

logger = LogManager("api").get_logger_and_add_handlers(is_add_stream_handler=True,
                                                       log_filename="api.log",
                                                       log_path=LOG_PATH
                                                        )

def purchases_information_list(s):
    '''
    采购信息管理列表查询
    :return:
    '''

    url = "https://testpurchases-partner.dmall.com.hk/cx/purchases/goods/list"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "https://testpartner.dmall.com.hk/"
        }
    body = {
            "form_data": '{"yn":1,"page":1,"pageSize":20}'
            }
    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r.json()


def load_down_template(s):
    '''
    采购信息模板下载
    :return:
    '''
    url="https://testpurchases-partner.dmall.com.hk/cx/purchases/goods/template"
    headers = {
        "Referer": "https://testpartner.dmall.com.hk/"
        }
    r = s.get(url, headers=headers)
    logger.debug("返回日志： %s" % r)
    return r



def export_purchases(s):
    '''
    导出采购信息数据
    :return:
    '''
    url="https://testpurchases-partner.dmall.com.hk/cx/purchases/goods/export"
    body={
            "form_data":'{"yn":1}'
    }
    headers={
    "Referer": "https://testpartner.dmall.com.hk/"
            }
    r=s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r.json()


def import_purchases(s):
    '''
    导入采购信息模板
    :return:
    '''
    real_path = os.path.dirname(os.path.realpath(__file__))
    cur_path = os.path.join(real_path, "cgxx.xlsx")
    url = "https://testpurchases-partner.dmall.com.hk/cx/purchases/goods/import"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"

            }
    f = {
        "file": ("cgxx.xlsx", open(cur_path, "rb"), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    }

    r=s.post(url, headers=headers, files=f,verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()

def add_purchasing_information(s):
    '''
    新增采购信息
    :return:
    '''

    url="https://testpurchases-partner.dmall.com.hk/cx/purchases/goods/addSave"
    headers={
            "Referer": "https://testpartner.dmall.com.hk/"

            }
    body={
        "form_data": '{"purchaseUnit":{"superMarket":"EA","market":"EA","store":"EA"},'
                     '"shopType":0,"supplierCode":"888880","supplierName":"柬埔寨001",'
                     '"bizType":1,"goodsCode":"666660","skuId":101301591,"goodsName":"柬埔寨商品123",'
                     '"baseUnit":"EA","withTaxPrice":"22","moq":"1"}'

        }
    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s"% r.json())
    return r.json()



def price_bill_details(s):
    '''
    查看历史变价单
    :param s:
    :return:
    '''

    url = "https://testpurchases-partner.dmall.com.hk/cx/price/bill/details"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"

            }
    body = {
          "form_data": '{"goodsCodes":"072202","supplierCodes":"CambodiaCard","page":1,"pageSize":20}'
    }
    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志： %s" % r.json())



def shop_purchases_list(s):
    '''
    门店货源管理列表查询
    :return:
    '''

    url = "https://testpurchases-partner.dmall.com.hk/cx/purchases/shop/list"
    body = {
        "form_data": '{"yn":1,"page":1,"pageSize":20}'
            }

    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"

            }
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志： %s" % r.json())


def load_shop_template(s):
    '''
    门店货源模板下载
    :return:
    '''

    url = "https://testpurchases-partner.dmall.com.hk/cx/purchases/shop/template"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"

            }
    r = s.get(url, headers=headers, verify=False)
    logger.debug("返回日志： %s" % r.json())


def export_param(s):
    '''
    导出门店货源列表数据
    :return:
    '''
    url = "https://testpurchases-partner.dmall.com.hk/cx/purchases/shop/initExportParam"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"

            }
    body = {
        "form_data": '{"yn":1}'

    }
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r


def import_good_puchase(s):
    '''
    门店货源模板数据导入
    :return:
    '''
    real_path=os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(real_path, "shop_purchase.xlsx")

    url = "https://testpurchases-partner.dmall.com.hk/cx/purchases/shop/import"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
    }
    f = {
        "file": ("shop_purchase.xlsx", open(path, "rb"),"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

            }

    r = s.post(url, headers=headers, files=f, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r


def add_purchase_shop(s):
    '''
    新增货源信息
    :return:
    '''
    url="https://testpurchases-partner.dmall.com.hk/cx/purchases/shop/saveOrUpdate"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
    }
    body={
        "form_data": '{"deliveryType":2,"storeId":"","shopName":"柬埔寨--门店01","skuId":101301591,'
                     '"goodsName":"柬埔寨商品123","supplierCode":"888880","supplierName":"柬埔寨001",'
                     '"goodsCode":"666660","shopCode":"jpz-01","deliveryTypeStr":null}'

        }
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r


def cat_shop_list(s):
    '''
    查看货源管理信息详情
    :return:
    '''

    url = "https://testpurchases-partner.dmall.com.hk/cx/purchases/shop/list"
    body = {
        "form_data":'{"yn":1,"page":1,"pageSize":20}'


    }
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
    }
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志： %s" % r.json())


def price_bill_list(s):
    '''
    变价单查询
    :return:
    '''
    url = "https://testpurchases-partner.dmall.com.hk/cx/price/bill/list"
    body = {
            "form_data": '{"promotion":0,"page":1,"pageSize":20}'

            }
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
    }

    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r.json()


def load_price_template(s):
    '''
    编辑单模板下载
    :return:
    '''
    url = "https://testpurchases-partner.dmall.com.hk/cx/price/bill/template"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
    }
    r = s.get(url, headers=headers, verify=False)
    logger.debug("返回日志： %s" % r)
    return r


def price_bill_detail(s):
    '''
    变价单详情查看
    :return:
    '''

    url = "https://testpurchases-partner.dmall.com.hk/cx/price/bill/details"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
                }
    body={
            "form_data": '{"billNos":"CP20102000000000","page":1,"pageSize":20}'

            }

    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志： %s" % r.json())




def cancel_Bill_price(s):
    '''
    取消变价单
    :param s:
    :return:
    '''
    url = "https://testpurchases-partner.dmall.com.hk/cx/price/bill/cancelBill"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
                }
    body={
        "form_data": '{"billNo":"CP20101900000003"}'
         }

    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r.json()


def create_price_bill(s):
    '''
    新增变价单
    :return:
    '''
    url = "https://testpurchases-partner.dmall.com.hk/cx/price/bill/create"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
                }
    body = {
        "form_data": '{"details":[{"goodsCode":"666660","goodsName":"柬埔寨商品123",'
                     '"supplierCode":"909090","supplierName":"深圳大源源呐999",'
                     '"lastWithTaxPrice":12,"withTaxPrice":"55","edit":true,'
                     '"csvMessage":null}],"billName":"柬埔寨_测试01","startDate":"2020-10-20"}'
                     }
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r.json()


def load_promotion_template(s):
    '''
    促销变价单模板下载
    :return:
    '''
    url="https://testpurchases-partner.dmall.com.hk/cx/price/promotion/template"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
                }
    r=s.get(url, headers=headers, verify=False)
    logger.debug("返回日志： %s" % r)
    return r


def apply_priceBill_list(s):
    '''
    调进价申请单查询
    :return:
    '''
    url = "https://testpurchases-partner.dmall.com.hk/cx/priceBill/apply/list"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
                }
    body={
            "form_data":'{"page":1,"pageSize":20}'
            }

    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r.json()


def view_apply_details(s):
    '''
    查看变价单详情
    :return:
    '''
    url = "https://testpurchases-partner.dmall.com.hk/cx/priceBill/apply/loadByBillNo4Approve"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
                }
    body = {
        "form_data": '{"billNo":"CP20102000000004"}'
        }
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r.json()


def remove_apply_priceBill(s):
    '''
    删除调进价单       # 需配置审批流
    :return:
    '''

    url='https://testpurchases-partner.dmall.com.hk/cx/priceBill/apply/removeByBillNo'
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
                }
    body = {
        "form_data": '{"billNo":"CP20102000000004","procInstId":null}'
    }
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r.json()



def promotionpriceBill_apply(s):
    '''
    促销调进价申请列表查询
    :return:
    '''
    url = "https://testpurchases-partner.dmall.com.hk/cx/promotionPriceBill/apply/list"
    body = {
        "form_data": '{"page":1,"pageSize":20}'

    }
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
                }
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r.json()



def promotionPriceBill_template(s):
    '''
    促销变价单模板下载
    :return:
    '''
    url="https://testpurchases-partner.dmall.com.hk/cx/promotionPriceBill/apply/template"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
                }
    r = s.get(url, headers=headers, verify=False)
    logger.debug("返回日志： %s" % r)
    return r


def Common_GetPriceBill(s):
    '''
    返回促销调进价申请列表页面
    :param s:
    :return:
    '''
    url = "https://testpurchases-partner.dmall.com.hk/cx/common/getPriceBillStatus?_=1603182508805"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
                }
    r = s.get(url, headers=headers, verify=False)
    logger.debug("返回日志： %s" % r.json())
    return r










if __name__ =="__main__":
    s = requests.session()
    DF_Login(s)
    purchases_information_list(s)

    # cancel_Bill_price(s)
    # create_price_bill(s)
    # load_promotion_template(s)
    # apply_priceBill_list(s)
    #
    promotionpriceBill_apply(s)
