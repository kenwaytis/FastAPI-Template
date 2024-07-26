from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

from fastapi import APIRouter, Depends

from service.base.redis_service import RedisService
from service.dependencies import redis_service_instance
from service.business.{{tmp}}_service import {{Tmp}}Service
from service.dependencies import {{tmp}}_service_instance

from logging_config import logger

router = APIRouter()

class {{Tmp}}Input(BaseModel):
    pass

@router.post("/{{tmp}}")
async def {{tmp}}(
    request: {{Tmp}}Input,
    redis_service: RedisService = Depends(lambda: redis_service_instance),
    {{tmp}}_service: {{Tmp}}Service = Depends(lambda: {{tmp}}_service_instance),
    ):
    return JSONResponse(content={})
