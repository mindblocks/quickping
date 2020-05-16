
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quickping",
    version="1.3.0",
    author="Sajjad Jawad",
    author_email="iamsajjad@mail.ru",
    description="Using Multi-Threads to find active IPv4 addresses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache License 2.0',
    url="https://github.com/sajjadlab/quickping.git",
    packages=setuptools.find_packages(),
    install_requires=[
        'Click',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        quickping=cli.cLI:cLI
    ''',
    python_requires='>=3.6',
)

