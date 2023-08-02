import requests

api_key = 'xx'  # Replace with your actual API key
file_url = 'https://huggingface.co/stabilityai/stable-diffusion-xl-base-0.9/resolve/main/sd_xl_base_0.9.safetensors' 
headers = {'Authorization': f'Bearer {api_key}'}

response = requests.get(file_url, headers=headers)

# Make sure the request was successful
if response.status_code == 200:
    # Get the file name by splitting the URL by the '/' character and getting the last element in the resulting list
    file_name = file_url.split('/')[-1]

    # Write the content to a file
    with open(file_name, 'wb') as file:
        file.write(response.content)
else:
    print(f'Request failed with status code {response.status_code}')
