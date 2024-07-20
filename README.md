# SnapScrib
## How to contribute

1. Fork and clone the repository
2. Set up with Poetry:
   - Install Poetry: https://python-poetry.org/docs/#installation
   - Run `poetry install` in project root

3. Create a new branch: `git checkout -b feature-branch`
4. Make changes and commit
5. Push to your fork: `git push origin feature-branch`
6. Open a pull request

### Useful poetry commands

- Creates env and set up dependencies: `poetry install`
- Activate env: `poetry shell`
- Add dependency: `poetry add package-name`
- Remove dependency `poetry remove package-name`

Update `pyproject.toml` for new dependencies.