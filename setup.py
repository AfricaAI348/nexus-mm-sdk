from setuptools import setup, find_packages

setup(
    name="nexus-mm-sdk",
    version="8.1.1",
    author="Daniel (daniel.engineers)",
    author_email="support@nexusmm.site",
    description="Official Python SDK wrapper for the NEXUS-MM Physics-Grounded World Model.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://nexusmm.site",
    packages=find_packages(),
    install_packages=["requests>=2.25.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.7",
)
