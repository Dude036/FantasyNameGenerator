from FantasyNameGenerator.DnD import *


class TestDnD:
    def test_Aarakocra(self):
        counter = 100
        for _ in range(counter):
            assert str(Aarakocra()) is not None

        for name in Aarakocra():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Aasimer(self):
        counter = 100
        for _ in range(counter):
            assert str(Aasimer()) is not None
            assert str(Aasimer.generate(Aasimer.AasimerType.Male)) is not None
            assert str(Aasimer.generate(Aasimer.AasimerType.Female)) is not None

        for name in Aasimer():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Bugbear(self):
        counter = 100
        for _ in range(counter):
            assert str(Bugbear()) is not None

        for name in Bugbear():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Centaur(self):
        counter = 100
        for _ in range(counter):
            assert str(Centaur()) is not None
            assert str(Centaur.generate(Centaur.CentaurType.Male)) is not None
            assert str(Centaur.generate(Centaur.CentaurType.Female)) is not None

        for name in Centaur():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Changeling(self):
        counter = 100
        for _ in range(counter):
            assert str(Changeling()) is not None

        for name in Changeling():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Dragonborn(self):
        counter = 100
        for _ in range(counter):
            assert str(Dragonborn()) is not None
            assert str(Dragonborn.generate(Dragonborn.DragonbornType.Male)) is not None
            assert str(Dragonborn.generate(Dragonborn.DragonbornType.Female)) is not None

        for name in Dragonborn():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Drow(self):
        counter = 100
        for _ in range(counter):
            assert str(Drow()) is not None
            assert str(Drow.generate(Drow.DrowType.Male)) is not None
            assert str(Drow.generate(Drow.DrowType.Female)) is not None

        for name in Drow():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Duergar(self):
        counter = 100
        for _ in range(counter):
            assert str(Duergar()) is not None
            assert str(Duergar.generate(Duergar.DuergarType.Male)) is not None
            assert str(Duergar.generate(Duergar.DuergarType.Female)) is not None

        for name in Duergar():
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
            assert str(Fetchling.generate(Fetchling.FetchlingType.Male)) is not None
            assert str(Fetchling.generate(Fetchling.FetchlingType.Female)) is not None

        for name in Fetchling():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Firbolg(self):
        counter = 100
        for _ in range(counter):
            assert str(Firbolg()) is not None
            assert str(Firbolg.generate(Firbolg.FirbolgType.Male)) is not None
            assert str(Firbolg.generate(Firbolg.FirbolgType.Female)) is not None

        for name in Firbolg():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Genasi(self):
        counter = 100
        for _ in range(counter):
            assert str(Genasi()) is not None
            assert str(Genasi.generate(Genasi.GenasiType.Air)) is not None
            assert str(Genasi.generate(Genasi.GenasiType.Water)) is not None
            assert str(Genasi.generate(Genasi.GenasiType.Fire)) is not None
            assert str(Genasi.generate(Genasi.GenasiType.Earth)) is not None

        for name in Genasi():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Gith(self):
        counter = 100
        for _ in range(counter):
            assert str(Gith()) is not None
            assert str(Gith.generate(Gith.GithType.Male)) is not None
            assert str(Gith.generate(Gith.GithType.Female)) is not None

        for name in Gith():
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
            assert str(Gnome.generate(Gnome.GnomeType.Male)) is not None
            assert str(Gnome.generate(Gnome.GnomeType.Female)) is not None

        for name in Goblin():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Goliath(self):
        counter = 100
        for _ in range(counter):
            assert str(Goliath()) is not None
            assert str(Goliath.generate(Goliath.GoliathType.Male)) is not None
            assert str(Goliath.generate(Goliath.GoliathType.Female)) is not None

        for name in Goliath():
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
            assert str(Hobgoblin.generate(Hobgoblin.HobgoblinType.Male)) is not None
            assert str(Hobgoblin.generate(Hobgoblin.HobgoblinType.Female)) is not None

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

    def test_HalfElf(self):
        counter = 100
        for _ in range(counter):
            assert str(HalfElf()) is not None
            assert str(HalfElf.generate(HalfElf.HalfElfType.Male)) is not None
            assert str(HalfElf.generate(HalfElf.HalfElfType.Female)) is not None

        for name in HalfElf():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_HalfOrc(self):
        counter = 100
        for _ in range(counter):
            assert str(HalfOrc()) is not None
            assert str(HalfOrc.generate(HalfOrc.HalfOrcType.Male)) is not None
            assert str(HalfOrc.generate(HalfOrc.HalfOrcType.Female)) is not None

        for name in HalfOrc():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Kalashtar(self):
        counter = 100
        for _ in range(counter):
            assert str(Kalashtar()) is not None
            assert str(Kalashtar.generate(Kalashtar.KalashtarType.Male)) is not None
            assert str(Kalashtar.generate(Kalashtar.KalashtarType.Female)) is not None

        for name in Kalashtar():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Kenku(self):
        counter = 100
        for _ in range(counter):
            assert str(Kenku()) is not None

        for name in Kenku():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Kobold(self):
        counter = 100
        for _ in range(counter):
            assert str(Kobold()) is not None
            assert str(Kalashtar.generate(Kalashtar.KalashtarType.Male)) is not None
            assert str(Kalashtar.generate(Kalashtar.KalashtarType.Female)) is not None

        for name in Kobold():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Lizardfolk(self):
        counter = 100
        for _ in range(counter):
            assert str(Lizardfolk()) is not None
            assert str(Lizardfolk.generate(Lizardfolk.LizardfolkType.Male)) is not None
            assert str(Lizardfolk.generate(Lizardfolk.LizardfolkType.Female)) is not None

        for name in Lizardfolk():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Loxodon(self):
        counter = 100
        for _ in range(counter):
            assert str(Loxodon()) is not None
            assert str(Loxodon.generate(Loxodon.LoxodonType.Male)) is not None
            assert str(Loxodon.generate(Loxodon.LoxodonType.Female)) is not None

        for name in Loxodon():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Minotaur(self):
        counter = 100
        for _ in range(counter):
            assert str(Minotaur()) is not None
            assert str(Minotaur.generate(Minotaur.MinotaurType.Male)) is not None
            assert str(Minotaur.generate(Minotaur.MinotaurType.Female)) is not None

        for name in Minotaur():
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

    def test_Shifter(self):
        counter = 100
        for _ in range(counter):
            assert str(Shifter()) is not None
            assert str(Shifter.generate(Shifter.ShifterType.Male)) is not None
            assert str(Shifter.generate(Shifter.ShifterType.Female)) is not None

        for name in Shifter():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_SimicHybrid(self):
        counter = 100
        for _ in range(counter):
            assert str(SimicHybrid()) is not None
            assert str(SimicHybrid.generate(SimicHybrid.SimicHybridType.Male)) is not None
            assert str(SimicHybrid.generate(SimicHybrid.SimicHybridType.Female)) is not None

        for name in SimicHybrid():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Svirfneblin(self):
        counter = 100
        for _ in range(counter):
            assert str(Svirfneblin()) is not None
            assert str(Svirfneblin.generate(Svirfneblin.SvirfneblinType.Male)) is not None
            assert str(Svirfneblin.generate(Svirfneblin.SvirfneblinType.Female)) is not None

        for name in Svirfneblin():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Tabaxi(self):
        counter = 100
        for _ in range(counter):
            assert str(Tabaxi()) is not None

        for name in Tabaxi():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Tiefling(self):
        counter = 100
        for _ in range(counter):
            assert str(Tiefling()) is not None
            assert str(Tiefling.generate(Tiefling.TieflingType.Male)) is not None
            assert str(Tiefling.generate(Tiefling.TieflingType.Female)) is not None

        for name in Tiefling():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Tortle(self):
        counter = 100
        for _ in range(counter):
            assert str(Tortle()) is not None

        for name in Tortle():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Triton(self):
        counter = 100
        for _ in range(counter):
            assert str(Triton()) is not None
            assert str(Triton.generate(Triton.TritonType.Male)) is not None
            assert str(Triton.generate(Triton.TritonType.Female)) is not None

        for name in Triton():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Vedalken(self):
        counter = 100
        for _ in range(counter):
            assert str(Vedalken()) is not None
            assert str(Vedalken.generate(Vedalken.VedalkenType.Male)) is not None
            assert str(Vedalken.generate(Vedalken.VedalkenType.Female)) is not None

        for name in Vedalken():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Warforged(self):
        counter = 100
        for _ in range(counter):
            assert str(Warforged()) is not None

        for name in Warforged():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1

    def test_Yuanti(self):
        counter = 100
        for _ in range(counter):
            assert str(Yuanti()) is not None

        for name in Yuanti():
            assert name is not None
            if counter <= 0:
                break
            else:
                counter -= 1
