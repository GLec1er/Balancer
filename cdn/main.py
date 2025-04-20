from fastapi import FastAPI, Request

cdn = FastAPI()


@cdn.get("/{origin}/{path:path}")
async def cdn_catch(origin: str, path: str, request: Request):
    return {
        "status": "CDN HIT ✅",
        "origin": origin,
        "path": path,
        "full_url": str(request.url)
    }
