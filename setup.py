import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="glslsyntax",
    version="0.0.1",
    author="Neylz",
    author_email="contact@neylz.dev",
    license='MIT',
    description="Imports GLSL Vector and Matrix notations in python with somme extra features.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['GLSL', 'VECTORS', 'VECTOR', 'MATRIX', 'MATRICES'],
    url="https://github.com/Neylz/GlslSyntax",
    project_urls={
        "Bug Tracker": "https://github.com/Neylz/GlslSyntax/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    packages=['glslsyntax'],
    python_requires=">=3.10"
)
