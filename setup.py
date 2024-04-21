from setuptools import setup

setup(
    name='JaBebeu',
    version='1.0',
    packages=[''],
    url='',
    license='GNU',
    author='LuizQuirino',
    author_email='luizfpq@gmail.com',
    description='será que bebi agua?',
    install_requires=[
        'tk',
        'plyer'
    ],
    entry_points={
        'console_scripts': [
            'jabebeu = src.reminder_app:main'
        ]
    }
)
