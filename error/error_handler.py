from fastapi import HTTPException
from datetime import datetime

class MinIOConnectionError(HTTPException):
    def __init__(self):
        super().__init__(status_code=503, detail="Cannot connect to MinIO server.")

class MinIOAuthError(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Invalid MinIO credentials.")

class MinIOClientError(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=500, detail=f"MinIO client error: {message}")

class MinIOUnexpectedError(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=500, detail=f"Unexpected error: {message}")
