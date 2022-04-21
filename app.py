from flask import request, jsonify, Blueprint

from flask import Flask


from database import setup
from database import tasks
from datetime import datetime
from resources.task import tasks_bp

app = Flask(__name__)
setup.create_tables()


@app.before_first_request
def create_tables():
    setup.create_tables()


app.register_blueprint(tasks_bp)


if __name__ == '__main__':
    app.run(debug=True)     # Para que el archivo corra
    


# Para pasar datos a url se usan argumentoss
# En método put http://127.0.0.1:5000/tasks?id=2