from routes.analyzeRoutes import analyze_bp

def register_blueprints(app):
    app.register_blueprint(analyze_bp, url_prefix="/api")
