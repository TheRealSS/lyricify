from setuptools import setup, find_packages

with open('README.md') as f:
    _description_ = f.read()

_name_ = "lyricify"

setup(
    name=_name_,
    version="1.2",
    description="Spotify lyrics for Linux",
    long_description=_description_,
    url="https://github.com/TheRealSS/lyricify",
    author="Sharad Swaminathan",
    author_email="swaminathan.sharad@gmail.com",
    packages=find_packages(),
    package_data={_name_: ["img/*"]},
    include_package_data=True,
    install_requires=[
        "requests",
        "bs4",
    ],
    entry_points={
        "console_scripts": [
            "{0} = {0}.spotifyctl:main".format(_name_)
        ],
    }
)
