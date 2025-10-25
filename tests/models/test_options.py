from datetime import datetime

import pytest
from sqlalchemy.exc import IntegrityError

from src.models import Options, PollsStatus

class TestOptions:
    @pytest.mark.parametrize("text", ["Python", "Java", "Javascript"])
    def test_create_valid_option(self, session, valid_poll, text):
        """Testa que é possível criar uma Option válida"""
        poll = valid_poll
        session.add(poll)
        session.commit()

        option = Options(text=text, poll_id=poll.id)
        session.add(option)
        session.commit()
        
        assert option.id is not None
        assert option.text == text
        assert option.poll_id == poll.id

    @pytest.mark.xfail(raises=IntegrityError)
    def test_option_without_text(self, session, valid_poll):
        """Testa que não é permitido criar Option sem texto"""
        poll = valid_poll
        session.add(poll)
        session.commit()

        option = Options(text=None, poll_id=poll.id)
        session.add(option)
        session.commit()

    def test_poll_with_options(self, session, valid_poll):
        """Testa que uma Poll pode ter Options associadas"""
        poll = valid_poll
        session.add(poll)
        session.commit()
        
        assert len(poll.options) == 3
        assert all(o.id is not None for o in poll.options)
        assert all(isinstance(o, Options) for o in poll.options)
