import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
import logging

sentry_sdk.init(dsn="https://0b8f03890a464d03a0dd06783d885136@sentry.io/1332439")

sentry_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.ERROR
)

sentry_sdk.init(
    dsn="https://0b8f03890a464d03a0dd06783d885136@sentry.io/1332439",
    integrations=[sentry_logging]
)

logging.debug("I am a breadcrumb")
logging.error("I am an event", extra=dict(just_test="True"))





# def before_breadcrumb(crumb, hint):
#     if 'log_record' in hint:
#         crumb['data']['thread'] = hint['log_record'].threadName
#     return crumb
#
#
# sentry_sdk.init(dsn="https://0b8f03890a464d03a0dd06783d885136@sentry.io/1332439",
#                 before_breadcrumb=before_breadcrumb)

x = 0
y = 1
print(y // x)
