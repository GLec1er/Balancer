# Сервис-балансировщик видео-трафика

Нужно написать максимально _простой_ сервис-балансировщик пользовательских
запросов, который должен отправлять пользователя с помощью 301-го HTTP
редиректа смотреть фильм либо на корневые сервера, либо отправлять его в CDN по
определённым правилам.

### Запусти основной сервер
uvicorn app.main:app --reload

http://localhost:8000/?video=http://s3.origin-cluster/video/9999/test123.m3u8
