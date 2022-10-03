from flaskr_admin import create_app

app = create_app()

if __name__ == "__main__":
    print(f'flask app created')
    app.run()
