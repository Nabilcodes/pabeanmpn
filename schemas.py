from pydantic import BaseModel, Field

class PaymentInfo(BaseModel):
    transaction_id: str = Field(..., example="txn12345")
    amount: float = Field(..., example=1000.50)
    bank_code: str = Field(..., example="BANK123")
    account_number: str = Field(..., example="123456789")
    payment_date: str = Field(..., example="2024-06-02")
