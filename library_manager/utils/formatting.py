"""
Модуль для форматирования данных книг.
"""

from typing import Dict


def format_book_data(data: Dict) -> str:
    """
    Форматирует данные книги для вывода в отчет.
    
    Args:
        data: Словарь с данными книги
        
    Returns:
        str: Отформатированная строка с данными книги
    """
    title = data.get('title', 'Неизвестно')
    author = data.get('author', 'Неизвестно')
    genre = data.get('genre', 'Неизвестно')
    
    return f"Title: {title}, Author: {author}, Genre: {genre}"


def format_book_short(book) -> str:
    """
    Форматирует книгу в коротком формате.
    
    Args:
        book: Экземпляр класса Book
        
    Returns:
        str: Короткое описание книги
    """
    return f"'{book.title}' - {book.author}"


def format_book_detailed(book) -> str:
    """
    Форматирует книгу в подробном формате.
    
    Args:
        book: Экземпляр класса Book
        
    Returns:
        str: Подробное описание книги
    """
    return f"Название: {book.title}\nАвтор: {book.author}\nЖанр: {book.genre}\n"