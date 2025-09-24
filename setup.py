from setuptools import setup, find_packages

setup(
    name="calculator-app",            # package name
    version="0.1.0",                  # version
    description="A simple Flask-based calculator",
    author="Your Name",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
    ],
    entry_points={
        "console_scripts": [
            "calculator=calculator.app:app.run",  
        ],
    },
)
