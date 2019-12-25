from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    lic = f.read()

setup(
    name="pi_light",
    version="0.1",
    description="Simple project to control Philips Hue lights via Raspberry Pi",
    long_description=readme,
    author="Chris Kittl",
    author_email="chris.kittl@tu-dortmund.de",
    url="https://github.com/ckittl/piLight",
    license=lic,
    packages=find_packages()
)
