from setuptools import setup

setup(
    name="mycos",
    version="0.1",
    packages=["my_utils"],
    install_requires=["numpy"],
    entry_points={
    "console_scripts": [
        "mycos = my_utils.my_utils:main",
    ],
},
)
