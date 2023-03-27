import postgre_logger as logger
import random
import time
import traceback
import logging
import sentry_logger
import newrelic.agent
import time
newrelic.agent.initialize('newrelic.ini')
import logging
from newrelic.agent import NewRelicContextFormatter
def division_postgre(val1, val2):
    logger.info(f'Divison started ({val1} / {val2})')
    result = None
    try:
        result = val1 / val2
        logger.info(f'Divison finished ({val1} / {val2} = {result})')
    except Exception as e:
        logger.error(f'Divison error ({val1} / {val2}). {traceback.format_exc()}')
    return result

def division_sentry(val1,val2):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    result = None
    try:
        result = val1 / val2
        logger.info(f'Divison finished ({val1} / {val2} = {result})')
    except ZeroDivisionError as err:
        logging.error(f'Divison error ({val1} / {val2}).{result}')
    return result
def execute_task(application, task_name,val1, val2):
    with newrelic.agent.BackgroundTask(application, name=task_name, group='Task'):
        def division_newrelic(val1, val2):
            try:
                result = val1 / val2
                return (f'Division finished ({val1} / {val2} = {result})')
            except ZeroDivisionError as err:
                result = f'Division error ({val1} / {val2}): {err}'
            return result
        result = division_newrelic(val1, val2)
        logging.info(result)
while True:
    (val1, val2) = (random.randint(1, 100), random.randint(0, 3))
    time.sleep(0.5)
    division_postgre(val1, val2)
    time.sleep(0.5)
    division_sentry(val1, val2)
    time.sleep(0.5)
    execute_task(newrelic.agent.register_application(timeout=0.2), "bar" ,val1, val2)





