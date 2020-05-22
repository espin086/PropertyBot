
"""
Setting up as a package
For additional information on how to set up
a package please read this post on Medium:
https://medium.com/@manivannan_data/create-python-package-to-your-python-code-28a1bde4ec51
"""


import setuptools

setuptools.setup(
    name='PropertyBot',
    version='0.0.1',
    author='JJ Espinoza',
    author_email='jj.espinoza.la@gmail.com',
    description="Automates real estate investing",
    url="https://github.com/espin086/JobHunter",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language:: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    )


)


