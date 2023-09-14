from flask import Flask
import jsonify

class RouteBuilder():

    def __init__(self, application, hfmodel):
        self.build_routes(app=application)
        self.hf_model = hfmodel

    def build_routes(self,app):

        @app.route('/')
        def hello_summarizer():
            return "message' :'This is a text summarizer"
            
        

        @app.route('/health/', methods=["GET"])
        def health_check(self):
            return jsonify(status = "UP")
        
        @app.route('/summarize_text/', methods=["POST"])
        def post_summarize():
            try:
                data = request.get_json()
                if data:
                    result = self.hf_model.model_serve(text_to_summarize=data)
                    return jsonify({
                        'message': 'Received POST data to summarize',
                        'data' : result
                    })
                else:
                    return jsonify({
                        'message' : 'No data received to summarize'
                    }), 400
            except error:
                print(f"Error enountered trying to complete summarize request . : Error Message :>: {error}")
