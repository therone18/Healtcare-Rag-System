from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import query, embed, upload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query.router, prefix="/api")
app.include_router(embed.router, prefix="/api")
app.include_router(upload.router, prefix="/api")