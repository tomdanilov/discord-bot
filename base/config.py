"""This file contains the Config class that handles the Configuration of the bot."""

from __future__ import annotations
from dataclasses import dataclass
import json


@dataclass
class Config:
    token: str
    cogs: list

    @staticmethod
    def load(filename: str = 'config.json') -> Config:
        with open(filename, 'r') as file:
            config_json = file.read()

        config_dict = json.loads(config_json)
        return Config(**config_dict)
