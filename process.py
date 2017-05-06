#!/usr/bin/env python3

import datetime
import sys
import time

from libcitizenwatt import database
from libcitizenwatt import tools
from libcitizenwatt.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

filename = "/tmp/sensor.log"


def get_rate_type(db):
    """Returns "day" or "night" according to current time
    """
    user = db.query(database.User).filter_by(is_admin=1).first()
    now = datetime.datetime.now()
    now = 3600 * now.hour + 60 * now.minute
    if user is None:
        return -1
    elif user.end_night_rate > user.start_night_rate:
        if now > user.start_night_rate and now < user.end_night_rate:
            return 1
        else:
            return 0
    else:
        if now > user.start_night_rate or now < user.end_night_rate:
            return 1
        else:
            return 0


def get_cw_sensor():
    """Returns the citizenwatt sensor object or None"""
    db = create_session()
    sensor = (db.query(database.Sensor)
              .filter_by(name="CitizenWatt")
              .first())
    db.close()
    return sensor


# Configuration
config = Config()

# DB initialization
database_url = (config.get("database_type") + "://" + config.get("username") +
                ":" + config.get("password") + "@" + config.get("host") + "/" +
                config.get("database"))
engine = create_engine(database_url, echo=config.get("debug"))
create_session = sessionmaker(bind=engine)
database.Base.metadata.create_all(engine)

sensor = get_cw_sensor()
while not sensor or not sensor.aes_key:
    tools.warning("Install is not complete ! " +
                  "Visit http://citizenwatt.local first.")
    time.sleep(1)
    sensor = get_cw_sensor()

try:
    with open(filename):
        pass
except FileNotFoundError:
    sys.exit("Unable to open file " + filename + ".")

lastTimer = 0

try:
    with open(config.get(filename), 'r'):
        while True:
            FileTemp = open(filename, 'r')
            measure = FileTemp.read()
            measure = measure.split(',')
            try:
                power = measure[0]
                timer = measure[1]
            except Exception as e:
                #print("Process.py - ERROR : Incorrect data > measure = " + str(measure))
                pass
            else:
                if timer == lastTimer:
                    pass
                else:
                    lastTimer = timer
                    #print("Process.py - Measure:" + str(measure))
                    try:
                        db = create_session()
                        #print("power:" + power)
                        measure_db = database.Measures(sensor_id=sensor.id,
                                                       value=power,
                                                       timestamp=datetime.datetime.now().timestamp(),
                                                       night_rate=get_rate_type(db))
                        db.add(measure_db)
                        sensor.last_timer = float(timer)
                        (db.query(database.Sensor)
                         .filter_by(name="CitizenWatt")
                         .update({"last_timer": sensor.last_timer}))
                        db.commit()
                    except Exception as e:
                        print("ERROR : DB commit failed")
                    else:
                        print("Saved successfully.")

except KeyboardInterrupt:
    pass
