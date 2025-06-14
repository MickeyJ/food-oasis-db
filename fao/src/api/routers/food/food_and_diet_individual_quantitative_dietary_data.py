from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, func, or_, text
from typing import Optional
from fao.src.core import settings
from fao.src.db.database import get_db
from fao.src.db.pipelines.food_and_diet_individual_quantitative_dietary_data.food_and_diet_individual_quantitative_dietary_data_model import FoodAndDietIndividualQuantitativeDietaryData
# Import core/reference tables for joins
from fao.src.db.pipelines.surveys.surveys_model import Surveys
from fao.src.db.pipelines.geographic_levels.geographic_levels_model import GeographicLevels
from fao.src.db.pipelines.population_age_groups.population_age_groups_model import PopulationAgeGroups
from fao.src.db.pipelines.food_groups.food_groups_model import FoodGroups
from fao.src.db.pipelines.indicators.indicators_model import Indicators
from fao.src.db.pipelines.elements.elements_model import Elements
from fao.src.db.pipelines.sexs.sexs_model import Sexs
from fao.src.db.pipelines.flags.flags_model import Flags

router = APIRouter(
    prefix="/food_and_diet_individual_quantitative_dietary_data",
    tags=["food_and_diet_individual_quantitative_dietary_data"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_food_and_diet_individual_quantitative_dietary_data(
    limit: int = Query(settings.default_limit, le=settings.max_limit, ge=1, description="Maximum records to return"),
    offset: int = Query(settings.default_offset, ge=0, description="Number of records to skip"),
    survey_code: Optional[str] = Query(None, description="Filter by surveys code"),
    survey: Optional[str] = Query(None, description="Filter by surveys description"),
    geographic_level_code: Optional[str] = Query(None, description="Filter by geographic_levels code"),
    geographic_level: Optional[str] = Query(None, description="Filter by geographic_levels description"),
    population_age_group_code: Optional[str] = Query(None, description="Filter by population_age_groups code"),
    population_age_group: Optional[str] = Query(None, description="Filter by population_age_groups description"),
    food_group_code: Optional[str] = Query(None, description="Filter by food_groups code"),
    food_group: Optional[str] = Query(None, description="Filter by food_groups description"),
    indicator_code: Optional[str] = Query(None, description="Filter by indicators code"),
    indicator: Optional[str] = Query(None, description="Filter by indicators description"),
    element_code: Optional[str] = Query(None, description="Filter by elements code"),
    element: Optional[str] = Query(None, description="Filter by elements description"),
    sex_code: Optional[str] = Query(None, description="Filter by sexs code"),
    sex: Optional[str] = Query(None, description="Filter by sexs description"),
    flag: Optional[str] = Query(None, description="Filter by flags code"),
    description: Optional[str] = Query(None, description="Filter by flags description"),
    db: Session = Depends(get_db)
):
    """
    food and diet individual quantitative dietary data data with filters.
    Filter options:
    - survey_code: Filter by surveys code
    - survey: Filter by surveys description (partial match)
    - geographic_level_code: Filter by geographic_levels code
    - geographic_level: Filter by geographic_levels description (partial match)
    - population_age_group_code: Filter by population_age_groups code
    - population_age_group: Filter by population_age_groups description (partial match)
    - food_group_code: Filter by food_groups code
    - food_group: Filter by food_groups description (partial match)
    - indicator_code: Filter by indicators code
    - indicator: Filter by indicators description (partial match)
    - element_code: Filter by elements code
    - element: Filter by elements description (partial match)
    - sex_code: Filter by sexs code
    - sex: Filter by sexs description (partial match)
    - flag: Filter by flags code
    - description: Filter by flags description (partial match)
    """
    
    query = (
        select(
            FoodAndDietIndividualQuantitativeDietaryData,
            Surveys.survey_code.label("surveys_code"),
            Surveys.survey.label("surveys_desc"),
            GeographicLevels.geographic_level_code.label("geographic_levels_code"),
            GeographicLevels.geographic_level.label("geographic_levels_desc"),
            PopulationAgeGroups.population_age_group_code.label("population_age_groups_code"),
            PopulationAgeGroups.population_age_group.label("population_age_groups_desc"),
            FoodGroups.food_group_code.label("food_groups_code"),
            FoodGroups.food_group.label("food_groups_desc"),
            Indicators.indicator_code.label("indicators_code"),
            Indicators.indicator.label("indicators_desc"),
            Elements.element_code.label("elements_code"),
            Elements.element.label("elements_desc"),
            Sexs.sex_code.label("sexs_code"),
            Sexs.sex.label("sexs_desc"),
            Flags.flag.label("flags_code"),
            Flags.description.label("flags_desc"),
        )
        .select_from(FoodAndDietIndividualQuantitativeDietaryData)
        .outerjoin(Surveys, FoodAndDietIndividualQuantitativeDietaryData.survey_code_id == Surveys.id)
        .outerjoin(GeographicLevels, FoodAndDietIndividualQuantitativeDietaryData.geographic_level_code_id == GeographicLevels.id)
        .outerjoin(PopulationAgeGroups, FoodAndDietIndividualQuantitativeDietaryData.population_age_group_code_id == PopulationAgeGroups.id)
        .outerjoin(FoodGroups, FoodAndDietIndividualQuantitativeDietaryData.food_group_code_id == FoodGroups.id)
        .outerjoin(Indicators, FoodAndDietIndividualQuantitativeDietaryData.indicator_code_id == Indicators.id)
        .outerjoin(Elements, FoodAndDietIndividualQuantitativeDietaryData.element_code_id == Elements.id)
        .outerjoin(Sexs, FoodAndDietIndividualQuantitativeDietaryData.sex_code_id == Sexs.id)
        .outerjoin(Flags, FoodAndDietIndividualQuantitativeDietaryData.flag_id == Flags.id)
    )
    
    # Apply filters
    if survey_code:
        query = query.where(Surveys.survey_code == survey_code)
    if survey:
        query = query.where(Surveys.survey.ilike("%" + survey + "%"))
    if geographic_level_code:
        query = query.where(GeographicLevels.geographic_level_code == geographic_level_code)
    if geographic_level:
        query = query.where(GeographicLevels.geographic_level.ilike("%" + geographic_level + "%"))
    if population_age_group_code:
        query = query.where(PopulationAgeGroups.population_age_group_code == population_age_group_code)
    if population_age_group:
        query = query.where(PopulationAgeGroups.population_age_group.ilike("%" + population_age_group + "%"))
    if food_group_code:
        query = query.where(FoodGroups.food_group_code == food_group_code)
    if food_group:
        query = query.where(FoodGroups.food_group.ilike("%" + food_group + "%"))
    if indicator_code:
        query = query.where(Indicators.indicator_code == indicator_code)
    if indicator:
        query = query.where(Indicators.indicator.ilike("%" + indicator + "%"))
    if element_code:
        query = query.where(Elements.element_code == element_code)
    if element:
        query = query.where(Elements.element.ilike("%" + element + "%"))
    if sex_code:
        query = query.where(Sexs.sex_code == sex_code)
    if sex:
        query = query.where(Sexs.sex.ilike("%" + sex + "%"))
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

















@router.get("/elements")
def get_available_elements(db: Session = Depends(get_db)):
    """Get all elements (measures/indicators) in this dataset"""
    query = (
        select(
            Elements.element_code,
            Elements.element,
            func.count(FoodAndDietIndividualQuantitativeDietaryData.id).label('record_count')
        )
        .join(FoodAndDietIndividualQuantitativeDietaryData, Elements.id == FoodAndDietIndividualQuantitativeDietaryData.element_code_id)
        .group_by(Elements.element_code, Elements.element)
        .order_by(func.count(FoodAndDietIndividualQuantitativeDietaryData.id).desc())
    )
    
    results = db.execute(query).all()
    
    return {
        "dataset": "food_and_diet_individual_quantitative_dietary_data",
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
            func.count(FoodAndDietIndividualQuantitativeDietaryData.id).label('record_count')
        )
        .join(FoodAndDietIndividualQuantitativeDietaryData, Flags.id == FoodAndDietIndividualQuantitativeDietaryData.flag_id)
        .group_by(Flags.flag, Flags.description)
        .order_by(func.count(FoodAndDietIndividualQuantitativeDietaryData.id).desc())
    )
    
    results = db.execute(query).all()
    
    return {
        "dataset": "food_and_diet_individual_quantitative_dietary_data",
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
            FoodAndDietIndividualQuantitativeDietaryData.year,
            func.count(FoodAndDietIndividualQuantitativeDietaryData.id).label('record_count')
        )
        .group_by(FoodAndDietIndividualQuantitativeDietaryData.year)
        .order_by(FoodAndDietIndividualQuantitativeDietaryData.year)
    )
    
    results = db.execute(query).all()
    years_data = [{"year": r.year, "record_count": r.record_count} for r in results]
    
    if not years_data:
        return {"dataset": "food_and_diet_individual_quantitative_dietary_data", "message": "No temporal data available"}
    
    return {
        "dataset": "food_and_diet_individual_quantitative_dietary_data",
        "earliest_year": min(r["year"] for r in years_data),
        "latest_year": max(r["year"] for r in years_data),
        "total_years": len(years_data),
        "total_records": sum(r["record_count"] for r in years_data),
        "years": years_data
    }

@router.get("/summary")
def get_dataset_summary(db: Session = Depends(get_db)):
    """Get comprehensive summary of this dataset"""
    total_records = db.query(func.count(FoodAndDietIndividualQuantitativeDietaryData.id)).scalar()
    
    summary = {
        "dataset": "food_and_diet_individual_quantitative_dietary_data",
        "total_records": total_records,
        "foreign_keys": [
            "surveys",
            "geographic_levels",
            "population_age_groups",
            "food_groups",
            "indicators",
            "elements",
            "sexs",
            "flags",
        ]
    }
    
    # Add counts for each FK relationship
    summary["unique_elements"] = db.query(func.count(func.distinct(FoodAndDietIndividualQuantitativeDietaryData.element_code_id))).scalar()
    
    return summary
