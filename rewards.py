from i_game_item import IGameItem


class GoldReward(IGameItem):

    def open(self) -> None:
        print('Открыли сундук с золотом')


class ChipReward(IGameItem):

    def open(self) -> None:
        print('Открыли сундук с чипсами')


class JamReward(IGameItem):

    def open(self) -> None:
        print('Открыли сундук с вареньем')


class BricksReward(IGameItem):

    def open(self) -> None:
        print('Открыли сундук с кирпичами')
