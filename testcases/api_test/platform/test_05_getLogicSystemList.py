import allure
import pytest
import os

from common import excel_oper
from common.logger import logger
from operation.platform import getLogicSystemList
from testcases.conftest import api_data


@allure.epic("XG9-S8系统接口自动化测试")
@allure.feature("SOA架构管理-平台")
class TestGetLogicSystemList():
    @allure.story("接口05--子系统列表查询")
    @allure.description("该用例是查询子系统")
    # @allure.issue("http://106.55.79.143/", name="生产环境系统地址")
    # @allure.testcase("http://106.55.79.143/", name="测试环境系统地址")
    @allure.title("测试数据：【{except_testcase_description}】")
    @pytest.mark.parametrize(
        "page_index, page_size,domainPid, platformPid, subSysName, "
        "except_code, except_result, except_msg, except_testcase_description",
        api_data["test_platform_getLogicSystemList"])
    def test_platform_getLogicSystemList(self, page_index, page_size, domainPid, platformPid, subSysName,
                                         except_code, except_result, except_msg, except_testcase_description):
        logger.info("*************** 开始执行用例 ***************")
        # 调用operation中的query_by_page方法
        result = getLogicSystemList(page_index, page_size, domainPid, platformPid, subSysName)
        excel_oper.write_data(result, "SOA服务管理-平台", "子系统列表查询", except_code, result.success == except_result,
                              except_result)
        # is_succ = result.success == except_result
        # param = username + password +
        # excel_result = ["用户登录模块", "登录用户", result.response.url, str(result.response.request.body),
        #                 str(except_code),
        #                 str(result.response.json().get("code")), str(is_succ)]
        # excel_oper.write_excel(excel_result)
        # 断言返回的结果是否等于yml,定义的值
        assert result.success == except_result
        assert result.code == except_code
        if result.success:
            if result is not None and result.msg is not None and len(result.msg.get("list")):
                for data in result.msg.get("list"):
                    if domainPid != "" and domainPid != "None":
                        assert domainPid == data.get("domainPid")
                    if platformPid != "" and platformPid != "None":
                        assert platformPid == data.get("platformPid")
                    if subSysName != "" and subSysName != "None":
                        assert subSysName in data.get("subSysName") or subSysName in data.get("subSysCnName")
        else:
            assert result.error == except_msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    # # 执行用例并生成allure测试报告
    pytest.main(['-s', './test_05_getLogicSystemList.py', '--alluredir', './result/'])
    # os.system('allure generate ./result/ -o ./report/ --clean')
