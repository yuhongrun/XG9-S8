import allure
import pytest

from common import excel_oper
from common.logger import logger
from operation.platform import updatePlatform
from testcases.conftest import api_data


@allure.epic("XG9-S8系统接口自动化测试")
@allure.feature("SOA架构管理-平台")
class TestUpdatePlatform():
    @allure.story("接口02--更新平台架构")
    @allure.description("该用例是更新平台架构")
    # @allure.issue("http://106.55.79.143/", name="生产环境系统地址")
    # @allure.testcase("http://106.55.79.143/", name="测试环境系统地址")
    @allure.title("测试数据：【{except_testcase_description}】")
    @pytest.mark.parametrize(
        "id,platformCnName,platformName,description,except_code,except_result,except_msg,except_testcase_description",
        api_data["test_platform_updatePlatform"])
    def test_platform_updatePlatform(self, id, platformCnName, platformName, description, except_code, except_result,
                                     except_msg, except_testcase_description):
        logger.info("*************** 开始执行用例 ***************")
        # 调用operation中的query_by_page方法
        result = updatePlatform(id, platformCnName, platformName, description)
        excel_oper.write_data(result, "SOA服务管理-平台", "更新平台架构", except_code, result.success == except_result,
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
        if not result.success:
            assert result.error == except_msg
        # logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.code))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    # # 执行用例并生成allure测试报告
    pytest.main(['-s', './test_02_updatePlatform.py', '--alluredir', './result/'])
    # os.system('allure generate ./result/ -o ./report/ --clean')
