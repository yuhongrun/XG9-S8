from config import setting
from core.rest_client import RestClient


class Services(RestClient):
    """
    管理后台-平台
    """

    def __init__(self):
        super(Services, self).__init__(setting.api_root_url)

    '''
    根据id查询服务详情
    '''

    def getMetaServiceDetail(self, id, **kwargs):
        return self.get("/v1/serviceAdmin/getMetaServiceDetail/{}".format(id), **kwargs)

    def getMetaServiceList(self, **kwargs):
        return self.post("/v1/serviceAdmin/getMetaServiceList", **kwargs)

    def addOrUpdateMetaService(self, **kwargs):
        return self.post("/v1/serviceAdmin/addOrUpdateMetaService", **kwargs)

    def batchUpdateField(self, **kwargs):
        return self.post("/v1/serviceAdmin/batchUpdateField", **kwargs)

    def getInterfaceList(self, **kwargs):
        return self.post("/v1/serviceAdmin/getInterfaceList", **kwargs)

    def updateInterfaceStatus(self, id, **kwargs):
        return self.get("/v1/serviceAdmin/updateInterfaceStatus/{}".format(id), **kwargs)

    def getHexId(self, **kwargs):
        return self.post("/v1/serviceAdmin/getHexId", **kwargs)

    def batchUpdateInterfaceField(self, **kwargs):
        return self.post("/v1/serviceAdmin/batchUpdateInterfaceField", **kwargs)

    def addOrUpdateInterface(self, **kwargs):
        return self.post("/v1/serviceAdmin/addOrUpdateInterface", **kwargs)

    def field_addOrUpdateInterface(self, **kwargs):
        return self.post("/v1/serviceAdmin/addOrUpdateInterface", **kwargs)

    def event_addOrUpdateInterface(self, **kwargs):
        return self.post("/v1/serviceAdmin/addOrUpdateInterface", **kwargs)

    def getInterfaceDetail(self, id, **kwargs):
        return self.get("/v1/serviceAdmin/getInterfaceDetail/{}".format(id), **kwargs)

    def updateInterfaceCategory(self, **kwargs):
        return self.post("/v1/serviceAdmin/updateInterfaceCategory", **kwargs)

services = Services()
