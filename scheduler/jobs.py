from services.sync_service import fetch_external_data

def daily_sync_job():
    # Nếu job này cần gọi async function thì bạn cần wrap bằng asyncio
    import asyncio
    asyncio.run(fetch_external_data())
