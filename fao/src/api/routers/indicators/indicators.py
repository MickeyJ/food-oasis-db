from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, func, or_, text
from typing import Optional
from fao.src.core import settings
from fao.src.db.database import get_db
from fao.src.db.pipelines.indicators.indicators_model import Indicators

router = APIRouter(
    prefix="/indicators",
    tags=["indicators"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_indicators(
    limit: int = Query(settings.default_limit, le=settings.max_limit, ge=1, description="Maximum records to return"),
    offset: int = Query(settings.default_offset, ge=0, description="Number of records to skip"),
    db: Session = Depends(get_db)
):
    """
    indicators data with filters.
    Filter options:
    """
    
    query = (
        select(
            Indicators,
        )
        .select_from(Indicators)
    )
    
    # Apply filters
   
    
    # Get total count (with filters)
    total_count = db.execute(select(func.count()).select_from(query.subquery())).scalar()
    
    # Paginate and execute
    query = query.offset(offset).limit(limit)
    results = db.execute(query).mappings().all()
    
    return {
        "total_count": total_count,
        "limit": limit,
        "offset": offset,
        "data": [dict(row) for row in results]
    }

