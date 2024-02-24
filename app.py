from flask import Flask, request, jsonify
import whisper


app = Flask(__name__)

# Load the ASR model once during the application startup
model = whisper.load_model("base")

@app.route('/upload', methods=['POST'])
def upload_mp3():
    try:
        # Check if the 'file_path' key is in the request data
        if 'file_path' not in request.form:
            return jsonify({'error': 'No file path provided'}), 400

        file_path = request.form['file_path']

        print("filepath"+file_path)

        # Check if the file has a valid extension
        if not file_path.endswith(('.mp3', '.m4a')):
            return jsonify({'error': 'Invalid file format. Please provide an MP3 file'}), 400

        # Read the content of the MP3 file into bytes


        # Convert the bytes data to a NumPy array


        # You can save the file or perform further processing here
        # For simplicity, let's just return a success message for now
        result = model.transcribe(file_path, fp16=False)


        response_data = {
                'message': 'MP3 file uploaded successfully',
                'transcription': result["text"]
            }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
