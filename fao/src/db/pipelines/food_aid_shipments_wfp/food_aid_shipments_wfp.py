import pandas as pd
from fao.src.db.utils import get_csv_path_for
from fao.src.db.database import run_with_session
from fao.src.db.pipelines.base import BaseDatasetETL
from .food_aid_shipments_wfp_model import FoodAidShipmentsWfp


class FoodAidShipmentsWfpETL(BaseDatasetETL):
    """ETL pipeline for food_aid_shipments_wfp dataset"""
    
    def __init__(self):
        super().__init__(
            csv_path=get_csv_path_for("Food_Aid_Shipments_WFP_E_All_Data_(Normalized)/Food_Aid_Shipments_WFP_E_All_Data_(Normalized).csv"),
            model_class=FoodAidShipmentsWfp,
            table_name="food_aid_shipments_wfp",
            exclude_columns=["Element", "Element Code", "Flag", "Item", "Item Code"],
            foreign_keys=[{"csv_column_name": "Item Code", "format_methods": [], "hash_columns": ["Item Code", "source_dataset"], "hash_fk_csv_column_name": "Item Code_id", "hash_fk_sql_column_name": "item_code_id", "hash_pk_sql_column_name": "id", "index_hash": "1a8f2e45_item_codes", "model_name": "ItemCodes", "pipeline_name": "item_codes", "reference_additional_columns": ["item_code_cpc", "item_code_fbs", "item_code_sdg"], "reference_column_count": 6, "reference_description_column": "item", "reference_pk_csv_column": "Item Code", "sql_column_name": "item_code", "table_name": "item_codes"}, {"csv_column_name": "Element Code", "format_methods": [], "hash_columns": ["Element Code", "source_dataset"], "hash_fk_csv_column_name": "Element Code_id", "hash_fk_sql_column_name": "element_code_id", "hash_pk_sql_column_name": "id", "index_hash": "2e50dc94_elements", "model_name": "Elements", "pipeline_name": "elements", "reference_additional_columns": [], "reference_column_count": 3, "reference_description_column": "element", "reference_pk_csv_column": "Element Code", "sql_column_name": "element_code", "table_name": "elements"}, {"csv_column_name": "Flag", "format_methods": ["upper"], "hash_columns": ["Flag"], "hash_fk_csv_column_name": "Flag_id", "hash_fk_sql_column_name": "flag_id", "hash_pk_sql_column_name": "id", "index_hash": "7143c7b3_flags", "model_name": "Flags", "pipeline_name": "flags", "reference_additional_columns": [], "reference_column_count": 3, "reference_description_column": "description", "reference_pk_csv_column": "Flag", "sql_column_name": "flag", "table_name": "flags"}]
        )
    
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Dataset-specific cleaning"""
        # Common cleaning first
        df = self.base_clean(df)
        
        # Column-specific cleaning
        # Recipient Country Code
        df['Recipient Country Code'] = df['Recipient Country Code'].astype(str).str.strip().str.replace("'", "")
        # Recipient Country Code (M49)
        df['Recipient Country Code (M49)'] = df['Recipient Country Code (M49)'].astype(str).str.strip().str.replace("'", "")
        # Recipient Country
        df['Recipient Country'] = df['Recipient Country'].astype(str).str.strip().str.replace("'", "")
        # Year Code
        df['Year Code'] = df['Year Code'].astype(str).str.strip().str.replace("'", "")
        # Year
        df['Year'] = df['Year'].astype(str).str.strip().str.replace("'", "")
        # Unit
        df['Unit'] = df['Unit'].astype(str).str.strip().str.replace("'", "")
        # Value
        df['Value'] = df['Value'].astype(str).str.strip().str.replace("'", "")
        df['Value'] = df['Value'].replace({'<0.1': 0.05, 'nan': None})
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
        # Note
        df['Note'] = df['Note'].astype(str).str.strip().str.replace("'", "")
        
        return df
    
    def build_record(self, row: pd.Series) -> dict:
        """Build record for insertion"""
        record = {}
        # Foreign key columns
        record['item_code_id'] = row['item_code_id']
        record['element_code_id'] = row['element_code_id']
        record['flag_id'] = row['flag_id']
        # Data columns
        record['recipient_country_code'] = row['Recipient Country Code']
        record['recipient_country_code_m49'] = row['Recipient Country Code (M49)']
        record['recipient_country'] = row['Recipient Country']
        record['year_code'] = row['Year Code']
        record['year'] = row['Year']
        record['unit'] = row['Unit']
        record['value'] = row['Value']
        record['note'] = row['Note']
        return record


# Module-level functions for backwards compatibility
etl = FoodAidShipmentsWfpETL()
load = etl.load
clean = etl.clean
insert = etl.insert
run = etl.run

if __name__ == "__main__":
    run_with_session(run)