from abc import ABC, abstractmethod

from collections import UserDict
from typing import ItemsView, Optional
from cli.models.record import Record

class BaseAddressBook(ABC):

    @abstractmethod
    def add_record(self, record: Record) -> None: ...

    @abstractmethod
    def find(self, name) -> Optional[Record]: ...

    @abstractmethod
    def find_all(self) -> ItemsView[str, Record]: ...

    @abstractmethod
    def delete(self, name) -> None: ...


class AddressBook(UserDict, BaseAddressBook):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def find_all(self):
        return self.data.items()

    def delete(self, name):
        if name in self.data:
            del self.data[name]
