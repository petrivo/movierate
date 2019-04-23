from setuptools import setup, find_packages

setup(
    name='movierate',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        hello=cli.commands:hello
        start_app=cli.commands:start_app
        dbinit=cli.commands:dbinit
    ''',
)