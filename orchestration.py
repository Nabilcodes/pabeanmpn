import uuid
from typing import Dict

class OrchestrationService:
    def __init__(self, djbc_service_client):
        self.djbc_service_client = djbc_service_client

    def generate_ntpn(self) -> str:
        # Generate a unique NTPN code
        return str(uuid.uuid4())

    def process_payment(self, payment_info: Dict) -> str:
        # Validate payment info (this can be more complex)
        if not payment_info.get("transaction_id") or not payment_info.get("amount"):
            raise ValueError("Invalid payment info")
        
        # Generate NTPN
        ntpn_code = self.generate_ntpn()
        ntpn_data = {
            "transaction_id": payment_info["transaction_id"],
            "ntpn": ntpn_code,
            "amount": payment_info["amount"],
            "bank_code": payment_info["bank_code"],
            "account_number": payment_info["account_number"],
            "payment_date": payment_info["payment_date"]
        }

        # Send NTPN data to DJBC service
        response = self.djbc_service_client.send_ntpn(ntpn_data)
        return response
