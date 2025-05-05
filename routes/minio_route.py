from fastapi import APIRouter, HTTPException
from botocore.client import Config
import boto3
from botocore.exceptions import EndpointConnectionError, NoCredentialsError, ClientError, BotoCoreError
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import logging
from error.error_handler import MinIOConnectionError, MinIOAuthError, MinIOClientError, MinIOUnexpectedError

# Thiết lập logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s', filename="app.log")

router = APIRouter()

# Response model
# class BucketItem(BaseModel):
#     name: str
#     created_at: str  # hoặc datetime nếu muốn trả ISO format

# class BucketListResponse(BaseModel):
#     buckets: List[BucketItem]

class BucketItem(BaseModel):
    name: str
    created_at: datetime

class OwnerInfo(BaseModel):
    display_name: str
    id: str

class BucketListResponse(BaseModel):
    buckets: List[BucketItem]
    owner: OwnerInfo
    request_id: Optional[str]
    http_status: Optional[int]

class BucketListErrorResponse(BaseModel):
    error_code: int
    error_message: str
    timestamp: datetime

# MinIO / S3 client
s3_client = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin",
    config=Config(signature_version="s3v4"),
    region_name="us-east-1"
)

@router.get("/", response_model=BucketListResponse)
def list_buckets():
    try:
        response = s3_client.list_buckets()
        # Extract bucket names from the response
        # syntax list comprehension to get the bucket names
        # bucket_names = [bucket["Name"] for bucket in response.get("Buckets", [])]

        # Cách viết bình thường
        # bucket_names = []
        # for bucket in response.get("Buckets", []):
        #     bucket_names.append(bucket["Name"])
        # print(response)

         # Trích xuất name và creation date của từng bucket
        # bucket_items = [
        #     BucketItem(
        #         name=bucket["Name"],
        #         created_at=bucket["CreationDate"].isoformat()
        #     )
        #     for bucket in response.get("Buckets", [])
        # ]
        # return BucketListResponse(buckets=bucket_items)

        bucket_items = [
            BucketItem(
                name=bucket["Name"],
                created_at=bucket["CreationDate"]
            )
            for bucket in response.get("Buckets", [])
        ]

        owner = response.get("Owner", {})
        metadata = response.get("ResponseMetadata", {})

        return BucketListResponse(
            buckets=bucket_items,
            owner=OwnerInfo(
                display_name=owner.get("DisplayName", ""),
                id=owner.get("ID", "")
            ),
            request_id=metadata.get("RequestId"),
            http_status=metadata.get("HTTPStatusCode")
        )
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=f"Failed to list buckets: {str(e)}")
     # Cụ thể hóa lỗi
    # except EndpointConnectionError:
    #     raise HTTPException(status_code=503, detail="Cannot connect to MinIO server.")
    # except NoCredentialsError:
    #     raise HTTPException(status_code=401, detail="Invalid MinIO credentials.")
    # except ClientError as e:
    #     raise HTTPException(status_code=500, detail=f"MinIO client error: {e.response['Error']['Message']}")
    # except BotoCoreError as e:
    #     # f"" là f-string, cho phép nhúng biểu thức vào chuỗi
    #     # Ví dụ: f"{variable}"
    #     # raise HTTPException(status_code=500, detail=f"BotoCore error: {str(e)}")
    #     # Đầu vào là một chuỗi, đầu ra là một chuỗi
    #     # Console: print(f"BotoCore error: {str(e)}")
    #     raise HTTPException(status_code=500, detail=f"BotoCore error: {str(e)}")
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    except EndpointConnectionError:
        logging.error("Cannot connect to MinIO server.")
        raise MinIOConnectionError()
    
    except NoCredentialsError:
        logging.error("Invalid credentials for MinIO.")
        raise MinIOAuthError()
    
    except ClientError as e:
        error_message = e.response['Error']['Message']
        logging.error(f"Client error: {error_message}")
        raise MinIOClientError(error_message)
    
    except BotoCoreError as e:
        logging.error(f"BotoCore error: {str(e)}")
        raise MinIOUnexpectedError(str(e))
    
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise MinIOUnexpectedError(str(e))
