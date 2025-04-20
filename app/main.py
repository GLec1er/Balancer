import random

from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse, HTMLResponse
from app.crud import get_config
from app.database import AsyncSessionLocal, get_db
from app.routers import config as config_router

app = FastAPI(title="Balancer", docs_url=None, redoc_url=None)
app.include_router(config_router.router, prefix="/api")


@app.get("/")
async def redirect_handler(
    video: str = None,
    db: AsyncSessionLocal = Depends(get_db)
):
    if not video:
        return HTMLResponse(content="""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Ошибка</title>
                <style>
                    body {
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background-color: #f2f2f2;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        height: 100vh;
                        margin: 0;
                    }
                    .container {
                        text-align: center;
                        padding: 40px;
                        background-color: #fff;
                        border-radius: 16px;
                        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                    }
                    h1 {
                        color: #f44336;
                        margin-bottom: 20px;
                    }
                    p {
                        color: #555;
                        font-size: 1.1rem;
                    }
                    a {
                        color: #4CAF50;
                        text-decoration: none;
                        font-weight: bold;
                    }
                    a:hover {
                        text-decoration: underline;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🚨 Параметр video не передан!</h1>
                    <p>Пожалуйста, передайте параметр <strong>video</strong> в запросе.</p>
                    <p>Пример запроса: <a href="http://localhost:8000/?video=http://s3.origin-cluster/video/9999/test123.m3u8">http://localhost:8000/?video=http://s3.origin-cluster/video/9999/test123.m3u8</a></p>
                </div>
            </body>
            </html>
        """, status_code=400)

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
