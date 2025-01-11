### Installing/Setup commands

## for server part

# create venv(virtual environment) and activate it

python -m venv .
Scripts/activate

# install all packages from requirement.txt

pip install -r requirements.txt

## for client part

# initialize npm

npm init [-y]

# install required packages

npm install

## Running/Execution Commands

# Go to server and activate the venv

add a 'Key.txt' file with your gemini key
cd server
Scripts/activate

# Run the server

py main.py

# You may check/test the server at

localhost:8000/ping
localhost:8000/docs

# Go to client and run the client

cd client
cd gemini-frontend
npm run dev

# got to localhost:5173

# Enter your question and see the response
