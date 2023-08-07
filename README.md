# Fantasy Names
A Python project dedicated to generating names from various bits of fantasy

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Installation

### pip

Install [FantasyNameGenerator](https://pypi.org/project/FantasyNameGenerator/) as a package with pip using this command:

`pip install FantasyNameGenerator`

### Source

Install FantasyNameGenerator as a package from source using this command while in the home directory

`pip install .`

## Usage

The main use case for this application is to generate a random name for something.
Since this project offers many different types of generators, the main formula for these follows this pattern:

```python
from FantasyNameGenerator.<Category> import <Thing>
```

#### Examples

Town Name Generator
```python
from FantasyNameGenerator.Stores import Town
print(Town())
var = Town()
for name in Town():
    print(name)
```

Weapon Name Generator
```python
from FantasyNameGenerator.Items import Weapon 
print(Weapon())
var = Weapon()
for name in Weapon():
    print(name)
```

Dungeon's & Dragons Aasimer Name
```python
from FantasyNameGenerator.DnD import Aasimer 
print(Aasimer())
var = Aasimer()
for name in Aasimer():
    print(name)
```

### Generators

There are a few name generators included with this repo. Here are the main categories and what they contain:

### Stores

- Antique
- Book
  - Children
  - Drama
  - Fiction
  - Horror
  - Humor
  - Mystery
  - Non-fiction
  - Romance
  - Sci-Fi
  - Tome
- Clothes
- Enchanter
- Alchemist
- Restaurant
  - Tavern
  - Diner
  - French
- Jeweller
- Blacksmith
- General
- Town
- Brothel
- Gunsmith
- Guild

### Items

- Relic
  - Armor
  - Book
  - Potion
  - Jewel
  - Other
- Weapon
  - Axe
  - Bow
  - Dagger
  - Hammer
  - Mace
  - Spear
  - Sword

### Pathfinder Races

- Coming Soon

### Dungeons & Dragons Races

*Note: Accessing this library in the package uses the preface `DnD` for simplicity.*

- Aarakocra
- Aasimer
- Bugbear
- Centaur
- Changeling
- Dragonborn
- Drow
- Duergar
- Dwarf
- Elf
- Fetchling
- Firbolg
- Genasi
- Gith
- Gnome
- Goblin
- Goliath
- Halfling
- Hobgoblin
- Human
- Half-Elf
- Half-Orc
- Kalashtar
- Kenku
- Kobold
- Lizardfolk
- Loxodon
- Minotaur
- Orc
- Shifter
- Simic Hybrid
- Svirfneblin
- Tabaxi
- Tiefling
- Tortle
- Triton
- Vedalken
- Warforged
- Yuan-ti

## Contributing

All are suggestions are welcome, and any additions you'd wish to make should be made as a Pull Request to the master branch.
There are a few things you need to do prior to making a pull request:

### Pull Request Checklist
- [ ] Unit test coverage added
- [ ] Black code format

#### Unit Test Coverage
This project uses pytest integrated with Tox to run unit tests.
To run unit test coverage and 

#### Black code formatting
This project is formatted automatically with [Black](https://black.readthedocs.io/en/latest/).
Prior to making a pull request, please format your code using the follow command:
`black --line-length=120 .`

#### Build Pipeline

Build Tarball

`python -m build --sdist .`

Publish via Twine

`python -m twine upload dist/FantasyNameGenerator-<Version #>.tar.gz`
