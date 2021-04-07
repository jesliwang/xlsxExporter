import setuptools
from xlsx2lua import __version__ as version

setuptools.setup(
    name = "xlsx2lua",
    packages = setuptools.find_packages(),
    include_package_data = True,
    version = version,
    author = "Jianhong Wang",
    description="A tool to convert xlsx",
    install_requires=[
        "openpyxl"
    ]
)