import allure
import pytest

from common import excel_oper
from common.logger import logger
from operation.services import field_addOrUpdateInterface
from testcases.conftest import api_data


@allure.epic("XG9-S8系统接口自动化测试")
@allure.feature("SOA服务管理-服务")
class TestAddOrUpdateInterface():
    @allure.story("接口09--接口field新增更新接口")
    @allure.description("该用例是接口新增更新接口")
    @allure.title("测试数据：【{except_testcase_description}】")
    @pytest.mark.parametrize(
        "servicePid,serviceInterfaceType,fieldInterfaceList, except_code, except_result, "
        "except_testcase_description",
        api_data["test_services_field_addOrUpdateInterface"])
    def test_services_field_addOrUpdateInterface(self, servicePid, serviceInterfaceType, fieldInterfaceList,
                                                 except_code, except_result,
                                                 except_testcase_description):
        logger.info("*************** 开始执行用例 ***************")
        # 调用operation中的query_by_page方法
        result = field_addOrUpdateInterface(servicePid, serviceInterfaceType, fieldInterfaceList)
        excel_oper.write_data(result, "SOA服务管理-服务", "接口field新增更新接口", except_code, result.success == except_result,
                              except_result)
        # 断言返回的结果是否等于yml,定义的值
        assert result.success == except_result
        if result.success:
            assert result.code == except_code
            # logger.info("code ==>> 期望数据条数：{}， 实际数据条数：【 {} 】".format(except_code,  result.code))
        else:
            assert result.code != except_code
        # logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.code))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    # 执行用例并生成allure测试报告
    pytest.main(['-s', './test_09_field_addOrUpdateInterface.py'])
    # pytest.main(['-s', './test_03_addOrUpdateMetaService.py', '--alluredir', './result/'])
    # os.system('allure generate ./result/ -o ./report/ --clean')
