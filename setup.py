from setuptools import find_packages, setup

setup(
    name='DTAT_bot',
    version='0.4.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'discord.py-rw',
        'requests',
    ],
    setup_requires=[
        "pytest-runner",
    ],
    tests_require=[
        "pytest",
        "pytest-cov",
        "mock",
        "pytest-asyncio",
    ],
)