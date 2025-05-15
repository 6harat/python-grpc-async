#!/bin/bash

# This script generates both synchronous and asynchronous Python stubs from Proto files

# Directory where proto files are located
PROTO_DIR="./proto"

# Directory where generated files will be placed
OUTPUT_DIR="./generated"

# Create the output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Generate synchronous stubs
python -m grpc_tools.protoc \
    --proto_path=$PROTO_DIR \
    --python_out=$OUTPUT_DIR \
    --grpc_python_out=$OUTPUT_DIR \
    $PROTO_DIR/*.proto

# Generate asynchronous stubs
# python -m grpc_tools.protoc \
#     --proto_path=$PROTO_DIR \
#     --python_out=$OUTPUT_DIR \
#     --grpc_python_out=$OUTPUT_DIR \
#     --grpc_python_opt=grpc_aio \
#     $PROTO_DIR/*.proto

# echo "Both synchronous and asynchronous stubs have been generated in $OUTPUT_DIR"
