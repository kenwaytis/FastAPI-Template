import os
import json

from service.base.redis_service import RedisService
from service.business.{{tmp}}_service import {{Tmp}}Service

with open("/home/app/config.json", "r") as config_file:
    config = json.load(config_file)


redis_config = config["redis_config"]
redis_service_instance = RedisService(
    redis_config["url"]
)

{{tmp}}_config = config["{{tmp}}_config"]
{{tmp}}_service_instance = {{Tmp}}Service()
