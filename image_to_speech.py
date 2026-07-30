import boto3

# AWS clients
rekognition = boto3.client("rekognition", region_name="us-east-1")
polly = boto3.client("polly", region_name="us-east-1")

IMAGE = "sample.jpg"

with open(IMAGE, "rb") as image:
    image_bytes = image.read()

description = []

# Detect labels
labels = rekognition.detect_labels(
    Image={"Bytes": image_bytes},
    MaxLabels=5,
    MinConfidence=80
)

if labels["Labels"]:
    description.append("I can see:")
    for label in labels["Labels"]:
        description.append(label["Name"])

# Detect text
text = rekognition.detect_text(Image={"Bytes": image_bytes})

words = [
    d["DetectedText"]
    for d in text["TextDetections"]
    if d["Type"] == "WORD"
]

if words:
    description.append("The image contains the text:")
    description.append(" ".join(words))

speech = ". ".join(description)

if not speech:
    speech = "Sorry, I could not recognize anything."

print("\nDescription:\n")
print(speech)

response = polly.synthesize_speech(
    Text=speech,
    OutputFormat="mp3",
    VoiceId="Joanna"
)

with open("output.mp3", "wb") as f:
    f.write(response["AudioStream"].read())

print("\nSaved as output.mp3")