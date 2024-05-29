from note import Note
import json

class NoteManager:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_notes(self):
        with open(self.filename, 'w') as file:
            json.dump(self.notes, file, indent=4)

    def create_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note.to_dict())
        self.save_notes()

    def list_notes(self):
        return self.notes

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note['id'] == note_id:
                return note
        return None

    def update_note(self, note_id, title=None, content=None):
        for note in self.notes:
            if note['id'] == note_id:
                if title:
                    note['title'] = title
                if content:
                    note['content'] = content
                self.save_notes()
                return True
        return False

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note['id'] != note_id]
        self.save_notes()
