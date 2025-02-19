from note import Note


class NotesApp:
    def __init__(self):
        self.notes = []

    def add_note(self, title: str, content: str):
        new_note = Note(title, content)
        self.notes.append(new_note)

    def search_notes(self, keyword: str):
        return [note for note in self.notes if
                keyword.lower() in note.title.lower() or keyword.lower() in note.content.lower()]

    def delete_note(self, title: str):
        self.notes = [note for note in self.notes if note.title != title]

    def display_notes(self):
        for note in self.notes:
            print(note)
            print("-" * 20)


if __name__ == "__main__":
    app = NotesApp()
    app.add_note("First Note", "This is the content of the first note.")
    app.add_note("Second Note", "This is the content of the second note.")

    print("All Notes:")
    app.display_notes()

    print("\nSearching for 'first':")
    search_results = app.search_notes("first")
    for note in search_results:
        print(note)

    print("\nDeleting 'First Note'...")
    app.delete_note("First Note")

    print("\nAll Notes after deletion:")
    app.display_notes()