# templates/model.py.jinja2
from sqlalchemy import (
    String,
    Integer,
    DateTime,
    ForeignKey,
    Index,
    Column,
    func,
)
from fao.src.db.database import Base


class Releases(Base):
    __tablename__ = "releases"
    # Lookup table - use domain primary key
    id = Column(Integer, primary_key=True)
    release_code = Column(String, nullable=False, index=False)
    release = Column(String, nullable=False, index=False)
    source_dataset = Column(String, nullable=False, index=False)
   
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    
    # Composite indexes for reference tables
    __table_args__ = (
        Index("ix_releases_release__src", 'release_code', 'source_dataset', unique=True),
    )
    # TODO: Indices for dataset tables
    #     
    def __repr__(self):
        return f"<Releases(release_code={self.release_code})>"
