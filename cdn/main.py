from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse

cdn = FastAPI(title="Mock CDN Server", docs_url=None, redoc_url=None)


@cdn.get("/", response_class=HTMLResponse)
async def main_page_cdn(request: Request):
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Mock CDN</title>
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
                color: #4CAF50;
                margin-bottom: 20px;
            }
            p {
                color: #555;
                font-size: 1.1rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>👋 Добро пожаловать в Mock CDN</h1>
            <p>Это тестовый CDN-сервер для отдачи контента.</p>
        </div>
    </body>
    </html>
    """


@cdn.get("/{origin}/{path:path}")
async def cdn_catch(origin: str, path: str, request: Request):
    return {
        "status": "CDN HIT ✅",
        "origin": origin,
        "path": path,
        "full_url": str(request.url)
    }
