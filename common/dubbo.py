#coding:utf-8


import json
import socket
import telnetlib

class Dubbo(telnetlib.Telnet):

    prompt = 'dubbo>'
    coding = 'utf-8'

    def __init__(self, host=None, port=0,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        super().__init__(host, port)
        self.write(b"\n")

    def command(self, flag, str_=""):
        data = self.read_until(flag.encode())
        self.write(str_.encode() + b"\n")
        return data

    def invoke(self, service_name, method_name):
        command_str = "invoke {0}.{1}()".format(
            service_name, method_name)    #这个地方的arg不能写成json.dumps(arg)，即不能转换成string型，提高复用性，在调2个或2个以上的接口的方法的参数时
        self.command(Dubbo.prompt, command_str)
        data = self.command(Dubbo.prompt, "")
        print("%s-----"%data)
        data = data.decode(Dubbo.coding, errors='ignore').split('\n')[0].strip()
        print(data)

        return data


    def dotest1(self, conn):  #含有泛型的json，看源码
        result = conn.invoke("com.dmall.scm.sdk.service.DubboTest","testPrint")  #
        # print("==========请求data参数为:==========" + str(data))
        print('fdfdf')
        return result
        # print(result)

if __name__ == '__main__':
    # count = 10001
    # for num in range(20190919200001, 20190919200006, 2):
    #     count += 100
    conn = Dubbo('10.12.68.187', 18163)  #这个是dubbo://的IP和端口

    # T_E006_BUDGET_DETAIL
#     data1 = {
#
# }

    result1 = conn.dotest1(conn)  #执行dotest_json_param测试用例（请求是json格式的）
    print(result1)
