from FantasyNameGenerator.Stores import *


class TestStores:
    def test_Antique(self):
        for _ in range(100):
            assert str(Antique()) is not None

        counter = 100
        for name in Antique():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Clothes(self):
        for _ in range(100):
            assert str(Clothes()) is not None

        counter = 100
        for name in Clothes():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Enchanter(self):
        for _ in range(100):
            assert str(Enchanter()) is not None

        counter = 100
        for name in Enchanter():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Alchemist(self):
        for _ in range(100):
            assert str(Alchemist()) is not None

        counter = 100
        for name in Alchemist():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Restaurant(self):
        for _ in range(100):
            assert str(Restaurant()) is not None

        counter = 100
        for name in Restaurant():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Tavern(self):
        for _ in range(100):
            assert str(Restaurant.Tavern()) is not None

        counter = 100
        for name in Restaurant.Tavern():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Diner(self):
        for _ in range(100):
            assert str(Restaurant.Diner()) is not None

        counter = 100
        for name in Restaurant.Diner():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_French(self):
        for _ in range(100):
            assert str(Restaurant.French()) is not None

        counter = 100
        for name in Restaurant.French():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Jeweller(self):
        for _ in range(100):
            assert str(Jeweller()) is not None

        counter = 100
        for name in Jeweller():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Blacksmith(self):
        for _ in range(100):
            assert str(Blacksmith()) is not None

        counter = 100
        for name in Blacksmith():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_General(self):
        for _ in range(100):
            assert str(General()) is not None

        counter = 100
        for name in General():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Town(self):
        for _ in range(100):
            assert str(Town()) is not None

        counter = 100
        for name in Town():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Brothel(self):
        for _ in range(100):
            assert str(Brothel()) is not None

        counter = 100
        for name in Brothel():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Gunsmith(self):
        for _ in range(100):
            assert str(Gunsmith()) is not None

        counter = 100
        for name in Gunsmith():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Guild(self):
        for _ in range(100):
            assert str(Guild()) is not None

        counter = 100
        for name in Guild():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1
