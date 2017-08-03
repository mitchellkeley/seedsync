# Copyright 2017, Inderpreet Singh, All rights reserved.

from datetime import datetime
from enum import Enum
from typing import Optional
from datetime import datetime


class ModelFile:
    """
    Represents a file or directory
    """
    class State(Enum):
        DEFAULT = 0
        DOWNLOADING = 1
        QUEUED = 2

    def __init__(self, name: str):
        self.__name = name  # file or folder name
        self.__state = ModelFile.State.DEFAULT  # status
        self.__remote_size = None  # remote size in bytes, None if file does not exist
        self.__local_size = None  # local size in bytes, None if file does not exist
        self.__downloading_speed = None  # in bytes / sec, None if not downloading
        now = datetime.now()
        self.__update_timestamp = now  # timestamp of the latest update
        self.__remote_update_timestamp = now  # timestamp of the remote size update
        self.__local_update_timestamp = now  # timestamp of the local size update

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return str(self.__dict__)

    @property
    def name(self) -> str: return self.__name

    @property
    def state(self) -> State: return self.__state

    @state.setter
    def state(self, state: State):
        if type(state) != ModelFile.State:
            raise TypeError
        self.__state = state

    @property
    def remote_size(self) -> Optional[int]: return self.__remote_size

    @remote_size.setter
    def remote_size(self, remote_size: Optional[int]):
        if type(remote_size) == int:
            if remote_size < 0:
                raise ValueError
            self.__remote_size = remote_size
        elif remote_size is None:
            self.__remote_size = remote_size
        else:
            raise TypeError

    @property
    def local_size(self) -> Optional[int]: return self.__local_size

    @local_size.setter
    def local_size(self, local_size: Optional[int]):
        if type(local_size) == int:
            if local_size < 0:
                raise ValueError
            self.__local_size = local_size
        elif local_size is None:
            self.__local_size = local_size
        else:
            raise TypeError

    @property
    def downloading_speed(self) -> Optional[int]: return self.__downloading_speed

    @downloading_speed.setter
    def downloading_speed(self, downloading_speed: Optional[int]):
        if type(downloading_speed) == int:
            if downloading_speed < 0:
                raise ValueError
            self.__downloading_speed = downloading_speed
        elif downloading_speed is None:
            self.__downloading_speed = downloading_speed
        else:
            raise TypeError

    @property
    def update_timestamp(self) -> datetime: return self.__update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp: datetime):
        if type(update_timestamp) != datetime:
            raise TypeError
        self.__update_timestamp = update_timestamp

    @property
    def remote_update_timestamp(self) -> datetime: return self.__remote_update_timestamp

    @remote_update_timestamp.setter
    def remote_update_timestamp(self, update_timestamp: datetime):
        if type(update_timestamp) != datetime:
            raise TypeError
        self.__remote_update_timestamp = update_timestamp

    @property
    def local_update_timestamp(self) -> datetime: return self.__local_update_timestamp

    @local_update_timestamp.setter
    def local_update_timestamp(self, update_timestamp: datetime):
        if type(update_timestamp) != datetime:
            raise TypeError
        self.__local_update_timestamp = update_timestamp