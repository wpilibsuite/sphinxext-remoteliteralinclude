import setuptools
import subprocess

ret = subprocess.run("git describe --tags --abbrev=0", stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE, check=True, shell=True)
version = ret.stdout.decode("utf-8").strip()


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sphinxext-remoteliteralinclude",
    version=version,
    author="Eli Barnett, Dalton Smith",
    author_email="daltzsmith@gmail.com",
    description="Extending literalinclude to include remote URLs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wpilibsuite/sphinxext-remoteliteralinclude",
    packages=['sphinxext'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
