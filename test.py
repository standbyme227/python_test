import sentry_sdk

sentry_sdk.init(dsn="https://0b8f03890a464d03a0dd06783d885136@sentry.io/1332439")

result_id = sentry_sdk.capture_exception(my_exeption)

x = 0
y = 1
print(y // x)
