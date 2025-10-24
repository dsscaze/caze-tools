from setuptools import setup, find_packages

setup(
    name="caze-tools",                # nome do pacote no PyPI (com hífen é ok)
    version="0.1.0",
    description="Command-line dev tools by Daniel Caze (dsscaze)",
    author="Daniel Caze",
    packages=find_packages(),
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "caze-tools=caze_tools.cli:main",   # comando global: caze-tools
            "cz=caze_tools.cli:main"
        ],
    },
    python_requires=">=3.8",
)
