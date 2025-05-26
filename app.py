import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")

# @app.route("/")
# def home():
#     return send_from_directory('templates', 'index.html')  # index.html ko templates folder me rakho

@app.route("/listings")
def get_listings():
    return send_from_directory('static', 'listings.json')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 👈 yeh line zaroori hai Render ke liye
    app.run(host='0.0.0.0', port=port)




# from flask import Flask, render_template, send_from_directory

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")  # static HTML serve karna

# @app.route("/listings")
# def get_listings():
#     return send_from_directory('static', 'listings.json')  # JSON data serve karna

# if __name__ == "__main__":
#     app.run(debug=True)
