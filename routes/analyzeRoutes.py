from flask import Blueprint
from controllers.analyzeController import analyze_text

# create blueprint
analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route("/analyze", methods=["GET"])
def analyze():
    return analyze_text() 
