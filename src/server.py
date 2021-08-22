from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import routers_products, routers_users

app = FastAPI()

# CORS
origins = [
  "http://localhost:3000"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins= origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(routers_products.router)
app.include_router(routers_users.router)
