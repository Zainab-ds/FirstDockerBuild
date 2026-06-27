# host:
# Tells Flask where to listen for incoming requests.

# host="0.0.0.0":
# Listen on all network interfaces.
# Allows your app to be accessed from your computer,
# other devices on the same network (if allowed),
# and Docker.

# port:
# Tells Flask which port (door number) to use.

# port=5000:
# Flask will run on port 5000.
# Open it in your browser using:
# http://localhost:5000
# or
# http://<your_ipv4_address>:5000

from flask import Flask

appe= Flask(__name__)

@appe.route("/")
def home():
    return "🚀 My first Docker image is finally running! After a lot of learning, debugging, and persistence, I made it. Every error taught me something new. On to the next challenge "

if __name__ == "__main__":
    appe.run(
        host="0.0.0.0",   # Listen on all network interfaces
        port=5000,        # Run the app on port 5000
        debug=True        # Restart automatically when code changes
    )