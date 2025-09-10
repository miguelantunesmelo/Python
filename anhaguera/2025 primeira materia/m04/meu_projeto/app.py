from flask import Flask
from routes.main import main_bp

app = Flask(__name__)

# Registra o blueprint das rotas principais
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
