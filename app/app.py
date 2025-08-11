from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='mysql-service',
        user='root',
        password='password',
        database='mydb'
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        item = request.form['item']
        cursor.execute("INSERT INTO items (name) VALUES (%s)", (item,))
        conn.commit()

    cursor.execute("SELECT name FROM items")
    items = cursor.fetchall()
    cursor.close()
    conn.close()

    html = '''
    <form method="post">
      <input name="item" placeholder="Add item" />
      <button type="submit">Add</button>
    </form>
    <ul>
      {% for item in items %}
        <li>{{ item[0] }}</li>
      {% endfor %}
    </ul>
    '''
    return render_template_string(html, items=items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
