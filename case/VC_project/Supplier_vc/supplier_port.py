# coding:utf-8
import requests
import random
import os
from case.VC_project.Supplier_vc.ts import generate_random_str
from case.VC_project.VCtest_login import VC_Login
from case.VC_project.Supplier_vc.readyaml import read_company_information
# from requests toolbelt import MultpartEncoder
import string
import json


def Save_imformation_company(s):
    '''
    新增公司信息
    :param s:
    :return:
    '''
    url = "http://testdf-vc-supplier.dmall.com.hk/vc/company/save"
    head = {
           "Referer": "http://testdf-vc.dmall.com.hk/"
           }

    body = {

        "form_data": '{"isUpdate":"I","socialCreditCode":"233233333333544434","companyName":"深圳大源源3","province":"010",\
"city":"11","companyAddress":"测试","hosenum":"测试","postcode":"434234","legalPeople":"吴",\
"registeredMoney":"123","foundedDate":"2020-09-01","businessStart":"2020-09-01",\
"businessEnd":"2020-12-31","businessScope":"测试","mainCategory":"测试","manageBrand":"测试",\
"proxyBrand":"测试","manageAreaCity":"1","manageMode":2,"organizationCode":"234332232323232323",\
"orgStartDate":"2020-07-01","orgEndDate":"2020-11-26","taxpayerNumber":"3224342332433223",\
"taxpayerType":"Z1","bankCode":"32414132421432","bankAccountNumber":"23433444","bankAccountName":"测试",\
"basicAccount":"234324324234432443243243","bankProvince":"010","bankCity":"11","bankAddress":"23434343","simpleName":"大源源呗2"\
}'
                }

    # body.form_data.socialCreditCode = 11

    r=s.post(url, data=body, headers=head, verify=False)
    print(1111)
    return r.json()



def Upload(s, type=0):
    '''
    资质证照上传 ,     type 0 营业执照  1 组织机构代码 2 税务登记证 3 银行开户许可证
    :return:
    '''
    realpath = os.path.dirname(os.path.realpath(__file__))
    print(realpath)
    path = os.path.join(realpath, "ces.png")
    print(path)
    url = "http://testdf-vc-supplier.dmall.com.hk/vc/image/upload"
    head = {
           "Referer": "http://testdf-vc.dmall.com.hk/"
           }

    body = {
            "type": type
            }
    f = {
          "file": ("ces.png", open(path, "rb"), "image/png")
           }
    r = s.post(url, data=body, files=f, headers=head, verify=False)
    return r.json()


def image_type(type=0):
    if type == 0:
        print("1111")
        urls = Upload(s, type=0)
        type_image=json.loads(urls)['data']
    elif type == 1:
        urls = Upload(s, type=1)
        type_image = json.loads(urls)['data']
    elif type == 2:
        urls = Upload(s, type=2)
        type_image=json.loads(urls)['data']
    elif type == 3:
        urls = Upload(s, type=3)
        type_image=json.loads(urls)['data']

    return type_image



def update_images(s):

    companyId = str(Save_imformation_company(s)['data'])
    print("----------11222222")
    print(type(companyId))
    print(companyId)
    url = "http://testdf-vc-supplier.dmall.com.hk/vc/company/addImgs"
    head={
               "Referer": "http://testdf-vc.dmall.com.hk/"
               }
    body = {
            "form_data": '{"martCode":"dfkh","companyId":companyId,"isSubmit":true,"fileParams":[{"certType":"0","fileName":"營業執照","fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfkh_4415_0_0b7ad76565c84a41941a413af01c7c1d/20200929/6ad4d6c3-9c6d-46b1-bcdf-3a444305b9a2","id":""},{"certType":"1","fileName":"組織機構代碼證","fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfkh_4415_1_0853941fec9a453092d12a381bdf3340/20200929/93582fea-b0c4-4e36-bb1e-d005d2c6869e","id":""},{"certType":"2","fileName":"稅務登記證","fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfkh_4415_2_0857fe16b8304b03a323c9b0df7c50ec/20200929/1592f90f-5baa-4484-b7b4-3f8feb05ec0b","id":""},{"certType":"3","fileName":"銀行開戶許可證","fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfkh_4415_3_3b5d954e5261429ca48f81cf0802bea1/20200929/771583c8-ab75-4eb4-9914-4926b1bd8800","id":""}]}'
    }
    r=s.post(url, data=body, headers=head, verify=False)
    print(body)
    return r.text


def second_update(s):
    '''
    公司信息审核未通过，编辑后二次提交
    :param s:
    :return:
    '''
    url = "http://testdf-vc-supplier.dmall.com.hk/vc/company/update/second"
    head = {
               "Referer": "http://testdf-vc.dmall.com.hk/"
               }

    body1={"form_data":'{"cxCertificatesDTOList":[{"martCode":"dfhk","fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfhk_4294_0_7aac0129d7aa460e934ddbe0fdfe1487/20200927/ba322624-2e21-43b3-aecb-a4018cd205ee","rejectCause":null,"companyId":10775,"certType":0,"examineStatus":1,"changeStatus":1,"fileName":"營業執照","id":1142,"venderId":10032,"lastOptUser":"有源[Dd00631483]","created":1601175693000,"yn":1,"createdStr":"2020-09-27 11:01:33","modifiedStr":"2020-09-27 11:02:45","ynDesc":"有效","modified":1601175765000},{"martCode":"dfhk","fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfhk_4294_1_f3e1643fac594439acd55d0d275f9b5b/20200927/994e0c5b-e2a0-494e-990f-5ee6a9d95fc5","rejectCause":null,"companyId":10775,"certType":1,"examineStatus":1,"changeStatus":1,"fileName":"組織機構代碼證","id":1143,"venderId":10032,"lastOptUser":"有源[Dd00631483]","created":1601175693000,"yn":1,"createdStr":"2020-09-27 11:01:33","modifiedStr":"2020-09-27 11:02:45","ynDesc":"有效","modified":1601175765000},{"martCode":"dfhk","fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfhk_4294_2_1a4256d800bd476585dd9d59a71b9450/20200927/1492a201-0b78-47ef-b232-3c8e37b29c13","rejectCause":null,"companyId":10775,"certType":2,"examineStatus":1,"changeStatus":1,"fileName":"稅務登記證","id":1144,"venderId":10032,"lastOptUser":"有源[Dd00631483]","created":1601175693000,"yn":1,"createdStr":"2020-09-27 11:01:33","modifiedStr":"2020-09-27 11:02:45","ynDesc":"有效","modified":1601175765000},{"martCode":"dfhk","fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfhk_4294_3_7084590c85b64f749f57d182d1aa8d51/20200927/180a1392-b095-450a-84ee-626b0d50fcb5","rejectCause":null,"companyId":10775,"certType":3,"examineStatus":1,"changeStatus":1,"fileName":"銀行開戶許可證","id":1145,"venderId":10032,"lastOptUser":"有源[Dd00631483]","created":1601175693000,"yn":1,"createdStr":"2020-09-27 11:01:33","modifiedStr":"2020-09-27 11:02:45","ynDesc":"有效","modified":1601175765000},{"martCode":"dfhk","fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfhk_4294_4_9f11e59326f44e9cafb01007da844347/20200927/a3426303-6cc8-4615-9529-865006e87705","rejectCause":null,"companyId":10775,"certType":4,"examineStatus":1,"changeStatus":1,"fileName":"cs","id":1146,"venderId":10032,"lastOptUser":"有源[Dd00631483]","created":1601175693000,"yn":1,"createdStr":"2020-09-27 11:01:33","modifiedStr":"2020-09-27 11:02:45","ynDesc":"有效","modified":1601175765000}],"provinceStr":"北京市","cityStr":"北京","bankProvinceStr":"北京市","bankCityStr":"北京","martCode":"dfhk","companyName":"ces ","taxpayerType":"Z1","legalPeople":"www123","isUpdate":"U","bankAccountName":"3232","bankName":"34444","basicAccount":"444444","companyType":"1","manageMode":2,"taxpayerNumber":"23323232323238888","province":"010","city":"11","bankProvince":"010","bankCity":"11","bankCode":"323232329999","hosenum":"ce","companyAddress":"ce","postcode":"233222","bankAddress":"3211","organizationCode":"232222222222222222","simpleName":"ce ","socialCreditCode":"232333333333333333","registeredMoney":12,"foundedDate":"2020-09-02","businessStart":"2020-09-30","businessEnd":"2020-07-08","businessScope":"ces ","mainCategory":"12","manageBrand":"2","proxyBrand":"21","manageAreaCity":"1","orgStartDate":"2020-09-08","orgEndDate":"2020-08-04","bankAccountNumber":"32","agent":"21","statusStr":"審批未通過","companyTypeStr":"商品類供應商","manageModeName":"經銷商","source":6,"status":2,"id":10775,"venderId":10032,"lastOptUser":"有源[Dd00631483]","created":1601171892000,"yn":1,"createdStr":"2020-09-27 09:58:12","modifiedStr":"2020-09-28 16:20:43","ynDesc":"有效","modified":1601281243000,"imgsParam":{"companyId":10775,"isSubmit":true,"fileParams":[{"id":1142,"companyId":10775,"fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfhk_4294_0_7aac0129d7aa460e934ddbe0fdfe1487/20200927/ba322624-2e21-43b3-aecb-a4018cd205ee","fileName":"營業執照","certType":0},{"id":1143,"companyId":10775,"fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfhk_4294_1_f3e1643fac594439acd55d0d275f9b5b/20200927/994e0c5b-e2a0-494e-990f-5ee6a9d95fc5","fileName":"組織機構代碼證","certType":1},{"id":1144,"companyId":10775,"fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfhk_4294_2_1a4256d800bd476585dd9d59a71b9450/20200927/1492a201-0b78-47ef-b232-3c8e37b29c13","fileName":"稅務登記證","certType":2},{"id":1145,"companyId":10775,"fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfhk_4294_3_7084590c85b64f749f57d182d1aa8d51/20200927/180a1392-b095-450a-84ee-626b0d50fcb5","fileName":"銀行開戶許可證","certType":3},{"id":1146,"companyId":10775,"fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfhk_4294_4_9f11e59326f44e9cafb01007da844347/20200927/a3426303-6cc8-4615-9529-865006e87705","fileName":"cs","certType":4}]}}}'}

    r = s.post(url, data=body1, headers=head, verify=False)
    print(r.json())

if __name__ == "__main__":
    s = requests.session()
    c = VC_Login(s)
    save=Save_imformation_company(s)
    print(save)




    # print(save['data'])
    # print(type(save['data']))
    # c=update_images(s)
    # print(c)

















    # str = update_images(s,)
    # print("------",str)


   # print(kk["code"])#没有code属性

#     body = {
#             "form_data":{"martCode":"dfhk","companyId":74,"isSubmit":True,"fileParams":[{"id":"","companyId":74,"fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfhk_4294_0_17a347752fad48bd8cce98d3cac68d52/20200928/ff0fd49a-86a1-4fd1-af8f-b1a823fcb8de","fileName":"營業執照","certType":0},{"id":573,"companyId":74,"fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfhk_4294_1_4c6f88019a3c40b5baacc8cab831f91e/20200831/a13381b2-9693-499b-a393-d29922b9fee5","fileName":"組織機構代碼證","certType":1},{"id":574,"companyId":74,"fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfhk_4294_2_68fcc0bcef084bb487590be58e4fd890/20200831/d3c7bc9c-d3f4-43b4-b2ca-de7d39fd2219","fileName":"稅務登記證","certType":2},{"id":"","companyId":74,"fileId":"http://df-test-vc-supplier.dmallcdn.com/testdf-vc-supplier/dfhk_4294_3_626c2768aeec41d3830a02ca4fd13cfd/20200928/ef0ed181-cb69-4292-8089-c63a268d9a5c","fileName":"銀行開戶許可證","certType":3}]}
#                         }
#
#     s=json.dumps(body)
#     print(s)
#     print(type(s))




















