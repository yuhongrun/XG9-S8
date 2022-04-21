import allure
import pytest
import os

from common import excel_oper
from common.logger import logger
from operation.data_type import postdata_type_list_query
from testcases.conftest import api_data


@allure.epic("XG9-S8系统接口自动化测试")
@allure.feature("管理后台--数据类型")
class Test_dataType_data_type_list_query():
    @allure.story("接口05--数据类型列表查询")
    @allure.description("该用例是数据类型列表查询")
    @allure.title("测试数据：【{except_testcase_description}】")
    @pytest.mark.parametrize(
        "pageSize,pageIndex,name,except_code,except_result,except_testcase_description",
        api_data["test_dataType_test_05_data_type_list_query"])
    def test_05_data_type_list_query(self, pageSize, pageIndex, except_code, name, except_result, except_testcase_description):
        logger.info("*************** 开始执行用例 ***************")
        # 调用operation中的query_by_page方法
        result = postdata_type_list_query(pageSize, pageIndex, name)
        excel_oper.write_data(result, "管理后台--数据类型", "数据类型列表查询", except_code,
                              result.success == except_result,
                              except_result)
        # is_succ = result.success == except_result
        # param = username + password +
        # excel_result = ["用户登录模块", "登录用户", result.response.url, str(result.response.request.body),
        #                 str(except_code),
        #                 str(result.response.json().get("code")), str(is_succ)]
        # excel_oper.write_excel(excel_result)
        # 断言返回的结果是否等于yml,定义的值
        assert result.success == except_result
        if result.success:
            assert result.code == except_code
            # logger.info("code ==>> 期望数据条数：{}， 实际数据条数：【 {} 】".format(except_code,  result.code))
        else:
            assert result.error != except_code
        # logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.code))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    # # 执行用例并生成allure测试报告
    pytest.main(['-s', './test_05_data_type_list_query.py', '--alluredir', './result/'])
    # os.system('allure generate ./result/ -o ./report/ --clean')
