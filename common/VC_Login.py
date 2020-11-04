import requests
from nb_log import LogManager
from nb_log_config import LOG_PATH

# logger = LogManager("api").get_logger_and_add_handlers(is_add_stream_handler=True,
#                                                        log_filename="api.log",
#                                                        log_path=LOG_PATH
#                                                        )
# s=requests.session()
# url = "http://testdf-vc-basemanage.dmall.com.hk/retails"
# headers = {
#      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
#      "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
#      "Cookie": "dmall-zone=null; dmall-locale=zh_HK",
#      "Connection": "keep-alive",
#      "Origin":"http://testdf-vc.dmall.com.hk",
#      "Referer":"http://testdf-vc.dmall.com.hk/"
#      }
# body = {
#   "loginName": "test_01",
#   "loginPassword": "Admin123456_",
#   "retailId": ""
#   }
# r=s.post(url=url,data=body,headers=headers,verify=False)
# print(r.json())
# values=r.json()['data'][0]['value']
# print(values)


def Vc_Login_Bf(s, loginName='0722test', loginPassword="Admin123456_"):
    '''登录提供value值
    :param : loginName
    :param : loginPassword
    :return : values
    '''
    # s=requests.session()
    url = "http://testdf-vc-basemanage.dmall.com.hk/retails"
    headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
         "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
         "Cookie": "dmall-zone=null; dmall-locale=zh_HK",
         "Connection": "keep-alive",
         "Origin":"http://testdf-vc.dmall.com.hk",
         "Referer":"http://testdf-vc.dmall.com.hk/"
         }
    body = {
      "loginName": loginName,
      "loginPassword": loginPassword,
      "retailId": ""
      }
    r=s.post(url=url,data=body,headers=headers,verify=False)
    # print(r.json())
    # print(type(r.json()))
    values=r.json()['data'][0]['value']
    return values

def VC_Login1 (s,values,loginName="admin",loginPassword="Dmall@1234"):
    '''VC登录,获取登录后的cookies
    :param: loginName
    :param:loginPassword
    return:
    '''
    url2="http://testdf-vc-basemanage.dmall.com.hk/login"
    h = {
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
        # "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        # "Cookie":"dmall-zone=null; dmall-locale=zh_HK",
        # "Connection":"keep-alive",
        # "Origin":"http://testdf-vc.dmall.com.hk",
         "Referer":"http://testdf-vc.dmall.com.hk/"
         }
    body2={
      "loginName":loginName,
      "loginPassword":loginPassword,
      "retailId":'%s'%values
     }
    r2=s.post(url=url2, headers=h, data=body2,verify=False)
    # print(r2.text)
    print (r2.cookies)
    return r2.json()
    print (r2.cookies)
    # print(r2.cookies['supplier_dmalltest'])
    # token=r2.cookies['supplier_dmalltest']

if __name__=="__main__":
    s=requests.session()
    VC_Login1(s)


























































# def login(s,loginName="admin",loginPassword="Dmall@1234"):
#     '''
#     VC国际化登录
#     :param loginName:admin
#     :param loginPassword: Dmall@1234
#     :return: r
#     '''
#     url="http://testdf-vc-basemanage.dmall.com.hk/login"
#     h={
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
#         "Cookie":"dmall-zone=null; dmall-locale=zh_HK; venderId=0",
#         "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
#         "Accept":"application/json",
#         "Origin":"http://testdf-vc.dmall.com.hk",
#         "Referer":"http://testdf-vc.dmall.com.hk/"
#
#          }
#     body={
#         "loginName":loginName,
#         "loginPassword":loginPassword,
#         "retailId":'0'
#         }
#
#     r=s.post(url,headers=h,data=body,verify=False)
#     logger.debug("返回日志：%s"%r.text)
#     s.headers.update(h)
#     # print("3223")
#     # print(r.cookies)
#     # print(r.text)
#     # print(s.headers)
#     # cookies=r.cookies["Cookie"]
#     # return r.cookies
# s=requests.session()
# login(s)
#
#
#
# url1="http://testdf-vc-basemanage.dmall.com.hk/tsysMenuResource/list"
# h={
#    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
#     "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
#     "Accept":"application/json"
# }
# body={
#     "resourceName":"",
#     "systemId":"",
#     "pageSize":20,
#     "currentPage":1
#     }
# r1=s.post(url=url1,headers=h,data=body,verify=False)
# print("1111")
# # print(r1.headers)
# logger.debug("返回日志：%s"%r1.text)
# print(s.cookies)
# print(r1.json())
# supplier_dmalltest=9UVmaEaZ+ovmCh/rmvGWFhnNB96vkFBqUhBQtGcuq5IVPc56ZP24vPODcCo/OMr54QrZ/JOWxU9M33wU4lgTIEM4f1yYpKyNCKb9x6irhF+lD91P+cpS3htNORTwKsktvMfjL/qyHsqenIXbPPwZJNfxZvqh+35+OfiE89cIX74P1HUxhfrGMWzbABfTFC1BzN/YwG0dh4TfRKDElYknyccVkzo307boQGqZfR2s/JDHgAevEppz8PysmZSGSpBCeuPzTaecAd0p00H9sXVeZkJix+yObMHxyDTxv6kX+LI/6DaNRWRw/jLwg9/XzrBb












# def inquire(s,resourceName,systemId):
#     """
#     资源管理查询
#     :param s:
#     :return:r.text
#     """
#     url1="http://testdf-vc-basemanage.dmall.com.hk/tsysMenuResource/list"
#     body={
#         # "resourceName":resourceName,
#         "systemId":systemId,
#         "pageSize":20,
#         "currentPage":1
#         }
#     r1=s.post(url=url1,data=body,verify=False)
#     print("1111")
#     print(s.cookies)
#     return r1.json()


# if __name__ == "__main__":
#     s=requests.session()
#     print("7777")
#     logins=login(s)
#     print(logins)
#     in_test=inquire(s,resourceName="",systemId="")
#     print("ceshi")
#     print(s.cookies)
#     print(in_test)












