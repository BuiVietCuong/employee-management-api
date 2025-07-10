import hashlib
import logging

import redis
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


logging.basicConfig(level=logging.INFO)
# Connect to Redis (adjust host/port as needed)
# redis_client = redis.Redis(host='redis', port=6379, db=0)


# For this middleware, because of limited time I only layout what Redis does to cache
# request to deal to reat limit requirement
class CacheMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, ttl: int = 60):
        super().__init__(app)
        self.ttl = ttl  # cache time-to-live in seconds

    async def dispatch(self, request: Request, call_next):
        logging.info("PROCESS IN MIDDLEWARE")
        if request.method != "GET":
            return await call_next(request)

        # Create a cache key based on path + query + headers
        org_id = request.headers.get("organization_id", "")
        key_raw = f"{request.url.path}?{request.url.query}&org={org_id}"
        cache_key = f"cache:{hashlib.md5(key_raw.encode()).hexdigest()}"

        # cached = redis_client.get(cache_key)
        # if cached:
        #     return JSONResponse(content=eval(cached.decode()), status_code=200)

        response = await call_next(request)

        # if response.status_code == 200 and response.headers.get("content-type") == "application/json":
        #     body = [section async for section in response.body_iterator]
        #     full_body = b"".join(body).decode()
        #     redis_client.setex(cache_key, self.ttl, full_body)
        #     return JSONResponse(content=eval(full_body), status_code=200)
        #
        return response
