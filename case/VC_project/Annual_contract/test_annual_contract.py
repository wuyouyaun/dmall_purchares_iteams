# coding:utf-8
import requests
import pytest
import time
import allure
from case.VC_project.Annual_contract.annuals_contract import *
from case.VC_project.VCtest_login import VC_Login

class Test_Ycontract_Listquire():

    @allure.feature("查询页面")
    def test_Ycontract_Listquire_01(self,login_xadmin):
        '''
        验证不传参数点击合同管理查询功能的有效性
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s)
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_02(self,login_xadmin):
        '''
        验证输入有效的合同编号可查询出相对应的合同数据
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, contractNo="20081900010")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_03(self,login_xadmin):
        '''
        验证输入无效的合同编号 查询结果为空
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, contractNo="2008190001")
        assert contract_list['data']['draftCount'] == 0
        assert contract_list['data']['auditingCount'] == 0

    def test_Ycontract_Listquire_04(self,login_xadmin):
        '''
        验证输入有效的供商卡号 ，可查询出有效的供商卡号合同
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, supplierCode="112233")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None


    @pytest.mark.skip("此处有个bug,按照查询条件的供商卡号查询只有登录的供应商")
    def test_Ycontract_Listquire_05(self,login_xadmin):
        '''
        验证输入无效的供商卡号 ，查询结果为空
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, supplierCode="112233")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None


    def test_Ycontract_Listquire_06(self,login_xadmin):
        '''
        验证输入业务状态为0，可查询出草稿的业务状态合同(当有草稿的业务数据)
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, businessStatus="0")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_07(self,login_xadmin):
        '''
        验证输入业务状态为0，返回的草稿业务状态合同为空(当没有草稿的业务数据)
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, businessStatus="0")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_08(self,login_xadmin):
        '''
        验证输入业务状态为3，可查询出业务审批中的业务状态合同(当有业务审批中的业务数据)
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, businessStatus="3")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_09(self,login_xadmin):
        '''
        验证输入业务状态为3，返回的业务审批中的业务状态合同为空(当无业务审批中的业务数据)
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, businessStatus="3")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_10(self,login_xadmin):
        '''
        验证输入业务状态为4，返回的待执行的业务状态合同为空(当无待执行的业务数据)
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, businessStatus="4")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_11(self,login_xadmin):
        '''
        验证输入业务状态为4，可查询出待执行的业务状态合同(当有待执行的业务数据)
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, businessStatus="4")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    #5执行中

    def test_Ycontract_Listquire_12(self,login_xadmin):
        '''
        验证输入业务状态为5，可查询出执行中的业务状态合同(当有待执行的业务数据)
        '''
        s = login_xadmin
        VC_Login(s)
        contract_list = Ycontract_Listquire(s, businessStatus="5")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_13(self,login_xadmin):
        '''
        验证输入业务状态为5，查询出执行中的业务状态合同为空(当无待执行的业务数据)
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, businessStatus="5")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    #6已结束
    def test_Ycontract_Listquire_14(self,login_xadmin):
        '''
        验证输入业务状态为6，查询出已结束的业务状态合同为空(当无待执行的业务数据)
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, businessStatus="6")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_15(self,login_xadmin):
        '''
        验证输入业务状态为6，可查询出执行中的业务状态合同(当有待执行的业务数据)
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, businessStatus="6")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    # 7已作废
    def test_Ycontract_Listquire_16(self,login_xadmin):
        '''
        验证输入业务状态为7，可查询出执行中的业务状态合同(当有待执行的业务数据)
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, businessStatus="7")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_17(self,login_xadmin):
        '''
        验证输入业务状态为7，查询出已结束的业务状态合同为空(当无待执行的业务数据)
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, businessStatus="7")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    # 8操作中
    def test_Ycontract_Listquire_18(self,login_xadmin):
        '''
        验证输入业务状态为8，查询出操作中的业务状态合同为空(当无待执行的业务数据)
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, businessStatus="7")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_19(self,login_xadmin):
        '''
        验证输入业务状态为8，可查询出操作中的业务状态合同(当有待执行的业务数据)
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, businessStatus="7")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None


    def test_Ycontract_Listquire_20(self,login_xadmin):
        '''
        验证合同创建开始时间小于合同创建结束时间，可查询出时间区间内的业务状态合同数据(当有待执行的业务数据)
        '''
        s = login_xadmin
        createTimeStart="2020-08-01 00:00:00"
        timeArray=time.strptime(createTimeStart,"%Y-%m-%d %H:%M:%S")
        print(timeArray)
        time1=int(time.mktime(timeArray))*1000
        print(time1)

        createTimeEnd="2020-09-03 23:59:59"
        timeArray=time.strptime(createTimeEnd,"%Y-%m-%d %H:%M:%S")
        print(timeArray)
        time2=int(time.mktime(timeArray))*1000
        print(time2)
        contract_list = Ycontract_Listquire(s, createTimeStart=time1,createTimeEnd=time2,tag=2)
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_21(self,login_xadmin):
        '''
        验证合同创建开始时间大于合同创建结束时间，查询出时间区间内的业务状态合同数据为空
        '''
        s = login_xadmin
        createTimeStart="2020-08-01 00:00:00"
        timeArray=time.strptime(createTimeStart,"%Y-%m-%d %H:%M:%S")
        print(timeArray)
        time1=int(time.mktime(timeArray))*1000
        print(time1)

        createTimeEnd="2020-09-03 23:59:59"
        timeArray=time.strptime(createTimeEnd,"%Y-%m-%d %H:%M:%S")
        print(timeArray)
        time2=int(time.mktime(timeArray))*1000
        print(time2)
        contract_list = Ycontract_Listquire(s, createTimeStart=time1,createTimeEnd=time2,tag=2)
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_22(self,login_xadmin):
        '''
        验证创建开始时间小于创建结束时间，可查询出时间区间内的业务状态合同数据(当无待执行的业务数据)
        '''
        s = login_xadmin
        createTimeStart="2020-08-01 00:00:00"
        timeArray=time.strptime(createTimeStart,"%Y-%m-%d %H:%M:%S")
        print(timeArray)
        time1=int(time.mktime(timeArray))*1000
        print(time1)

        createTimeEnd="2020-09-03 23:59:59"
        timeArray=time.strptime(createTimeEnd,"%Y-%m-%d %H:%M:%S")
        print(timeArray)
        time2=int(time.mktime(timeArray))*1000
        print(time2)
        contract_list = Ycontract_Listquire(s, createTimeStart=time1,createTimeEnd=time2,tag=2)
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None


    def test_Ycontract_Listquire_23(self,login_xadmin):
        '''
        验证合同开始时间小于合同结束时间，可查询出时间区间内的业务状态合同数据(当时间区间无合同业务数据)
        '''
        s = login_xadmin
        createTimeStart="2020-08-01 00:00:00"
        timeArray=time.strptime(createTimeStart,"%Y-%m-%d %H:%M:%S")
        print(timeArray)
        time1=int(time.mktime(timeArray))*1000
        print(time1)

        createTimeEnd="2020-09-03 23:59:59"
        timeArray=time.strptime(createTimeEnd,"%Y-%m-%d %H:%M:%S")
        print(timeArray)
        time2=int(time.mktime(timeArray))*1000
        print(time2)
        contract_list = Ycontract_Listquire(s, executeStart=time1, executeEnd=time2, tag=2)
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_24(self,login_xadmin):
        '''
        验证合同开始时间大于合同结束时间，查询出来的时间区间内的业务状态合同数据为空
        '''
        s = login_xadmin
        createTimeStart="2020-08-01 00:00:00"
        timeArray=time.strptime(createTimeStart,"%Y-%m-%d %H:%M:%S")
        print(timeArray)
        time1=int(time.mktime(timeArray))*1000

        createTimeEnd="2020-09-03 23:59:59"
        timeArray=time.strptime(createTimeEnd,"%Y-%m-%d %H:%M:%S")
        # print(timeArray)
        time2=int(time.mktime(timeArray))*1000
        # print(time2)
        contract_list = Ycontract_Listquire(s, executeStart=time1, executeEnd=time2, tag=2)
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_25(self,login_xadmin):
        '''
        验证合同开始时间小于合同结束时间，查询出来的时间区间内的业务状态合同数据为空(当时间区间无合同业务数据)
        '''
        s = login_xadmin
        createTimeStart = "2020-08-01 00:00:00"
        timeArray = time.strptime(createTimeStart, "%Y-%m-%d %H:%M:%S")
        print(timeArray)
        time1=int(time.mktime(timeArray))*1000
        print(time1)

        createTimeEnd = "2020-09-03 23:59:59"
        timeArray = time.strptime(createTimeEnd,"%Y-%m-%d %H:%M:%S")
        print(timeArray)
        time2 = int(time.mktime(timeArray))*1000
        print(time2)
        contract_list = Ycontract_Listquire(s, executeStart=time1, executeEnd=time2, tag=2)
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None


    # 合同编号
    def test_Ycontract_Listquire_26(self,login_xadmin):
        '''
        验证输入有效的合同类型模板，可查询出相对应的合同编号数据(当有合同业务数据)
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s,contractTemplateNo="T20080300005")
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_27(self,login_xadmin):
        '''
        验证输入无效的合同类型模板，查询出合同编号数据为空
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s,contractTemplateNo="T20080")
        assert contract_list['data']['draftCount'] == 0
        assert contract_list['data']['auditingCount'] == 0

    @pytest.mark.skip()
    def test_Ycontract_Listquire_28(self,login_xadmin):
        '''
        验证输每页展示20条数据的有效性（展示当前的业务数据，默认最大为20条）
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, pageSize=20)
        assert contract_list['data']['draftCount'] == 16
        assert contract_list['data']['auditingCount'] == 13

    def test_Ycontract_Listquire_29(self,login_xadmin):
        '''
        验证输每页展示40条数据的有效性（展示当前的业务数据，默认最大为20条，且页面中只有15条数据）
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, pageSize=40)
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_30(self,login_xadmin):
        '''
        验证分页功能的有效性（展示默认第一页的数据）
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, pageNum=1)
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_31(self,login_xadmin):
        '''
        验证分页功能的有效性（展示默认第一页的数据）
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, pageNum=2)
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_32(self,login_xadmin):
        '''
        验证年度合同各有效的查询条件组合一起查询数据的有效性
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, contractNo = None, supplierCode=None, businessStatus=None, createTimeStart=None, createTimeEnd=None,
                            executeStart=None, executeEnd=None, contractTemplateNo=None, tag=1, pageSize=20, pageNum=1)
        assert contract_list['success'] == True
        assert contract_list['errorCode'] == None

    def test_Ycontract_Listquire_33(self,login_xadmin):
        '''
        验证年度合同查询条件组合一起查询数据的有效性（有查询条件无效）
        '''
        s = login_xadmin
        contract_list = Ycontract_Listquire(s, contractNo=213, supplierCode=None, businessStatus=None, createTimeStart=None,createTimeEnd=None,
                            executeStart=None, executeEnd=None, contractTemplateNo=None, tag=1, pageSize=20, pageNum=1)
        assert contract_list['data']['draftCount'] == 0
        assert contract_list['data']['auditingCount'] == 0


class Test_Contract_details():
    '''
    合同详情信息查询
    '''
    @pytest.mark.skip
    def test_Contract_details_34(self,login_xadmin):                       # 这个接口因为数据原因（数据都被删），供应商无法查看自己的合同数据
        '''
        验证输入有效的合同编号，可对合同详情信息进行查询
        '''
        s = login_xadmin
        details=Contract_details(s,contractNo=20090900006)
        assert details['data']['baseInfo']['contractNo'] == 20090900006
        assert details['success'] == True

    def test_Contract_details_35(self,login_xadmin):
        '''
        验证输入无效的合同编号，查询的合同为空
        '''
        s = login_xadmin
        details=Contract_details(s,contractNo=200909000)
        assert details['success'] == False
        print("66666666")
        assert '未搵到該合同' in details['errorMsg']

    def test_Contract_details_36(self,login_xadmin):
        '''
        无合同编号，提示输入合同编号
        '''
        s = login_xadmin
        details=Contract_details(s)
        assert details['success'] == False
        assert details['errorMsg'] == '合同編號不能為空'



class Test_check_pdf_list():
    '''
    checkpdf是否存在
    '''

    def test_check_pdf_37(self,login_xadmin):
        '''
        存在有效的合同编号，点击预览，prd存在
        '''
        s = login_xadmin
        pdf_01 = check_pdf(s, contractNo=20090900006)
        assert pdf_01['success'] == True
        assert pdf_01['data'] == None

    def test_check_pdf_38(self,login_xadmin):
        '''
        不存在的合同编号，点击预览，prd不存在
        '''
        s =login_xadmin
        pdf_01 = check_pdf(s, contractNo=20090900032)
        assert pdf_01['success'] == False
        assert pdf_01['errorMsg'] == "資源文件不存在"

    @pytest.mark.skip()
    def test_check_pdf_39(self,login_xadmin):
        '''
        合同编号为空，点击预览，提示合同编号不能为空
        '''
        s =login_xadmin
        pdf_01 = check_pdf(s, contractNo='')
        assert pdf_01['success']==False
        assert pdf_01['errorMsg']=='合同編號不能為空'


    # @pytest.mark.skip()
    def test_preview_pdf_40(self, login_xadmin):                 # 合同预览 prd预览
        '''
        存在有效的合同编号，点击预览，预览prd
        '''
        s = login_xadmin
        preview_pdf(s,contractNo=20091500002)
        fp = write_pdf(s, contractNo=20091500002)
        Pdf = parsePdf(fp)
        assert "合同价格" in Pdf
        assert "合同生效" in Pdf


    # @pytest.mark.skip()
    def test_preview_pdf_41(self,login_xadmin):
        '''
        不存在的合同编号，点击预览，无法预览prd
        '''
        s = login_xadmin
        Pdf = preview_pdf(s, contractNo="")
        Pdf01=write_pdf(s, contractNo="")
        assert Pdf01 == "文件格式为非pdf"

    def test_preview_pdf_42(self,login_xadmin):
        '''
        不存在的合同编号，点击预览，无法预览prd
        '''
        s=login_xadmin
        pdf_02 = preview_pdf(s, contractNo="20091500034")
        Pdf01=write_pdf(s, contractNo="20091500034")
        assert Pdf01 == "文件格式同非pdf格式"

    def test_preview_pdf_43(self,login_xadmin):
        '''
        验证有效的合同号预览后可成功下载pdf
        '''
        s=login_xadmin
        preview_pdf(s, contractNo="20091500034")
        d_pdf=downlaod_pdf(s, contractNo="20091500034")
        assert d_pdf.status_code ==200

    def test_preview_pdf_44(self,login_xadmin):
        '''
        验证有效的合同号预览后可成功下载pdf,且pdf为该合同号的pdf文本
        '''
        s=login_xadmin
        preview_pdf(s, contractNo="20091500034")
        d_pdf = downlaod_pdf(s, contractNo="20091500034")
        fp = open_pdf(real_path="D:\htsj\hetong.pdf")
        parse = parsePdf(fp)
        assert "合同价格" in parse
        assert "付款方式" in parse

    # def test_preview_pdf_45(self,login_xadmin):
    #     '''
    #     验证无效的合同号预览后不成功下载pdf
    #     '''
    #     s=login_xadmin
    #     preview_pdf(s, contractNo="")
    #     d_pdf = downlaod_pdf(s, contractNo="")
    #     assert








































