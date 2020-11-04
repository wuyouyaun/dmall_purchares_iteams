# conding:utf-8
import time
import os
import requests
import importlib
import sys
import time
import os.path
from pdfminer.pdfparser import  PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from nb_log import LogManager
from nb_log_config import LOG_PATH

logger = LogManager("api").get_logger_and_add_handlers(is_add_stream_handler=True,
                                                       log_filename="api.log",
                                                       log_path=LOG_PATH
                                                        )

importlib.reload(sys)
time1 = time.time()
from case.VC_project.VCtest_login import VC_Login

def Ycontract_Listquire(s, contractNo = None,supplierCode=None,businessStatus=None,createTimeStart=None,createTimeEnd=None,
                        executeStart=None,executeEnd=None,contractTemplateNo=None,tag=1,pageSize=20,pageNum=1):
    '''
    年度合同列表查询
    :param :
    return: r2.json()
    '''
    url="http://testcxcontract-partner.dmall.com.hk/vc/contract/contract/list"
    params={
        "contractNo": contractNo,                           # 合同编号
        "supplierCode": supplierCode,                       # 供商卡号
        "businessStatus": businessStatus,                   # 业务状态  0草稿, 3业务审批中，4待执行，5执行中，6已结束，7已作废，8操作中
        "createTimeStart": createTimeStart,                 # 创建开始时间
        "createTimeEnd":createTimeEnd,                      # 创建结束时间
        "executeStart": executeStart,                       # 合同开始时间
        "executeEnd": executeEnd,                           # 合同结束时间
        "contractTemplateNo":contractTemplateNo,            # 合同模板编号
        "tag": tag,
        "pageSize": pageSize,
        "pageNum": pageNum
    }

    r2=s.get(url=url,params=params)
    logger.debug("返回日志：%s" % r2.json())
    return r2.json()


def Contract_details(s,contractNo=None):      # 用例已输出
    '''
    合同详情信息查询
    :param : contractNo
    :return: r.json()
    '''
    url = "http://testcxcontract-partner.dmall.com.hk/vc/contract/contract/detail"
    params = {
           "contractNo": contractNo      # 合同编号
          }
    r=s.get(url=url, params=params)
    logger.debug("返回日志：%s" % r.json())
    return r.json()

def Contract_export(s):                   # 此处有bug，无法选中审批的合同数据
    '''
    导出合同内容
    :return: r.json()
    '''

    url="http://testcxcontract-partner.dmall.com.hk/vc/contract/contract/exportData"
    params={
                "contractTemplateNo": "",
                "contractNo": "",
                "supplierCode": "",
                "businessStatus": "",
                "createTimeStart": "",
                "createTimeEnd": "",
                "executeStart": "",
                "executeEnd": "",
                "supplierCodeIn": "",
                "supplierAccount": "",
                "midCategoreIn": "",
                "customPermissionFieldIn": ""
                }
    r=s.get(url=url,params=params)
    logger.debug("返回日志：%s" % r.json())
    return r.json()

def generate_Pdf(s,contractNo=None):     # 没用到
    '''
    生成pdf
    :param s: contractNo
    :return: r.json()
    '''
    url = "http://testcxcontract-partner.dmall.com.hk/vc/contract/contract/generatePdf"
    params = {
           "contractNo": contractNo         # 合同编号
            }
    r = s.get(url=url, params=params)
    logger.debug("返回日志：%s" % r.json())
    return r



def downlaod_pdf(s, contractNo=None):
    '''
    下载pdf
    :param:
    :return:
    '''
    url="http://testcxcontract-partner.dmall.com.hk/cx/contract/contract/downloadPdf"
    params={
            "contractNo": contractNo    # 合同编号

            }
    r = s.get(url=url, params=params)
    logger.debug("返回日志：%s" % r.json())
    return r

def check_pdf(s, contractNo=None):       # 用例输出
    '''
    检查pdf是否存在,在pdf页面上展示为预览，预览前会去查这个pdf是否存在
    :param: contractNo
    :return:
    '''
    url = "http://testcxcontract-partner.dmall.com.hk/vc/contract/contract/checkPdf/"+"%s"%contractNo
    params = {
            "contractNo": contractNo    # 合同编号
             }
    r = s.get(url=url, params=params)
    logger.debug("返回日志：%s" % r.json())
    return r.json()



def preview_pdf(s, contractNo=None):             # 用例输出
    '''
    预览pdf  （页面上进行预览）
    :param: contractNo
    :return: r.json()
    '''
    url = "http://testcxcontract-partner.dmall.com.hk/vc/contract/contract/previewPdf/"+"%s"%contractNo
    params = {
            "contractNo": contractNo      # 合同编号
            }
    r = s.get(url=url, params=params)
    logger.debug("返回日志：%s" % r.json())
    return r

def open_pdf(real_path="D:\htsj\hetong.pdf"):
    '''
    查看pdf内容
    :return:
    '''
    real_path=real_path
    with open(real_path, "r") as fp:
        fp.close()
    fp = open(real_path, 'rb')
    return fp

def write_pdf(s, contractNo=None):
    text_path = "./file02.pdf"
    r = preview_pdf(s, contractNo=contractNo)
    # try:
    if r.status_code == 404 :
        print("404")
        return "文件格式为非pdf"
    elif r.status_code == 500:
        print("500")
        return "文件格式同非pdf格式"



    with open(text_path, mode="wb+") as f:
        f.write(r.content)
        f.close()
        # return f
        f = open(text_path, 'rb')
        return f

def parsePdf(fp):
    '''解析PDF文本，并保存到TXT文件中'''
    # text_path = "./file02.pdf"
    # r = preview_pdf(s, contractNo=contractNo)
    # # try:
    # if r.status_code == 404 :
    #     print("404")
    #     return "文件格式为非pdf"
    # elif r.status_code == 500:
    #     print("500")
    #     return "文件格式同非pdf格式"
    # # except Exception as message:
    #
    # with open(text_path, mode="wb+") as f:
    #     f.write(r.content)
    #     f.close()
    #     # return text_path

    # fp = open(real_path, 'rb')
    # 用文件对象创建一个PDF文档分析器
    parser = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器，与文档对象
    parser.set_document(doc)
    doc.set_parser(parser)

    #提供初始化密码，如果没有密码，就创建一个空的字符串
    doc.initialize()

    #检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        #创建PDF，资源管理器，来共享资源
        rsrcmgr = PDFResourceManager()
        #创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr,laparams=laparams)
        #创建一个PDF解释其对象
        interpreter = PDFPageInterpreter(rsrcmgr,device)

        #循环遍历列表，每次处理一个page内容
        # doc.get_pages() 获取page列表
        for page in doc.get_pages():
            interpreter.process_page(page)
            #接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
            # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
            # 想要获取文本就获得对象的text属性，
            for x in layout:
                if(isinstance(x,LTTextBoxHorizontal)):
                    # with open(r'2.txt','a') as f:
                        results = x.get_text()
                        print(results)
                        # f.write(results  +"\n")
            print(type(results))
            print("ces")

    return results

def inquire_supplier():
    '''
    :param: supplierCode
    :return:
    '''
    url = "http://10.248.224.252:6006/mock/15/vc/contract/contract/supplierInfo"
    params = {
            "supplierCode": ""    #
            }
    r = s.get(url=url)
    logger.debug("返回日志：%s" % r.json())
    return r.json()

def inquire_template_list():
    '''
    模板列表查询
    :param:
    :return:
    '''
    url="http://10.248.224.252:6006/mock/15/vc/contract/contract/contractTemplateList"
    params={
            "is": "",
             "name": "",
             "status": "",
             "type": "",
            "joinDiscountElement": "",
            "postpone": "",
            "ticketDiscountWay": "",
            "contractTemplateNo": "",
            "hasAgreement": "",
            "agreementInfos": "",
            "approvalAgreementId": ""
            }

if __name__ == "__main__":
    s = requests.session()

    login = VC_Login(s)
    print(login)

    # c = downlaod_pdf(s, contractNo='20091500002')
    # print(c)
    preview_pdf(s, contractNo="")
    d_pdf = downlaod_pdf(s, contractNo="")
    print(d_pdf.status_code)

    # fp=write_pdf(contractNo='20091500002')
    # parsePdf(fp)
    # print("22222")
    # print(fp)
    # fp=open_pdf(real_path="D:\htsj\hetong.pdf")
    # parsePdf(fp)
    # preview_pdf(s, contractNo='20091500002')
    # print("233443432")
    # fp=write_pdf(contractNo=20091500002)
    # parsePdf(fp)
    # Pdf = preview_pdf(s, contractNo="")
    # print(Pdf)
    # c = write_pdf(s, contractNo="")
    # print(c)









    # check_pdf(s, contractNo=20091500002)
    # downlaod=downlaod_pdf(s, contractNo=20091500002)
    # print(downlaod)
    # real_path="D:\htsj\hetong.pdf"
    # with open(real_path,"r") as fp:
    #     # fp.open(downlaod.content)
    #     # fp.close()
    #     fp.close()








    # details = Contract_details(s,contractNo='20091500002')
    # print(details)
    # previews=preview_pdf(s, contractNo="20091500002")
    # print(previews)
    # print(type(previews))

    # if type(previews) !=
    # a=check_pdf(s,contractNo="20091500002")
    # print(a)
    # previews = preview_pdf(s, contractNo="20091500002")

    # pdf_01 = preview_pdf(s, contractNo=20091500002)
    # Pdf=parsePdf(s,contractNo=20091500002)

    # c = preview_pdf(s, contractNo="2009150034")
    # print("2321323")
    # print(c)
    #
    # par = parsePdf(s, contractNo="20091500034")

    # generate = generate_Pdf(s, contractNo=20091500002)
    # print(generate)




























    # print(details['data']['baseInfo']['contractNo'])
# contractNo=112
#     c=check_pdf(s,contractNo=20090900054)
#     print(c)
#     details=Contract_details(s,contractNo=20090900006)













































    # createTimeStart="2020-08-01 00:00:00"
    # timeArray=time.strptime(createTimeStart,"%Y-%m-%d %H:%M:%S")
    # print(timeArray)
    # time1=int(time.mktime(timeArray))*1000
    # print(time1)
    #
    # createTimeEnd="2020-09-03 23:59:59"
    #
    # timeArray=time.strptime(createTimeEnd,"%Y-%m-%d %H:%M:%S")
    # print(timeArray)
    # time2=int(round(time.mktime(timeArray)))*1000
    # print(time2)
    # # contract_list = Ycontract_Listquire(s, executeStart=time1, executeEnd=time2, tag=2)     #,supplierCode="",businessStatus="")
    # contract_list = Ycontract_Listquire(s, contractNo = 2221,supplierCode=None,businessStatus=None,createTimeStart=None,createTimeEnd=None,
    #                     executeStart=None,executeEnd=None,contractTemplateNo=None,tag=1,pageSize=20,pageNum=1)
    # print(contract_list)
    # print(contract_list['data']['draftCount'])
    # print(contract_list['data']['auditingCount'])

    # details=Contract_details(s)
    # print(details)
    # export = Contract_export(s)
    # print(export)






