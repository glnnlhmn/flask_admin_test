from flaskr_admin import create_app, admin, db
from model2 import User
from flask_admin.contrib.sqla import ModelView

app = create_app()

admin.add_view(ModelView(User, db.session))

if __name__ == "__main__":
    print(f'flask app created')
    app.run(debug=True)
