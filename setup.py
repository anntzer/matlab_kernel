from distutils.version import LooseVersion
import setuptools
from setuptools import setup, find_packages


if LooseVersion(setuptools.__version__) < "40.1":
    raise ImportError("setuptools>=40.1 is required")


setup(
    name="imatlab",
    description="A Juyter kernel for MATLAB.",
    long_description=open("README.rst", encoding="utf-8").read(),
    author="Antony Lee",
    url="https://github.com/imatlab/imatlab",
    license="MIT",
    classifiers=[
        "Framework :: IPython",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Shells",
    ],
    packages=find_packages("lib"),
    package_dir={"": "lib"},
    package_data={"imatlab": ["data/imatlab_export_fig.m", "data/matlab.tpl"]},
    python_requires=">=3.5",
    setup_requires=["setuptools_scm"],
    use_scm_version=lambda: {
        "version_scheme": "post-release",
        "local_scheme": "node-and-date",
    },
    install_requires=[
        "ipykernel>=4.1",  # Current version of --user install.
        "matlabengineforpython>=R2016b",  # Not PyPI installable.
        "importlib_metadata; python_version<'3.8'",
    ],
    entry_points={
        "nbconvert.exporters": [
            "matlab = imatlab._exporter:MatlabExporter",
        ],
    },
)
