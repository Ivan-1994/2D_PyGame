
class NewHero:
    def __init__(self, nick_name):
        self.level = 1
        self.__nick_name = nick_name
        print(self.__nick_name)

    def up_lvl(self):
        self.level += 1


class Hero(NewHero):
    def __init__(self, nick):
        super().__init__(nick)
        self.level += 1
        print(nick)

    def show(self):
        print(self.level)

Hero('nick')


