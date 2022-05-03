"""
https://packaging.python.org/en/latest/tutorials/packaging-projects/
markdown
"""


import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latestearthquake-Indonesia",
    version="0.0.1",
    author="hani mustika adi",
    author_email="mustikahani@yahoo.com",
    description="his package will get the latest earthquake from BMKG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hanimustikaadi/latest-indonesia-earthquake",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    #package_dir={"": "src"},
    #packages=setuptools.find_packages(where="src"),
    #package_dir={"": "src"},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
