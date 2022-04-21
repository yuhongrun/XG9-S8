import allure
import pytest
import os

from common import excel_oper
from common.logger import logger
from operation.element_model import get_Meta_ServiceInterFaceList
from testcases.conftest import api_data


@allure.epic("XG9-S8系统接口自动化测试")
@allure.feature("车型元模型管理")
class Test_get_Meta_ElementTree():
    @allure.story("接口06-车元模型—关联详情—接口列表")
    @allure.description("该用例是元模型元素查询数据")
    # @allure.issue("http://106.55.79.143/", name="生产环境系统地址")
    # @allure.testcase("http://106.55.79.143/", name="测试环境系统地址")
    @allure.title("测试数据：【{except_testcase_description}】")
    @pytest.mark.parametrize("page_size, page_index, series_code, model_code, platform_id, status, interface_name, "
                             "interface_bid,field_property, service_interface_type, service_pid, except_result, "
                             "except_code, except_testcase_description",
                             api_data["test_06_element_model_get_Meta_ServiceInterFaceList"])
    def test_get_Meta_ServiceInterFaceList(self, page_size, page_index, series_code, model_code, platform_id, status, interface_name, interface_bid,
                    field_property, service_interface_type, service_pid, except_result, except_code, except_testcase_description):
        logger.info("*************** 开始执行用例 ***************")
        # 调用operation中的query_by_page方法
        result = get_Meta_ServiceInterFaceList(page_size, page_index, series_code, model_code, platform_id, status,
                                               interface_name, interface_bid, field_property, service_interface_type, service_pid)
        excel_oper.write_data(result, "车型元模型管理", "接口列表", except_code,
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
        assert result.code == except_code
        if result.success:
            assert result.code == except_code
            # logger.info("code ==>> 期望数据条数：{}， 实际数据条数：【 {} 】".format(except_code,  result.code))

        # logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.code))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    # # 执行用例并生成allure测试报告
    pytest.main(['-s', './test_06_getMetaServiceInterfaceList.py', '--alluredir', './result/'])
    # os.system('allure generate ./result/ -o ./report/ --clean')
