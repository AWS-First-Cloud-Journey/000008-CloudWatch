#!/usr/bin/env python3
import logging
import logging.handlers
import random
import time

# --- Thiết lập logger ---
logger = logging.getLogger('logger.runJob')
logger.setLevel(logging.DEBUG)  # cho phép tất cả cấp độ log

# Gửi log đến syslog
syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')
formatter = logging.Formatter('%(name)s: %(levelname)s: %(message)s')
syslog_handler.setFormatter(formatter)
logger.addHandler(syslog_handler)

# --- Một vài câu log mẫu ---
info_messages = [
    "The job finished successfully.",
    "Connection established to database.",
    "Backup process completed.",
    "User session initialized.",
    "Cache warm-up finished.",
]

warning_messages = [
    "Disk usage at 85%, consider cleanup.",
    "Configuration file not found, using defaults.",
    "Job took longer than expected.",
    "API rate limit approaching threshold.",
    "Deprecated function call detected.",
]

error_messages = [
    "Failed to connect to Redis server.",
    "FileNotFoundError: Missing dependency file.",
    "The job failed with critical error. Please check the job configuration.",
    "Timeout while waiting for external service.",
    "Data validation failed: missing required fields.",
]

debug_messages = [
    "Processing batch ID=84219 with size=256",
    "Retrying operation #3 after transient error",
    "Loaded 120 configuration entries",
    "Incoming request headers parsed successfully",
    "Thread pool expanded to 8 workers",
]

critical_messages = [
    "System is out of memory!",
    "Database corruption detected — manual intervention required.",
    "Security breach detected — shutting down services.",
    "Critical dependency missing. Halting execution.",
]

# --- Vòng lặp ghi log ---
while True:
    level = random.choice(['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
    if level == 'DEBUG':
        msg = random.choice(debug_messages)
        logger.debug(msg)
    elif level == 'INFO':
        msg = random.choice(info_messages)
        logger.info(msg)
    elif level == 'WARNING':
        msg = random.choice(warning_messages)
        logger.warning(msg)
    elif level == 'ERROR':
        msg = random.choice(error_messages)
        logger.error(msg)
    elif level == 'CRITICAL':
        msg = random.choice(critical_messages)
        logger.critical(msg)

    time.sleep(random.uniform(1, 4))  # log xen kẽ ngẫu nhiên
