import random

from fastapi import FastAPI, Request, Depends
from starlette.responses import RedirectResponse
from app.config import settings
from app.crud import get_config
from app.database import AsyncSessionLocal, get_db
from app.routers import config as config_router

app = FastAPI()
app.include_router(config_router.router, prefix="/api")


@app.get("/")
async def redirect_handler(
    video: str,
    db: AsyncSessionLocal = Depends(get_db)
):
    cdn_host = await get_config(db, "cdn_host")
    origin_ratio = int(await get_config(db, "origin_ratio"))

    if random.randint(1, origin_ratio) == 1:
        return RedirectResponse(video, status_code=301)
    else:
        origin_host = video.split("//")[1].split("/")[0]
        server_name = origin_host.split(".")[0]
        path = "/".join(video.split("/")[3:])
        cdn_url = f"http://{cdn_host}/{server_name}/{path}"
        return RedirectResponse(cdn_url, status_code=301)
