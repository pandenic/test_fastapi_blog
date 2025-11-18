from __future__ import annotations

import logging
from typing import Coroutine

from fastapi import HTTPException, status

from exceptions import ItemNotFoundError
from models import SQLModelType


async def execute_and_handle_api_exceptions(
    coroutine: Coroutine, logger: logging.Logger,
) -> SQLModelType | None:
    try:
        obj: SQLModelType | list[SQLModelType] | None = await coroutine
    except ItemNotFoundError as e:
        raise e
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return obj