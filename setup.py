from setuptools import setup, find_packages

setup(
    name="powerpy",
    version="0.1.0",
    description="A collection of constructs for Python3",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jacopodl/powerpy",
    author="Jacopo De Luca",
    author_email="jacopo.delu@gmail.com",
    license="MIT",
    keywords=["awesome", "library", "patterns", "constructs"],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ])
