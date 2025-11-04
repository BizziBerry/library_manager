"""
Модуль для генерации отчетов о книгах в библиотеке.
"""

from typing import List
from .catalog import Library, Book
from .utils.formatting import format_book_data


def generate_report(library: Library) -> str:
    """
    Генерирует отчет о всех книгах в библиотеке.
    
    Args:
        library: Экземпляр класса Library
        
    Returns:
        str: Отформатированный отчет
    """
    books = library.get_all_books()
    
    if not books:
        return "Библиотека пуста."
    
    report_lines = [f"Отчет о книгах в библиотеке (всего: {len(books)})", 
                   "=" * 50]
    
    for i, book in enumerate(books, 1):
        book_data = book.to_dict()
        formatted_book = format_book_data(book_data)
        report_lines.append(f"{i}. {formatted_book}")
    
    return "\n".join(report_lines)


def generate_detailed_report(library: Library) -> str:
    """
    Генерирует детализированный отчет с группировкой по авторам и жанрам.
    
    Args:
        library: Экземпляр класса Library
        
    Returns:
        str: Детализированный отчет
    """
    books = library.get_all_books()
    
    if not books:
        return "Библиотека пуста."
    
    # Группировка по авторам
    authors = {}
    genres = {}
    
    for book in books:
        author = book.author
        genre = book.genre
        
        if author not in authors:
            authors[author] = []
        authors[author].append(book)
        
        if genre not in genres:
            genres[genre] = []
        genres[genre].append(book)
    
    report_lines = [
        f"Детализированный отчет о библиотеке (всего книг: {len(books)})",
        "=" * 60
    ]
    
    # Отчет по авторам
    report_lines.append("\nКниги по авторам:")
    report_lines.append("-" * 30)
    for author, author_books in sorted(authors.items()):
        report_lines.append(f"\n{author} ({len(author_books)} книг):")
        for book in author_books:
            report_lines.append(f"  - {book.title} ({book.genre})")
    
    # Отчет по жанрам
    report_lines.append("\n\nКниги по жанрам:")
    report_lines.append("-" * 30)
    for genre, genre_books in sorted(genres.items()):
        report_lines.append(f"\n{genre} ({len(genre_books)} книг):")
        for book in genre_books:
            report_lines.append(f"  - {book.title} - {book.author}")
    
    return "\n".join(report_lines)