import sentry_sdk
import.logging
sentry_sdk.init(
    "https://40c6f5d872f542209a18bf65c549dd2f@o1078166.ingest.sentry.io/6081752",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

logger=logging.getlogger("sentry")
try:
    storage_read=open("writting10.txt")
    container=storage_read.read()
    print(container)

except FileNotFound as hint:
    logger.error(hint)
    