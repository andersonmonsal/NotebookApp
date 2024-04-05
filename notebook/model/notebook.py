from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Note:
    code: int
    title: str
    text: str
    importance: str
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    creation_date: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"Code: {self.code}\nCreation date: {self.creation_date}\n{self.title}: {self.text}\n"

    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)


@dataclass
class Notebook:
    notes: Dict[int, Note] = field(default_factory=dict)
    last_code: int = 0

    def add_note(self, title: str, text: str, importance: str) -> int:
        self.last_code += 1
        new_note = Note(self.last_code, title, text, importance)
        self.notes[self.last_code] = new_note
        return self.last_code

    def list_notes(self) -> List[Note]:
        return list(self.notes.values())

    def important_notes(self) -> List[Note]:
        return [note for note in self.notes.values() if note.importance.upper() in ("HIGH", "MEDIUM")]

    def delete_note(self, code: int) -> None:
        if code in self.notes:
            del self.notes[code]
        else:
            print(f"No existe ninguna nota con el código {code}")

    def tags_note_count(self) -> Dict[str, int]:
        tags_count: Dict[str, int] = {}
        for note in self.notes.values():
            for tag in note.tags:
                tags_count[tag] = tags_count.get(tag, 0) + 1
        return tags_count


def init_notebook() -> Notebook:
    return Notebook()


def add_note(notebook: Notebook, title: str, text: str, importance: str) -> None:
    code = notebook.add_note(title, text, importance)
    print(f"Nota agregada con código {code}")


def list_notes(notebook: Notebook) -> None:
    notes = notebook.list_notes()
    for note in notes:
        print(note)


def add_tag(notebook: Notebook, code: int, tag: str) -> None:
    note = notebook.notes.get(code)
    if note:
        note.add_tag(tag)
        print(f"Etiqueta '{tag}' agregada a la nota {code}")
    else:
        print(f"No se encontró la nota con código {code}")


def important_notes(notebook: Notebook) -> None:
    notes = notebook.important_notes()
    for note in notes:
        print(note)


def delete_note(notebook: Notebook, code: int) -> None:
    notebook.delete_note(code)
    print(f"Nota con código {code} eliminada")


def tags_notes_count(notebook: Notebook) -> None:
    tags_count = notebook.tags_note_count()
    for tag, count in tags_count.items():
        print(f"Etiqueta '{tag}': {count} notas")


