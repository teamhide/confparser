# encoding: utf-8
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="confparser",
    version="0.1.6",
    author="teamhide",
    author_email="padocon@naver.com",
    description="Python config parser library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/teamhide/confparser",
    download_url='https://pypi.python.org/pypi/confparser',
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pyyaml==5.3.1',
    ],
    python_requires='>=3.4',
)
