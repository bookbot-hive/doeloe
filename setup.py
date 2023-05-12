from setuptools import find_packages, setup

setup(
    name="doeloe",
    version="0.0.1",
    description="A tool to convert old Indonesian language into EYD (Ejaan yang Disempurnakan)",
    author="David Samuel",
    author_email="davidsamuel.7878@gmail.com",
    url="https://github.com/bookbot-hive/doeloe",
    license="Apache License",
    packages=find_packages(),
    include_package_data=True,
    platforms=["linux", "unix", "windows"],
)
