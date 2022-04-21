import os
import shutil
from pathlib import Path

import pytest

from common import excel_oper

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def delete_file():
    report_path = Path(BASE_PATH + "/api_test/services/report")
    result_path = Path(BASE_PATH + "/api_test/services/result")
    if report_path.exists():
        # os.rmdir(report_path)
        shutil.rmtree(report_path)
    if result_path.exists():
        # os.rmdir(result_path)
        shutil.rmtree(result_path)


if __name__ == "__main__":
    delete_file()
    excel_oper.create_file()

    pytest.main(['-s', '--alluredir', './result/'])
    os.system('allure generate ./result/ -o ./report/ --clean')

