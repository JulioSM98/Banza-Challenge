from fastapi import FastAPI

from utils.main_utils import tag_metadata
from core.db.dabase_engine import engine
from core.db import models

from routes.client_route import client_router
from routes.movements_route import movements_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Banza Challenge",
    description="funcionalidad básica de un sistema de control de movimientos monetarios.",
    openapi_tags=tag_metadata,
)

app.include_router(client_router, prefix="/api")
app.include_router(movements_router, prefix="/api")
