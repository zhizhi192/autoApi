import json

import pytest

from common.logger import logger
from common.request_utils import RequestUtil
from common.yaml_utils import YamlUtil
from common.utils import Utils


def setup_method():
    print('每个测试方法前执行')


def teardown_method():
    print('每个方法之后执行')


class TestAnonymous:

    @pytest.mark.run(order=1)
    @pytest.mark.anonymous
    @pytest.mark.parametrize('case_info', YamlUtil().read_case_yaml('anonymous.yaml'))
    def test_create_anonymous(self, case_info, base_url):
        rep = RequestUtil().send_request2(case_info=case_info, base_url=base_url)
        Utils.validate(validate_list=case_info["validate"], response=rep)
        if rep.status_code == 200:
            logger.info("test end:"+str(case_info["name"]))
        else:
            logger.error("请求错误："+str(rep.status_code))

'''
    @pytest.mark.g2
    def test_get_anonymous(self):
        token = AccountUtils().create_anonymous()
        YamlUtil().write_extract_yaml({"anon_token": token})
        print("写入anon_token")
'''

if __name__ == '__main__':
    pytest.main()
