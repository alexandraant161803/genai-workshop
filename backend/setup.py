#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages


setup(
    author="Netlight",
    author_email="aumb@netlight.com",
    python_requires=">=3.9",
    description="API for Netlight GenAI workshop",
    keywords="gen_ai_workshop_api",
    name="gen_ai_workshop_api",
    packages=find_packages(include=["gen_ai_workshop_api", "gen_ai_workshop_api.*"]),
    version="1.0.0",
    zip_safe=False,
)
