import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil.files import data_files

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
from sklearn.datasets import load_iris
import joblib

# Loading sklearn's built-in iris dataset
iris = load_iris()

@anvil.server.callable
def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
  model = joblib.load(data_files['knn.skmodel'])
  classification = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
  return iris.target_names[classification][0]