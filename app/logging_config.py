import sys
import json
from loguru import logger

with open("/home/app/config.json", "r") as config_file:
    config = json.load(config_file)["logging_config"]

# 定义日志格式
log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{module}</cyan>.<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)

# 移除默认的handler
logger.remove()

# 添加handler用于文件输出
logger.add(
    config["log_file"],
    rotation=config["rotation"],
    retention=config["retention"],
    level=config["logging_level"],
    format=log_format,
    colorize=False,
    serialize=False,
)

# 添加handler用于标准输出
logger.add(
    sys.stdout,
    level=config["logging_level"],
    format=log_format,
    colorize=True,
    serialize=False,
)
