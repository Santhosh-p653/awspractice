🖼️ Image to Speech using Amazon Rekognition & Amazon Polly

Overview

This project demonstrates how to use AWS AI services to convert an image into spoken audio.

The application analyzes an input image using Amazon Rekognition to identify objects and detect text. It then generates a natural language description of the image and converts that description into speech using Amazon Polly. The resulting audio is saved as an MP3 file.

This project showcases the integration of multiple AWS AI services using Python and the AWS SDK (Boto3).

---

Features

- Detects objects in an image using Amazon Rekognition
- Detects text present in the image
- Generates a human-readable description
- Converts the description into speech using Amazon Polly
- Saves the generated speech as "output.mp3"

---

AWS Services Used

- Amazon Rekognition
- Amazon Polly
- AWS IAM
- Boto3 (AWS SDK for Python)

---

Project Structure

.
├── image_to_speech.py
├── sample.jpg
├── output.mp3
├── README.md
└── .gitignore

---

Prerequisites

- Python 3.9 or later
- AWS Account
- AWS CLI installed
- Boto3

---

Installation

Clone the repository:

git clone <your-repository-url>
cd <repository-name>

Create a virtual environment:

python3 -m venv .venv

Activate it:

Linux / macOS

source .venv/bin/activate

Windows

.venv\Scripts\activate

Install dependencies:

pip install boto3

---

Configure AWS Credentials

Install the AWS CLI (if not already installed), then configure your credentials:

aws configure

Provide:

- AWS Access Key ID
- AWS Secret Access Key
- Default Region (for example: "us-east-1")
- Output format ("json")

Ensure your IAM user has permissions for:

- Amazon Rekognition
- Amazon Polly

---

Running the Project

Place an image named:

sample.jpg

in the project directory.

Run:

python image_to_speech.py

The program will:

1. Read the image.
2. Detect objects and text using Amazon Rekognition.
3. Generate a description.
4. Convert the description into speech using Amazon Polly.
5. Save the output as:

output.mp3

---

Example

Input

sample.jpg

Detected Description

I can see:
Laptop
Keyboard
Computer

The image contains the text:
OPEN AI

Output

output.mp3

---

Future Improvements

- Deploy using AWS Lambda
- Trigger processing automatically using Amazon S3
- Expose the functionality through Amazon API Gateway
- Build a web interface using AWS Amplify
- Support multiple languages and voices

---

License

This project is intended for educational and learning purposes.
