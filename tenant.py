from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone_number = Column(String)
    email_address = Column(String)
    house_number = Column(String)
    date_of_rent_payment = Column(String)
    amount_of_rent_to_be_paid = Column(Integer)
    property_id = Column(Integer, ForeignKey("properties.id"))

    property = relationship("Property", back_populates="tenants")
