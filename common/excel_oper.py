import os

import xlrd
import xlwt
from xlutils.copy import copy

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_file_path():
    return os.path.join(BASE_PATH, "data", "接口测试报告_s8.xls")


def delete_file():
    if os.path.exists(get_file_path()):
        os.remove(get_file_path())
        print("删除文件成功")
    else:
        print("文件不存在")


def create_file():
    delete_file()
    book = xlwt.Workbook()
    sheet = book.add_sheet(u'接口测试报告_s8', cell_overwrite_ok=True)
    row = ["接口模块", "接口名称", "接口请求地址", "请求参数", "期望返回码", "实际返回码", "是否测试通过"]
    # 生成第一行
    for i in range(0, len(row)):
        sheet.write(0, i, row[i])

    book.save(get_file_path())
    print("创建文件成功")


def get_excel_rows():
    work = xlrd.open_workbook(get_file_path())
    sheet = work.sheet_by_index(0)
    print(sheet.nrows)
    print(sheet.ncols)
    return sheet.nrows


def write_data(result, module_name, method_name, except_code, is_suck, except_result):
    except_code_str = except_code
    if not except_result:
        if except_code == 0:
            except_code_str = "非{}".format(except_code)
    excel_result = [module_name, method_name, result.response.url, str(result.response.request.body),
                    except_code_str,
                    result.code, str(is_suck)]
    write_excel(excel_result)


def write_excel(args):
    print("开始写入文件")
    work = xlrd.open_workbook(get_file_path())
    sheet1 = work.sheet_by_index(0)
    book = copy(work)
    sheet = book.get_sheet(0)
    print(sheet1.nrows)
    print(sheet1.ncols)
    for i in range(0, len(args)):
        sheet.write(sheet1.nrows, i, args[i])

    book.save(get_file_path())
    print("写入文件完成")


if __name__ == "__main__":
    print(get_file_path())
    create_file()
    print(get_excel_rows())
