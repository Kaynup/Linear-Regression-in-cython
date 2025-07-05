from setuptools import setup, Extension
from Cython.Build import cythonize

module = Extension(
    name="LR_v1.linear_regressor", 
    sources=["LR_v1/linear_regressor.pyx"], 
    language="c++",
    extra_compile_args=["-std=c++17"],
)

setup(
    name="LR_v1",
    version="1.0.0",
    packages=["LR_v1"],
    ext_modules=cythonize(module, compiler_directives={"language_level": 3})
)