import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models import Base

@pytest.fixture(scope="function")
def session():
    # Banco SQLite em memória para testes isolados
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session  
    
    session.rollback()
    session.close()

