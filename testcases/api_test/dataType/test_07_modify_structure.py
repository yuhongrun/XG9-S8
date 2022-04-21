import allure
import pytest

from common import excel_oper
from common.logger import logger
from operation.data_type import modify_structure
from testcases.conftest import api_data


@allure.epic("XG9-S8系统接口自动化测试")
@allure.feature("管理后台--数据类型")
class Testmodify_structure():

    @allure.story("接口07--修改数据类型结构体")
    @allure.description("该用例是修改数据类型结构体")
    # @allure.issue("http://106.55.79.143:30441/", name="s8系统地址")
    # @allure.testcase("http://106.55.79.143:30441/", name="s8系统地址")
    @allure.title(
        "测试数据：【 {except_testcase_description}】")
    @pytest.mark.parametrize(
        "id,namePrefix,name,category,baseDatatype,description,refDataTypeId,name1,unit,except_result,except_code,except_testcase_description",
        api_data["test_dataType_modify_structure"])
    def test_post_modify_structure(self, id, namePrefix, name, category, baseDatatype, description, refDataTypeId, name1,
                                   unit, except_result, except_code,except_testcase_description):
        logger.info("*************** 开始执行用例 ***************")
        # 调用operation中的方法
        result = modify_structure(id, namePrefix, name, category, baseDatatype, description, refDataTypeId, name1, unit)
        excel_oper.write_data(result, "管理后台--数据类型", "修改数据类型结构体", except_code,
                              result.success == except_result,
                              except_result)
        # is_succ = result.success == except_result
        # param = username + password +
        # excel_result = ["用户登录模块", "登录用户", result.response.url, str(result.response.request.body),
        #                 str(except_code),
        #                 str(result.response.json().get("code")), str(is_succ)]
        # excel_oper.write_excel(excel_result)
        assert result.success == except_result  # 实际结果成功==期望结果
        assert result.code == except_code
        # if result.success:                       #如果成功
        #     assert result.code == except_code       #那么返回状态码==期望状态码
        # else:
        #     assert result.code != except_code          #否则返回状态码不等于期望状态码

        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.code))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    # # 执行用例并生成allure测试报告
    pytest.main(['-s', './test_07_modify_structure.py', '--alluredir', './result/'])
    # os.system('allure generate ./result/ -o ./report/ --clean')
