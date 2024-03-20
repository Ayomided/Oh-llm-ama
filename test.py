import ollama
from ollama import generate
from PIL import Image
from io import BytesIO

def process_image(image_file):
    print(f"Processing image {image_file}")
    with Image.open(image_file) as img:
        with BytesIO() as buffer:
            img.save(buffer, format='JPEG')
            image_bytes = buffer.getvalue()
    
    full_response = ''

    for response in generate(model='llava',
                             prompt='What device what the picture taken on? look into the metadata of the bytes for information',
                             images=[image_bytes],
                             stream=True):
        print(response['response'], end='', flush=True)
        full_response += response['response']


process_image('./IMG_7746.jpeg')

# stream = ollama.chat(
#     model='llama2',
#     messages=[
#         {'role': 'user', 'content': 'Where can I get a light saber?'}],
#     stream=True,
# )

# for chunk in stream:
#   print(chunk['message']['content'], end='', flush=True)
