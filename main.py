from note_manager import NoteManager

def main():
    manager = NoteManager()

    # Создание заметки
    manager.create_note('Первая заметка', 'Это содержание первой заметки')

    # Список всех заметок
    notes = manager.list_notes()
    print("Все заметки:")
    for note in notes:
        print(note)

    # Обновление заметки
    if notes:
        first_note_id = notes[0]['id']
        manager.update_note(first_note_id, content='Обновленное содержание первой заметки')

    # Получение заметки по id
    note = manager.get_note_by_id(first_note_id)
    if note:
        print("Обновленная заметка:")
        print(note)

    # Удаление заметки
    manager.delete_note(first_note_id)
    print("Заметки после удаления:")
    print(manager.list_notes())

if __name__ == "__main__":
    main()
