from config import setting
from core.rest_client import RestClient

class EventGroup(RestClient):
    """
    时间组
    """

    def __init__(self):
        super(EventGroup, self).__init__(setting.api_root_url)

    def query_list(self, **kwargs):
        return self.post("/v1/eventGroupAdmin/getEventGroupList", **kwargs)

    def detail_id(self, **kwargs):
        return self.get("/v1/eventGroupAdmin/getEventGroupDetail", **kwargs)

    def face_list(self, **kwargs):
        return self.post("/v1/eventGroupAdmin/getEventGroupInterfaceList", **kwargs)

    def add_update(self, **kwargs):
        return self.post("/v1/eventGroupAdmin/addOrUpdateEventGroup", **kwargs)

    def id_generate(self, **kwargs):
        return self.post("/v1/eventGroupAdmin/generateEventGroupBId", **kwargs)

    def update_batch(self, **kwargs):
        return self.post("/v1/eventGroupAdmin/batchUpdateField", **kwargs)

    def generate_bid(self, **kwargs):
        return self.get("/BusinessIdService/generateBid", **kwargs)

    def register_bid(self, **kwargs):
        return self.post("/BusinessIdService/registerBid", **kwargs)


eventGroup = EventGroup()