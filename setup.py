from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pip-migrate",
    version="1.0",
    author="Rohaan Ahmed",
    author_email="silent.death3500@gmail.com",
    description="A tool to backup and migrate Python packages",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "pip-migrate = pip_migrate.pip_migrate:main",
        ],
    },
    install_requires=["setuptools", "wheel", "progress"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.6",
    url="https://github.com/crushr3sist/pip-migrate",
    keywords="pip migrate backup restore python packages utility tool",
)
