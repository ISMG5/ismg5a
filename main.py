from flask import Flask
import os
import psycopg2

app = Flask(__name__)

# conexión global (simple)
conn = psycopg2.connect(os.getenv("DATABASE_URL"))

@app.route("/")
def home():
    return "Hola, Railway 🚀"

@app.route("/db")
def test_db():
    try:
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        return f"PostgreSQL conectado: {version}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)