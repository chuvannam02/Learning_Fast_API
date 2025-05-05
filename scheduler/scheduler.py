from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from scheduler.jobs import daily_sync_job
import logging

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()

def start_scheduler():
    logger.info("⏰ Starting APScheduler...")
    scheduler.add_job(daily_sync_job, CronTrigger(hour=2, minute=0))  # 2:00 sáng
    # scheduler.add_job(daily_sync_job, CronTrigger(hour=14, minute=0))  # 2:00 chiều
    # scheduler.add_job(daily_sync_job, CronTrigger(hour=22, minute=0))  # 10:00 tối
    # scheduler.add_job(daily_sync_job, 'interval', minutes=1)
    scheduler.add_job(daily_sync_job, 'interval', seconds=10)  # Mỗi 10 giây (chỉ để test)
    
    scheduler.start()

def shutdown_scheduler():
    logger.info("🛑 Shutting down scheduler...")
    scheduler.shutdown()
