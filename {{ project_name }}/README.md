# {{ project_name }}

## Setup

1. `pipenv install --dev`

## Running the app

{% if target == "commandline" -%}
Run `pipenv run cli`

This refers to the `cli` script defined in `Pipfile`.
{% else -%}
Run `env FLASK_APP={{ project_name }}/api.py pipenv run flask run`
{% endif %}

## Testing

Run `pipenv run test`
