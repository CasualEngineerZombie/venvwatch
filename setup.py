from setuptools import setup, find_packages

setup(
    name='venvwatch',
    version='0.5',
    description='Automatically updates requirements.txt by watching your virtual environment for changes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Casual Engineer Zombie',
    author_email='py@casualzom.dev',
    packages=find_packages(),
    install_requires=[
        'watchdog',
    ],
    entry_points={
        'console_scripts': [
            'venvwatch = venvwatch.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
     project_urls={
        'Source': 'https://github.com/CasualEngineerZombie/venvwatch',
        'Tracker': 'https://github.com/CasualEngineerZombie/venvwatch/issues',
    },
)