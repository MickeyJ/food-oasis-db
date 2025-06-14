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


class PopulationAgeGroups(Base):
    __tablename__ = "population_age_groups"
    # Lookup table - use domain primary key
    id = Column(Integer, primary_key=True)
    population_age_group_code = Column(String, nullable=False, index=False)
    population_age_group = Column(String, nullable=False, index=False)
    source_dataset = Column(String, nullable=False, index=False)
   
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    
    # Composite indexes for reference tables
    __table_args__ = (
        Index("ix_populati_populati_src", 'population_age_group_code', 'source_dataset', unique=True),
    )
    # TODO: Indices for dataset tables
    #     
    def __repr__(self):
        return f"<PopulationAgeGroups(population_age_group_code={self.population_age_group_code})>"
