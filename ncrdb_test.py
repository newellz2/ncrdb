#!/usr/bin/env python3
import sys
import json
from ncrdb.database import engine, SessionLocal, Base
from ncrdb.models import User, Environment, Container, VM, UserContainerVM
from sqlalchemy import select


# create tables
Base.metadata(engine)

u = User()
e = Environment()
c = Container()
vm = VM()
uvms = UserContainerVM()

print('Test CRUD operations')

session = SessionLocal()

statement = select(User).filter_by(username="username")

result = session.execute(statement).scalars().first()

print(f'Username: {result.username}')

sys.exit(0)

cdb_file = open('ncrdb/couchdb.json', 'r')

text = cdb_file.read()

cdb_file.close()

cdb_json = json.loads(text)

for e in cdb_json['rows']:
    id = e['doc']['id']
    username = e['doc']['username']
    doc = e['doc']
    print(f'Username: {username}, ID:{id}')
    u = User(username=username)
    env = Environment(id=id, document=doc)
    u.environments.append(env)

    session.add(u)

#e.users.append(u)
#session.add(e)
session.commit()
