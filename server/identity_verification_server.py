#!/usr/bin/env python3

import time
import uuid
from datetime import datetime
import grpc
from concurrent import futures

# Import the generated stubs
# Note: These imports will work after generating the stubs using the generate_stubs.sh script
import sys
sys.path.append('./generated')

import identity_verification_pb2 as iv_pb2
import identity_verification_pb2_grpc as iv_pb2_grpc

class IdentityVerificationServicer(iv_pb2_grpc.IdentityVerificationServiceServicer):
    """Implementation of the Identity Verification Service."""

    def VerifyIdentity(self, request, context):
        """
        Verify an identity based on application details.
        Business logic:
        - If first_name is 'John', application is marked as VERIFIED
        - If first_name is 'Paul', application is marked as MANUAL_REVIEW
        - Otherwise, application is REJECTED
        """
        print(f"Processing verification request for application ID: {request.application_id}")
        print(f"Applicant name: {request.applicant.first_name} {request.applicant.last_name}")
        
        # Create a response
        response = iv_pb2.VerificationResponse()
        response.application_id = request.application_id
        response.verification_id = str(uuid.uuid4())
        response.timestamp = datetime.now().isoformat()
        
        # Apply the business rules based on first name
        first_name = request.applicant.first_name
        
        if first_name == "John":
            response.status = iv_pb2.VerificationResponse.VerificationStatus.VERIFIED
            response.message = "Identity verified successfully"
            response.confidence_score = 0.95
        elif first_name == "Paul":
            response.status = iv_pb2.VerificationResponse.VerificationStatus.MANUAL_REVIEW
            response.message = "Application requires manual review"
            response.confidence_score = 0.50
        else:
            response.status = iv_pb2.VerificationResponse.VerificationStatus.REJECTED
            response.message = "Identity verification failed"
            response.confidence_score = 0.25
            
        print(f"Verification result: {response.status}, Message: {response.message}")
        return response
    
    def StreamVerifications(self, request_iterator, context):
        """Handle streaming verification requests."""
        for request in request_iterator:
            yield self.VerifyIdentity(request, context)


def serve():
    """Start the gRPC server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    iv_pb2_grpc.add_IdentityVerificationServiceServicer_to_server(
        IdentityVerificationServicer(), server)
    
    # Listen on port 50051
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Identity Verification Service started on port 50051...")
    
    try:
        # Keep the server running until interrupted
        while True:
            time.sleep(86400)  # One day in seconds
    except KeyboardInterrupt:
        server.stop(0)
        print("Server stopped.")


if __name__ == '__main__':
    serve()
