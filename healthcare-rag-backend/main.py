from fastapi import FastAPI
from routers import upload, embed

app = FastAPI()

app.include_router(embed.router, prefix="/api")
