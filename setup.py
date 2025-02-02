#!/usr/bin/env python3

import getpass
import os

def _set_env(var: str):
    # Check if the variable is already set in the environment
    if not os.environ.get(var):
        # Prompt the user for the value securely
        value = getpass.getpass(f'Enter {var}:')
        
        # Set the environment variable for the current session
        os.environ[var] = value
        
        # Save it to a .env file to persist across sessions
        with open('.env', 'a') as env_file:
            env_file.write(f'{var}={value}\n')
        print(f'{var} has been set and saved to .env')

_set_env("OPENAI_API_KEY")

