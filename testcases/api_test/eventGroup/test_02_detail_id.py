import allure
import pytest

from common import excel_oper
from common.logger import logger
from operation.eventGroup import detail_id
from testcases.conftest import api_data


@allure.epic("XG9-S8系统接口自动化测试")
@allure.feature("SOA服务管理-事件组")
class TestDetailId():

    @allure.story("接口02--事件组详情")
    @allure.description("该用例是查询事件组详情")
    @allure.issue("http://106.55.79.143/", name="S8系统地址")
    @allure.testcase("http://106.55.79.143/", name="S8系统地址")
    @allure.title("测试数据：【{except_testcase_description}】")
    @pytest.mark.parametrize("id, except_result , except_code ,except_testcase_description",
                             api_data["test_eventGroup_detail_id"])
    def test_detail_id(self, id, except_result, except_code, except_testcase_description):
        logger.info("*************** 开始执行用例 ***************")
        result = detail_id(id)
        excel_oper.write_data(result, "SOA服务管理-事件组", "事件组详情", except_code,
                              result.success == except_result,
                              except_result)
        # is_succ = result.success == except_result
        # param = username + password +
        # excel_result = ["用户登录模块", "登录用户", result.response.url, str(result.response.request.body),
        #                 str(except_code),xxxxx
        #                 str(result.response.json().get("code")), str(is_succ)]
        # excel_oper.write_excel(excel_result)
        assert result.success == except_result
        # if result.success:
        #     assert result.code == except_code
        # else:
        #     assert result.code != except_code
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.code))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':

    # # 执行用例并生成allure测试报告
    pytest.main(['-s', './test_02_detail_id.py', '--alluredir', './result/'])
    # os.system('allure generate ./result/ -o ./report/ --clean')