from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"))
    units = Column(Integer)
    occupied_units = Column(Integer)

    location = relationship("Location", back_populates="properties")
    tenants = relationship("Tenant", back_populates="property")
