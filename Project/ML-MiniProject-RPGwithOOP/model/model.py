from abc import ABC, abstractmethod


class Model(ABC):
    def __init__(self, name:str) -> None:
        self.name = name
    