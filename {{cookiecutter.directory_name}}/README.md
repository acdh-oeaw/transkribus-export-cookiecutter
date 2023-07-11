# {{cookiecutter.directory_name}}-transkribus-export

Automagically export and upconvert data from [Transkribus](https://readcoop.eu/) collections into TEI/XML using [page2tei](https://github.com/dariok/page2tei) from @dariok and [acdh-transkribus-pyutils](https://github.com/acdh-oeaw/acdh-transkribus-utils).

## initial (local) set up

* create a virtual environment `python -m venv venv`
* update pip to latest version and install needed python packages `pip install -U pip && pip install -r requirements.txt`
* copy/rename `dummy.env` to `secret.env` and add your Transkribus credentials
* clone (tei2html-repo)[https://github.com/dariok/page2tei] by @dariok `git clone --depth=1 --branch master --single-branch https://github.com/dariok/page2tei.git`

## export the data

* add the Transkribus collection IDs to `./col_ids.txt` (each ID on a new line)
run `./export_env_variables.sh` to set your Transkribus credentials as environment variables.
* run `python dump_data.py`


## GitHub-Actions

* Create GitHub secrets called `TR_USER` and `TR_PW` and add your Transkribus credentials

* Go to GitHub Actions and start the workflow -> the exported METS and TEI/XML files will be checked into your repo