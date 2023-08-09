from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding='UTF-8') as f:
    README = f.read()

setup(
    name="FantasyNameGenerator",
    version="0.0.4",
    description="A name generator from various worlds of fantasy",
    long_description=README,
    long_description_content_type="text/markdown",
    project_urls={
        "Source": "https://github.com/Dude036/FantasyNameGenerator",
    },
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 2 - Pre-Alpha"
    ],
)
