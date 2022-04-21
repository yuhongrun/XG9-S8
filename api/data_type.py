from config import setting
from core.rest_client import RestClient


class DataType(RestClient):
    """
    管理后台-平台
    """

    def __init__(self):
        super(DataType, self).__init__(setting.api_root_url)


    #"新增数据类型非结构体"   1
    def post_new_data_type_non_structure(self, **kwargs):
        return self.post("/v1/dataTypeAdmin/add", **kwargs)

    #"修改数据类型非结构体"   2
    def post_modify_data_type_non_structure(self, **kwargs):
        return self.post("/v1/dataTypeAdmin/edit", **kwargs)

    #"获取详情非结构体"      3
    def get_get_details_non_structure(self, **kwargs):
        return self.get("/v1/dataTypeAdmin/getDetail", **kwargs)

    #"删除数据类型"        4

    def get_delete_data_type(self, **kwargs):
        return self.get("/v1/dataTypeAdmin/dele", **kwargs)

    # "数据类型列表查询"     5
    #
    def post_data_type_list_query(self, **kwargs):
        return self.post("/v1/dataTypeAdmin/pageList", **kwargs)   #搞
    #
    # "新增数据类型结构体"   6
    #
    def get_new_data_type_structure(self, **kwargs):
        return self.post("/v1/dataTypeAdmin/addStruct", **kwargs)    #搞
    #
    # "修改数据类型结构体"    7
    #
    def post_modify_data_type_structure(self, **kwargs):
        return self.post("/v1/dataTypeAdmin/editStruct", **kwargs)
    #
    # "获取详情结构体"
    #
    def get_detail_structure(self, **kwargs):
        return self.get("/v1/dataTypeAdmin/getDetailStruct", **kwargs)  #搞








data_type = DataType()

