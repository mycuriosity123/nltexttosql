from setuptools import find_packages, setup

setup(
    name = 'NLTOSQL AI Project',
    version= '0.1.0',
    author= 'kiran',
    author_email= 'saip89199@gmail.com',
    description="Convert natural language text to sql query",
    packages= find_packages(),
    install_requires = [],
    python_requires=">=3.9",
       entry_points={
        "console_scripts": [
            "run_my_flask_app = src.app:run_app", 
        ],
    },
    include_package_data=True,

)