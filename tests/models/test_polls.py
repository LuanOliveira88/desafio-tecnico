import copy
from datetime import datetime

import pytest
from sqlalchemy.exc import IntegrityError
from src.models import Polls, PollsStatus

class TestPolls:


    def test_valid_polls(self, session, valid_poll):
    
        session.add(valid_poll)
        session.commit()
        retrieved_poll = session.query(Polls).first() 
        assert retrieved_poll.question == "Qual a sua linguagem favorita?"
        assert retrieved_poll.status == PollsStatus.NAO_INICIADO
        assert retrieved_poll.start_date == datetime(2025, 11, 24)
        assert retrieved_poll.end_date == datetime(2025, 11, 25)

    @pytest.mark.xfail(raises=IntegrityError)
    def test_no_question_polls(self, session, valid_poll):

        no_question_poll = copy.deepcopy(valid_poll)
        no_question_poll.question = None

        session.add(no_question_poll)
        session.commit()


    @pytest.mark.xfail(raises=IntegrityError)
    def test_no_start_date_polls(self, session, valid_poll):

        no_start_date_poll = copy.deepcopy(valid_poll)
        no_start_date_poll.start_date = None

        session.add(no_start_date_poll)
        session.commit()
        
    @pytest.mark.xfail(raises=IntegrityError)
    def test_no_end_date_polls(self, session, valid_poll):

        no_end_date_poll = copy.deepcopy(valid_poll)
        no_end_date_poll.end_date = None

        session.add(no_end_date_poll)
        session.commit()
        

    @pytest.mark.xfail(raises=ValueError)
    def test_min_options(self, session, valid_poll):

        two_options_poll = copy.deepcopy(valid_poll)
        two_options_poll.options.pop()

        session.add(two_options_poll)
        session.commit()