"""Ядро графа идеи: карточки, связи, операции, журнал. Без интерфейса и без моделей."""

from .errors import ConflictError, GraphError
from .model import (
    ACCEPTED,
    DETAIL,
    HUMAN,
    PROPOSED,
    ROOT_KIND,
    STATUS_NAMES,
    STATUSES,
    author_name,
    is_human,
)
from .store import DIR_NAME, Store
from . import views

__version__ = "0.1.0"

__all__ = [
    "ACCEPTED", "DETAIL", "DIR_NAME", "HUMAN", "PROPOSED", "ROOT_KIND", "STATUSES", "STATUS_NAMES",
    "ConflictError", "GraphError", "Store", "author_name", "is_human", "views",
]
