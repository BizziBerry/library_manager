"""
Пакет для управления библиотекой.
"""

from .catalog import Library
from .report import generate_report

__all__ = ['Library', 'generate_report']
__version__ = '1.0.0'