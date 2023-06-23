from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Harsh@2002',
    database='Temp'
)

def get_word_from_db():
    cursor = db.cursor()
    cursor.execute('SELECT word FROM config')
    result = cursor.fetchone()
    return result[0] if result else ''

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the API home page! To acess the api please go to /api/test. And to acess the admin please go to /admin."

@app.route('/api/test', methods=['GET'])
def get_test():
    word = get_word_from_db()
    return jsonify({'test': word})

@app.route('/admin', methods=['GET', 'POST'])
def admin_panel():
    if request.method == 'POST':
        new_word = request.form.get('word')
        cursor = db.cursor()
        cursor.execute('UPDATE config SET word=%s', (new_word,))
        db.commit()
    word = get_word_from_db()
    return '''
        <form method="post">
            <label for="word">New Word:</label>
            <input type="text" id="word" name="word" value="{word}">
            <input type="submit" value="Submit">
        </form>
    '''.format(word=word)

if __name__ == '__main__':
    app.run()
