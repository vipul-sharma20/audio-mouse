import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="audio-mouse",
    version="1.0.1",
    author="Vipul Sharma",
    author_email="vipul.sharma20@gmail.com",
    description="Control mouse with audio input",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vipul-sharma20/audio-mouse",
    packages=setuptools.find_packages(),
    install_requires=["numpy", "aubio", "pyaudio", "autopy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
