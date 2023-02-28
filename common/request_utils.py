import json
from common.utils import Utils
import requests
from requests import Response
from common.logger import logger


class RequestUtil:
    session = requests.session()

    def send_request(self, method, url, data, headers, **kwargs,) -> Response:
        if method.upper() == 'GET':
            rep = self.session.request(method='get', url=url, params=data, headers=headers, **kwargs)
            return rep
        elif method.upper() == 'POST':
            data = json.dumps(data)
            rep = self.session.request(method='post', url=url, data=data, headers=headers, **kwargs)
            return rep
        else:
            raise Exception('不支持的请求！')

    def send_request2(self, case_info, base_url, **kwargs) -> Response:
        # 替换参数
        logger.info("test start："+str(case_info["name"])+" "+str(case_info["request"]["url"]))
        case_info = Utils.handle_case_info(case_info=case_info, base_url=base_url)
        url = case_info['request']['url']
        method = case_info['request']['method']
        data = case_info['request']['data']
        headers = case_info['request']['headers']
        rep = self.do_request(url=url, method=method, data=data, headers=headers, **kwargs)
        if "extract" in str(case_info):
            # 提取参数
            Utils.extract(extract_data=case_info["extract"], response=rep)
        return rep

    def do_request(self, method, url, data, **kwargs):
        if method.upper() == 'GET':
            rep = self.session.request(method='get', url=url, params=data, verify=False, **kwargs)
            return rep
        elif method.upper() == 'POST':
            data = json.dumps(data)
            rep = self.session.request(method='post', url=url, data=data, verify=False, **kwargs)
            return rep
        else:
            raise Exception('不支持的请求！')
