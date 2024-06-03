from pydantic import BaseModel
import uuid

class PaymentBase(BaseModel):
    payment_name: str
    payment_email: str
    ntpn : str
    value: int

class BillingCreate(PaymentBase):
    pass

class Billing(PaymentBase):
    id: uuid
    status: str

    class Config:
        from_attributes = True
        arbitrary_types_allowed=True
