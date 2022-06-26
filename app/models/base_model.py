from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, DateTime
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import json
Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    def set_attributes(self, values):
        if not isinstance(values, dict):
            values = json.loads(values.json())
        for key, value in values.items():
            if (hasattr(self, key) and ((isinstance(value, str) and value)
                                        or (isinstance(value, (bool, int, float, list))))):
                setattr(self, key, value)

class AuditMixin(Base):
    __abstract__ = True

    created_on = Column(DateTime(timezone=True), default=datetime.now)
    modified_on = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)


class CreatedMixin(Base):
    __abstract__ = True

    created_by = Column(String(256), nullable=False)
    created_on = Column(DateTime(timezone=True), nullable=False, default=datetime.now)


class ModifiedMixin(Base):
    __abstract__ = True

    modified_by = Column(String(256), nullable=False)
    modified_on = Column(DateTime(timezone=True), nullable=False, default=datetime.now, onupdate=datetime.now)
