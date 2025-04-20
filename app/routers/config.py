from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.crud import get_config, set_config
from app.models import ConfigUpdate

router = APIRouter()


@router.get("/config/{key}")
async def read_config(key: str, db: AsyncSession = Depends(get_db)):
    value = await get_config(db, key)
    return {
        "key": key,
        "value": value
    }


@router.post("/config/")
async def write_config(cfg: ConfigUpdate, db: AsyncSession = Depends(get_db)):
    config = await set_config(db, cfg.key, cfg.value)
    return {
        "status": "created_or_updated",
        "key": config.key,
        "value": config.value
    }
