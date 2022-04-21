from api.data_type import data_type
from common.logger import logger
from config import http_config
from core.result_base import ResultBase


# 数据类型
# name,description,category,base_datatype,name_Prefix
# 01新增
def postNewdatatypenonstruche(name=None, description=None, category=None, baseDatatype=None, namePrefix=None,
                              discretes=None, resolution=None):
    result = ResultBase()
    json = {}
    # pageInfo = {}
    discrete = []
    discrete_data = {}
    data = {}
    if namePrefix != 'None':
        data["namePrefix"] = namePrefix
    if name != 'None':
        data["name"] = name
    if description != 'None':
        data["description"] = description
    if category != 'None':
        data["category"] = category
    if baseDatatype != 'None':
        data["baseDatatype"] = baseDatatype
    if discretes != 'None':
        data["discretes"] = discrete
    if resolution != 'None':
        data["resolution"] = resolution

    json["data"] = data
    # json["pageInfo"] = pageInfo

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = data_type.post_new_data_type_non_structure(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("新增数据类型非结构体 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


# 02 修改

def postModifydatatypenonstruche(id=None, namePrefix=None, name=None, category=None, baseDatatype=None, unit=None):
    result = ResultBase()
    json = {}
    # pageInfo = {}
    data = {}
    if id != 'None':
        data["id"] = id
    if namePrefix != 'None':
        data["namePrefix"] = namePrefix
    if name != 'None':
        data["name"] = name
    if category != 'None':
        data["category"] = category
    if baseDatatype != 'None':
        data["baseDatatype"] = baseDatatype
    if unit != 'None':
        data["unit"] = unit

    json["data"] = data
    # json["pageInfo"] = pageInfo

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = data_type.post_modify_data_type_non_structure(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("修改数据类型非结构体 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


# 03 获取详情结构体
def getgetdetailsnonstructure(id=None):
    result = ResultBase()
    # json = {}
    # pageInfo = {}
    data = {}
    if id != 'None':
        data["id"] = id

    # json["data"] = data
    # json["pageInfo"] = pageInfo

    headers = http_config.param_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = data_type.get_detail_structure(params=data, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("修改数据类型非结构体 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


#  05 数据类型列表查询
def postdata_type_list_query(pageSize=None, pageIndex=None, name=None):
    result = ResultBase()
    json = {}
    pageInfo = {}
    data = {}

    if pageSize != 'None':
        pageInfo["pageSize"] = pageSize
    if pageIndex != 'None':
        pageInfo["pageIndex"] = pageIndex
    if name != 'None':
        pageInfo["name"] = name

    json["data"] = data
    json["pageInfo"] = pageInfo

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = data_type.post_data_type_list_query(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("数据类型列表查询 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


# 06 新增数据类型结构体
def new_data_type_structure(namePrefix=None, name=None, category=None, description=None,
                            refDataTypeId=None, baseDatatype=None, name1=None, unit=None):
    result = ResultBase()
    json = {}
    members = []
    members_data = {"discretes": []}
    # members_data["baseDatatype"]="uint16"
    members_data["description"] = ""
    # members_data["preDataTypeId"] = refDataTypeId
    # members_data["name"] ="opoi"
    data = {}

    if namePrefix != 'None':
        data["namePrefix"] = namePrefix
    if name != 'None':
        data["name"] = name
    if category != 'None':
        data["category"] = category
    if description != 'None':
        data["description"] = description
    if refDataTypeId != 'None':
        members_data["refDataTypeId"] = refDataTypeId
    if baseDatatype != 'None':
        members_data["baseDatatype"] = baseDatatype
    if name1 != 'None':
        members_data["name"] = name1
    if unit != 'None':
        members_data["unit"] = unit

    members.append(members_data)
    data["members"] = members

    json["data"] = data

    # json["members"] = members

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    res = data_type.get_new_data_type_structure(json=json, headers=headers)  # 修改的参考路径
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            # result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("新增数据类型-结构体 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


#  08 获取详情结构体
def get_detail_structure(id=None):
    result = ResultBase()
    # json = {}
    # pageInfo = {}
    data = {}
    if id != 'None':
        data["id"] = id

    # json["data"] = data
    # json["pageInfo"] = pageInfo

    headers = http_config.param_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = data_type.get_detail_structure(params=data, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("获取数据类型非结构体 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


def get_unstructured(id=None):
    """
    元模块视图组件管理-delete_by_id
    :param id:
    :return:自定义的关键字返回结果 result
    """
    result = ResultBase()
    data = {}
    if id != 'None':
        data["id"] = id
    headers = http_config.param_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    res = data_type.get_get_details_non_structure(params=data, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        try:
            result.msg = res.json()["result"]
            result.success = True
        except:
            result.error = res.json()["msg"]
        # if res.json()["code"] == 0:
        #
        # else:
        #
        logger.info("获取详情-非结构体 ==>> 返回结果 ==>> {}".format(res.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    result.response = res
    return result


def modify_structure(id=None, namePrefix=None, name=None, category=None, baseDatatype=None,
                     description=None,refDataTypeId=None, name1=None, unit=None):
    result = ResultBase()
    json = {}
    members = []
    members_data = {"description": "", "discretes": []}
    # members_data["preDataTypeId"] = 1643355914670
    # members_data["name"] = "opoi"
    data = {}
    if id != 'None':
        data["id"] = id
    if namePrefix != 'None':
        data["namePrefix"] = namePrefix
    if name != 'None':
        data["name"] = name
    if category != 'None':
        data["category"] = category
    if description != 'None':
        data["description"] = description
    if unit != 'unit':
        members_data["unit"] = unit
    if baseDatatype != 'None':
        members_data["baseDatatype"] = baseDatatype

    if refDataTypeId != 'None':
        members_data["refDataTypeId"] = refDataTypeId
    if name1 != 'None':
        members_data["name"] = name1

    members.append(members_data)
    data["members"] = members
    json["data"] = data


    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    res = data_type.post_modify_data_type_structure(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            # result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("修改数据类型-结构体 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


def delete_data_type(id=None):
    """
    元模块视图组件管理-delete_by_id
    :param id:
    :return:自定义的关键字返回结果 result
    """
    result = ResultBase()
    data = {}
    if id != 'None':
        data["id"] = id
    headers = http_config.param_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    res = data_type.get_delete_data_type(params=data, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["msg"]
            # result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("通过id删除数据类型 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result
