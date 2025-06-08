import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "chickenDiseaseClassification"
AUTHOR_NAME = "Harshith Reddy Gundra"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "gundraharshith15@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN application specifically for chicken disease classification",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/HarshithReddyG/chickenDiseaseClassification",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)