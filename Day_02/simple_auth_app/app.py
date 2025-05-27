from flask import Flask
from auth import auth_bp
from protected import protected_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'  # Secret for JWT

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(protected_bp)

if __name__ == "__main__":
    app.run(debug=True)
