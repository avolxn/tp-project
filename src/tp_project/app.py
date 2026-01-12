from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tp_project.api import router
from tp_project.services import get_cache_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await get_cache_service().close()


app = FastAPI(
    title="Currency and Temperature Converter",
    description="API for Currency and Temperature Converter",
    version="0.1.0",
    docs_url="/docs",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
