import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="johtk",
    version="0.0.1",
    author="Johannes Dornheim",
    author_email="johannes.dornheim@mailbox.org",
    description="a collection of python tools and functions of great personal use (continuously developed)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johannes-dornheim/joh-tk.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.0",
    ],
    tests_require=["pytest>=6.1.0"],
)