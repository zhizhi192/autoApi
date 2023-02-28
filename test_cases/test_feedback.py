import pytest
from common.yaml_utils import YamlUtil
from common.request_utils import RequestUtil
from common.utils import Utils
from common.logger import logger


class TestFeedback:

    @pytest.mark.feedback
    @pytest.mark.parametrize("case_info", YamlUtil().read_case_yaml("feedback.yaml"))
    def test_feedback(self, case_info, base_url):
        rep = RequestUtil().send_request2(case_info=case_info, base_url=base_url)
        Utils.validate(case_info["validate"], response=rep)
        logger.info("http返回:"+rep.text)
        logger.info("test end："+str(case_info["name"]))

