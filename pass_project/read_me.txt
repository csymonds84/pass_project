set FLASK_APP=app    (app name)
set FLASK_ENV=development
flask run

gitBash
export FLASK_APP=app      (app name you used)
export FLASK_ENV=development
flask run

-- to setup the venv --
py -3 -m venv .venv
.venv\scripts\activate

then pip installs