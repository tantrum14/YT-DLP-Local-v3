from flask import Flask, request, render_template, flash, redirect, url_for
import yt_dlp
import os
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key

# Ensure downloads directory exists
DOWNLOADS_DIR = Path('downloads')
DOWNLOADS_DIR.mkdir(exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        url = request.form.get('url', '').strip()
        
        if not url:
            flash('Please enter a valid URL', 'error')
            return redirect(url_for('index'))
        
        try:
            # yt-dlp options
            ydl_opts = {
                'outtmpl': str(DOWNLOADS_DIR / '%(title)s.%(ext)s'),
                'format': 'best[height<=720]/best',  # Download best quality up to 720p
            }
            
            # Download the video using yt-dlp
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            flash('Video downloaded successfully!', 'success')
            
        except yt_dlp.DownloadError as e:
            flash(f'Download failed: {str(e)}', 'error')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
        
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5050)

# Created with Comet Assistant
