from setuptools import setup, find_packages

requirements = [
    "requests",
    "websocket-client==1.3.1", 
    "setuptools", 
    "json_minify", 
    "six",
    "aiohttp",
    "websockets"
]

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name="aminoxii",
    license="MIT",
    author="Aimou90",
    version="0.1",
    author_email="aimouu26@gmail.com",
    description="Library for Amino. Discord. ",
    url="https://github.com/Aimou90/aminoxii",
    packages=find_packages(),
    long_description=long_description,
    install_requires=requirements,
    keywords=[
        'aminoapps',
        'aminoxii',
        'amino',
        'amino-bot',
        'narvii',
        'api',
        'python',
        'python3',
        'python3.x',
 
    ],
    python_requires='>=3.6',
)
