from sqlalchemy.orm import Session

from models.prompt import Prompt


class CRUDPrompt:
    model = Prompt

    def get(self, db: Session, id: int) -> Prompt | None:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session) -> list[Prompt]:
        return db.query(self.model).all()


crud_prompt = CRUDPrompt()
