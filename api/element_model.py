from config import setting
from core.rest_client import RestClient


class element_mode(RestClient):
    """
    管理后台-平台
    """

    def __init__(self):
        super(element_mode, self).__init__(setting.api_root_url)

    '''
    查询平台架构
    '''

    def getPlatformList(self, **kwargs):
        return self.post("/v1/platformAdmin/getPlatformList", **kwargs)

    '''关联管理——元模型元素查询'''

    '''车元模型——元模型元素查询 01'''
    def get_Meta_ElementTree(self, **kwargs):
        return self.post("/v1/vehicleModelAdmin/getMetaElementTree", **kwargs)

    '''车元模型——列表查询 02'''
    def post_page_Model(self, **kwargs):
        return self.post("/v1/modelAdmin/pageModel", **kwargs)

    '''车元模型——车系列表 03'''
    def postSeriesList(self, **kwargs):
        return self.post("/v1/modelAdmin/getSeriesList", **kwargs)

    '''车元模型——车型列表'''
    def get_ModelList(self, **kwargs):
        return self.post("/v1/modelAdmin/getModelList", **kwargs)

    '''关联详情——保存关联元素'''
    def add_OrUpdateLinkedElement(self, **kwargs):
        return self.post("/v1/vehicleModelAdmin/addOrUpdateLinkedElement", **kwargs)

    '''关联详情——接口列表'''
    def get_Meta_ServiceInterFaceList(self, **kwargs):
        return self.post("/v1/modelAdmin/getMetaServiceInterfaceList", **kwargs)

    '''关联管理——获取元模型类型列表'''
    def get_Meta_TypeList(self, **kwargs):
        return self.get("/v1/vehicleModelAdmin/getMetaTypeList", **kwargs)

    '''一键复制——保存关联元素'''
    def copy_Model_Linked_Detail(self, **kwargs):
        return self.post("/v1/vehicleModelAdmin/copyModelLinkedDetail", **kwargs)

    '''一键复制——查询目标车型是否有关联数据'''
    def get_Model_Linked_Detail(self, **kwargs):
        return self.post("/v1/vehicleModelAdmin/getModelLinkedDetail", **kwargs)


element_model = element_mode()
