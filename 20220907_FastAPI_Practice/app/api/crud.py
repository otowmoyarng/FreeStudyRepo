from sqlalchemy import select
from sqlalchemy.orm import Session
from app.api.schemas import ProgrammerDetail
from app.db.models import Programmer, ProgrammerLanguage
from typing import List


def get_programmers(db: Session) -> List[Programmer]:
    programmers = db.scalars(
        select(
            Programmer,
        ).order_by("id")
    ).all()
    return programmers


def _get_programmer_by_name(
    db: Session,
    name: str
) -> ProgrammerDetail:
    """nameをキーにprogrammerを返します"""

    return db.execute(
        select(
            Programmer,
        ).
        filter_by(
            name=name
        )
    ).scalar()


def get_programmer_detail_by_name(
    db: Session,
    name: str
) -> ProgrammerDetail:
    """nameをキーにprogrammer詳細を返します"""

    programmer = _get_programmer_by_name(db, name)
    programmer_detail = ProgrammerDetail(
        name=programmer.name,
        twitter_id=programmer.twitter_id,
        languages=[
            language.name for language in programmer.languages
        ]
    )
    return programmer_detail


def add_programmer(db: Session, programmer_detail: ProgrammerDetail):
    programmer = Programmer()
    programmer.name = programmer_detail.name
    programmer.twitter_id = programmer_detail.twitter_id
    programmer.languages = [
        ProgrammerLanguage(name=language)
        for language in programmer_detail.languages
    ]
    db.add(programmer)
    db.commit()


def update_programmer(db: Session, name: str, programmer_detail: ProgrammerDetail):
    programmer = _get_programmer_by_name(db, name)
    programmer.name = programmer_detail.name
    programmer.twitter_id = programmer_detail.twitter_id
    programmer.languages = [
        ProgrammerLanguage(name=language)
        for language in programmer_detail.languages
    ]
    db.add(programmer)
    db.commit()


def delete_programmer(db: Session, name: str):
    programmer = _get_programmer_by_name(db, name)
    db.delete(programmer)
    db.commit()


def exists_programmer(db: Session, name: str) -> bool:
    return db.execute(
        select(
            select(Programmer).filter_by(name=name).exists(),
        )
    ).scalar_one()
