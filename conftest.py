from common.account_utils import AccountUtils
from common.logger import logger
import pytest

from common.yaml_utils import YamlUtil


# 运行时会弹出图片验证码需要手动输入，本地调试时注释，token固定不改，之后再考虑ocr识别
# 每次运行前清空extract.yaml的文件内容
@pytest.fixture(scope='session', autouse=True)
def clear_yaml():
    YamlUtil().clean_extract_yaml()
    print("------extract.yaml has been cleand------")


# 运行前在extract.yaml写入px用户token
@pytest.fixture(scope='session', autouse=True)
def set_user_token():
    token = AccountUtils().login_by_password(user_info={"user_name": "14000100201", "password": "Qyff2011"})
    pxs_token = {"pxs_token": token["token"]}
    YamlUtil().write_extract_yaml(data=pxs_token)
    print("------set user token to extract.yaml succeed-----")


@pytest.fixture(scope="session", autouse=True)
def base_url():
    base_url = "https://api.qingshuxuetang.com/v22_13/"
    logger.info("\n=========================Test on base url:"+base_url+" =========================")
    return base_url
