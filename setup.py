from setuptools import setup

setup(
    name="filemoon",
    version="0.2.2",
    description="Unofficial python api wrapper from https://filemoon.sx/api",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    keywords="api, filemoon, video, hosting",
    url="https://github.com/BalaPriyan/filemoon",
    author="balapriyan",
    author_email="balapriyanbalusamy@gmail.com",
    packages=["filemoon"],
    install_requires=["requests",],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
    ],
    zip_safe=False,
)
