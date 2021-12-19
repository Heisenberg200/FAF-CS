# Cryptography-and-Security-II
# Author: Corman Daniel


* Data Base connection:
...
class DatabaseConnection:
    def __init__(self):
        client = MongoClient(port=int(os.getenv('PORT')), username=os.getenv('USERNAME'),
                             password=os.getenv("PASSWORD"))
        self.db = client.application

    def get_all_data(self):
        return self.db.users.find({}, {"_id": 0})
...
* The Encryption:
...

class Encryption:

    def __init__(self):
        key = self.call_key()
        self.crypto = Fernet(key)

    @staticmethod
    def call_key():
        return open("pass.key", "rb").read()

    @staticmethod
    def write_key():
        key = Fernet.generate_key()

        with open("pass.key", "wb") as key_file:
            key_file.write(key)

    def encrypt_data(self, data):
        return self.crypto.encrypt(data.encode())

    def decrypt_data(self, data):
        return self.crypto.decrypt(data).decode()
...

* Main application

...
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
...

# Conclusion:
  During this laboratory I have created an application, that shows the sensible content from a database.