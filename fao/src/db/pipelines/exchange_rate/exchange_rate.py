import pandas as pd
from fao.src.db.utils import get_csv_path_for
from fao.src.db.database import run_with_session
from fao.src.db.pipelines.base import BaseDatasetETL
from .exchange_rate_model import ExchangeRate


class ExchangeRateETL(BaseDatasetETL):
    """ETL pipeline for exchange_rate dataset"""
    
    def __init__(self):
        super().__init__(
            csv_path=get_csv_path_for("Exchange_rate_E_All_Data_(Normalized)/Exchange_rate_E_All_Data_(Normalized).csv"),
            model_class=ExchangeRate,
            table_name="exchange_rate",
            exclude_columns=["Area", "Area Code", "Area Code (M49)", "Currency", "Element", "Element Code", "Flag", "ISO Currency Code"],
            foreign_keys=[{"csv_column_name": "Area Code", "format_methods": [], "hash_columns": ["Area Code", "source_dataset"], "hash_fk_csv_column_name": "Area Code_id", "hash_fk_sql_column_name": "area_code_id", "hash_pk_sql_column_name": "id", "index_hash": "b408a449_area_codes", "model_name": "AreaCodes", "pipeline_name": "area_codes", "reference_additional_columns": ["area_code_m49"], "reference_column_count": 4, "reference_description_column": "area", "reference_pk_csv_column": "Area Code", "sql_column_name": "area_code", "table_name": "area_codes"}, {"csv_column_name": "Element Code", "format_methods": [], "hash_columns": ["Element Code", "source_dataset"], "hash_fk_csv_column_name": "Element Code_id", "hash_fk_sql_column_name": "element_code_id", "hash_pk_sql_column_name": "id", "index_hash": "a8b36093_elements", "model_name": "Elements", "pipeline_name": "elements", "reference_additional_columns": [], "reference_column_count": 3, "reference_description_column": "element", "reference_pk_csv_column": "Element Code", "sql_column_name": "element_code", "table_name": "elements"}, {"csv_column_name": "ISO Currency Code", "format_methods": [], "hash_columns": ["ISO Currency Code", "source_dataset"], "hash_fk_csv_column_name": "ISO Currency Code_id", "hash_fk_sql_column_name": "iso_currency_code_id", "hash_pk_sql_column_name": "id", "index_hash": "72bfc3cb_currencies", "model_name": "Currencies", "pipeline_name": "currencies", "reference_additional_columns": [], "reference_column_count": 3, "reference_description_column": "currency", "reference_pk_csv_column": "ISO Currency Code", "sql_column_name": "iso_currency_code", "table_name": "currencies"}, {"csv_column_name": "Flag", "format_methods": ["upper"], "hash_columns": ["Flag"], "hash_fk_csv_column_name": "Flag_id", "hash_fk_sql_column_name": "flag_id", "hash_pk_sql_column_name": "id", "index_hash": "efc1dbdd_flags", "model_name": "Flags", "pipeline_name": "flags", "reference_additional_columns": [], "reference_column_count": 3, "reference_description_column": "description", "reference_pk_csv_column": "Flag", "sql_column_name": "flag", "table_name": "flags"}]
        )
    
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Dataset-specific cleaning"""
        # Common cleaning first
        df = self.base_clean(df)
        
        # Column-specific cleaning
        # Year Code
        df['Year Code'] = df['Year Code'].astype(str).str.strip().str.replace("'", "")
        # Year
        df['Year'] = df['Year'].astype(str).str.strip().str.replace("'", "")
        # Months Code
        df['Months Code'] = df['Months Code'].astype(str).str.strip().str.replace("'", "")
        # Months
        df['Months'] = df['Months'].astype(str).str.strip().str.replace("'", "")
        # Unit
        df['Unit'] = df['Unit'].astype(str).str.strip().str.replace("'", "")
        # Value
        df['Value'] = df['Value'].astype(str).str.strip().str.replace("'", "")
        df['Value'] = df['Value'].replace({'<0.1': 0.05, 'nan': None})
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
        
        return df
    
    def build_record(self, row: pd.Series) -> dict:
        """Build record for insertion"""
        record = {}
        # Foreign key columns
        record['area_code_id'] = row['area_code_id']
        record['element_code_id'] = row['element_code_id']
        record['iso_currency_code_id'] = row['iso_currency_code_id']
        record['flag_id'] = row['flag_id']
        # Data columns
        record['year_code'] = row['Year Code']
        record['year'] = row['Year']
        record['months_code'] = row['Months Code']
        record['months'] = row['Months']
        record['unit'] = row['Unit']
        record['value'] = row['Value']
        return record


# Module-level functions for backwards compatibility
etl = ExchangeRateETL()
load = etl.load
clean = etl.clean
insert = etl.insert
run = etl.run

if __name__ == "__main__":
    run_with_session(run)