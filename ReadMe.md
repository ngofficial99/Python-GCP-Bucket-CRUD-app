# GCP Bucket Management Script

## Overview
A Python utility for managing Google Cloud Storage buckets, allowing users to list, upload, and delete objects with a simple command-line interface.

## Features
- List objects in a GCP bucket
- Upload files to the bucket
- Delete objects from the bucket
- Secure credential management using `.env`

## Prerequisites
- Python 3.7+
- Google Cloud Platform account
- GCP Service Account with Storage permissions

## Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
1. Create a `.env` file with:
```
GCP_BUCKET_NAME=your-bucket-name
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account-key.json
```

## Usage
```bash
python bucket_manager.py
```

## Security
- Uses environment variables for credential management
- Requires service account key with minimal necessary permissions

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push and create a pull request


## Support
For issues, please open a GitHub issue with detailed description.