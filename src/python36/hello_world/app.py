# -*- coding: utf-8 -*-

import requests


def lambda_handler(event, context):
    url = 'https://checkip.amazonaws.com'
    res = requests.get(url)
    return {
        'status_code': res.status_code,
        'ip_addr': res.text.strip(),
    }
