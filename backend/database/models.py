from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    phone = Column(String(30))
    email = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)

    employees = relationship("Employee", back_populates="business")


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    business_id = Column(Integer, ForeignKey("businesses.id"))

    name = Column(String(100))
    role = Column(String(50))
    system_prompt = Column(Text)

    business = relationship("Business", back_populates="employees")


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True)

    employee_id = Column(Integer, ForeignKey("employees.id"))

    customer_name = Column(String(100))

    created_at = Column(DateTime, default=datetime.utcnow)


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)

    conversation_id = Column(Integer, ForeignKey("conversations.id"))

    sender = Column(String(20))

    message = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
