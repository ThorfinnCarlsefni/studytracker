from flask import Flask, send_from_directory

def run_server(web_dir):
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return send_from_directory(web_dir, 'index.html')
    
    @app.route('/<path:path>')
    def static_files(path):
        return send_from_directory(web_dir, path)
    
    print("Сервер запущен на http://127.0.0.1:5000")
    print("Нажмите Ctrl+C для остановки\n")
    
    app.run(host='127.0.0.1', port=5000, debug=False)