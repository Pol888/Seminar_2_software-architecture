from item_fabric import ItemFabric
from rewards import *


class GoldGen(ItemFabric):
    def create_item(self) -> IGameItem:
        print('Создали сундук(золото)')
        return GoldReward()

class ChipGen(ItemFabric):
    def create_item(self) -> IGameItem:
        print('Создали сундук(чипсы)')
        return ChipReward()

class JamGen(ItemFabric):
    def create_item(self) -> IGameItem:
        print('Создали сундук(варенье)')
        return JamReward()

class BricksGen(ItemFabric):
    def create_item(self) -> IGameItem:
        print('Создали сундук(кирпичи)')
        return BricksReward()
