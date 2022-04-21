from api.element_model import element_model
from common.logger import logger
from config import http_config
from core.result_base import ResultBase


# 管理后台——车型元模型


# 车型元模型——元模型元素查询  series_code, model_code, platform_id, search_meta_type, search_name,
def get_Meta_ElementTree(series_code=None, model_code=None, platform_id=None, search_meta_type=None, search_name=None):
    result = ResultBase()
    json = {}
    # pageInfo = {}
    data = {}

    if series_code != 'None':
        data["series_code"] = series_code
    if model_code != 'None':
        data["model_code"] = model_code
    if platform_id != 'None':
        data["platform_id"] = platform_id
    if search_meta_type != 'None':
        data["search_meta_type"] = search_meta_type
    if search_name != 'None':
        data["search_name"] = search_name

    json["data"] = data
    # json["pageInfo"] = pageInfo
    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = element_model.get_Meta_ElementTree(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("车系列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


# 车型元模型——列表查询  page_index,page_size,series_code,model_code,platformPid,interfaceId
def PostPageModel(page_index=None, page_size=None, series_code=None, model_code=None, platformPid=None,
                  interfaceId=None, link_type=None):
    result = ResultBase()
    json = {}
    pageInfo = {}
    data = {}

    if page_index != 'None':
        pageInfo["pageIndex"] = page_index
    if page_size != 'None':
        pageInfo["pageSize"] = page_size
    if series_code != 'None':
        data["series_code"] = series_code
    if model_code != "None":
        data["model_code"] = model_code
    if platformPid != "None":
        data["platformPid"] = platformPid
    if interfaceId != "None":
        data["interfaceId"] = interfaceId
    if link_type != "None":
        data["link_type"] = link_type

    json["data"] = data
    json["pageInfo"] = pageInfo

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = element_model.post_page_Model(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("车系列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


# 车型元模型——车系列表  page_index,page_size,series_code,series_name,
def PostSeriesList(page_index=None, page_size=None, series_code=None, series_name=None):
    result = ResultBase()
    json = {}
    pageInfo = {}
    data = {}

    if page_index != 'None':
        pageInfo["pageIndex"] = page_index
    if page_size != 'None':
        pageInfo["pageSize"] = page_size
    if series_code != 'None':
        data["series_code"] = series_code
    if series_name != "None":
        data["series_name"] = series_name

    json["data"] = data
    json["pageInfo"] = pageInfo

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = element_model.postSeriesList(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("车系列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


# 车型元模型——车型列表  page_index,page_size,series_code,model_code,model_name
def GetModelList(page_index=None, page_size=None, series_code=None, model_code=None, model_name=None):
    result = ResultBase()
    json = {}
    pageInfo = {}
    data = {}

    if page_index != 'None':
        pageInfo["pageIndex"] = page_index
    if page_size != 'None':
        pageInfo["pageSize"] = page_size
    if series_code != 'None':
        data["series_code"] = series_code
    if model_code != "None":
        data["model_code"] = model_code
    if model_name != "None":
        data["model_name"] = model_name

    json["data"] = data
    json["pageInfo"] = pageInfo

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = element_model.postSeriesList(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("车系列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


# 车型元模型——一保存关联元素
# series_code, model_code, platform_id, meta_type, link_id,link_type,
def add_OrUpdate_Linked_Element(seriesCode=None, modelCode=None, platformId=None, linkId=None, linkType=None, metaType=None, preId=None):

    result = ResultBase()
    json = {}
    childLit = []
    childLit_data = {}
    childLit_data["linkId"] = linkId
    childLit_data["linkType"] = linkType
    childLit_data["metaType"] = metaType
    childLit_data["preId"] = preId
    childLit.append(childLit_data)
    data = {}

    if seriesCode != 'None':
        data["seriesCode"] = seriesCode
    if modelCode != 'None':
        data["modelCode"] = modelCode
    if platformId != 'None':
        data["platformId"] = platformId
    if childLit != 'None':
        data["childLit"] = childLit

    json["data"] = data
    # json["childLit"] = childLit

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = element_model.add_OrUpdateLinkedElement(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("车系列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


# 车型元模型——接口列表  page_size,page_index,series_code,model_code,platform_id,status,interface_name,interface_bid,
                   # field_property, service_interface_type,service_pid
def get_Meta_ServiceInterFaceList(page_size=None, page_index=None, series_code=None, model_code=None, platform_id=None,
                                  status=None, interface_name=None, interface_bid=None, field_property=None, service_interface_type=None, service_pid=None):
    result = ResultBase()
    json = {}
    pageInfo = {}
    data = {}

    if page_size != 'None':
        pageInfo["pageSize"] = page_size
    if page_index != 'None':
        pageInfo["page_index"] = page_index
    if series_code != 'None':
        data["series_code"] = series_code
    if model_code != "None":
        data["model_code"] = model_code
    if platform_id != "None":
        data["platform_id"] = platform_id
    if status != "None":
        data["status"] = interface_bid
    if interface_name != "None":
        data["interface_name"] = interface_name
    if interface_bid != "None":
        data["interface_bid"] = interface_bid
    if field_property != "None":
        data["field_property"] = field_property
    if service_interface_type != "None":
        data["service_interface_type"] = service_interface_type
    if service_pid != "None":
        data["service_pid"] = service_pid

    json["data"] = data
    json["pageInfo"] = pageInfo

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = element_model.postSeriesList(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("车系列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


# 车型元模型——关联管理——获取元模型类型列表
def get_Meta_Type_List():

    result = ResultBase()

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = element_model.get_Meta_TypeList(headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("车系列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


# 车型元模型——一键复制——保存关联元素  series_code, model_code, platform_id, targe_series_code, targe_model_code,
def copy_Model_Linkd_Dateil(seriesCode=None, modelCode=None, platformId=None, targetSeriesCode=None, targetModelCode=None):

    result = ResultBase()
    json = {}
    # pageInfo = {}
    data = {}

    if seriesCode != 'None':
        data["seriesCode"] = seriesCode
    if modelCode != 'None':
        data["modelCode"] = modelCode
    if platformId != 'None':
        data["platformId"] = platformId
    if targetSeriesCode != 'None':
        data["targetSeriesCode"] = targetSeriesCode
    if targetModelCode != 'None':
        data["targetModelCode"] = targetModelCode


    json["data"] = data
    # json["pageInfo"] = pageInfo

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = element_model.copy_Model_Linked_Detail(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            # result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("车系列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


# 车型元模型——一键复制——查询目标车型是否有关联数据
# series_code, model_code, platform_id, targe_series_code, targe_model_code,creator, create_time
def get_Model_Linked_Datail(seriesCode=None, modelCode=None, platformId=None, targetSeriesCode=None, targetModelCode=None, creator=None, create_time=None):

    result = ResultBase()
    json = {}
    # pageInfo = {}
    data = {}

    if seriesCode != 'None':
        data["seriesCode"] = seriesCode
    if modelCode != 'None':
        data["modelCode"] = modelCode
    if platformId != 'None':
        data["platformId"] = platformId
    if targetSeriesCode != 'None':
        data["targetSeriesCode"] = targetSeriesCode
    if targetModelCode != 'None':
        data["targetModelCode"] = targetModelCode
    if creator != 'None':
        data["creator"] = creator
    if create_time != 'None':
        data["create_time"] = create_time

    json["data"] = data
    # json["pageInfo"] = pageInfo

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = element_model.get_Model_Linked_Detail(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("车系列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


