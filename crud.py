from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_envs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Environment).offset(skip).limit(limit).all()

def get_env(db: Session, env_id):
    return db.query(models.Environment).filter(models.Environment.id == env_id).first()

