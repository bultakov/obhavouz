import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ObHavoUz",
    version="1.0",
    author="Bultakov Ibrohim",
    author_email="bii23.uz@gmail.com",
    description="ObHavoUz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bultakov/obhavouz",
    packages=setuptools.find_packages(),
    install_requires=[
        'aiohttp',
        'bs4'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
