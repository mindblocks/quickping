
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quickping",
    version="1.0.0",
    author="Sajjad Jawad",
    author_email="iamsajjad@mail.ru",
    description="Using Multi-Threads to find active IPv4 addresses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache License 2.0',
    #url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

