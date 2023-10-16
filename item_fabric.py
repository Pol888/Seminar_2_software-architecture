from abc import ABC, abstractmethod

from i_game_item import IGameItem


class ItemFabric(ABC):

    @abstractmethod
    def create_item(self) -> IGameItem:
        pass
