from setuptools import find_packages, setup

LATEST_VERSION = "0.14.0"

exclude_packages = [
    "selenium",
    "webdriver",
    "fastapi",
    "fastapi.*",
    "uvicorn",
    "jinja2",
    "gpt-researcher",
    "langgraph"
]

with open(r"README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    reqs = [line.strip() for line in f if not any(pkg in line for pkg in exclude_packages)]

setup(
    name="gpt-researcher",
    version=LATEST_VERSION,
    description="GPT Researcher is an autonomous agent designed for comprehensive web research on any task",
    package_dir={'gpt_researcher': 'gpt_researcher'},
    packages=find_packages(exclude=exclude_packages),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/assafelovic/gpt-researcher",
    author="Assaf Elovic",
    author_email="assaf.elovic@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.11',
    install_requires=reqs,
    entry_points={
        "console_scripts": [
            "gpt-researcher=gpt_researcher.cli:entrypoint",
        ]
    },


)