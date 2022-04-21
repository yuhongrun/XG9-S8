import allure
import pytest

from common import excel_oper
from common.logger import logger
from operation.InteractiveManagement import get_interactive_interface_list
from testcases.conftest import api_data


@allure.epic("XG9-S8系统接口自动化测试")
@allure.feature("API-对外接口服务-交互管理")
class TestGetinteractiveinterfacelist():
    @allure.story("接口02--获取交互接口列表")
    @allure.description("该用例是获取交互接口列表")
    @allure.issue("http://106.55.79.143/", name="生产环境系统地址")
    @allure.testcase("http://106.55.79.143/", name="测试环境系统地址")
    @allure.title("测试数据：【{except_testcase_description}】")
    @pytest.mark.parametrize(
        "category,pageIndex,pageSize,interfaceName,servicePid,modelCodeList,except_result,except_code,except_testcase_description",
        api_data["test_get_interactive_interface_list"])
    def test_post_get_interactive_interface_list(self, category, pageIndex , pageSize , interfaceName, servicePid,modelCodeList, except_result,except_code,except_testcase_description
                                      ):
        logger.info("*************** 开始执行用例 ***************")
        # 调用operation中的get_interactive_interface_list方法
        result = get_interactive_interface_list(category,pageIndex,pageSize,interfaceName,servicePid,modelCodeList)
        excel_oper.write_data(result, "API-对外接口服务-交互管理", "获取交互接口列表", except_code, result.success == except_result,
                              except_result)
        # is_succ = result.success == except_result
        # param = username + password +
        # excel_result = ["用户登录模块", "登录用户", result.response.url, str(result.response.request.body),
        #                 str(except_code),
        #                 str(result.response.json().get("code")), str(is_succ)]
        # excel_oper.write_excel(excel_result)
        # 断言返回的结果是否等于yml,定义的值
        assert result.success == except_result
        # assert result.code == except_code
        if result.success:
            if result.msg is not None and len(result.msg.get("list")) > 0:  #如果返回结果不为空并且返回结果里面有列表
                if interfaceName != "None" and interfaceName != "":      #如果interfaceName不传参并且interfaceName不为空
                    for data in result.msg.get("list"):           #那就遍历返回数据里面的列表
                        assert interfaceName in data.get("interfaceName")   #检查interfaceName是否在返回的数据中
        else:
            assert result.error != except_code
                # if servicePid != "None" and servicePid != "":
                #     for data in result.msg.get("list"):
                #         assert servicePid == data.get("servicePid")   这个断言暂时不用
        # logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.code))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    # # 执行用例并生成allure测试报告
    pytest.main(['-s', './test_002_get_interactive_interface_list.py', '--alluredir', './result/'])
    # os.system('allure generate ./result/ -o ./report/ --clean')
