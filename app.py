import gunicorn.glogging

from api import api

if __name__ == "__main__":
    api.run(host='0.0.0.0')