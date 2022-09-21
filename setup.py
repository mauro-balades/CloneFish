from setuptools import setup

with open("clonefish/__version__.py") as f:
    info = {}
    for line in f.readlines():
        if line.startswith("version"):
            exec(line, info)
            break

setup(
    name="CloneFish",
    version=info["version"],
    description="Clone any website and convert it into a phishing website.",
    author="Mauro Balades",
    author_email="mauro.balades@tutanota.com",
    url="https://github.com/mauro-balades/CloneFish",
    packages=["clonefish"],
    requirements=[
        "hiurlparser",
        "Jinja2",
        "falcon",
        "minify-html",
    ],
    entry_points = {
          'console_scripts': [
              'clonefish = package.module:main',                  
          ],              
      },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
