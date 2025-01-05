from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

def hash_text(text, algorithm):
    """Hashes the input text using the specified algorithm and returns the first 6 characters of the hash."""
    try:
        if algorithm == 'sha256':
            hash_object = hashlib.sha256(text.encode())
        elif algorithm == 'sha512':
            hash_object = hashlib.sha512(text.encode())
        elif algorithm == 'sha224':
            hash_object = hashlib.sha224(text.encode())
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
        
        # Get the hexadecimal digest and return the first 6 characters
        return hash_object.hexdigest()[:6]
    
    except Exception as e:
        print(f"Error in hashing: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        algorithm = request.form['algorithm']
        
        hashed = hash_text(text, algorithm)
        
        if hashed:
            # Display the result as a color
            color_code = hashed
            if len(color_code) < 6:
                color_code = color_code.ljust(6, '0')
            
            return render_template('index.html', hashed=hashed, color_code=color_code)
        else:
            return render_template('index.html', error="An error occurred during hashing.")
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
