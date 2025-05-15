#!/usr/bin/env python3

import grpc
import uuid
import sys
sys.path.append('./generated')

import identity_verification_pb2 as iv_pb2
import identity_verification_pb2_grpc as iv_pb2_grpc


def run_verification(first_name, last_name):
    """
    Run a verification request with the given name.
    
    Args:
        first_name: First name of the applicant
        last_name: Last name of the applicant
    """
    # Create a gRPC channel
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a stub (client)
        stub = iv_pb2_grpc.IdentityVerificationServiceStub(channel)
        
        # Create a verification request
        request = iv_pb2.VerificationRequest()
        request.application_id = str(uuid.uuid4())
        
        # Set applicant details
        request.applicant.first_name = first_name
        request.applicant.last_name = last_name
        request.applicant.date_of_birth = "1990-01-01"
        
        # Set address
        request.applicant.address.street = "123 Main St"
        request.applicant.address.city = "Anytown"
        request.applicant.address.state = "CA"
        request.applicant.address.postal_code = "12345"
        request.applicant.address.country = "US"
        
        # Set document details
        request.document.type = iv_pb2.Document.DocumentType.DRIVERS_LICENSE
        request.document.document_number = "DL123456"
        request.document.issuing_country = "US"
        request.document.expiry_date = "2030-01-01"
        
        # Call the service
        print(f"\nSending verification request for {first_name} {last_name}...")
        response = stub.VerifyIdentity(request)
        
        # Process the response
        status_name = iv_pb2.VerificationResponse.VerificationStatus.Name(response.status)
        print(f"Response received:")
        print(f"  Application ID: {response.application_id}")
        print(f"  Verification ID: {response.verification_id}")
        print(f"  Status: {status_name}")
        print(f"  Message: {response.message}")
        print(f"  Confidence Score: {response.confidence_score}")
        print(f"  Timestamp: {response.timestamp}")


def run():
    """Run the client with different test cases."""
    # Test case 1: John (should be VERIFIED)
    run_verification("John", "Doe")
    
    # Test case 2: Paul (should be MANUAL_REVIEW)
    run_verification("Paul", "Smith")
    
    # Test case 3: Alice (should be REJECTED)
    run_verification("Alice", "Johnson")


if __name__ == '__main__':
    run()
