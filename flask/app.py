from flask import Flask
from routes import urls_blueprint
import database

app = Flask(__name__)
app.register_blueprint(urls_blueprint)
database.init_db()


if __name__ == '__main__':
    # hw_relatorio(session)
    # app.run(debug=True, host='172.20.0.2', port=5000)
    app.run(debug=True,  host='172.20.0.5', port=5000)
