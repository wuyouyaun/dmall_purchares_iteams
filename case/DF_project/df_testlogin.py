#coding:utf-8
import urllib3
urllib3.disable_warnings()
import requests

from nb_log import LogManager
from nb_log_config import LOG_PATH

logger = LogManager("api").get_logger_and_add_handlers(is_add_stream_handler=True,
                                                       log_filename="api.log",
                                                       log_path=LOG_PATH
                                                        )

def DF_Login(s):
    '''
    将登录需要的cookies添加到session里，以跳过登录时的验证码      (有两个商家，一个DF，一个是柬埔寨，不同的商家对应的cookies不同)
    :return: r.cookies     #采用的是柬埔寨商家的cookies
    '''
    # s=requests.session()
    url="https://testpartner.dmall.com.hk/#full/partner/login"
    header={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"
            }

    # s=requests.session()
    r = s.get(url,headers=header,verify=False)
    # print(s.cookies)

    c=requests.cookies.RequestsCookieJar()
    c.set("ticket","7E0D38F737DF4D3CDAFA743D79A42B786041FA56A93DBE1E8F1E56A0AA699132E870F65AC5940E21009EF5E93BD0F8B2169A314FCCDC660B711C7CA0CDA6C7C12DF0DF3813180B414FAAC5D394C49C17C728D544D64C1A56826D7846810FA97A55A12F24399AEA31E3E1D204DDE11F4FC21775EB2EDEC257470C8744F6D237BB")
    c.set("UYBFEWAEE","191C976215F4DC1312811C2395316AF433E5B01790EA7999A5E6B5DF6076E14811313D454884F5161920E9378BBB008088B4D7B6DEFC5FBCDC588CD92FC2EDB8")
    c.set("_gid","GA1.3.495679190.1598509078")
    c.set("login_no","MTExMTExMTFfbWZZbmRTYWZucW9QUzdaUnl3M3RUQT09")
    c.set("dmall-locale","zh_HK")
    s.cookies.update(c)
    # logger.debug("返回日志：%s" % r.json())
    print("%s"%r)
    return s.cookies



def df_inquire(s):
    '''查询'''
    # s=requests.session()
    url2="https://testpomanage-partner.dmall.com.hk/cx/dh/shop/query"
    headers={
        "Referer":"https://testpartner.dmall.com.hk/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
        "Origin":"https://testpartner.dmall.com.hk"
            }
    body={
        "form_data":'{"pageSize":20,"page":1}'

        }

    r2=s.post(url=url2,data=body,headers=headers,verify=False)
    logger.debug("返回日志：%s" % r2.json())
    return r2
# return r2.text

if __name__ == "__main__":
    s = requests.session()
    df_login = DF_Login(s)
    print("12234")
    print(df_login)


