import sentry_sdk
import logging
from sentry_sdk.integrations.logging import LoggingIntegration

serty_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.INFO
)
sentry_sdk.init(
    dsn="Your_dsn",
    traces_sample_rate=1.0,
    integrations=[
        serty_logging
    ]
)

