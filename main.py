from fastapi import FastAPI
from routes.user_route import router as user_router
from routes.minio_route import router as minio_router
from utils.error_handler import add_custom_exception_handler
import logging
from scheduler.scheduler import start_scheduler, shutdown_scheduler

# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s', filename="app.log")
# logger = logging.getLogger(__name__)
# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set logger level

# Create file handler to log to a file
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.ERROR)  # Log ERROR and above to file
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Create console handler to log to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Log INFO and above to console
console_formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

app = FastAPI(title="My FastAPI App", version="1.0.0")
# from fastapi.middleware.cors import CORSMiddleware

# Add route
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(minio_router, prefix="/minio", tags=["MinIO"])

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

@app.on_event("startup")
def on_startup():
    logger.info("🛠 Starting scheduler...")
    try:
        start_scheduler()
        logger.info("🛠 Scheduler initialized.")
        logger.info("✅ Scheduler started.")
    except Exception as e:
        logger.error(f"❌ Failed to start scheduler: {e}")

@app.on_event("shutdown")
def on_shutdown():
    shutdown_scheduler()
    logger.info("🛑 App stopped.")

@app.get("/")
def root():
    return {"message": "Scheduler is running. Check logs for sync."}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}