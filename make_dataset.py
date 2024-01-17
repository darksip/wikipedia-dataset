import os
import pyarrow.parquet as pq
import pyarrow as pa
from tqdm import tqdm
import datasets

# Paths
source_dir = 'data/20240101/fr'
destination_dir = 'datasets/20240101/fr'

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Function to write sharded parquet files
def write_sharded_parquet(table, dir_path, shard_size_mb=50):
    # Convert MB to bytes for shard size
    shard_size_bytes = shard_size_mb * 1024 * 1024

    # Iterate over the table and write shards
    for i in range(0, table.num_rows, shard_size_bytes):
        shard = table.slice(i, shard_size_bytes)
        shard_file_path = os.path.join(dir_path, f'shard_{i}.parquet')
        pq.write_table(shard, shard_file_path)

# Reading all the parquet files and concatenating them into a single Arrow Table
file_paths = [f for f in os.listdir(source_dir) if f.endswith('.parquet')]
tables = []
total_bytes_loaded = 0

# tqdm for progress tracking
with tqdm(total=sum(os.path.getsize(os.path.join(source_dir, f)) for f in file_paths), 
          unit='B', unit_scale=True, desc="Loading Bytes") as pbar:
    for file in file_paths:
        file_path = os.path.join(source_dir, file)
        table = pq.read_table(file_path)
        tables.append(table)
        file_size = os.path.getsize(file_path)
        total_bytes_loaded += file_size
        pbar.update(file_size)

full_table = pa.concat_tables(tables)
# print size of the table
print(f"Table size: {full_table.num_rows} rows, {full_table.num_columns} columns")
# Write the full table into sharded

# convert to dataset
print("Converting to dataset")
dataset = datasets.Dataset.from_arrow_table(full_table)

# tqdm for progress tracking
with tqdm(total=full_table.num_rows, unit='rows', desc="Writing Rows") as pbar:
    write_sharded_parquet(full_table, destination_dir)
    pbar.update(full_table.num_rows)

# test to load dataset from the sharded parquet files
dataset = datasets.load_from_disk(destination_dir)
print(dataset.num_rows)