# Logic handle call API và manipulate response
import httpx
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

async def fetch_external_data():
    logger.info(f"[{datetime.now()}] 🔄 Starting daily sync job...")

    try:
        response = httpx.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()
        data = response.json()
        logger.info(f"✅ Synced {len(data)} items.")
        # TODO: Save to DB here
    except httpx.RequestError as e:
        logger.error(f"❌ Request error: {e}")
    except httpx.HTTPStatusError as e:
        logger.error(f"❌ HTTP error: {e.response.status_code}")
    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")
