from FantasyNameGenerator.Items import *


class TestItems:
    def test_Book(self):
        for _ in range(100):
            assert str(Book()) is not None

        counter = 100
        for name in Book():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Children(self):
        for _ in range(100):
            assert str(Book.Children()) is not None

        counter = 100
        for name in Book.Children():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Drama(self):
        for _ in range(100):
            assert str(Book.Drama()) is not None

        counter = 100
        for name in Book.Drama():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Fiction(self):
        for _ in range(100):
            assert str(Book.Fiction()) is not None

        counter = 100
        for name in Book.Fiction():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Horror(self):
        for _ in range(100):
            assert str(Book.Horror()) is not None

        counter = 100
        for name in Book.Horror():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Humor(self):
        for _ in range(100):
            assert str(Book.Humor()) is not None

        counter = 100
        for name in Book.Humor():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Mystery(self):
        for _ in range(100):
            assert str(Book.Mystery()) is not None

        counter = 100
        for name in Book.Mystery():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Nonfiction(self):
        for _ in range(100):
            assert str(Book.Nonfiction()) is not None

        counter = 100
        for name in Book.Nonfiction():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Romance(self):
        for _ in range(100):
            assert str(Book.Romance()) is not None

        counter = 100
        for name in Book.Romance():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_SciFi(self):
        for _ in range(100):
            assert str(Book.SciFi()) is not None

        counter = 100
        for name in Book.SciFi():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Tome(self):
        for _ in range(100):
            assert str(Book.Tome()) is not None

        counter = 100
        for name in Book.Tome():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Relic(self):
        for _ in range(100):
            assert str(Relic()) is not None

        counter = 100
        for name in Relic():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Armor(self):
        for _ in range(100):
            assert str(Relic.Armor()) is not None

        counter = 100
        for name in Relic.Armor():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Book(self):
        for _ in range(100):
            assert str(Relic.Book()) is not None

        counter = 100
        for name in Relic.Book():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Potion(self):
        for _ in range(100):
            assert str(Relic.Potion()) is not None

        counter = 100
        for name in Relic.Potion():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Jewel(self):
        for _ in range(100):
            assert str(Relic.Jewel()) is not None

        counter = 100
        for name in Relic.Jewel():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Other(self):
        for _ in range(100):
            assert str(Relic.Other()) is not None

        counter = 100
        for name in Relic.Other():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Weapon(self):
        for _ in range(100):
            assert str(Weapon()) is not None

        counter = 100
        for name in Weapon():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Axe(self):
        for _ in range(100):
            assert str(Weapon.Axe()) is not None

        counter = 100
        for name in Weapon.Axe():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Bow(self):
        for _ in range(100):
            assert str(Weapon.Bow()) is not None

        counter = 100
        for name in Weapon.Bow():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Dagger(self):
        for _ in range(100):
            assert str(Weapon.Dagger()) is not None

        counter = 100
        for name in Weapon.Dagger():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Hammer(self):
        for _ in range(100):
            assert str(Weapon.Hammer()) is not None

        counter = 100
        for name in Weapon.Hammer():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Mace(self):
        for _ in range(100):
            assert str(Weapon.Mace()) is not None

        counter = 100
        for name in Weapon.Mace():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Spear(self):
        for _ in range(100):
            assert str(Weapon.Spear()) is not None

        counter = 100
        for name in Weapon.Spear():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Sword(self):
        for _ in range(100):
            assert str(Weapon.Sword()) is not None

        counter = 100
        for name in Weapon.Sword():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1
