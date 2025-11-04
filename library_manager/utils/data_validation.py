"""
Модуль для валидации данных книг.
"""

from typing import Dict


def validate_book_data(data: Dict) -> bool:
    """
    Проверяет корректность данных книги.
    
    Args:
        data: Словарь с данными книги
        
    Returns:
        bool: True если данные корректны, False в противном случае
    """
    required_fields = ['title', 'author', 'genre']
    
    # Проверяем наличие всех обязательных полей
    for field in required_fields:
        if field not in data:
            return False
    
    # Проверяем, что поля не пустые
    for field in required_fields:
        value = data[field]
        if not isinstance(value, str) or not value.strip():
            return False
    
    # Проверяем длину полей (опционально)
    if len(data['title'].strip()) < 1:
        return False
    if len(data['author'].strip()) < 2:
        return False
    if len(data['genre'].strip()) < 2:
        return False
    
    return True


def validate_book_exists(library, title: str, author: str) -> bool:
    """
    Проверяет, существует ли книга с таким названием и автором.
    
    Args:
        library: Экземпляр библиотеки
        title: Название книги
        author: Автор книги
        
    Returns:
        bool: True если книга существует, False в противном случае
    """
    existing_books = library.search_books(title=title, author=author)
    return len(existing_books) > 0