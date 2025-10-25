from sqlalchemy.orm import Session as SessionType

from src.models import Polls

def before_commit_listener(session: SessionType):
    for obj in session.new:
        if isinstance(obj, Polls) and len(obj.options) < 3:
            raise ValueError('Uma enquete deve ter pelo menos 3 opções')


