from hamcrest import *
import jsonpath
from common.logger import logger
import json
from common.yaml_utils import YamlUtil


class Utils:

    @staticmethod
    def handle_case_info(case_info: dict, base_url):
        for i in range(0, str(case_info).count("${")):
            if "${" in json.dumps(case_info) and "}" in json.dumps(case_info):
                start_index = str(case_info).find("${")
                end_index = str(case_info)[start_index:].find("}") + start_index
                old_value = str(case_info)[start_index:end_index + 1]
                new_value = YamlUtil().read_extract_yamml(key=old_value[2:-1])
                case_info = eval(str(case_info).replace(old_value, new_value))
        case_info["request"]["url"] = base_url+case_info["request"]["url"]
        return case_info

    @staticmethod
    def extract(extract_data, response):
        for key, val in extract_data.items():
            value = jsonpath.jsonpath(response.json(), val)[0]
            logger.info("提取参数"+key+"："+str(value))
            YamlUtil().write_extract_yaml(data={key: value})

    @staticmethod
    def validate(validate_list: list, response):
        # Todo: 断言错误的请求，状态400之类
        if response.status_code == 200:
            for valid in validate_list:
                for k, v in valid.items():
                    for key, val in v.items():
                        actual_val = jsonpath.jsonpath(response.json(), key)[0]
                        logger.info(f"{key}预期结果是：{val}")
                        logger.info(f"{key}实际结果是：{actual_val}")
                        if k == "eq":
                            assert_that(actual_val, equal_to(val))
                        else:
                            logger.info("暂不支持该方法")
        else:
            raise Exception("请求失败，暂不支持验证! http error:"+str(response.status_code))

    @staticmethod
    # Todo: 如何全量校验返回json的所有字段？
    def validate_new(validate_list: list, response):
        for valid in validate_list:
            for key, item in valid.items():
                for key_json_path, item_expect in item.items():
                    logger.info(f"预期结果的值是{item_expect}")
                    actual_val = jsonpath.jsonpath(response, key_json_path)[0]
                    logger.info(f"获取真实值是{actual_val}")
                    if key == "equal_to":  # 断言相等
                        assert_that(actual_val, equal_to(item_expect))
                    elif key == "less_than":
                        assert_that(actual_val, less_than(item_expect))
                    elif key == "greater_than":
                        assert_that(actual_val, greater_than(item_expect))
                    elif key == "has_length":
                        assert_that(actual_val, has_length(item_expect))
                    elif key == "has_string":
                        assert_that(actual_val, has_string(item_expect))
                    elif key == "greater_than_or_equal_to":
                        assert_that(actual_val, greater_than_or_equal_to(item_expect))
                    elif key == "less_than_or_equal_to":
                        assert_that(actual_val, less_than_or_equal_to(item_expect))
                    else:
                        logger.info("-------暂时不支持该断言方法---------")
