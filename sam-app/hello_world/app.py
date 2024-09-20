import pytest
from aws_lambda_powertools import Logger
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()


def add(a, b):
    return a + b


def lambda_handler(event, context: LambdaContext) -> dict:
    return "test"
