# transkribus-export-cookiecutter

# DSE-Static-Cookiecutter

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template to export (and process) TEI/XML from Transkribus

## what is this for

The current repo should ease the process of setting up an export (and process) TEI/XML from Transkribus workflow

## Quickstart
* Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.7.0 or higher) by running `pip install -U cookiecutter`
* To generate a new to export (and process) TEI/XML from Transkribus project run `cookiecutter gh:acdh-oeaw/transkribus-export-cookiecutter` and answer the following questions, see below:

```json
{
    "directory_name": "transkribus-out",
} 
```
* change into the new created repo, by default `$ transkribus-out`
* create a virtual env
* install requierements `pip install -r requirements.txt`
* add/modfiy environment-variables in `env.default`, rename it into e.g. `env.secret`
* change `set_env_varibales.sh` so it uses your actual env-file