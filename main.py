import argparse
from note_manager import NoteManager

def main():
    parser = argparse.ArgumentParser(description="Note Management System")
    subparsers = parser.add_subparsers(dest='command')

    # Команда для добавления заметки
    add_parser = subparsers.add_parser('add', help='Add a new note')
    add_parser.add_argument('--title', required=True, help='Title of the note')
    add_parser.add_argument('--msg', required=True, help='Content of the note')

    # Команда для чтения всех заметок
    list_parser = subparsers.add_parser('list', help='List all notes')

    # Команда для чтения заметок по дате
    filter_parser = subparsers.add_parser('filter', help='Filter notes by date')
    filter_parser.add_argument('--date', required=True, help='Date to filter notes (YYYY-MM-DD)')

    # Команда для обновления заметки
    update_parser = subparsers.add_parser('update', help='Update a note')
    update_parser.add_argument('--id', type=int, required=True, help='ID of the note')
    update_parser.add_argument('--title', help='New title of the note')
    update_parser.add_argument('--msg', help='New content of the note')

    # Команда для удаления заметки
    delete_parser = subparsers.add_parser('delete', help='Delete a note')
    delete_parser.add_argument('--id', type=int, required=True, help='ID of the note')

    args = parser.parse_args()
    manager = NoteManager()

    if args.command == 'add':
        manager.create_note(args.title, args.msg)

    elif args.command == 'list':
        notes = manager.list_notes()
        for note in notes:
            print(note)

    elif args.command == 'filter':
        notes = manager.filter_notes_by_date(args.date)
        for note in notes:
            print(note)

    elif args.command == 'update':
        manager.update_note(args.id, title=args.title, content=args.msg)

    elif args.command == 'delete':
        manager.delete_note(args.id)

if __name__ == "__main__":
    main()
