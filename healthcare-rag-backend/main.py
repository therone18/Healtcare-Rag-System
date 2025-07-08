from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import query, embed  # ✅ make sure this exists

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include both routers
app.include_router(query.router, prefix="/api")
app.include_router(embed.router, prefix="/api")
