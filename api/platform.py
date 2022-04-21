from config import setting
from core.rest_client import RestClient


class Platform(RestClient):
    """
    管理后台-平台
    """

    def __init__(self):
        super(Platform, self).__init__(setting.api_root_url)
    '''
    查询平台架构
    '''
    def getPlatformList(self, **kwargs):
        return self.post("/v1/platformAdmin/getPlatformList", **kwargs)

    # 编辑平台架构
    def updatePlatform(self, **kwargs):
        return self.post("/v1/platformAdmin/updatePlatform", **kwargs)

    # 更新逻辑域
    def updateDomain(self, **kwargs):
        return self.post("/v1/domainAdmin/updateDomain", **kwargs)

    # 获取逻辑域列表
    def getDomainList(self, **kwargs):
        return self.post("/v1/domainAdmin/getDomainList", **kwargs)

    # 子系统列表查询接口
    def getLogicSystemList (self, **kwargs):
        return self.post("/v1/logicSystemAdmin/getLogicSystemList", **kwargs)

    #子系统新增更新接口
    def addOrUpdateLogicSystem (self, **kwargs):
        return self.post("/v1/logicSystemAdmin/addOrUpdateLogicSystem", **kwargs)

    #子系统详情接口
    def getLogicSystemDetail(self, id, **kwargs):
        if id != "None":
            return self.get("/v1/logicSystemAdmin/getLogicSystemDetail/{}".format(id), **kwargs)
        else:
            return self.get("/v1/logicSystemAdmin/getLogicSystemDetail/", **kwargs)

    #子系统删除服务
    def batchUpdateField(self, **kwargs):
        return self.post("/v1/logicSystemAdmin/batchUpdateField", **kwargs)


platform = Platform()
