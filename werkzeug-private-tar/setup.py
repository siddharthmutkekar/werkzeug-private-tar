import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="werkzeug_private_tar",
    version="2.3.3",
    author="Siddharth Mutkekar",
    author_email="siddharthmutkekar@in.ibm.com",
    description="A function that returns 'world'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/siddharthmutkekar/werkzeug-private-tar",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)