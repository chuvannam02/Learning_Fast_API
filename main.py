from fastapi import FastAPI
from routes.user_route import router as user_router
from utils.error_handler import add_custom_exception_handler

app = FastAPI(title="My FastAPI App", version="1.0.0")
# from fastapi.middleware.cors import CORSMiddleware

# Add route
app.include_router(user_router, prefix="/users", tags=["Users"])

# Add CORS middleware (if needed)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins (or specify a list of allowed origins)
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all HTTP methods (or specify a list of allowed methods)
#     allow_headers=["*"],  # Allow all headers (or specify a list of allowed headers)
# )

# Custom error handler
add_custom_exception_handler(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}