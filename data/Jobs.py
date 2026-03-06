from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader = Column(Integer, index=True)
    job = Column(String, nullable=False)
    work_size = Column(Integer, default=0)
    collaborators = Column(String, default='')
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_finished = Column(Boolean, default=False)
