# Workflow

This document describes the development workflow for the project.

## Branching Strategy
- Use `main` for stable releases.
- Use `dev` for ongoing development.
- Feature branches: `feature/<name>`
- Bugfix branches: `bugfix/<name>`
- Pull requests must target `dev` unless hotfixing production.

## CI/CD Pipelines
- GitHub Actions run on push and pull request.
- Workflows: `build.yml`, `test.yml`, `deploy.yml`.
- Automated tests and linting required for all PRs.
- Deployment is triggered from `main` branch.

## Code Review Process
- All code changes require PRs and at least one approval.
- Use issue templates for bug reports and feature requests.
- Reviewers check for style, documentation, and test coverage.

## Automation
- Scripts in `scripts/` automate build, test, and deployment.
- Pre-commit hooks for linting and formatting.

## Documentation
- Update `CHANGELOG.md` for every release.
- Keep `README.md` and `docs/` up to date.
