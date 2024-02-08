import pyarrow as pa
import pyarrow.parquet as pq
from pandas import DataFrame
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './credentials/dummy_credentials.json'

bucket_name = 'mage-zoomcamp-2024-alex-korga'
project_id = 'dezoomcamp2024-412718'

table_name = 'green_taxi_data'

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(df: DataFrame, *args, **kwargs):
    table = pa.Table.from_pandas(df)
    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table, 
        root_path, 
        partition_cols=['lpep_pickup_date'], 
        filesystem=gcs
    )
