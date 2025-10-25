from datetime import datetime

import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session as SessionType

from src.models import Base, Polls, PollsStatus, Options
from src.db.events import before_commit_listener

@pytest.fixture(scope="function")
def session():
    # Banco SQLite em memória para testes isolados
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)
    
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    event.listen(SessionLocal, 'before_commit', before_commit_listener)
    # event.listen(Polls)

    yield session  
    
    session.rollback()
    session.close()


@pytest.fixture(scope='function')
def valid_poll():
    valid_poll = Polls(
            question="Qual a sua linguagem favorita?",
            status=PollsStatus.NAO_INICIADO,
            start_date=datetime(2025, 11, 24),
            end_date=datetime(2025, 11, 25)
        )
    valid_poll.options = [
        Options(text='Python'),
        Options(text='Javascript'),
        Options(text='Java'),
    ]

    return valid_poll