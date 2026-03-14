# Here is where we define our assets. Assets are the core unit of computation in Dagster, and represent a piece of data or a computation that we want to track and manage.
# Each asset is defined as a Python function, and can have dependencies on other assets. When an asset is materialized, it will automatically materialize all of its dependencies first.
# An asset can be a database table, a machine learning model, a data file, or any other piece of data that we want to track.
# Assets can also have metadata associated with them, which can be used for documentation, monitoring, and debugging purposes.
# It's where our business logic lives, and it's where we define the transformations that we want to apply to our data.
# We can test it runs locally by typing our "dg launch --assets quickstart_etl" in our terminal, and we can also see the results of our asset materialization in the Dagster UI.

# If we need to partition our assets (e.g. by date), we can use the `@asset(partitions_def=...)` decorator to define a partitioned asset.
# This allows us to materialize our assets for specific partitions, and to track the lineage of our data across partitions.

# Once we have our assets we want to input a data quality layer, leveraging asset checks, that run any time an asset is materialized, so we know the data is correct and in the right format before downstream assets run.
# We can also set up sensors to automatically materialize our assets on a schedule, or in response to certain events (e.g. when new data is available).

# Recommendation, add metadata to assets, to help organize data platform