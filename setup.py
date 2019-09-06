import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sphinxcontrib-remoteliteralinclude",
    version="0.0.1",
    author="Eli Barnett, Dalton Smith",
    author_email="daltzsmith@gmail.com",
    description="Extending literalinclude to include remote URLs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daltz333/sphinxcontrib-remoteliteralinclude",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
