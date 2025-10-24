from enum import Enum
import uuid
from datetime import datetime
from sqlalchemy.dialects import postgresql
from sqlalchemy import types
from sqlalchemy import DateTime, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class PollsStatus(Enum):
    NAO_INICIADO = "não iniciado"
    INICIADO = "iniciado"
    EM_ANDAMENTO = "em andamento"
    FINALIZADO = "finalizado"

class Polls(Base):
    __tablename__="polls"

    id: Mapped[uuid.UUID] = mapped_column(
        postgresql.UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4
    )
    question: Mapped[str] = mapped_column(String(200))
    status: Mapped[PollsStatus] = mapped_column(
        types.Enum(PollsStatus, 
        name="poll_status_enum"), 
        nullable=False, 
        default=PollsStatus.NAO_INICIADO
    )
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    options: Mapped[list["Options"]] =relationship(
        back_populates="poll", 
        cascade="all, delete-orphan"
    )

class Options(Base):
    __tablename__="options"

    id: Mapped[uuid.UUID] = mapped_column(
        postgresql.UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4
    )
    poll_id: Mapped[uuid.UUID] = mapped_column(
        postgresql.UUID(as_uuid=True), 
        ForeignKey("polls.id", ondelete="CASCADE"), 
        nullable=False
    )
    text: Mapped[str]
    votes: Mapped[int] = mapped_column(default=0)

    polls: Mapped["Polls"] = relationship(back_populates="options")

    