from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="major-ds-312", # the name that you will install via pip
    version="1.0",
    author="Christopher Major",
    author_email="your@email.com",
    description="contains enlarge funtion",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/ChristopherMajor/major-ds-312",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)