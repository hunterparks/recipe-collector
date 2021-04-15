# Recipe Collector API

## Setup

### Prerequisites

Please ensure the following are installed:

* Python
* Virtualenv

### (One-time) Virtualenv Set Up

Run `virtalenv -p python3 venv`

### Pip Requirements

Run `pip install -r requirements.txt`

## Development

1) Change directory into the `api` folder.

2) Activate virtualenv

    - `source ./venv/bin/activate`

3) Run project

    - `uvicorn main:app --reload`

When done, deactivate the virtualenv by running `deactivate`.