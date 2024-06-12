from core.config import DATABASE_NAME, MONGO_URI
from motor.motor_tornado import MotorClient


def get_db():
    client = MotorClient(MONGO_URI)
    return client.get_database(DATABASE_NAME)
