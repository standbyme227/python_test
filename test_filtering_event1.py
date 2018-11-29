import sentry_sdk

def strip_sensitive_data(event, hint):
    # Modify event
    # event = None
    return event

sentry_sdk.init(
    dsn="https://0b8f03890a464d03a0dd06783d885136@sentry.io/1332439",
    before_send=strip_sensitive_data
)

x = 0
y = 1
print(y // x)