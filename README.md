# transkribus-export-cookiecutter

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template to export (and process) TEI/XML from Transkribus

## what is this for

Automagically export and upconvert data from [Transkribus](https://readcoop.eu/) collections into TEI/XML using [page2tei](https://github.com/dariok/page2tei) from @dariok and [acdh-transkribus-pyutils](https://github.com/acdh-oeaw/acdh-transkribus-utils).


## Quickstart
* Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.7.0 or higher) by running `pip install -U cookiecutter`
* To generate a new to export (and process) TEI/XML from Transkribus project run `cookiecutter gh:acdh-oeaw/transkribus-export-cookiecutter` and answer the following questions, see below:

```json
{
    "projcet_name": "Transkribus Export",  // some eyecandy, used only in the created repo's REAMDE.md
    "directory_name": "transkribus-out", // the name of the directory cookiecutter will create the export-repo
    "col_id": 1234567 // the id of the/a collection to export, can be changed later any time
} 
```
* change into the new created repo, by default `transkribus-out`
* follow the instructions of the README.me located in `transkribus-out/README.md`