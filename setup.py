from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()




__version_ = "0.0.0"

REPO_NAME = "Text_Summarizer_Project"

Author_User_Name = "Sijibomiaol"
SRC_REPO  = "textSummarizer"

Author_EMAIL = "aderinlewomoses@gmail.com"

setup(

    name= SRC_REPO, 
    version= __version_,
    author= Author_User_Name,
    author_email=Author_EMAIL,
    description= "A small python package for NLP app",
    long_description= long_description,
    long_description_content_type = "text/markdown",
    url=f"https://github.com/{Author_User_Name}/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/{Author_User_Name}/{REPO_NAME}"},
    package_dir= {"": "src"},
    packages= find_packages(where="src"),
    # install_requires = get_requirements('requirements.txt')
)


