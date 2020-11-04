

import string
import random


# from case.VC_project.Supplier_vc.supplier_port import Upload




# c=random.randint(10000,20000)
# print(c)
#
#
#

def generate_random_str(randomlength=16):
  '''
  生成一个指定长度的随机字符串，其中
  string.digits=0123456789
  string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
  '''
  str_list = [random.choice(string.digits) for i in range(randomlength)]
  random_str = ''.join(str_list)
  return random_str


# body = {
#
#         "form_data" : "{'isUpdate':'I','socialCreditCode':'233233333333334433','companyName':'深圳大源源呗','province':'010',\
#                 'city':'11','companyAddress':'测试','hosenum':'测试','postcode':'434234','legalPeople':'吴',\
#                 'registeredMoney':'123','foundedDate':'2020-09-01','businessStart':'2020-09-01',\
#                 'businessEnd':'2020-12-31','businessScope':'测试','mainCategory':'测试','manageBrand':'测试',\
#                 'proxyBrand':'测试','manageAreaCity':'1','manageMode':2,'organizationCode':'234332232323232323',\
#                 'orgStartDate':'2020-07-01','orgEndDate':'2020-11-26','taxpayerNumber':'3224342332433223',\
#                 'taxpayerType':'Z1','bankCode':'32414132421432','bankAccountNumber':'23433444','bankAccountName':'测试',\
#                 'basicAccount':'234324324234432443243243','bankProvince':'010','bankCity':'11','bankAddress':'23434343','simpleName':'大源源呗'\
#                 }"
#                 }
# print(body)
#


# j=1
# list=[]
# i=random.sample(range(0,9),j)
# list=''.join(str(i))
# print(list)


# a=range(0,9)
# i=[]
# for i in a:
#     # print(i)
#     list=''.join(str(i))
#     print(list)
#     list
#     list=random.sample(list,8)
#     print(list)

# for i in range(0,5):
#     list=''.join(str(i))
#     print(list)
#     slice = random.sample(list, 5)
#     print(slice)
# for i in range(5):
#     print(i)
#     slice = random.sample(list, 5)
#     print(slice)

# import os
#
# realpath = os.path.dirname(os.path.realpath(__file__))
# print(realpath)
# path=os.path.join(realpath,"ces.png")
# print(path)
#
# import os
# dirpath=os.path.dirname(os.path.realpath(__file__))
# print(dirpath)
#
# yamlpath=os.path.join(dirpath,"suppliers.yml")
# print(yamlpath)






url = "http://testdf-vc-supplier.dmall.com.hk/vc/company/updateImgs"
head={
               "Referer": "http://testdf-vc.dmall.com.hk/"
               }
body = {"form_data": '{"martCode":"dfhk","companyId":74,"isSubmit":true,"fileParams":[{"id":"",\
"companyId":74,"fileId":fileId,\
"fileName":"營業執照","certType":0},{"id":573,"companyId":74,"fileId":fileId,\
"fileName":"組織機構代碼證","certType":1},{"id":574,"companyId":74,"fileId":fileId,\
"fileName":"稅務登記證","certType":2},{"id":"","companyId":74,"fileId":fileId,\
"fileName":"銀行開戶許可證","certType":3}]}'}






