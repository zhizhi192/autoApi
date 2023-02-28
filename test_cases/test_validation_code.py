import pytest
import json
from common.account_utils import AccountUtils
from common.logger import logger
from common.yaml_utils import YamlUtil
from common.request_utils import RequestUtil
from common.utils import Utils


class TestValidation:

    """def setup_class(self) -> None:
        token = AccountUtils().create_anonymous()
        YamlUtil().write_extract_yaml({"anon_token": token})
        print("写入anon_token")"""

    @pytest.mark.validation
    @pytest.mark.parametrize("case_info", YamlUtil().read_case_yaml("validation.yaml"))
    def test_get_validation_code(self, case_info, base_url):
        rep = RequestUtil().send_request2(case_info=case_info, base_url=base_url)
        Utils.validate(validate_list=case_info["validate"], response=rep)
        logger.info("test end:"+str(case_info["name"]))
