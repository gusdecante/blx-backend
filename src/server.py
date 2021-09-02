from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.routers import routers_products, routers_auth, routers_deals

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
app.include_router(routers_auth.router, prefix="/auth")
app.include_router(routers_deals.router)

@app.middleware('http')
async def process_request_time(request: Request, next):
  print('Inteceptou a chegada...')
  response = await next(request)

  print('Interceptou a volta')
  return response