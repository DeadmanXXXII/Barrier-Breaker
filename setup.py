from setuptools import setup, find_packages

setup(
    name="barrier-breaker",
    version="0.1.0",
    author="DeadmanXXXII",
    author_email="themadhattersplayground@gmail.com",
    description="Barrier Breaker: A translation tool with improved accuracy.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DeadmanXXXII/Barrier-Breaker",
    packages=find_packages(),
    install_requires=open("requirements.txt").readlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
