[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# General Information


This repository holds the basic directory layout for new python projects as a template for [cookiecutter](https://www.cookiecutter.io/). Additional to a reasonable minimum of features (setup.py, requirements.txt, directory structure, ...) it contains the following extras:

- basic unittest
- `script.py` and associated entrypoint in `pyproject.toml` (allows to call some functionality of the package directly from command line (try `{{ cookiecutter.project_name }} cmd1`))


## Usage

- Install cookiecutter e.g. via `pip install cookiecutter`
- Go to the directory where you want to create the new package
- Run `cookiecutter <path-to-this-template-repo>`
- Check `pyproject.toml`.
- Add your source. a) Either to [`core.py`](src/{{ cookiecutter.project_name }}/core.py) or b) to your own separate file(s).
    - a) simplifies importing your module
    - b) is more flexible but you have to take care of importability yourself.


For local development it is recommended to install your package in [editable mode](https://pip.pypa.io/en/latest/cli/pip_wheel/?highlight=editable#cmdoption-e): `pip install -e .` (run from where `pyproject.toml` lives).


## Testing

Run `pytest` in the root directory of the package (where `pyproject.toml` lives).
Use `pytest -s` to disable input and output suppression (i.e. see the output of your code)
Use `pytest -k _01` to execute only testcases containing the substring "_01".

## Publishing on pypi

To publish your package on [Python Package Index (pypi)](pypi.org/) the following commands should work:

- Install necessary tooling: `pip install build setuptools_scm twine`
- create the uploadable pack: `rm -rf dist/*; python3 -m build`
- Register a username on <https://pypi.org/>
- upload package: `twine upload -r pypi dist/*`
    - use this for testing `twine upload -r testpypi dist/*`



