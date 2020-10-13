from setuptools import setup, find_packages

with open("README.md", 'r') as fh:
    long_description = fh.read()

setup(
    name="modern-greek-inflexion",
    version="0.1.1",
    description="Python 3 library for creating inflected forms for Modern Greek words",
    long_description_content_type="text/markdown",
    long_description=long_description,
    license="MIT",
    url="http://github.com/PicusZeus/modern-greek-inflexion",
    author="Krzysztof Hilman",
    author_email="picusdev@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    python_requires=">+3.6"
)
