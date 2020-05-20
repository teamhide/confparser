# encoding: utf-8
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="confparser",
    version="0.1.0",
    author="teamhide",
    author_email="padocon@naver.com",
    description="Python config parser library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/teamhide/confparser",
    download_url='https://pypi.python.org/pypi/confparser',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pyyaml',
    ],
    dependency_links=[
        'git+https://github.com/yaml/pyyaml.git',
    ],
    python_requires='>=3.4',
)
