from sqlalchemy import ForeignKey, JSON, Column, String, Integer
from sqlalchemy.orm import relationship
from .database import Base


class UserEnvironment(Base):
    __tablename__ = "ncr_user_environments"

    user_id         = Column(ForeignKey("ncr_users.id"), primary_key=True)
    environment_id  = Column(ForeignKey("ncr_environments.id"), primary_key=True)
    document        = Column(JSON, nullable=True)

    environment = relationship("Environment", back_populates="environment_users")
    user        = relationship("User", back_populates="user_environments")

# UCVM
class UserContainerVM(Base):
    __tablename__ = "ncr_user_container_vms"

    id = Column(Integer, primary_key=True, index=True)
    
    user_id       = Column(ForeignKey("ncr_users.id"), nullable=True)
    container_id  = Column(ForeignKey("ncr_containers.id"), nullable=True)
    vm_id         = Column(ForeignKey("ncr_vms.id"), nullable=True)

    document = Column(JSON, nullable=True)

    user      = relationship("User")
    container = relationship("Container")
    vm        = relationship("VM")


class User(Base):
    __tablename__ = "ncr_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)

    #Environments
    environments = relationship(
        "Environment",
        secondary="ncr_user_environments", 
        back_populates="users",
        overlaps='user,environment',
    )
    user_environments = relationship(
        "UserEnvironment",
        back_populates="user",
        overlaps="environments"
    )

    ucvms = relationship(
        "UserContainerVM",
        back_populates="user"
    )

class Environment(Base):
    __tablename__ = "ncr_environments"
    id = Column(String, primary_key=True, index=True)
    document = Column(JSON)
    users = relationship(
        "User",
        secondary="ncr_user_environments", 
        back_populates="environments",
        overlaps="user,environment,user_environments",
    )

    environment_users = relationship(
        "UserEnvironment",
        back_populates="environment",
        overlaps="environments,users"
    )


class Container(Base):
    __tablename__ = "ncr_containers"
    id = Column(Integer, primary_key=True, index=True)
    document = Column(JSON)

    ucvms = relationship(
        "UserContainerVM",
        back_populates="container"
    )

class VM(Base):
    __tablename__ = "ncr_vms"
    id = Column(Integer, primary_key=True, index=True)
    document = Column(JSON)

    ucvms = relationship(
        "UserContainerVM",
        back_populates="vm"
    )