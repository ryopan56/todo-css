# setup.py

import os
from flask_todo import create_app


flask_todo_app = create_app()

if __name__ == '__main__':
    debug = os.getenv("APP_DEBUG", "0") == "1"
    host = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_RUN_PORT", 5000))
    flask_todo_app.run(debug=debug, host='0.0.0.0')
