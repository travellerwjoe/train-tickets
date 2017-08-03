from setuptools import setup

setup(
    name='trainTickets',
    py_modules=['trainTickets', 'stations', 'trainsCollection'],
    install_requires=['requests', 'colorama', 'docopt', 'prettytable'],
    entry_points={
        'console_scripts': ['train-tickets=trainTickets:cli']
    }
)
