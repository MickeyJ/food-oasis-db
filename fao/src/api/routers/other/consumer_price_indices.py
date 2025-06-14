from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, func, or_, text
from typing import Optional
from fao.src.core import settings
from fao.src.db.database import get_db
from fao.src.db.pipelines.consumer_price_indices.consumer_price_indices_model import ConsumerPriceIndices
# Import core/reference tables for joins
from fao.src.db.pipelines.area_codes.area_codes_model import AreaCodes
from fao.src.db.pipelines.item_codes.item_codes_model import ItemCodes
from fao.src.db.pipelines.elements.elements_model import Elements
from fao.src.db.pipelines.flags.flags_model import Flags

router = APIRouter(
    prefix="/consumer_price_indices",
    tags=["consumer_price_indices"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_consumer_price_indices(
    limit: int = Query(settings.default_limit, le=settings.max_limit, ge=1, description="Maximum records to return"),
    offset: int = Query(settings.default_offset, ge=0, description="Number of records to skip"),
    area_code: Optional[str] = Query(None, description="Filter by area_codes code"),
    area: Optional[str] = Query(None, description="Filter by area_codes description"),
    item_code: Optional[str] = Query(None, description="Filter by item_codes code"),
    item: Optional[str] = Query(None, description="Filter by item_codes description"),
    element_code: Optional[str] = Query(None, description="Filter by elements code"),
    element: Optional[str] = Query(None, description="Filter by elements description"),
    flag: Optional[str] = Query(None, description="Filter by flags code"),
    description: Optional[str] = Query(None, description="Filter by flags description"),
    db: Session = Depends(get_db)
):
    """
    consumer price indices data with filters.
    Filter options:
    - area_code: Filter by area_codes code
    - area: Filter by area_codes description (partial match)
    - item_code: Filter by item_codes code
    - item: Filter by item_codes description (partial match)
    - element_code: Filter by elements code
    - element: Filter by elements description (partial match)
    - flag: Filter by flags code
    - description: Filter by flags description (partial match)
    """
    
    query = (
        select(
            ConsumerPriceIndices,
            AreaCodes.area_code.label("area_codes_code"),
            AreaCodes.area.label("area_codes_desc"),
            ItemCodes.item_code.label("item_codes_code"),
            ItemCodes.item.label("item_codes_desc"),
            Elements.element_code.label("elements_code"),
            Elements.element.label("elements_desc"),
            Flags.flag.label("flags_code"),
            Flags.description.label("flags_desc"),
        )
        .select_from(ConsumerPriceIndices)
        .outerjoin(AreaCodes, ConsumerPriceIndices.area_code_id == AreaCodes.id)
        .outerjoin(ItemCodes, ConsumerPriceIndices.item_code_id == ItemCodes.id)
        .outerjoin(Elements, ConsumerPriceIndices.element_code_id == Elements.id)
        .outerjoin(Flags, ConsumerPriceIndices.flag_id == Flags.id)
    )
    
    # Apply filters
    if area_code:
        query = query.where(AreaCodes.area_code == area_code)
    if area:
        query = query.where(AreaCodes.area.ilike("%" + area + "%"))
    if item_code:
        query = query.where(ItemCodes.item_code == item_code)
    if item:
        query = query.where(ItemCodes.item.ilike("%" + item + "%"))
    if element_code:
        query = query.where(Elements.element_code == element_code)
    if element:
        query = query.where(Elements.element.ilike("%" + element + "%"))
    if flag:
        query = query.where(Flags.flag == flag)
    if description:
        query = query.where(Flags.description.ilike("%" + description + "%"))
   
    
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

# Metadata endpoints for understanding the dataset

@router.get("/areas")
def get_available_areas(db: Session = Depends(get_db)):
    """Get all areas with data in this dataset"""
    query = (
        select(
            AreaCodes.area_code,
            AreaCodes.area,
            func.count(ConsumerPriceIndices.id).label('record_count')
        )
        .join(ConsumerPriceIndices, AreaCodes.id == ConsumerPriceIndices.area_code_id)
        .group_by(AreaCodes.area_code, AreaCodes.area)
        .order_by(func.count(ConsumerPriceIndices.id).desc())
    )
    
    results = db.execute(query).all()
    
    return {
        "dataset": "consumer_price_indices",
        "total_areas": len(results),
        "areas": [
            {
                "area_code": r.area_code,
                "area": r.area,
                "record_count": r.record_count
            }
            for r in results
        ]
    }


@router.get("/items")
def get_available_items(db: Session = Depends(get_db)):
    """Get all items available in this dataset with record counts"""
    query = (
        select(
            ItemCodes.item_code,
            ItemCodes.item,
            func.count(ConsumerPriceIndices.id).label('record_count')
        )
        .join(ConsumerPriceIndices, ItemCodes.id == ConsumerPriceIndices.item_code_id)
        .group_by(ItemCodes.item_code, ItemCodes.item)
        .order_by(func.count(ConsumerPriceIndices.id).desc())
    )
    
    results = db.execute(query).all()
    
    return {
        "dataset": "consumer_price_indices",
        "total_items": len(results),
        "items": [
            {
                "item_code": r.item_code,
                "item": r.item,
                "record_count": r.record_count
            }
            for r in results
        ]
    }





@router.get("/elements")
def get_available_elements(db: Session = Depends(get_db)):
    """Get all elements (measures/indicators) in this dataset"""
    query = (
        select(
            Elements.element_code,
            Elements.element,
            func.count(ConsumerPriceIndices.id).label('record_count')
        )
        .join(ConsumerPriceIndices, Elements.id == ConsumerPriceIndices.element_code_id)
        .group_by(Elements.element_code, Elements.element)
        .order_by(func.count(ConsumerPriceIndices.id).desc())
    )
    
    results = db.execute(query).all()
    
    return {
        "dataset": "consumer_price_indices",
        "total_elements": len(results),
        "elements": [
            {
                "element_code": r.element_code,
                "element": r.element,
                "record_count": r.record_count
            }
            for r in results
        ]
    }




@router.get("/flags")
def get_data_quality_summary(db: Session = Depends(get_db)):
    """Get data quality flag distribution for this dataset"""
    query = (
        select(
            Flags.flag,
            Flags.description,
            func.count(ConsumerPriceIndices.id).label('record_count')
        )
        .join(ConsumerPriceIndices, Flags.id == ConsumerPriceIndices.flag_id)
        .group_by(Flags.flag, Flags.description)
        .order_by(func.count(ConsumerPriceIndices.id).desc())
    )
    
    results = db.execute(query).all()
    
    return {
        "dataset": "consumer_price_indices",
        "total_records": sum(r.record_count for r in results),
        "flag_distribution": [
            {
                "flag": r.flag,
                "description": r.description,
                "record_count": r.record_count,
                "percentage": round(r.record_count / sum(r2.record_count for r2 in results) * 100, 2)
            }
            for r in results
        ]
    }

@router.get("/years")
def get_temporal_coverage(db: Session = Depends(get_db)):
    """Get temporal coverage information for this dataset"""
    # Get year range and counts
    query = (
        select(
            ConsumerPriceIndices.year,
            func.count(ConsumerPriceIndices.id).label('record_count')
        )
        .group_by(ConsumerPriceIndices.year)
        .order_by(ConsumerPriceIndices.year)
    )
    
    results = db.execute(query).all()
    years_data = [{"year": r.year, "record_count": r.record_count} for r in results]
    
    if not years_data:
        return {"dataset": "consumer_price_indices", "message": "No temporal data available"}
    
    return {
        "dataset": "consumer_price_indices",
        "earliest_year": min(r["year"] for r in years_data),
        "latest_year": max(r["year"] for r in years_data),
        "total_years": len(years_data),
        "total_records": sum(r["record_count"] for r in years_data),
        "years": years_data
    }

@router.get("/summary")
def get_dataset_summary(db: Session = Depends(get_db)):
    """Get comprehensive summary of this dataset"""
    total_records = db.query(func.count(ConsumerPriceIndices.id)).scalar()
    
    summary = {
        "dataset": "consumer_price_indices",
        "total_records": total_records,
        "foreign_keys": [
            "area_codes",
            "item_codes",
            "elements",
            "flags",
        ]
    }
    
    # Add counts for each FK relationship
    summary["unique_areas"] = db.query(func.count(func.distinct(ConsumerPriceIndices.area_code_id))).scalar()
    summary["unique_items"] = db.query(func.count(func.distinct(ConsumerPriceIndices.item_code_id))).scalar()
    summary["unique_elements"] = db.query(func.count(func.distinct(ConsumerPriceIndices.element_code_id))).scalar()
    
    return summary
