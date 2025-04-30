from app import create_app

app = create_app()

if __name__ == "__main__":
    # convenient: python run.py
    app.run()