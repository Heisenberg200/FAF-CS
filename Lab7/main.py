from flask import Flask, render_template
from database import DatabaseConnection
from encryption import Encryption

app = Flask(__name__)
CRYPTO = Encryption()
DB = DatabaseConnection()


def get_value_by_key(key, user):
    encrypted_keys = ["email", "date_birth"]

    if key in encrypted_keys:
        val = CRYPTO.decrypt_data(user[key])
    else:
        val = user[key]

    return val


def get_final_data(data):
    final_data = []

    for user in data:
        obj = {}
        for key in user.keys():
            obj[key] = get_value_by_key(key, user)
        final_data.append(obj)

    return final_data


@app.route('/')
def all_users():
    data = DB.get_all_data()
    final_data = get_final_data(data)
    return render_template('index.html', users=final_data)


if __name__ == '__main__':
    app.run(port=3000)
