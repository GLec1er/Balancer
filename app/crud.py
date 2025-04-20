from sqlalchemy.future import select
from app.models import Config


async def get_config(db, key: str):
    result = await db.execute(select(Config.value).where(Config.key == key))
    config = result.scalar_one_or_none()
    return config


async def set_config(db, key: str, value: str):
    config = Config(key=key, value=value)
    db.add(config)
    await db.commit()
    return config
