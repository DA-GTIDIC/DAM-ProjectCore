#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import logging
import os

from sqlalchemy.sql import text

import db
import settings
from db.models import SQLAlchemyBase, User, GenereEnum, RolEnum, UserToken, Event, EventTypeEnum
from settings import DEFAULT_LANGUAGE

# LOGGING
mylogger = logging.getLogger(__name__)
settings.configure_logging()


def execute_sql_file(sql_file):
    sql_folder_path = os.path.join(os.path.dirname(__file__), "sql")
    sql_file_path = open(os.path.join(sql_folder_path, sql_file), encoding="utf-8")
    sql_command = text(sql_file_path.read())
    db_session.execute(sql_command)
    db_session.commit()
    sql_file_path.close()


if __name__ == "__main__":
    settings.configure_logging()

    db_session = db.create_db_session()

    # -------------------- REMOVE AND CREATE TABLES --------------------
    mylogger.info("Removing database...")
    SQLAlchemyBase.metadata.drop_all(db.DB_ENGINE)
    mylogger.info("Creating database...")
    SQLAlchemyBase.metadata.create_all(db.DB_ENGINE)



    # -------------------- CREATE USERS --------------------
    mylogger.info("Creating default users...")
    # noinspection PyArgumentList
    user_admin = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="admin",
        email="admin@damcore.com",
        name="Administrator",
        surname="DamCore",
        genere=GenereEnum.female,
        rol=RolEnum.premium,
    )
    user_admin.set_password("DAMCoure")

    # noinspection PyArgumentList
    user_1= User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="usuari1",
        email="usuari1@gmail.com",
        name="usuari",
        surname="1",
        birthdate=datetime.datetime(1989, 1, 1),
        genere=GenereEnum.male,
        rol=RolEnum.premium,
    )
    user_1.set_password("a1s2d3f4")
    user_1.tokens.append(UserToken(token="656e50e154865a5dc469b80437ed2f963b8f58c8857b66c9bf"))

    # noinspection PyArgumentList
    user_2 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user2",
        email="user2@gmail.com",
        name="user",
        surname="2",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.male,
        rol=RolEnum.freemium,
    )
    user_2.set_password("r45tgt")
    user_2.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f584b2"))

    # noinspection PyArgumentList
    user_3 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user3",
        email="user3@gmail.com",
        name="user",
        surname="3",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.female,
        rol=RolEnum.freemium,
    )
    user_3.set_password("r45tgt")
    user_3.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f584b3"))

    # noinspection PyArgumentList
    user_4 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user4",
        email="user4@gmail.com",
        name="user",
        surname="4",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.female,
        rol=RolEnum.freemium,
    )
    user_4.set_password("r45tgt")
    user_4.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f584b4"))

    # noinspection PyArgumentList
    user_5 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user5",
        email="user5@gmail.com",
        name="user",
        surname="5",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.male,
        rol=RolEnum.premium,
    )
    user_5.set_password("r45tgt")
    user_5.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f584b5"))

    # noinspection PyArgumentList
    user_6 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user6",
        email="user6@gmail.com",
        name="user",
        surname="6",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.female,
        rol=RolEnum.freemium,
    )
    user_6.set_password("r45tgt")
    user_6.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f584b6"))

    # noinspection PyArgumentList
    user_7 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user7",
        email="user7@gmail.com",
        name="user",
        surname="7",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.male,
        rol=RolEnum.freemium,
    )
    user_7.set_password("r45tgt")
    user_7.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f584b7"))

    # noinspection PyArgumentList
    user_8 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user8",
        email="user8@gmail.com",
        name="user",
        surname="8",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.female,
        rol=RolEnum.premium,
    )
    user_8.set_password("r45tgt")
    user_8.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f584b8"))

    # noinspection PyArgumentList
    user_9 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user9",
        email="user9@gmail.com",
        name="user",
        surname="9",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.male,
        rol=RolEnum.premium,
    )
    user_9.set_password("r45tgt")
    user_9.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f584b9"))

    # noinspection PyArgumentList
    user_10 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user10",
        email="user10@gmail.com",
        name="user",
        surname="10",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.male,
        rol=RolEnum.premium,
    )
    user_10.set_password("r45tgt")
    user_10.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f585b2"))

    # noinspection PyArgumentList
    user_11 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user11",
        email="user11@gmail.com",
        name="user",
        surname="11",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.female,
        rol=RolEnum.freemium,
    )
    user_11.set_password("r45tgt")
    user_11.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f586b2"))

    # noinspection PyArgumentList
    user_12 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user12",
        email="user12@gmail.com",
        name="user",
        surname="12",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.male,
        rol=RolEnum.freemium,
    )
    user_12.set_password("r45tgt")
    user_12.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f587b2"))

    # noinspection PyArgumentList
    user_13 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user13",
        email="user13@gmail.com",
        name="user",
        surname="13",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.male,
        rol=RolEnum.freemium,
    )
    user_13.set_password("r45tgt")
    user_13.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f588b2"))

    # noinspection PyArgumentList
    user_14 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user14",
        email="user14@gmail.com",
        name="user",
        surname="14",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.male,
        rol=RolEnum.premium,
    )
    user_14.set_password("r45tgt")
    user_14.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f589b2"))

    # noinspection PyArgumentList
    user_15 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user15",
        email="user15@gmail.com",
        name="user",
        surname="15",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.female,
        rol=RolEnum.freemium,
    )
    user_15.set_password("r45tgt")
    user_15.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f684b2"))

    # noinspection PyArgumentList
    user_16 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user16",
        email="user16@gmail.com",
        name="user",
        surname="16",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.female,
        rol=RolEnum.premium,
    )
    user_16.set_password("r45tgt")
    user_16.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f784b2"))

    # noinspection PyArgumentList
    user_17 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user17",
        email="user17@gmail.com",
        name="user",
        surname="17",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.female,
        rol=RolEnum.premium,
    )
    user_17.set_password("r45tgt")
    user_17.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f884b2"))

    # noinspection PyArgumentList
    user_18 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user18",
        email="user18@gmail.com",
        name="user",
        surname="18",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.male,
        rol=RolEnum.freemium,
    )
    user_18.set_password("r45tgt")
    user_18.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f429f984b2"))

    # noinspection PyArgumentList
    user_19 = User(
        created_at=datetime.datetime(2020, 1, 1, 0, 1, 1),
        username="user19",
        email="user19@gmail.com",
        name="user",
        surname="19",
        birthdate=datetime.datetime(2017, 1, 1),
        genere=GenereEnum.female,
        rol=RolEnum.premium,
    )
    user_19.set_password("r45tgt")
    user_19.tokens.append(UserToken(token="0a821f8ce58965eadc5ef884cf6f7ad99e0e7f58f439f584b2"))

    db_session.add(user_admin)
    db_session.add(user_1)
    db_session.add(user_2)
    db_session.add(user_3)
    db_session.add(user_4)
    db_session.add(user_5)
    db_session.add(user_6)
    db_session.add(user_7)
    db_session.add(user_8)
    db_session.add(user_9)
    db_session.add(user_10)
    db_session.add(user_11)
    db_session.add(user_12)
    db_session.add(user_13)
    db_session.add(user_14)
    db_session.add(user_15)
    db_session.add(user_16)
    db_session.add(user_17)
    db_session.add(user_18)
    db_session.add(user_19)


    # -------------------- CREATE EVENTS --------------------

    day_period = datetime.timedelta(days=1)

    event_hackatoon = Event(
        created_at=datetime.datetime.now(),
        name="event1",
        description="description 1",
        type=EventTypeEnum.hackathon,
        start_date=datetime.datetime.now() + (day_period * 3),
        finish_date=datetime.datetime.now() + (day_period * 5),
        owner_id = 0,
        poster="logo.png",
        registered=[user_1, user_2]
    )

    event_livecoding = Event(
        created_at=datetime.datetime.now(),
        name="event2",
        description="descr2",
        type=EventTypeEnum.livecoding,
        start_date=datetime.datetime.now() - (day_period * 5),
        finish_date=datetime.datetime.now() - (day_period * 4),
        owner_id=1,
        registered=[user_2]
    )

    event_lanparty = Event(
        created_at=datetime.datetime.now(),
        name="event3",
        description="desc3",
        type=EventTypeEnum.lanparty,
        start_date=datetime.datetime.now(),
        finish_date=datetime.datetime.now() + (day_period * 1),
        owner_id=1,
        registered=[]
    )

    db_session.add(event_hackatoon)
    db_session.add(event_livecoding)
    db_session.add(event_lanparty)



    db_session.commit()
    db_session.close()
