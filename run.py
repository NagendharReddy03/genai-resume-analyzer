from app import create_app

app = create_app()

if __name__ == "__main__":
    # by default, host="127.0.0.1", port=5000
    app.run(host="0.0.0.0", port=5000, debug=True)