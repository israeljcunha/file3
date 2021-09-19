import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="file3",
    version="0.0.1",
    author="Israel Cunha",
    author_email="ms.israel.cunha@gmail.com",
    keywords='file files',
    description="Converting Files and Types (IntToBin, IntToHex, CharToASCII, CharToHex, BinStrToDecimal, HexToInt, IntToByte, StrToHex, StrToBytes, StrToASCII, StrToBin)n",
    license='Python License',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/israeljcunha/file3",
    packages=setuptools.find_packages(exclude=['venv','file-test-env']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
