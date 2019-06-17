# -*- coding: utf-8 -*-

import logging
import os
import json
import boto3
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info(">>>>> Function start")
    search_endpoint = os.environ['ESHOST']
    region = os.environ['REGION']
    query = event.get('queryStringParameters').get('q')
    resultsize = event.get('queryStringParameters').get('size') or 20
    resultfrom = event.get('queryStringParameters').get('from') or 0
    session = boto3.session.Session()
    credentials = session.get_credentials()
    awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, 'es', session_token=credentials.token)

    es = Elasticsearch(
        hosts=[{'host': search_endpoint, 'port': 443}],
        http_auth=awsauth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )

    try:
        result = es.search(index='amiga-freeware', q=query, size=resultsize, from_=resultfrom)
    except Exception as e:
        logger.error("Something bad happened", exc_info=True)
        result = "exception - see log"

    return {
        "statusCode": 200,
        "headers": {
            "X-Content-Type-Options" : "nosniff",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "query": query,
            "result": result
        })
    }
