from case.DF_project.df_testlogin import DF_Login
import pytest
import os
import allure
import requests
from case.DF_project.conftest import df_login_xadmin
from case.DF_project.DF_supplier.supplier import save_supplier_information, check_supplier_information,find_supplier_infor,find_account_list
from case.DF_project.DF_supplier.conftest import delete_register,delete_account_infor,delete_cards_infor
from case.VC_project.connect_mysql import select_sql,delete_db
from case.DF_project.DF_supplier.supplier import find_account_cards, update_account_information, add_supplier_cards
from case.DF_project.DF_supplier.supplier import account_resetPWD, Add_supplier_card
from case.DF_project.DF_supplier.supplier import update_supplier_infor, approve_supplier_card, supplier_loadown_template,import_company
from case.DF_project.DF_supplier.read_yaml import yaml_path, updata_company, find_company_infor, find_account_lists
from case.DF_project.DF_supplier.read_yaml import update_account_informations
real_path = os.path.dirname(os.path.realpath(__file__))
# 新增公司信息数据
curpathread = os.path.join(real_path, "supplier_company")
yaml_data = yaml_path(curpathread)['add_company']
# 修改公司信息数据
updata_data = updata_company(curpathread)['updata_company_information']
# 查询公司档案信息数据
find_company = find_company_infor(curpathread)['find_supplier_infor']
# 查询账号管理列表数据
find_account = find_account_lists(curpathread)['find_account_lists']
# 修改账号信息数据
update_information=update_account_informations(curpathread)['update_account_information']


'''
@allure.severity按严重性级别来标记case　　　
执行指定测试用例 --allure-severities blocker
BLOCKER = 'blocker'　　阻塞缺陷
CRITICAL = 'critical'　严重缺陷
NORMAL = 'normal'　　  一般缺陷
MINOR = 'minor'　　    次要缺陷
TRIVIAL = 'trivial'　　轻微缺陷　
'''


@allure.story("新增公司信息")
@allure.severity("blocker")
@allure.title("验证新增公司信息有效性")
def test_save_supplier_information_01(df_login_xadmin, delete_register, delete_account_infor):
    '''
    新建公司信息，如果数据库中有这条数据就先删除该数据
    '''
    s = df_login_xadmin
    DF_Login(s)
    save = save_supplier_information(s)
    # delete_account_infor()
    assert save['code'] == 0
    assert save['message'] == None


# @allure.feature("供应商模块")
@allure.story("新增公司信息")
@allure.severity("normal")
@pytest.mark.parametrize("taxpayerType,companyName,legalPeople,"
                         "companyAddress, taxpayerNumber,"
                         "bankCode,simpleName,basicAccount,bankName,bankAccountName,expected",
                         yaml_data,

                         ids=[
                             "新增公司档案，未填写公司名称,异常场景-新建失败",
                             "新增公司档案，未填写銀行基本戶帳號,异常场景-新建失败",
                             "新增公司档案，未填写納稅識別號,异常场景-新建失败",
                             "新增公司档案，未填写銀行開戶名,异常场景-新建失败"
                             ])
def test_add_company_information_02(df_login_xadmin, taxpayerType, companyName, legalPeople,
                                     companyAddress, taxpayerNumber,bankCode,simpleName,basicAccount,
                                     bankName,bankAccountName,expected):
    with allure.step("step1 :登录"):
        s = df_login_xadmin
        DF_Login(s)
    with allure.step("step2 :新增公司信息"):
        add_supplier = save_supplier_information(s, taxpayerType=taxpayerType, companyName=companyName, legalPeople=legalPeople,
                                                 companyAddress=companyAddress, taxpayerNumber=taxpayerNumber, bankCode=bankCode,
                                                 simpleName=simpleName, basicAccount=basicAccount,
                                                 bankName=bankName, bankAccountName=bankAccountName)
    with allure.step("step3 :断言"):
        assert add_supplier['succ'] == expected['succ']


# @allure.feature("供应商模块")
@allure.story("新增公司信息")
@allure.severity("normal")
@allure.title("验证公司名稱+銀行開戶名+銀行賬號重復，公司信息无法新增")
# @allure.testcase("")
def test_add_company_information_03(df_login_xadmin):
    '''
    当公司名稱+銀行開戶名+銀行賬號重復,不允許新建公司信息
    '''
    s = df_login_xadmin
    add_company = save_supplier_information(s, taxpayerType="Z1", companyName="深圳大源源呐939", legalPeople="大源源",
                                            companyAddress="2222", taxpayerNumber="111111111111111", bankCode="1111111111",
                                            simpleName="11111", basicAccount="11111111112",
                                            bankName="建行", bankAccountName="建行西丽分行1")
    print("@##@#@##@#@", add_company)
    print("33333333333333333333")
    add_company = save_supplier_information(s, taxpayerType="Z1", companyName="深圳大源源呐939", legalPeople="大源源",
                                            companyAddress="2222", taxpayerNumber="111111111111111", bankCode="1111111111",
                                            simpleName="11111", basicAccount="11111111112",
                                            bankName="建行", bankAccountName="建行西丽分行1")
    assert add_company['data']['companyName'] == "公司名稱+銀行開戶名+銀行賬號重復,不允許新建公司信息"
    assert add_company['succ'] == True


# @allure.feature("供应商模块")
@allure.story("查询公司信息详情")
@allure.severity("normal")
@allure.title("验证查询公司信息详情有效性")
def test_check_supplier_information_04(df_login_xadmin, delete_register):
    '''
    验证输入有效的id，查询公司信息详情有效性
    前置:登录
    用例步骤：1.先将数据库的数据进行清理 2.新增供应商公司档案 3.点击查看该公司档案详情
    '''
    s = df_login_xadmin
    DF_Login(s)
    with allure.step("step1 :删除数据后新增.点击查看该公司档案详情"):
        check_supplier=check_supplier_information(s)
    with allure.step("step2 :断言"):
        assert check_supplier['succ'] == True
        assert check_supplier['code'] == 0


# @allure.feature("供应商模块")
@allure.story("修改公司信息")
@allure.severity("normal")
@pytest.mark.parametrize("taxpayerType, companyName,"
                         "legalPeople,companyAddress, taxpayerNumber,"
                         "bankCode,simpleName,basicAccount,bankName,"
                         "bankAccountName,mainName,mainPhone,expected",
                         updata_data,
                         ids=[
                             "1.修改公司信息中纳税类型, 修改成功",
                             "2.修改公司信息中公司名称, 修改成功",
                             "3.修改公司信息中修改法人, 修改成功",
                             "4.修改公司信息中修改公司地址, 修改成功",
                             "5.修改公司信息中纳税人识别号, 修改成功",
                             "6.修改公司信息中支行联行号, 修改成功",
                             "7.修改公司信息中公司简称, 修改成功",
                             "8.修改公司信息中银行账号, 修改成功",
                             "9.修改公司信息中开户银行, 修改成功",
                             "10.修改公司信息中開戶銀行名, 修改成功",
                             "11.修改公司信息中公司联系人, 修改成功",
                             "12.修改公司信息中公司联系人手机号, 修改成功"
                                ])
def test_update_supplier_infor_05(df_login_xadmin,delete_register,taxpayerType, companyName,legalPeople,companyAddress,
                                     taxpayerNumber,bankCode,simpleName,basicAccount,bankName,bankAccountName,
                                     mainName,mainPhone,expected):
    '''
    验证修改公司信息字段的有效性
    '''
    # s = df_login_xadmin
    # DF_Login(s)
    print("测试第一步")
    with allure.step("step1 :登录"):
        s = df_login_xadmin
        DF_Login(s)
    with allure.step("step2 :新增公司信息后，修改公司信息字段"):
        update_infor = update_supplier_infor(s, taxpayerType=taxpayerType, companyName=companyName, legalPeople=legalPeople,
                                             companyAddress=companyAddress, taxpayerNumber=taxpayerNumber, bankCode=bankCode,
                                             simpleName=simpleName, basicAccount=basicAccount, bankName=bankName,
                                             bankAccountName=bankAccountName, mainName=mainName, mainPhone=mainPhone)
    with allure.step("step3 :断言"):
        assert update_infor['data'] == expected['data']
        assert update_infor['succ'] == expected['succ']


@pytest.mark.parametrize("pageSize,currentPage,companyName,expected",
                         find_company,
                         ids=[
                             "1.一页10条，第一页，查询公司档案列表, 成功 ",
                             "2.一页20条，第一页，查询公司档案列表, 成功 ",
                             "3.一页50条，第一页，查询公司档案列表, 成功 ",
                             "4.一页100条，第一页，查询公司档案列表, 成功 ",
                             "5.数据量足够时，一页10条，随机第3页，查询公司档案列表, 成功 ",
                             "6.数据量足够时，一页20条，随机第3页，查询公司档案列表, 成功 ",
                             "7.数据量足够时，一页50条，随机第3页，查询公司档案列表, 成功 ",
                             "8.数据量足够时，一页100条，随机第3页，查询公司档案列表, 成功 ",
                             "9.公司名称为查询条件，查询该公司名称档案信息"
                             # "9.当传入的页数和页面均为空时，查询公司档案列表, 失败 ",
                                ])
# @allure.feature("供应商模块")
@allure.story("查询公司信息列表")
@allure.severity("normal")
def test_find_supplier_infor_06(df_login_xadmin, pageSize, currentPage, companyName, expected):
    '''
    验证查询公司档案列表有效性
    '''
    with allure.step("step1 :登录"):
        s = df_login_xadmin
    DF_Login(s)
    with allure.step("step2 :点击查询按钮，或输入查询条件，再进行查询"):
        find_infor = find_supplier_infor(s, pageSize=pageSize, currentPage=currentPage, companyName=companyName)
    with allure.step("step3 :断言"):
        assert find_infor['succ'] == expected['succ']
        assert find_infor['code'] == expected['code']


# @allure.feature("供应商模块")
@allure.story("查询公司信息列表")
@allure.title("验证当页数，页码为空时，无法查询")
@allure.severity("normal")
def test_find_supplier_infor_07(df_login_xadmin):
    '''
    验证当页数，页码为空时，无法查询
    '''
    s = df_login_xadmin
    DF_Login(s)
    find_infor = find_supplier_infor(s, pageSize="", currentPage="")
    assert find_infor['code'] == 100
    assert find_infor['succ'] == False


@allure.story("公司信息模板下载")
@allure.title("验证公司信息模板下载有效性")
@allure.severity("critical")
def test_download_template_08(df_login_xadmin):
    '''
    验证公司信息模板下载的有效性
    '''
    with allure.step("step1 :登录 "):
        s = df_login_xadmin
        DF_Login(s)
    with allure.step("step2 :点击下载模板按钮 "):
        load_template=supplier_loadown_template(s)
    with allure.step("step3 :断言 "):
        assert load_template == 200


@allure.story("模板导入")
@allure.title("验证公司档案信息模板可成功导入")
@allure.severity("critical")
def test_import_company_09(df_login_xadmin):
    '''
    验证公司档案信息模板导入功能有效性
    '''
    with allure.step("step1 :登录"):
        s = df_login_xadmin
        DF_Login(s)
    with allure.step("step2 :编辑相对应的模板，点击导入"):
        list_company = import_company(s, name="供商公司導入模板 (4).xls")
    with allure.step("step3 :断言"):
        assert list_company['succ'] == True
        assert list_company['code'] == 0


@pytest.mark.skip("导入不填写字段，也可导入，待定")
@allure.story("模板导入")
@allure.title("验证公司档案信息模板不可导入")
@allure.severity("critical")
def test_import_company_10(df_login_xadmin):
    '''
    验证公司档案信息模板导入功能有效性
    '''
    s = df_login_xadmin
    DF_Login(s)
    list_company = import_company(s, name="供商公司導入模板.xls")      # 效验字段，文件里会有多种情况
    assert list_company['succ'] == True
    assert list_company['code'] == 0


@pytest.mark.parametrize("pageSize,currentPage,supplierName,expected",
                         find_account,
                         ids=[
                             "1.一页10条，第一页，查询账号管理列表, 成功 ",
                             "2.一页20条，第一页，查询账号管理列表, 成功 ",
                             "3.一页50条，第一页，查询账号管理列表, 成功 ",
                             "4.一页100条，第一页，查询账号管理列表, 成功 ",
                             "5.数据量足够时，一页10条，随机第3页，查询账号管理列表, 成功 ",
                             "6.数据量足够时，一页20条，随机第3页，查询账号管理列表, 成功 ",
                             "7.数据量足够时，一页50条，随机第3页，查询账号管理列表, 成功 ",
                             "8.数据量足够时，一页100条，随机第3页，查询账号管理列表, 成功 ",
                             "9.供商名称为查询条件，查询该供商名称账号信息"
                            ])
@allure.story("查询账号管理列表")
@allure.severity("normal")
def test_find_account_list_11(df_login_xadmin, pageSize, currentPage, supplierName, expected):
    '''
    验证点击账号管理列表接口查询有效性
    '''
    with allure.step("step1 : 登录"):
        s = df_login_xadmin
        DF_Login(s)
    with allure.step("step2 : 点击账号管理列表查询按钮"):
        find_list = find_account_list(s, pageSize=pageSize, currentPage=currentPage, supplierName=supplierName)
    with allure.step("step3 : 断言"):
        assert find_list['succ'] == expected['succ']
        assert find_list['code'] == expected['code']


# @allure.story("查询账号管理列表")
# @allure.title("验证当页数，页码为空时，无法查询")
# @allure.severity("normal")
# def test_find_supplier_infor_06(df_login_xadmin):
#     '''
#     验证当页数，页码为空时，无法查询
#     '''
#     s = df_login_xadmin
#     DF_Login(s)
#     find_infor = find_supplier_infor(s, pageSize="", currentPage="", companyName='')
#     assert find_infor['code'] == 100
#     assert find_infor['succ'] == False


@allure.story("查询账号卡号信息")
@allure.title("验证查询卡号信息功能有效性")
@allure.severity("normal")
def test_find_account_cards_12(df_login_xadmin):
    '''
    验证查看账号卡号功能的有效性（没有卡号）
    :return:
    '''
    s = df_login_xadmin
    DF_Login(s)
    find_cards = find_account_cards(s)
    assert find_cards['succ'] == True
    assert find_cards['data']['pageSize'] == 20


@allure.story("修改账号信息")
@allure.severity("normal")
@pytest.mark.parametrize("mobile,contacts,email,status,expected",
                         update_information,
                         ids=[
                              "1.修改账号信息--手机号 ,成功",
                              "2.修改账号信息 -- 联系人 ,成功",
                              "3.修改账号信息 -- 邮箱 ,成功",
                              "4.修改账号信息--手机号（为空） ,成功",      # 建议前后端做限制
                              "5.修改账号信息--联系人（为空） ,成功",
                              "6.修改账号信息--邮箱（为空） ,成功",
                              "7.修改账号信息--账号状态（正常） ,成功",
                              "8.修改账号信息--邮箱（禁用） ,成功",

                              ])
def test_update_account_information_13(df_login_xadmin, mobile, contacts, email,status,expected):
    '''
    验证修改账号信息的有效性
    '''
    with allure.step("step1 : 登录"):
        s = df_login_xadmin
        DF_Login(s)
    with allure.step("step2 : 修改账号信息字段"):
        account_information = update_account_information(s, mobile=mobile, contacts=contacts, email=email, status=status)
        print("@@@@@@@",account_information)
    with allure.step("step3 : 断言"):
        assert account_information['succ'] == expected["succ"]
        assert account_information['code'] == expected['code']


def account_resetpwd_14(df_login_xadmin):
    '''
    验证修改密码的有效性
    '''
    with allure.step("step1 :登录"):
        s = df_login_xadmin
        DF_Login(s)
    with allure.step("step2 :获取新增公司信息的供商账号字段"):
        account_reset = find_supplier_infor(s)
        account_resets = account_reset['data']['list'][0]['groupNo']
    with allure.step("step3 :获取账号管理中的与新增公司信息的供商名称相对应的数据"):
        account_list = find_account_list(s, pageSize="20", currentPage="1", supplierName="深圳大源源呐939")
        print(account_list['data']['list'][0]['mobile'])
        account_lists = account_list['data']['list'][0]['mobile']
    with allure.step("step4 :点击修改密码按钮"):
        accountet = account_resetPWD(s, supplierAccount=account_resets, contactsPhone=account_lists)
    with allure.step("step5 :断言"):
        assert accountet['data'] == "密碼重置完成,信息已發送到該供應商聯系電話上"
        assert accountet['succ'] == True


class TestClass_card:
    '''
    卡号管理用例
    '''
    def test_card_list(self, df_login_xadmin):
        '''
        验证查询卡号管理列表功能有效性
        '''
        s = df_login_xadmin
        DF_Login(s)
        card_list = Add_supplier_card(s).card_list()
        assert card_list['succ'] == True
        assert card_list['data']['pageSize'] == 20

    def test_add_aupplier(self, df_login_xadmin, delete_cards_infor):
        '''
        验证新增供应商（卡号）有效性
        '''
        s = df_login_xadmin
        DF_Login(s)
        add_supplier = add_supplier_cards(s)
        assert add_supplier['data'] == '操作成功'
        assert add_supplier['code'] == 0


    def test_approve_supplier_card(df_login_xadmin,delete_cards_infor):
        '''
        验证审核有效性
        '''
        s = df_login_xadmin
        DF_Login(s)
        add_supplier_cards(s)
        approve = approve_supplier_card(s)
        assert approve['data'] == '審批完成'
        assert approve['succ'] == True









