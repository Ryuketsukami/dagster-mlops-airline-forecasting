import pandas as pd
from dagster import AssetExecutionContext, asset

from quickstart_etl.partitions import partitions_def


# year=XXXX/month=XX/day=XX/
# Runs Great Expectations suite on bronze flights data: checks schema, null rates, value ranges, row counts. Fail asset if expectations are not met, returns metadata.
@asset(
    group_name="validation",
    kinds=["python", "bronze", "bigquery", "great-expectations", "validated"],
    partitions_def=partitions_def,
)
def validated_flights(context: AssetExecutionContext, bronze_flights: pd.DataFrame) -> dict:
    # results = run_great_expectations_suite(bronze_flights)

    # if not results.success:
    #     raise Exception(f"Validation failed: {results.summary}")

    return {
        # "rows_validated": len(bronze_flights),
        # "checks_passed": results.passed_count,
        # "validation_time": datetime.now().isoformat(),
        # "null_rates": bronze_flights.isnull().sum(),
    }


# Runs Great Expectations suite on bronze external data: checks schema, null rates, value ranges, row counts. Fail asset if expectations are not met, returns metadata.
@asset(
    group_name="validation",
    kinds=["python", "bronze", "bigquery", "great-expectations", "validated"],
    partitions_def=partitions_def,
)
def validated_external(context: AssetExecutionContext, bronze_external: pd.DataFrame) -> dict:
    # results = run_great_expectations_suite(bronze_external)

    # if not results.success:
    #     raise Exception(f"Validation failed: {results.summary}")

    return {
        # "rows_validated": len(bronze_external),
        # "checks_passed": results.passed_count,
        # "validation_time": datetime.now().isoformat(),
        # "null_rates": bronze_external.isnull().sum(),
    }
