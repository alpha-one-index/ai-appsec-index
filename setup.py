from setuptools import setup, find_packages

setup(
    name="ai-appsec-index",
    version="1.0.0",
    description="The definitive open-source reference for AI-augmented application security",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Alpha One Index",
    url="https://github.com/alpha-one-index/ai-appsec-index",
    project_urls={
        "Documentation": "https://alpha-one-index.github.io/ai-appsec-index/",
        "Kaggle": "https://www.kaggle.com/datasets/alphaoneindex/ai-appsec-index",
        "Issues": "https://github.com/alpha-one-index/ai-appsec-index/issues",
    },
    packages=find_packages(),
    package_data={"ai_appsec_index": ["data/*.json", "kaggle/*.csv"]},
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Security",
        "Topic :: Software Development :: Quality Assurance",
    ],
    keywords="appsec ai security vulnerability cve aspm benchmark false-positive cra",
)
