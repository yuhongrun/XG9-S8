from config import setting
from core.rest_client import RestClient


class InteractiveManagement(RestClient):
    """
    对外接口服务
    """
    def __init__(self):
        super(InteractiveManagement, self).__init__(setting.api_root_url)

    # 定义获取获取交互接口列表的函数"
    def get_interactive_interface_list(self, **kwargs):
        return self.post("/v1/interaction/getInteractionInterfaceList", **kwargs)
    # 定义根据交互接口ID集合查询交互接口详情的函数
    def query_details_by_id(self, **kwargs):
        return self.post("/v1/interaction/getInteractionInterfaceDetailList", **kwargs)

interactive_Management = InteractiveManagement()