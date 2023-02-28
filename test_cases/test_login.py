import pytest
from common.yaml_utils import YamlUtil
from common.account_utils import AccountUtils
from common.utils import Utils
from common.request_utils import RequestUtil


class TestLogin:

    @pytest.mark.run(order=1)
    @pytest.mark.login2
    @pytest.mark.parametrize('case_info', YamlUtil().read_case_yaml("login.yaml"))
    def test_login_by_password2(self, case_info):
        user_info = case_info["user_info"]
        rep = AccountUtils().login_by_password(user_info=user_info)
        # Utils.validate(validate_list=case_info["validate"], response=rep)
        print(rep)

    """@pytest.mark.login1
    @pytest.mark.parametrize('case_info', YamlUtil().read_case_yaml("login.yaml"))
    def test_login_by_password(self, case_info):
        url = case_info['request']['url']
        method = case_info['request']['method']
        data = case_info['request']['data']
        headers = case_info['request']['headers']
        user_info = case_info['user_info']
        valid = AccountUtils().get_validation(user_info=user_info)
        headers['Authorization-QS'] = valid[1]
        img_code = valid[0]['code']
        img_data = base64.b64decode(img_code)
        with open('1.png', mode='wb') as f:
            f.write(img_data)
        Image.open('1.png').show()
        data['validation']['userInput'] = input("请输入图片验证码计算结果:")
        data['validation']['sessionId'] = valid[0]['sessionId']
        rep = RequestUtil().send_request(url=url, method=method, data=data, headers=headers)
        print(rep.json())
"""
