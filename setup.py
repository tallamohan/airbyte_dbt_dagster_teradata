from setuptools import find_packages, setup

setup(
    name="airbyte-dbt-dagster-teradata",
    packages=find_packages(),
    install_requires=[
        "dbt-teradata==1.8.0",
        "dbt-core",
        "dagster==1.7.9",
        "dagster-webserver==1.7.9",
        "dagster-dbt==0.23.9",
        "dagster-airbyte==0.23.9",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)