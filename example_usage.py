import sys
import os
from datetime import datetime

from library_manager import Library, generate_report

def main():
    # Создаем библиотеку
    library = Library()
    
    # Добавляем книги
    library.add_book("Война и мир", "Лев Толстой", "Роман")
    library.add_book("Преступление и наказание", "Федор Достоевский", "Роман")
    library.add_book("Мастер и Маргарита", "Михаил Булгаков", "Фантастика")
    library.add_book("1984", "Джордж Оруэлл", "Антиутопия")
    library.add_book("Гарри Поттер и философский камень", "Джоан Роулинг", "Фэнтези")
    
    # Получаем текущую дату и время
    current_time = datetime.now()
    formatted_time = current_time.strftime("%d.%m.%Y %H:%M:%S")
    
    print("=" * 60)
    print(f"ОТЧЕТ СГЕНЕРИРОВАН: {formatted_time}")
    print("=" * 60)
    
    # Генерируем отчет
    print("\n=== ОСНОВНОЙ ОТЧЕТ О БИБЛИОТЕКЕ ===")
    report = generate_report(library)
    print(report)
    
    print("\n" + "=" * 50)
    print("ПОИСК И ОПЕРАЦИИ С КНИГАМИ")
    print("=" * 50)
    
    # Поиск по автору
    print("\n--- Поиск по автору 'Толстой' ---")
    tolsto_books = library.search_by_author("Толстой")
    print(f"Найдено книг: {len(tolsto_books)}")
    for book in tolsto_books:
        print(f"  - {book.title} ({book.genre})")
    
    # Поиск по жанру
    print("\n--- Поиск по жанру 'Роман' ---")
    novels = library.search_by_genre("роман")
    print(f"Найдено книг: {len(novels)}")
    for book in novels:
        print(f"  - {book.title} - {book.author}")
    
    # Поиск по нескольким критериям
    print("\n--- Поиск русской классики ---")
    russian_classics = library.search_books(author="Достоевский", genre="Роман")
    print(f"Найдено книг: {len(russian_classics)}")
    for book in russian_classics:
        print(f"  - {book.title}")
    
    print("\n" + "=" * 50)
    print("ОПЕРАЦИИ С БИБЛИОТЕКОЙ")
    print("=" * 50)
    
    # Показываем текущее состояние
    print(f"\nКоличество книг до удаления: {library.count_books()}")
    
    # Удаление книги
    print("\n--- Удаление книги '1984' ---")
    if library.remove_book("1984"):
        print("Книга успешно удалена!")
    else:
        print("Книга не найдена!")
    
    # Показываем итоговое состояние
    print(f"\nКоличество книг после удаления: {library.count_books()}")
    
    # Финальный отчет
    print("\n" + "=" * 60)
    print("ФИНАЛЬНЫЙ ОТЧЕТ")
    print("=" * 60)
    final_report = generate_report(library)
    print(final_report)
    
    # Статистика
    print("\n" + "=" * 40)
    print("СТАТИСТИКА БИБЛИОТЕКИ")
    print("=" * 40)
    print(f"Общее количество книг: {library.count_books()}")
    
    # Группировка по жанрам
    genres = {}
    for book in library.get_all_books():
        if book.genre not in genres:
            genres[book.genre] = 0
        genres[book.genre] += 1
    
    print("\nКниги по жанрам:")
    for genre, count in genres.items():
        print(f"  - {genre}: {count} книг(и)")
    
    print("\n" + "=" * 60)
    print(f"ОТЧЕТ ЗАВЕРШЕН: {formatted_time}")
    print("=" * 60)

if __name__ == "__main__":
    main()