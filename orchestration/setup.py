from setuptools import find_packages, setup

setup(
    name="orchestration",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-teradata<1.9",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)