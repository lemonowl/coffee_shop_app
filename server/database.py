import abc
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

DATABASE_URI = "mongodb://localhost:27017/"


class DatabaseClient:
    _instance = None

    def __new__(cls) -> None:
        if not cls._instance:
            cls._instance = super(DatabaseClient, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, 'db'):
            client = MongoClient(DATABASE_URI)
            self.db = client.coffeeshop_db


class DatabaseModel:

    def __init__(self):
        self.__db = DatabaseClient().db

    @property
    def db(self) -> Database:
        return self.__db

    @property
    @abc.abstractmethod
    def collection(self) -> Collection:
        pass
