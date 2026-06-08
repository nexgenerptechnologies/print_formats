import os
from setuptools import setup, find_packages

install_requires = []
if os.path.exists("requirements.txt"):
    with open("requirements.txt") as f:
        install_requires = [r.strip() for r in f.read().strip().split("\n") if r.strip()]

setup(
    name="print_formats",
    version="0.0.1",
    description="Professional Print Formats for ERPNext",
    author="Marketplace Publisher",
    author_email="hello@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
