import sqlite3
import logging
import sys

from flask import (
    Flask,
    jsonify,
    json,
    render_template,
    request,
    url_for,
    redirect,
    flash,
)
from werkzeug.exceptions import abort

# Define the Flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = "your secret key"
app.config["conn_count"] = 0

##########################################
#            HELPER FUNCTIONS            #
##########################################


def get_db_connection():
    """This function connects to database with the name database.db."""

    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row

    app.config["conn_count"] = app.config["conn_count"] + 1
    return connection


def get_post(post_id):
    """Function to get a post using its ID."""

    connection = get_db_connection()
    post = connection.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    connection.close()

    return post


##########################################
#               APP ROUTES               #
##########################################


@app.route("/")
def index():
    """Define the main route of the web application."""

    connection = get_db_connection()
    posts = connection.execute("SELECT * FROM posts").fetchall()
    connection.close()
    return render_template("index.html", posts=posts)


@app.route("/<int:post_id>")
def post(post_id):
    """
        Define how each individual article is rendered.
        If the post ID is not found a 404 page is shown.
    """

    post = get_post(post_id)
    if post is None:
        app.logger.error(f"Article with ID: {post_id} does not exist!")
        return render_template("404.html"), 404
    else:
        post_title = post["title"]
        app.logger.info(f'Article with title: "{post_title}" retrieved!')
        return render_template("post.html", post=post)


@app.route("/about")
def about():
    """Define the About Us page."""

    app.logger.info(f"About page accessed!")
    return render_template("about.html")


@app.route("/create", methods=("GET", "POST"))
def create():
    """Define the post creation functionality."""

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title:
            flash("Title is required!")
        else:
            connection = get_db_connection()
            connection.execute(
                "INSERT INTO posts (title, content) VALUES (?, ?)", (title, content)
            )
            connection.commit()
            connection.close()

            app.logger.info(f'Article with title: "{title}" created!')
            return redirect(url_for("index"))

    return render_template("create.html")


@app.route("/healthz")
def healthz():
    """Define the health check endpoint."""

    try:
        connection = get_db_connection()
        connection.execute("SELECT * FROM posts").fetchall()
        connection.close()

        response = app.response_class(
            response=json.dumps({"result": "OK - healthy"}),
            status=200,
            mimetype="application/json",
        )
    except sqlite3.OperationalError:
        response = app.response_class(
            response=json.dumps({"result": "ERROR - unhealthy"}),
            status=500,
            mimetype="application/json",
        )

    return response


@app.route("/metrics")
def metrics():
    """Define metrics endpoint."""

    connection = get_db_connection()
    posts = connection.execute("SELECT * FROM posts").fetchall()
    connection.close()

    response = app.response_class(
        response=json.dumps(
            {"db_connection_count": app.config["conn_count"], "post_count": len(posts)}
        ),
        status=200,
        mimetype="application/json",
    )

    return response


##########################################
#                 RUN APP                #
##########################################

# start the application on port 3111
if __name__ == "__main__":
    # set logger to handle STDOUT and STDERR
    stdout_handler = logging.StreamHandler(sys.stdout)
    stderr_handler = logging.StreamHandler(sys.stderr)
    handlers = [stderr_handler, stdout_handler]

    format_output = "%(levelname)s:%(name)s:%(asctime)s, %(message)s"

    logging.basicConfig(
        format=format_output, level=logging.DEBUG, handlers=handlers,
    )
    app.run(host="0.0.0.0", port="3111")
