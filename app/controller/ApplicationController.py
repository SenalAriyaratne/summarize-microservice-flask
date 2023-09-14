from flask import Flask , request
import jsonify


class Application:

    def __init__(self, approutes, modelbuilder):

        self.app = Flask(__name__)
        self.hf_model = modelbuilder.Model(model_path=r'X:\2023ProjectRepo\Summarize_Microservice\resources\led-large-book-summary')
        self.route_builder = approutes.RouteBuilder(self.app, self.hf_model)
    
    def run_application(self):
        self.app.run(debug=True)

    
        
