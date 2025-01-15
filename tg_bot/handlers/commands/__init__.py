from aiogram import Router

router = Router()

from . import entrance
from . import compliant

__all__ = ["router"]
