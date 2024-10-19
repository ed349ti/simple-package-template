from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",
    version="0.0.1",
    author="EdsonGermano",
    author_email="ed349.ti@gmail.com",
    description="Meu_Primeiro_Pacote_Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ed349ti/simple-package-template"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)
