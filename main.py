# file: /0XY_healthcare_data_analysis/main.py

from backend import create_app
import os

app = create_app()

port = int(os.environ.get("PORT", 5000))

if __name__=='__main__':
    app.run(host='0.0.0.0', port=port, debug = False)