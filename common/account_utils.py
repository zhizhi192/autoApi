import json
import requests
from PIL import Image
import base64


class AccountUtils:
    session = requests.session()

    def create_anonymous(self) -> str:
        url = "https://api.qingshuxuetang.com/v22_13/account/createAnonymous"
        data = {"deviceToken": "46E3CCBB-7C6D-43BD-BE29-0E25B4DBA8E4", "clientType": 1}
        headers = {
            "User-Agent-QS": "QSXT",
            "Content-Type": "application/json",
            "DeviceIdentifier-QS": "6AD57A14-7C5B-4C9E-BC46-5CB5168FE5B8"
        }
        rep = self.session.request(method="post", url=url, data=json.dumps(data), headers=headers, verify=False,)
        return rep.json()['data']['token']

    def get_validation(self, user_info) -> list:
        # 获取图片验证码，第二项是请求所用的匿名用户token
        anonymous_token = self.create_anonymous()
        url = 'https://api.qingshuxuetang.com/v22_13/account/getValidationCode'
        data = {"recv": user_info["user_name"], "validationType": 3}
        headers = {
            "Authorization-QS": anonymous_token,
            "User-Agent-QS": "QSXT",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Accept": "application/json"
        }
        rep = self.session.request(method="post", url=url, json=data, headers=headers, verify=False)
        return [rep.json()['data'], anonymous_token]

    def login_by_password(self, user_info) -> dict:
        # 通过用户名密码登录后返回data
        # todo:放在conftest.py更合适，需要改成ocr识别验证码，目前需要手动输入图片验证码结果
        valid = self.get_validation(user_info)
        img_code = valid[0]['code']
        img_data = base64.b64decode(img_code)
        with open('1.png', mode='wb') as f:
            f.write(img_data)
        img = Image.open('1.png')
        img.show()
        url = 'https://api.qingshuxuetang.com/v22_13/account/login'
        data = {"password": user_info["password"], "validation":
                {"type": 3, "sessionId": valid[0]['sessionId'], "userInput": input("请输入图片验证码计算结果:")},
                "name": user_info["user_name"], "type": 1}
        headers = {
            "Authorization-QS": valid[1],
            "User-Agent-QS": "QSXT",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Accept": "application/json",
            "User-Agent": "ELearningQSXT/22.12.1 (iPhone; iOS 13.3; Scale/2.00)"
        }
        img.close()
        rep = self.session.request(method="post", url=url, json=data, headers=headers, verify=False)
        # data下的token为登录时使用，key是仅作为学习记录时验证使用，保留返回但暂时不用
        return rep.json()['data']
