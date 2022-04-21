import os
import allure
import pytest

from common import excel_oper
from common.logger import logger
from operation.data_type import delete_data_type
from testcases.conftest import api_data


@allure.epic("XG9-S8系统接口自动化测试")
@allure.feature("管理后台--数据类型")
class Testdeletebyid():

    @allure.story("接口04--删除数据类型")
    @allure.description("该用例删除数据类型")
    # @allure.issue("http://106.55.79.143:30441/", name="s4系统地址")
    # @allure.testcase("http://106.55.79.143:30441/", name="s4系统地址")
    @allure.title("测试数据：【 {except_testcase_description}】")
    @pytest.mark.parametrize(
        "id, except_result, except_code, except_testcase_description",
        api_data["test_04_delete_data_type"])
    def test_delete_data_type(self, id, except_result, except_code, except_testcase_description):
        logger.info("*************** 开始执行用例 ***************")
        # 调用operation中的方法
        result = delete_data_type(id)
        excel_oper.write_data(result, "管理后台--数据类型", "删除数据类型", except_code,
                              result.success == except_result,
                              except_result)
        # is_succ = result.success == except_result
        # param = username + password +
        # excel_result = ["用户登录模块", "登录用户", result.response.url, str(result.response.request.body),
        #                 str(except_code),
        #                 str(result.response.json().get("code")), str(is_succ)]
        # excel_oper.write_excel(excel_result)
        # assert result.success == except_result
        assert result.code == except_code
        assert result.code == except_code

        # if result.success:
        #     assert result.msg == except_msg
        # else:
        #     assert result.error == except_msg

        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.code))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    # # 执行用例并生成allure测试报告
    pytest.main(['-s', './test_04_delete_data_type.py', '--alluredir', './result/'])
    # os.system('allure generate ./result/ -o ./report/ --clean')
