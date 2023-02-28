from common.logger import logger


logger.debug("debug log output")
logger.info("输出info日志")
logger.error("错误")
logger.warning("warning message")


def test_base_url(base_url):
    print(base_url)
    logger.info(base_url)
