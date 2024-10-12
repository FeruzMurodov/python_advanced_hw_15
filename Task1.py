import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.setFormatter(formatter)
logger.addHandler(debug_info_handler)

warnings_error_handler = logging.FileHandler('warnings_error.log')
warnings_error_handler.setLevel(logging.WARNING)
warnings_error_handler.setFormatter(formatter)
logger.addHandler(warnings_error_handler)

logger.debug("This message is of level DEBUG")
logger.info("This message is of level INFO")
logger.warning("This message is of level WARNING")
logger.error("This message is of level ERROR")
logger.critical("This message is of level CRITICAL")
