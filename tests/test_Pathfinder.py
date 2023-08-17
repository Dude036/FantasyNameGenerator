from FantasyNameGenerator.Pathfinder import *


class TestPathfinder:
    def test_Anadi(self):
        counter = 100
        for _ in range(counter):
            assert str(Anadi()) is not None

        for name in Anadi():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Android(self):
        counter = 100
        for _ in range(counter):
            assert str(Android()) is not None

        for name in Android():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Automaton(self):
        counter = 100
        for _ in range(counter):
            assert str(Automaton()) is not None

        for name in Automaton():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Azarketi(self):
        counter = 100
        for _ in range(counter):
            assert str(Azarketi()) is not None

        for name in Azarketi():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Catfolk(self):
        counter = 100
        for _ in range(counter):
            assert str(Catfolk()) is not None
            assert str(Catfolk.generate(Catfolk.CatfolkType.Male)) is not None
            assert str(Catfolk.generate(Catfolk.CatfolkType.Female)) is not None

        for name in Catfolk():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Conrasu(self):
        counter = 100
        for _ in range(counter):
            assert str(Conrasu()) is not None

        for name in Conrasu():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Dhampir(self):
        counter = 100
        for _ in range(counter):
            assert str(Dhampir()) is not None
            assert str(Dhampir.generate(Dhampir.DhampirType.Male)) is not None
            assert str(Dhampir.generate(Dhampir.DhampirType.Female)) is not None

        for name in Dhampir():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Dwarf(self):
        counter = 100
        for _ in range(counter):
            assert str(Dwarf()) is not None
            assert str(Dwarf.generate(Dwarf.DwarfType.Male)) is not None
            assert str(Dwarf.generate(Dwarf.DwarfType.Female)) is not None

        for name in Dwarf():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Elf(self):
        counter = 100
        for _ in range(counter):
            assert str(Elf()) is not None
            assert str(Elf.generate(Elf.ElfType.Male)) is not None
            assert str(Elf.generate(Elf.ElfType.Female)) is not None

        for name in Elf():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Fetchling(self):
        counter = 100
        for _ in range(counter):
            assert str(Fetchling()) is not None

        for name in Fetchling():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Fleshwarp(self):
        counter = 100
        for _ in range(counter):
            assert str(Fleshwarp()) is not None

        for name in Fleshwarp():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Ghoran(self):
        counter = 100
        for _ in range(counter):
            assert str(Ghoran()) is not None

        for name in Ghoran():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Gillman(self):
        counter = 100
        for _ in range(counter):
            assert str(Gillman()) is not None
            assert str(Gillman.generate(Gillman.GillmanType.Male)) is not None
            assert str(Gillman.generate(Gillman.GillmanType.Female)) is not None

        for name in Gillman():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Gnoll(self):
        counter = 100
        for _ in range(counter):
            assert str(Gnoll()) is not None

        for name in Gnoll():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Gnome(self):
        counter = 100
        for _ in range(counter):
            assert str(Gnome()) is not None
            assert str(Gnome.generate(Gnome.GnomeType.Male)) is not None
            assert str(Gnome.generate(Gnome.GnomeType.Female)) is not None

        for name in Gnome():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Goblin(self):
        counter = 100
        for _ in range(counter):
            assert str(Goblin()) is not None
            assert str(Goblin.generate(Goblin.GoblinType.Male)) is not None
            assert str(Goblin.generate(Goblin.GoblinType.Female)) is not None

        for name in Goblin():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Goloma(self):
        counter = 100
        for _ in range(counter):
            assert str(Goloma()) is not None

        for name in Goloma():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Grippli(self):
        counter = 100
        for _ in range(counter):
            assert str(Grippli()) is not None
            assert str(Grippli.generate(Grippli.GrippliType.Male)) is not None
            assert str(Grippli.generate(Grippli.GrippliType.Female)) is not None

        for name in Grippli():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Halfling(self):
        counter = 100
        for _ in range(counter):
            assert str(Halfling()) is not None
            assert str(Halfling.generate(Halfling.HalflingType.Male)) is not None
            assert str(Halfling.generate(Halfling.HalflingType.Female)) is not None

        for name in Halfling():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Hobgoblin(self):
        counter = 100
        for _ in range(counter):
            assert str(Hobgoblin()) is not None

        for name in Hobgoblin():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Human(self):
        counter = 100
        for _ in range(counter):
            assert str(Human()) is not None
            assert str(Human.generate(Human.HumanType.Male)) is not None
            assert str(Human.generate(Human.HumanType.Female)) is not None

        for name in Human():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Ifrit(self):
        counter = 100
        for _ in range(counter):
            assert str(Ifrit()) is not None
            assert str(Ifrit.generate(Ifrit.IfritType.Male)) is not None
            assert str(Ifrit.generate(Ifrit.IfritType.Female)) is not None

        for name in Ifrit():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Kashrishi(self):
        counter = 100
        for _ in range(counter):
            assert str(Kashrishi()) is not None

        for name in Kashrishi():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Kitsune(self):
        counter = 100
        for _ in range(counter):
            assert str(Kitsune()) is not None
            assert str(Kitsune.generate(Kitsune.KitsuneType.Male)) is not None
            assert str(Kitsune.generate(Kitsune.KitsuneType.Female)) is not None

        for name in Kitsune():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Kobold(self):
        counter = 100
        for _ in range(counter):
            assert str(Kobold()) is not None
            assert str(Kobold.generate(Kobold.KoboldType.Male)) is not None
            assert str(Kobold.generate(Kobold.KoboldType.Female)) is not None

        for name in Kobold():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Leshy(self):
        counter = 100
        for _ in range(counter):
            assert str(Leshy()) is not None

        for name in Leshy():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Lizardfolk(self):
        counter = 100
        for _ in range(counter):
            assert str(Lizardfolk()) is not None

        for name in Lizardfolk():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Merfolk(self):
        counter = 100
        for _ in range(counter):
            assert str(Merfolk()) is not None
            assert str(Merfolk.generate(Merfolk.MerfolkType.Male)) is not None
            assert str(Merfolk.generate(Merfolk.MerfolkType.Female)) is not None

        for name in Merfolk():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Nagaji(self):
        counter = 100
        for _ in range(counter):
            assert str(Nagaji()) is not None
            assert str(Nagaji.generate(Nagaji.NagajiType.Male)) is not None
            assert str(Nagaji.generate(Nagaji.NagajiType.Female)) is not None

        for name in Nagaji():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Orc(self):
        counter = 100
        for _ in range(counter):
            assert str(Orc()) is not None
            assert str(Orc.generate(Orc.OrcType.Male)) is not None
            assert str(Orc.generate(Orc.OrcType.Female)) is not None

        for name in Orc():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Oread(self):
        counter = 100
        for _ in range(counter):
            assert str(Oread()) is not None
            assert str(Oread.generate(Oread.OreadType.Male)) is not None
            assert str(Oread.generate(Oread.OreadType.Female)) is not None

        for name in Oread():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Poppet(self):
        counter = 100
        for _ in range(counter):
            assert str(Poppet()) is not None

        for name in Poppet():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Ratfolk(self):
        counter = 100
        for _ in range(counter):
            assert str(Ratfolk()) is not None
            assert str(Ratfolk.generate(Ratfolk.RatfolkType.Male)) is not None
            assert str(Ratfolk.generate(Ratfolk.RatfolkType.Female)) is not None

        for name in Ratfolk():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Shisk(self):
        counter = 100
        for _ in range(counter):
            assert str(Shisk()) is not None

        for name in Shisk():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Shoony(self):
        counter = 100
        for _ in range(counter):
            assert str(Shoony()) is not None

        for name in Shoony():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Skeleton(self):
        counter = 100
        for _ in range(counter):
            assert str(Skeleton()) is not None

        for name in Skeleton():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Sprite(self):
        counter = 100
        for _ in range(counter):
            assert str(Sprite()) is not None

        for name in Sprite():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Strix(self):
        counter = 100
        for _ in range(counter):
            assert str(Strix()) is not None
            assert str(Strix.generate(Strix.StrixType.Male)) is not None
            assert str(Strix.generate(Strix.StrixType.Female)) is not None

        for name in Strix():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Suli(self):
        counter = 100
        for _ in range(counter):
            assert str(Suli()) is not None
            assert str(Suli.generate(Suli.SuliType.Male)) is not None
            assert str(Suli.generate(Suli.SuliType.Female)) is not None

        for name in Suli():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Sylph(self):
        counter = 100
        for _ in range(counter):
            assert str(Sylph()) is not None
            assert str(Sylph.generate(Sylph.SylphType.Male)) is not None
            assert str(Sylph.generate(Sylph.SylphType.Female)) is not None

        for name in Sylph():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Tengu(self):
        counter = 100
        for _ in range(counter):
            assert str(Tengu()) is not None
            assert str(Tengu.generate(Tengu.TenguType.Male)) is not None
            assert str(Tengu.generate(Tengu.TenguType.Female)) is not None

        for name in Tengu():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Tian(self):
        counter = 100
        for _ in range(counter):
            assert str(Tian()) is not None
            assert str(Tian.generate(Tian.TianType.Male)) is not None
            assert str(Tian.generate(Tian.TianType.Female)) is not None

        for name in Tian():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Undine(self):
        counter = 100
        for _ in range(counter):
            assert str(Undine()) is not None
            assert str(Undine.generate(Undine.UndineType.Male)) is not None
            assert str(Undine.generate(Undine.UndineType.Female)) is not None

        for name in Undine():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Vanara(self):
        counter = 100
        for _ in range(counter):
            assert str(Vanara()) is not None

        for name in Vanara():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Vishkanya(self):
        counter = 100
        for _ in range(counter):
            assert str(Vishkanya()) is not None

        for name in Vishkanya():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1
