from flask import Flask
from flask_graphql import GraphQLView
from bd.reader import load_data
from api.schemas.schema import schema

load_data()

app = Flask(__name__)
app.add_url_rule(
    '/',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)
app.run(debug=True)