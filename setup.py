from setuptools import find_packages, setup
from pathlib import Path

this_path = Path(__file__).parent

readme_path = this_path / "README.md"

long_description = readme_path.read_text(encoding="utf-8")

setup(
    name="doeloe",
    version="0.0.1",
    description="A tool to convert old Indonesian language into EYD (Ejaan yang Disempurnakan)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="David Samuel",
    author_email="davidsamuel.7878@gmail.com",
    url="https://github.com/bookbot-hive/doeloe",
    license="Apache License",
    packages=find_packages(),
    include_package_data=True,
    platforms=["linux", "unix", "windows"],
)
