from flask import Flask
app = Flask(__name__)
app.register_blueprint(user_pages)
app.config.from_object('config')
