# Identity Verification gRPC Service

This project implements a simple Identity Verification service using gRPC and Protocol Buffers.

## Project Structure

```
.
├── proto/
│   └── identity_verification.proto    # Protocol Buffers definition
├── generated/                         # Generated Python code (after running generate_stubs.sh)
├── server/
│   └── identity_verification_server.py # Server implementation
├── client/
│   └── identity_verification_client.py # Client for testing
├── generate_stubs.sh                  # Script to generate Python code from .proto
└── requirements.txt                   # Python dependencies
```

## Protocol Buffers Contract

The service defines the following:

- `IdentityVerificationService`: A service with methods for verifying identity
  - `VerifyIdentity`: Single request/response method
  - `StreamVerifications`: Bidirectional streaming method

- Message types:
  - `VerificationRequest`: Contains applicant information
  - `VerificationResponse`: Contains verification result
  - `Applicant`: Contains personal details
  - `Address`: Contains address information
  - `Document`: Contains identity document details

## Verification Rules

The service implements the following dummy rules:

- If first name is "John": Application is VERIFIED
- If first name is "Paul": Application is sent for MANUAL_REVIEW
- For all other names: Application is REJECTED

## Setup and Installation

### Automated Installation

For an automated setup, you can use one of the following scripts:

#### Bash Script (Linux/macOS)
```bash
chmod +x install.sh
./install.sh
```

#### Python Script (Cross-platform)
```bash
python install.py
```

These scripts will help you create a virtual environment (optional), install dependencies, generate stubs, and set up permissions.

### Manual Installation

If you prefer to install manually or if you encounter issues:

1. **Set up a virtual environment (recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install prerequisites**:
   ```bash
   pip install --upgrade pip wheel setuptools
   ```

3. **Install dependencies**:
   
   If you encounter the `Failed to build installable wheels` error, try these approaches:
   
   **Method 1**: Install with no build isolation
   ```bash
   pip install --no-build-isolation grpcio grpcio-tools protobuf
   ```
   
   **Method 2**: Install system dependencies first
   - Ubuntu/Debian: `sudo apt-get install python3-dev build-essential`
   - macOS: `xcode-select --install`
   - Windows: Install Visual C++ Build Tools
   
   **Method 3**: For macOS, try:
   ```bash
   GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1 pip install grpcio grpcio-tools
   ```
   
   **Method 4**: Try using pre-compiled binaries
   ```bash
   pip install --only-binary=:all: grpcio grpcio-tools
   ```

4. **Generate Python stubs**:
   
   Using Bash script (Linux/macOS):
   ```bash
   chmod +x generate_stubs.sh
   ./generate_stubs.sh
   ```
   
   Using Python script (Cross-platform):
   ```bash
   python generate_stubs.py
   ```

5. **Set up permissions**:
   ```bash
   chmod +x server/identity_verification_server.py
   chmod +x client/identity_verification_client.py
   ```

6. **Run the demo** (starts both server and client in one command):
   ```bash
   python demo.py
   ```

   Or run server and client separately:

   **Run the server**:
   ```bash
   python server/identity_verification_server.py
   ```

   **In a separate terminal, run the client**:
   ```bash
   python client/identity_verification_client.py
   ```

## Generated Code

After running `generate_stubs.sh`, the following files will be created in the `generated` directory:

- `identity_verification_pb2.py`: Contains message classes
- `identity_verification_pb2_grpc.py`: Contains synchronous client and server classes
- Files with asynchronous stubs (when using the `grpc_aio` option)

## Command to Generate Protobuf Stubs

The following command generates both synchronous and asynchronous stubs:

```bash
# Synchronous stubs
python -m grpc_tools.protoc \
    --proto_path=./proto \
    --python_out=./generated \
    --grpc_python_out=./generated \
    ./proto/*.proto

# Asynchronous stubs
python -m grpc_tools.protoc \
    --proto_path=./proto \
    --python_out=./generated \
    --grpc_python_out=./generated \
    --grpc_python_opt=grpc_aio \
    ./proto/*.proto
```
# python-grpc-async
