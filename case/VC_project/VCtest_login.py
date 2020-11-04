#coding:utf-8

import requests

def VC_Login(s,loginName='test_001',loginPassword='Admin123456_'):

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
    r = s.post(url=url, data=body, headers=headers, verify=False)
    values = r.json()['data'][0]['value']
    print(values)

    # 请求登录接口
    body2={
      "loginName": loginName,
      "loginPassword": loginPassword,
      "retailId": values
     }

    url2 = "http://testdf-vc-basemanage.dmall.com.hk/login"
    h = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
         "Referer": "http://testdf-vc.dmall.com.hk/"

         }

    r2 = s.post(url=url2, headers=h, data=body2, verify=False)
    print(r2.cookies)
    return r2.json()

def list_inquire(s):
    '''查询'''
    url3 = "http://testdf-vc-basemanage.dmall.com.hk/tsysSystem/list"
    head = {
         "Referer": "http://testdf-vc.dmall.com.hk"
         }

    body3={
        "systemName": "",
        "pageSize": 20,
        "currentPage": 1
        }
    r=s.post(url=url3, data=body3,headers=head, verify=False)
    print(r.text)

if __name__ == "__main__":
    s = requests.session()
    login = VC_Login(s)

    print(login)
    c = list_inquire(s)
    print(c)

    # print(type(login))
    # print(login['code'])

























