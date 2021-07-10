from re import S
import sys

from app import create_app
from models import db

app = create_app()

if __name__ == "__main__":
    if "db:migration" in sys.argv:
        db.create_all(app=app)
    elif "db:drop" in sys.argv:
        db.drop_all(app=app)
    elif "run:prod" in sys.argv:
        app.run("0.0.0.0", port=5000)
    elif "run:dev" in sys.argv:
        app.run("0.0.0.0", port=5000, debug=True)
