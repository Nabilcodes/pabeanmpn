from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from .database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    payment_name = Column(String, index=True)
    payment_email = Column(String, index=True)
    ntpn = Column(String, index=True)
    value = Column(Integer, index=True)
    status = Column(String, index=True)