<div align="center">
  <h1>Campus Insider</h1>
</div>

## Project workflow

### Setting up your local development environment
```bash
mkdir campus_project && cd campus_project

# create python environment, project uses python3.10, Django 4.0
python -m venv env
source ./env/bin/activate

# get repo
git clone git@github.com:davidshindra/campusinsider.git

cd campusinsider
pip install -r requirements.txt
```

```txt
# .env
ENVIRONMENT=development
DATABASE_URL=postgresql://postgres@127.0.0.1:5432/campusinsider
SECRET_KEY=some_very_secret_key
ALLOWED_HOSTS=127.0.0.1
TINYFY_API_KEY=your_tinify_api_key
```
```sql
--setup db - postgresql
CREATE DATABASE campusinsider;
\c campusinsider
```

### Project structure
```
campus_project/                   <- Local wrapper directory, not tracked by git
├── campusinsider/                <- Project root (BASE_DIR) and git repository
│   ├── .git/
|   ├── apps/                     <- Contains all project apps
│   ├── manage.py
|   ├── static/                   <- static files
|   ├── src/                      <- development static files ie ts, scss
|   ├── templates/                <- templates
│   └── config/                   <- Project configuration, settings, wsgi, asgi
|       ├── settings/
|       |   ├── __init__.py
|       |   ├── base.py           <- Settings common to all environments
|       |   ├── development.py    <- Development specific settings
|       |   ├── production.py     <- Production specific settings
│       ├── __init__.py
│       ├── asgi.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
└── env/                          <- virtual environment
└── media/                        <- media files
```

## Git workflow

### Branching
#### long running branches
Never to be deleted

- **main** - This is the main production branch. No commits should be made directly to main, only merges with dev branch.
- **develop** - Preview, testing branch, were all development happens, its the parent of all short lived branches.
#### The short lived branches
These are to be deleted once work on them is done, all these are based off dev branch, or another short lived branch, not main ie `git branch feature/dark-mode develop`


- **feature/feat** - Work on a new feature ie `feature/dark-mode`.
- **fix/bug** - Fix a bug ie `fix/user-not-logging-in`.
- **branch** - Generic branch

### Committing
Commit

- Each commit should leave the application in a functional state, consider stashing changes if otherwise.
- Use imperative tone (ie Add page title).
- Capitalize the first letter of the the subject line.
- Don't end the subject line with a period.
- Use the commit message body to explain what and why, not how.