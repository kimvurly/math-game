# init is an imported file from the project folder
from website import create_app

app = create_app()

# only if we run this file, not import, will we execute this line
if __name__ == '__main__':
    # runs a flask application
    app.run(debug=True)