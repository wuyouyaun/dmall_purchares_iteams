import requests
from nb_log import LogManager
from nb_log_config import LOG_PATH

logger = LogManager("api").get_logger_and_add_handlers(is_add_stream_handler=True,
                                                       log_filename="api.log",
                                                       log_path=LOG_PATH
                                                        )

def login(s):
    # s=requests.session()
    url="http://8.129.172.40:8888/api/login/"
    h={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
       }
    body={
        "account":"admin",
        "password":"123456a"
        }
    r=s.post(url,headers=h,data=body)
    logger.debug("返回日志：%s"%r.text)
    return r.text
    # print(r.cookies)


if __name__=="__main__":
    s=requests.session()
    c=login(s)
    print(c)
