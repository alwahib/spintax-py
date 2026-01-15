"""Setup configuration for spintax-py library."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="spintax-py",
    version="1.0.0",
    author="aalwhaib",
    description="A combinatorial string generation library that creates all possible combinations from templates with variable elements",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aalwhaib/spintax-py",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
