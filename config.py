import os
from dotenv import load_dotenv

load_dotenv()

env_variables = {
    "CLICKUP_API_KEY" : os.getenv( "CLICKUP_API_KEY"),
    "TEAM_ID" : os.getenv("TEAM_ID")
}