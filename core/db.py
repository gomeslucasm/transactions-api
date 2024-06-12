from core.config import MONGO_URI
from motor.motor_tornado import MotorClient


def get_db():
    client = MotorClient(MONGO_URI)
    return client.cappta
