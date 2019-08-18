# create project directory
#echo "creating project directory"
#mkdir my_todo_app
#cd my_todo_app

# we are using python 3
# setup python virtual environment
echo "setting up virtual environment"
python3 -m venv simpleclientserverenv


# activate virtual environment
echo "activating virtual environment"
. simpleclientserverenv/bin/activate

echo "virtual environment created successfully"

echo "install Flask"
pip install Flask flask_socketio

echo "--- Installed Successfully ---"


# command to deactivate virtual environment
#deactivate
