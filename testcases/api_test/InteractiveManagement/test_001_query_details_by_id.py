import allure
import pytest
import os

from common import excel_oper
from common.logger import logger
from operation.InteractiveManagement import query_details_by_id
from testcases.conftest import api_data


@allure.epic("XG9-S8系统接口自动化测试")
@allure.feature("API-对外接口服务-交互管理")
class TestGetPlatformList():
    @allure.story("接口01--根据交互接口ID集合查询交互接口详情")
    @allure.description("该用例是根据交互接口ID集合查询交互接口详情")
    # @allure.issue("http://106.55.79.143/", name="生产环境系统地址")
    # @allure.testcase("http://106.55.79.143/", name="测试环境系统地址")
    @allure.title("测试数据：【{except_testcase_description}】")
    @pytest.mark.parametrize(
        "idList,pageIndex ,pageSize,except_result,except_code,except_testcase_description",
        api_data["test_query_details_by_id"])
    def test_post_query_details_by_id(self, idList,pageIndex ,pageSize,except_result,except_code,except_testcase_description):
        logger.info("*************** 开始执行用例 ***************")
        # 调用operation中的query_by_page方法
        result = query_details_by_id(idList,pageIndex ,pageSize,)
        excel_oper.write_data(result, "API-对外接口服务-交互管理", "根据交互接口ID集合查询交互接口详情", except_code, result.success == except_result,
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
            if idList != "None" and idList != "":                               #如果传参idList不为空和传参，那么判断
                if result.msg is not None and len(result.msg.get("list")) > 0:   #如果返回的数据不为空并且数据中返回的数据中有列表数据并且数据大于0，那么
                    is_succ = False                                             #首先定义这条用例失败
                    for id in idList:                                           #判断id是否在idList列表中
                        for data in result.msg.get("list"):                     #遍历idList列表中的数据
                           if id == data.get("id"):                             #如果传参数组里面的id和返回数据里id相等
                               is_succ = True                                   #那么定义这条用例成功
                    assert is_succ                                               #返回结果成功
        else:
            assert result.error != except_code
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.code))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    # # 执行用例并生成allure测试报告
    pytest.main(['-s', './test_001_query_details_by_id.py', '--alluredir', './result/'])
    # os.system('allure generate ./result/ -o ./report/ --clean')
