from setuptools import setup

setup(
    name='flask_r',
    packages=['flask_r'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
 setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)