import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


    __version__= "0.0.0"

    REPO_NAME = "textsummarizer"
    AUTHOR_USER_NAME = "harshitasinhaa"
    SRC_REPO = "textsummarizer"
    AUTHOR_EMAIL = "getharshitasinhaa11@gmail.com"

    setuptools.setup(
        name="textsummarizer",
        version=__version__,
        author="harshitasinhaa",
        author_email="getharshitasinhaa11@gmail.com",
        description="A small python pacakage for NLP app",
        long_description=long_description,
        long_description_content="text/markdown",
        url=f"https://github.com/harshitasinhaa/textsummarizer",
        project_urls={
            "Bug Tracker": f"https://github.com/harshitasinhaa/textsummarizer/issues",
        },
        package_dir={"", "src"},
        packages=setuptools.find_packages(where="src")


    )