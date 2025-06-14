"""year code string(8)

Revision ID: 1fb8d8ecd03e
Revises: feabfc639277
Create Date: 2025-06-09 11:03:58.287427

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1fb8d8ecd03e'
down_revision: Union[str, None] = 'feabfc639277'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pipeline_progress')
    op.alter_column('aquastat', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('asti_expenditures', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('asti_researchers', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('climate_change_emissions_indicators', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('commodity_balances_non_food', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('commodity_balances_non_food_2010', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('commodity_balances_non_food_2013_old_methodology', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('consumer_price_indices', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('cost_affordability_healthy_diet_co_ahd', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('deflators', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('development_assistance_to_agriculture', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('emissions_agriculture_energy', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('emissions_crops', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('emissions_drained_organic_soils', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('emissions_land_use_fires', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('emissions_land_use_forests', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('emissions_livestock', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('emissions_pre_post_production', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('emissions_totals', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('employment_indicators_agriculture', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('employment_indicators_rural', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('environment_bioenergy', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('environment_cropland_nutrient_budget', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('environment_emissions_by_sector', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('environment_emissions_intensities', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('environment_food_waste_disposal', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('environment_land_cover', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('environment_land_use', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('environment_livestock_manure', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('environment_livestock_patterns', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('environment_pesticides', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('environment_soil_nutrient_budget', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('environment_temperature_change', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('exchange_rate', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('fertilizers_detailed_trade_matrix', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('food_aid_shipments_wfp', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('food_balance_sheets', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('food_balance_sheets_historic', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('food_security_data', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('forestry', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('forestry_pulp_paper_survey', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('forestry_trade_flows', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('inputs_fertilizers_archive', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('inputs_fertilizers_nutrient', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('inputs_fertilizers_product', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('inputs_land_use', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('inputs_pesticides_trade', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('inputs_pesticides_use', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('investment_capital_stock', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('investment_country_investment_statistics_profile', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('investment_credit_agriculture', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('investment_foreign_direct_investment', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('investment_government_expenditure', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('investment_machinery', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('investment_machinery_archive', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('macro_statistics_key_indicators', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('population', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('prices', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('prices_archive', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('production_crops_livestock', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('production_indices', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('sdg_bulk_downloads', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('sua_crops_livestock', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    op.alter_column('supply_utilization_accounts_food_and_diet', 'year_code',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=8),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('supply_utilization_accounts_food_and_diet', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('sua_crops_livestock', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('sdg_bulk_downloads', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('production_indices', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('production_crops_livestock', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('prices_archive', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('prices', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('population', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('macro_statistics_key_indicators', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('investment_machinery_archive', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('investment_machinery', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('investment_government_expenditure', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('investment_foreign_direct_investment', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('investment_credit_agriculture', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('investment_country_investment_statistics_profile', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('investment_capital_stock', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('inputs_pesticides_use', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('inputs_pesticides_trade', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('inputs_land_use', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('inputs_fertilizers_product', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('inputs_fertilizers_nutrient', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('inputs_fertilizers_archive', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('forestry_trade_flows', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('forestry_pulp_paper_survey', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('forestry', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('food_security_data', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('food_balance_sheets_historic', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('food_balance_sheets', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('food_aid_shipments_wfp', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('fertilizers_detailed_trade_matrix', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('exchange_rate', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('environment_temperature_change', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('environment_soil_nutrient_budget', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('environment_pesticides', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('environment_livestock_patterns', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('environment_livestock_manure', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('environment_land_use', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('environment_land_cover', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('environment_food_waste_disposal', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('environment_emissions_intensities', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('environment_emissions_by_sector', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('environment_cropland_nutrient_budget', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('environment_bioenergy', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('employment_indicators_rural', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('employment_indicators_agriculture', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('emissions_totals', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('emissions_pre_post_production', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('emissions_livestock', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('emissions_land_use_forests', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('emissions_land_use_fires', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('emissions_drained_organic_soils', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('emissions_crops', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('emissions_agriculture_energy', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('development_assistance_to_agriculture', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('deflators', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('cost_affordability_healthy_diet_co_ahd', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('consumer_price_indices', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('commodity_balances_non_food_2013_old_methodology', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('commodity_balances_non_food_2010', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('commodity_balances_non_food', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('climate_change_emissions_indicators', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('asti_researchers', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('asti_expenditures', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.alter_column('aquastat', 'year_code',
               existing_type=sa.String(length=8),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)
    op.create_table('pipeline_progress',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('table_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('last_row_processed', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('total_rows', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('last_chunk_time', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=20), server_default=sa.text("'in_progress'::character varying"), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pipeline_progress_pkey')),
    sa.UniqueConstraint('table_name', name=op.f('pipeline_progress_table_name_key'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    # ### end Alembic commands ###
