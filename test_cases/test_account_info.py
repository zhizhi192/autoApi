import pytest
from common.yaml_utils import YamlUtil
from common.request_utils import RequestUtil
from common.utils import Utils
from common.logger import logger


class TestAccountInfo:

    def setup_class(self):
        print("\n"+"test account_info start:")

    def teardown_class(self):
        print("\n" + "test account_info end:")

    @pytest.mark.account_info
    @pytest.mark.parametrize("case_info", YamlUtil().read_case_yaml("account_info.yaml"))
    def test_account_info(self, case_info, base_url):
        rep = RequestUtil().send_request2(case_info=case_info, base_url=base_url)
        Utils.validate(validate_list=case_info["validate"], response=rep)
        logger.info("Http返回："+rep.text)
