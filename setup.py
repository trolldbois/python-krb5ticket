import os

from setuptools import setup, find_packages


version = "1.0.4"

setup(
    name="python-krb5ticket",
    version=version,
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "gssapi",
        "pandas"
    ],
    author="Deric Degagne",
    author_email="deric.degagne@gmail.com",
    description="Simple Python wrapper to create Kerberos ticket-granting tickets (TGT)",
    url="https://github.com/degagne/python-krb5ticket",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.6",
)
