from sqlalchemy import create_engine, text


class SubjectsTable:
    def __init__(self, connection_string: str):
        self.db = create_engine(connection_string)

    def get_max_id(self) -> int:
        with self.db.connect() as conn:
            result = conn.execute(
                text("SELECT COALESCE(MAX(subject_id), 0) FROM subject")
            )
            return result.scalar()

    def create(self, subject_id: int, title: str):
        with self.db.begin() as conn:
            conn.execute(
                text(
                    "INSERT INTO subject (subject_id, subject_title) "
                    "VALUES (:id, :title)"
                ),
                {"id": subject_id, "title": title}
            )

    def get_by_id(self, subject_id: int):
        with self.db.connect() as conn:
            result = conn.execute(
                text("SELECT * FROM subject WHERE subject_id = :id"),
                {"id": subject_id}
            )
            return result.mappings().first()

    def update(self, subject_id: int, new_title: str):
        with self.db.begin() as conn:
            conn.execute(
                text(
                    "UPDATE subject SET subject_title = :title "
                    "WHERE subject_id = :id"
                ),
                {"id": subject_id, "title": new_title}
            )

    def delete(self, subject_id: int):
        with self.db.begin() as conn:
            conn.execute(
                text("DELETE FROM subject WHERE subject_id = :id"),
                {"id": subject_id}
            )
