from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from os import path
app = Flask(__name__)

@app.route('/upload')
def upload_file():
    return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
    print("Uploader running!")
    if request.method == 'POST':
        print("****************")
        print(request)
        print("****************")
        for key in request.files:
            f = request.files[key]# ['file']
            print(request)
            print("****************")
            output_filename = secure_filename(f.filename)
            output_filepath = path.join("Uploads", output_filename)
            f.save(output_filepath)
            return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = False)