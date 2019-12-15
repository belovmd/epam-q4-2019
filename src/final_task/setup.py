import setuptools


setuptools.setup(
    name="rss-reader",
    license="MIT",
    version="0.4.0",
    author="Anastasiya Infarovich",
    author_email="ainfarovich@gmail.com",
    description="A pure Python rss reader",
    url="https://github.com/AnInf/epam-q4-2019/final_task",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": ["rss-reader=rss_reader.rss_reader:main"]
    },
)
