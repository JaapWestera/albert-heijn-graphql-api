import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='appy_graphql',
    version='0.1.0',
    author="Jaap Westera",
    author_email="jaap@305.nl",
    description="Python API for Albert Heijn using its (internal?) GraphQL API",
    long_description=long_description,
    install_requires=[
        'requests',
        'aiohttp'
    ],
    long_description_content_type="text/markdown",
    url="https://github.com/JaapWestera/appy-graphql",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)