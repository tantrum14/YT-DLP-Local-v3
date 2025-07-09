# YT-DLP-Local-v3

A minimal Flask-powered local web UI for yt-dlp video downloads. This simple web application allows users to paste video URLs and download them via a yt-dlp backend through an intuitive web interface.

## Features

- **Simple Web Interface**: Clean, minimal UI for entering video URLs
- **yt-dlp Integration**: Leverages the powerful yt-dlp library for video downloading
- **Local Deployment**: Runs locally on your machine at http://127.0.0.1:5050
- **Modern Stack**: Built with latest Flask (3.1.1) and yt-dlp (2025.7.7.233044-nightly)
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/tantrum14/YT-DLP-Local-v3.git
   cd YT-DLP-Local-v3
   ```

2. Install required dependencies:
   ```bash
   pip install flask==3.1.1 yt-dlp==2025.7.7.233044-nightly
   ```

   Or install from requirements.txt (if available):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5050
   ```

3. Paste a video URL into the input field and click download

4. The video will be downloaded to your local machine using yt-dlp

## Supported Sites

This application supports all sites that yt-dlp supports, including:
- YouTube
- Vimeo
- Twitter/X
- TikTok
- Instagram
- And many more (1000+ sites)

For a complete list, visit the [yt-dlp supported sites documentation](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).

## Configuration

The application runs on `http://127.0.0.1:5050` by default. You can modify the host and port in the main application file if needed.

## Dependencies

- **Flask 3.1.1**: Modern Python web framework
- **yt-dlp 2025.7.7.233044-nightly**: YouTube-dl fork with additional features and fixes

## Project Structure

```
YT-DLP-Local-v3/
├── app.py              # Main Flask application
├── templates/          # HTML templates
├── static/            # CSS, JS, and other static files
├── downloads/         # Downloaded videos directory (created automatically)
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source. Please check the LICENSE file for details.

## Disclaimer

This tool is for personal use only. Please respect copyright laws and the terms of service of the platforms you're downloading from. Always ensure you have permission to download content.

## Troubleshooting

### Common Issues

1. **Port already in use**: If port 5050 is already in use, modify the port in app.py
2. **yt-dlp errors**: Ensure you have the latest version of yt-dlp installed
3. **Permission errors**: Make sure the application has write permissions in the download directory

### Getting Help

If you encounter issues:
1. Check the console output for error messages
2. Ensure all dependencies are properly installed
3. Verify the video URL is from a supported site
4. Create an issue on this GitHub repository

---

*Created with Comet Assistant*
