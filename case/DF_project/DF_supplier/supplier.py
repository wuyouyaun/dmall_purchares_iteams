# coding:utf-8
import requests
import pytest
from case.DF_project.df_testlogin import DF_Login
from nb_log import LogManager
from nb_log_config import LOG_PATH
import json
import os
import shutil

logger = LogManager("api").get_logger_and_add_handlers(is_add_stream_handler=True,
                                                       log_filename="api.log",
                                                       log_path=LOG_PATH
                                                        )


# companyName公司名称不能為空    'basicAccount': '銀行基本戶帳號不能為空', 'taxpayerNumber': '納稅識別號不能為空' 'bankAccountName': '銀行開戶名不能為空'
def save_supplier_information(s, taxpayerType="Z1", companyName="深圳大源源呐939", legalPeople="大源源",
                                    companyAddress="2222", taxpayerNumber="111111111111111", bankCode="1111111111",
                                    simpleName="11111", basicAccount="11111111111",
                                    bankName="建行",bankAccountName="建行西丽分行"):

    '''
    新增公司信息档案               #  taxpayerType 纳税类型    # companyName  公司名称   #  legalPeople 法人   # companyAddress 公司地址
                                   #   taxpayerNumber 纳税人识别号    # bankCode 支行联行号  # simpleName  公司简称  # 公司联系人和公司联系人手机号非空
    :return: r                     #   basicAccount   银行账号     # bankName 开户银行   #  bankAccountName  開戶銀行名
    '''

    data = {"taxpayerType": taxpayerType, "companyName": companyName, "legalPeople": legalPeople,
            "companyAddress": companyAddress, "taxpayerNumber": taxpayerNumber, "bankCode": bankCode,
            "simpleName": simpleName, "basicAccount": basicAccount,
            "bankName": bankName, "bankAccountName": bankAccountName, "mainName": "22222", "mainPhone": "18571519920"}

    datas = json.dumps(data)       # 将字典转换成json

    url = "https://testdf-vc-supplier.dmall.com.hk/cx/company/save"
    headers = {"Referer": "https://testpartner.dmall.com.hk/"}
    body = {
          "form_data": datas

            }
    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.text)
    return r.json()


def check_supplier_information(s):
    '''
    公司信息档案详情
    :param s: id
    :return: r.json()
    '''
    common = save_supplier_information(s)['data']
    data = {"id": common}
    datas = str(data)
    body11 = datas.replace(" ", "")
    print("---------", body11)

    body12 = eval(body11)         # 先将字符串转换成字典
    dataes = json.dumps(body12)     # 将字典转换成json格式
    print(type(dataes))
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/company/details"
    header = {
            "Referer": "https://testpartner.dmall.com.hk/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "Origin": "https://testpartner.dmall.com.hk",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"

        }
    body = {
            "form_data": dataes
            }

    print("123456",body)
    r = s.post(url, headers=header, data=body, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def update_supplier_infor(s, taxpayerType = "Z1", companyName = "深圳大源源呐990", legalPeople = "大源源",
                            companyAddress="2222", taxpayerNumber="111111111111111", bankCode="1111111111",
                            simpleName="11111", basicAccount="11111111111", bankName="建行",
                            bankAccountName="建行西丽分行", mainName="22222", mainPhone="18571519920"):
    '''
    修改公司信息
    '''
# "createdStr": "2020-10-22 19:52:02","modifiedStr": "2020-10-22 19:52:02",
    ids = save_supplier_information(s)['data']   # 新增公司信息返回的id
    print(ids)
    data = {
            "taxpayerType": taxpayerType,
            "companyName": companyName, "legalPeople": legalPeople,
            "companyAddress": companyAddress, "taxpayerNumber": taxpayerNumber, "bankCode": bankCode,
            "simpleName": simpleName, "basicAccount": basicAccount,
            "bankName": bankName, "bankAccountName": bankAccountName,
            "mainName": mainName, "mainPhone": mainPhone,
            "id": ids, "isUpdate": "I", "companyType": "1", "manageMode": 1,
            "groupNo": "GH000172", "martCode": "dfhk",
            "statusStr": "正常", "companyTypeStr": "商品類供應商",
            "manageModeName": "制造商", "taxpayerTypeName": "壹般納稅人(0;9%;13%)", "source": 2,
            "status": 3, "ynDesc": "有效", "venderId": 10032, "lastOptUser": "有源[Dd00631483]",
            "createdStr": "" + "2020-10-22 19:52:02", "modifiedStr": "" + " 2020-10-22 19:52:02",
            "created": 1603367522000, "yn": 1, "modified": "1603367522000"
             }

    print("@@@@@@@@@@@@@@  ----", data)
    bodys = json.dumps(data)
    print("######## ----- ----", bodys)
    body1 = bodys.replace(" ", "")
    print("111111", body1)
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/company/update"
    headers = {"Referer": "https://testpartner.dmall.com.hk/"}
    body = {

        "form_data": body1

        }

    print("----------", body)
    print(type(body))
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def supplier_loadown_template(s):
    '''
    公司档案信息模板下载
    :param s:
    :return:
    '''
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/company/template"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/"
                }
    r = s.get(url, headers=headers, verify=False)
    logger.debug("返回日志: %s" % r)
    # return r
    # print("124345")
    path = os.path.dirname(os.path.realpath(__file__))
    print(path)
    real_path = os.path.join(path, "供商公司導入模板.xls")
    print(real_path)
    # if os.path.exists(real_path):
    #     shutil.rmtree(real_path)
    fp = open("供商公司導入模板.xls", "wb")
    fp.write(r.content)
    fp.close()
    return r.status_code
    # return r.text


def import_company(s, name="供商公司導入模板 (4).xls"):
    '''
    公司档案信息模板导入
    :return:
    '''
    # name = name
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/company/import"
    headers = {
                "Referer": "https://testpartner.dmall.com.hk/"

                }
    path = os.path.dirname(os.path.realpath(__file__))
    real_path = os.path.join(path, name)
    f = {
        "file": (name, open(real_path, "rb"), "Content-Type: application/vnd.ms-excel")
    }
    r = s.post(url, headers=headers, files=f, verify=False)
    logger.debug("返回日志: %s" % r.json())
    print(r.json())
    return r.json()


def find_supplier_infor(s, pageSize="20", currentPage="1", companyName="深圳大源源呐939"):
    '''
    查询公司信息列表接口
    :return:
    '''
    form_data = {"pageSize": pageSize, "currentPage": currentPage, "companyName": companyName}
    form_datas = json.dumps(form_data)
    url="https://testdf-vc-supplier.dmall.com.hk/cx/company/find"
    headers = {"Referer": "https://testpartner.dmall.com.hk/"}
    body = {
            "form_data": form_datas
        }

    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def find_account_list(s, pageSize="20", currentPage="1", supplierName="深圳大源源呐939" ):
    '''
    账号管理列表查询
    :return:                                        #   还有查询条件
    '''
    form_data = {"pageSize": pageSize, "currentPage": currentPage, "supplierName": supplierName}
    form_datas = json.dumps(form_data)
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/account/find"
    headers = {"Referer": "https://testpartner.dmall.com.hk/"}
    body = {
            "form_data": form_datas

        }
    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def find_account_cards(s):
    '''
    查看账号卡号详情
    :return:
    '''
    account_card = find_supplier_infor(s)
    account_cards = account_card['data']['list'][0]['groupNo']
    card = {"supplierAccount": account_cards, "pageSize": 20, "currentPage": 1}
    print("@@@@@@@@", card)
    cards = json.dumps(card)     # 将字典转换成json
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/supplier/find"
    headers = {"Referer": "https://testpartner.dmall.com.hk/"}
    body = {

        "form_data": cards
        }
    r = s.post(url, headers=headers, data=body, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def update_account_information(s, mobile="18571519920", contacts="2" , email="353558733@qq.com",status=2):
    '''
    修改账号信息（校验手机号，邮箱及启用状态）     #cx_supplier_account
    :return:r.json
    '''                                            # status 启用状态 1.禁用 2.启用
    account_card = find_supplier_infor(s)
    account_cards = account_card['data']['list'][0]['groupNo']
    form_list = {"mainAccount": account_cards, "supplierAccount": account_cards,
                  "mobile": mobile, "supplierName": "深圳大源源呐939", "accountType": 1,
                  "contacts": contacts, "email": email, "companyId": 10820, "supplierGroup": "GH000089",
                  "sourceName": "来客", "accountTypeDesc": "管理賬號（壹級賬號）", "statusStr": "正常", "source": 2, "status": status, "id": 4437,
                  "martCode": "dfkh", "venderId": 10039, "lastOptUser": "大源源呗[Dd00631484]", "created": 1602567391000, "yn": 1,
                  "ynDesc": "有效", "createdStr": "2020-10-13 13:36:31", "modifiedStr": "2020-10-13 14:18:31"}
    print("#####", 124344)
    print(form_list)
    form_data = json.dumps(form_list)
    print("-------------  %s" % form_data)
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/account/update"
    headers = {"Referer": "https://testpartner.dmall.com.hk/"}
    body = {
           "form_data": form_data
                        }
    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def account_resetPWD(s,supplierAccount="supplierAccount", contactsPhone="contactsPhone"):
    '''
    账号重置密码
    :return:                # 1.先调用公司信息接口  2.再调用账号管理接口
    '''
    # account_reset = find_supplier_infor(s)
    # account_resets = account_reset['data']['list'][0]['groupNo']
    # account_list = find_account_list(s, pageSize="20", currentPage="1", supplierName="深圳大源源呐939")
    # print(account_list['data']['list'][0]['mobile'])
    # account_lists = account_list['data']['list'][0]['mobile']
    account = {"martCode": "dfkh", "supplierAccount": supplierAccount, "contactsPhone": contactsPhone}
    form_account = json.dumps(account)
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/account/resetPWD"
    headers = {"Referer": "https://testpartner.dmall.com.hk/"}
    body = {
            "form_data": form_account
            }
    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


class Add_supplier_card():
    ''' 卡号管理 '''
    def __init__(self, s):
        self.s = s

    def card_list(self):
        """
        卡号管理列表查询
        :return:r.json()
        """
        url = "https://testdf-vc-supplier.dmall.com.hk/cx/supplier/find"
        headers = {"Referer": "https://testpartner.dmall.com.hk/"}
        body = {
            "form_data": '{"currentPage":1,"pageSize":20}'
            }
        r = self.s.post(url, data=body, headers=headers, verify=False)
        logger.debug("返回日志：%s" % r.json())
        return r.json()


def add_supplier_cards(s):
    """                      # supplierFullName 公司名称   #
    新增供应商卡号         # cx_supplier

    """
    # cards_informations =

    url = "https://testdf-vc-supplier.dmall.com.hk/cx/supplier/add"
    headers = {
            "Referer": "https://testpartner.dmall.com.hk/",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"

            }
    body = {
            "form_data": '{"supplierCode":"909090","supplierFullName":"深圳大源源呐999","supplierShortName":"11111",'
                         '"supplierType":1,"bizType":"TO_C","supplierStatus":"1","businessType":1,"taxType":"Z1",'
                         '"contacts":"2","contactsPhone":"18571519920","purchaseGroup":"1002","returnSupplier":1,'
                         '"settleCompany":"10039","payType":"2","plannedDeliveryTime":"1","minOrderAmount":"0",'
                         '"orderCalendar":"8","manualPriceRevision":"1","autoConfirmOrders":"0","settlePeriod":"2",'
                         '"settleMethod":"2","accountPeriodStartDay":"0",'
                         '"accountPeriod":"30","grossProfitCompensate":"2","paymentFreeze":"0",'
                         '"generateZeroSettleSheet":"0","checkStock":"0","checkCost":"0","companyId":10820,'
                         '"supplierAccount":"GH000089",'
                         '"supplierGroup":"GH000089","email":"353558733@qq.com","configers":[]}'
    }
    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


def approve_supplier_card(s):
    '''
    卡号审批     status：2.同意 4.驳回
    :return:
    '''
    url = "https://testdf-vc-supplier.dmall.com.hk/cx/supplier/approve"
    headers = {
        "Referer": "https://testpartner.dmall.com.hk/",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"

            }
    body = {
        "form_data": '{"supplierCode":"909090","status":2,"rejectCause":"同意","martCode":"dfkh"}'
        }
    r = s.post(url, data=body, headers=headers, verify=False)
    logger.debug("返回日志：%s" % r.json())
    return r.json()


if __name__ == "__main__":
    s = requests.session()
    df_login = DF_Login(s)
    # update_account_information(s)
    # update_account_information(s, mobile="18571519920", contacts="2" , email="353558733@qq.com", status=1)

    # find_supplier_infor(s, pageSize="", currentPage="", companyName="")
    # cc = save_supplier_information(s, taxpayerType="Z1", companyName="深圳大源源呐939", legalPeople="大源源",
    #                                companyAddress="2222", taxpayerNumber="111111111111111", bankCode="1111111111",
    #                                simpleName="11111", basicAccount="11111111112",
    #                                bankName="建行", bankAccountName="建行西丽分行1")
    #
    # print(cc['data']['companyName'])
    # print(type(cc['data']['companyName']))
    # ck = find_account_list(s, pageSize="20", currentPage="1", supplierName="深圳大源源呐939")
    # print(ck['data']['list'][0]['mobile'])
    # account_reset = find_supplier_infor(s)
    # account_resets = account_reset['data']['list'][0]['groupNo']
    # account_list = find_account_list(s, pageSize="20", currentPage="1", supplierName="深圳大源源呐939")
    # print(account_list['data']['list'][0]['mobile'])
    # account_lists = account_list['data']['list'][0]['mobile']
    # account_resetPWD(s, supplierAccount=account_resets, contactsPhone=account_lists)
    # import_company(s, name="供商公司導入模板 (4).xls")
    # add_company = save_supplier_information(s, taxpayerType="Z1", companyName="深圳大源源呐939", legalPeople="大源源",
    #                                         companyAddress="2222", taxpayerNumber="111111111111111", bankCode="1111111111",
    #                                         simpleName="11111", basicAccount="11111111112",
    #                                         bankName="建行", bankAccountName="建行西丽分行1")
    # print("@##@#@##@#@", add_company)

    zz = Add_supplier_card()
    zz.card_list()


