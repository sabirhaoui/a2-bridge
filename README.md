# a2-bridge

Integration foundation for AVEVA Unified Engineering and Aras.

The business scope, API versions, authentication methods, object mappings,
and direction of exchange must be confirmed before implementing adapters.
No vendor API calls or data writes are implemented yet.

## Quick start

Requires Python 3.11+ and Git. Run from this repository:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m a2_bridge --check-config
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Set `A2_AVEVA_BASE_URL` and
`A2_ARAS_BASE_URL` in your process environment for configuration validation.
`.env.example` documents settings; `.env` files are not automatically loaded.
Configuration validation does not contact either platform.

## Layout

```text
src/a2_bridge/
  adapters/          Vendor integration boundaries
  domain/            Shared engineering data model
  services/          Exchange orchestration
  config.py          Environment configuration
tests/               Offline unit tests
docs/                Architecture and discovery notes
config/              Example mapping configuration
scripts/             Local verification
.gitlab-ci.yml       Offline CI checks
```

## GitLab

Create a blank GitLab project named `a2-bridge` without an initial README.
Then run:

```powershell
git add .
git commit -m "Initialize a2-bridge foundation"
git remote add origin <gitlab-repository-url>
git push -u origin main
```

If the initializer already configured `origin`, skip `git remote add`.
Keep credentials out of source control; use your organization's approved
secret store or protected GitLab CI variables.
