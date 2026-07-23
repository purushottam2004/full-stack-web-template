# Template Supabase Setup

## First Time Setup

### Pre-requisites

- Docker Daemon Should Be Running
- Python>=3.13 Should be Present

### Setup Guide

```bash
# Installing the CLI
# Install from homebrew via the official supabase tap as recommended on the supabase documentation
brew install supabase/tap/supabase

# Starting the Containers
# Note: If starting for the first time, it will pull the images of respective containers and may take longer time than usual start
# Move to the supabase directory
cd supabase
# Start the containers
supabase start
# Few variables will be shown on the terminal as the output from the above command. Store these, as they will be used as environment variables for the supabase itself as well as the backend and frontend

# Copying the .env.example file
cp .env.example .env
# Paste the outputs of the 'supabase start' command into the .env file

# By default 'supabase start' command seeds any data from the sql files inside the supabase/seeds folder if exits
# Apart from the sql seed files, there are data seeding python files in the folder supabase/python_seeds

# Creating virtual Environment for Using the Pythonic Seed Scripts
python -m venv venv
# Activate this environment (linux and mac)
source ./venv/bin/activate
# Installing the pre-req libs for seedig
pip install -r requirements.txt
# Seeding the pythonic scripts
python seed.py

