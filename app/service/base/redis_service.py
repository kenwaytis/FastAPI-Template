import asyncio
import aioredis
from aioredis import Redis
from logging_config import logger


class RedisService:
    def __init__(self, redis_url: str, max_retries: int = 3):
        self.redis_url = redis_url
        self.max_retries = max_retries
        self.redis: Redis = None

    async def connect(self):
        self.redis = await aioredis.from_url(self.redis_url)
        logger.info("Connected to Redis")

    async def disconnect(self):
        if self.redis:
            await self.redis.close()
            logger.info("Disconnected from Redis")

    async def insert_message(self, message_id: str):
        try:
            await self.redis.set(message_id, "")
            logger.info(f"Inserted message with ID: {message_id}")
            return True  # 操作成功
        except Exception as e:
            logger.error(f"Failed to insert message: {e}")
            return False  # 操作失败

    async def update_message(self, message_id: str, new_value: str):
        try:
            await self.redis.set(message_id, new_value)
            logger.info(f"Updated message with ID: {message_id}")
            return True  # 操作成功
        except Exception as e:
            logger.error(f"Failed to update message: {e}")
            return False  # 操作失败

    async def get_message(self, message_id: str):
        try:
            message = await self.redis.get(message_id)
            message = message.decode("utf-8")
            if message or message == "":
                logger.info(f"Fetched message: {message}")
                return message
            else:
                print(message)
                logger.info("Message not found")
                return None
        except Exception as e:
            logger.error(f"Failed to fetch message: {e}")
            return None

    async def delete_message(self, message_id: str):
        try:
            await self.redis.delete(message_id)
            logger.info(f"Deleted message with ID: {message_id}")
            return True  # 删除成功
        except Exception as e:
            logger.error(f"Failed to delete message: {e}")
            return False  # 删除失败
        