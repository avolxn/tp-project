from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tp_project.api import router

app = FastAPI(
    title="Currency and Temperature Converter",
    description="API for Currency and Temperature Converter",
    version="0.1.0",
    docs_url="/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
