import logging

import requests
from requests.exceptions import Timeout, RequestException

logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
)

logger = logging.getLogger(__name__)

handles = []

base_url = 'https://twitter.com/{}'

logger.info('Running on {}'.format(', '.join(handles)))

for h in handles:
    try:
        resp = requests.get(base_url.format(h))
    except RequestException as e:
        logger.error(e)
        pass

    if resp.status_code == 404:
        logger.info(f'404 on {h}')
    elif resp.status_code == 200:
        logger.info(f'200 on {h}')
    else:
        logger.info(f'{resp.status_code} on {h}')
