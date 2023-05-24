import requests

def upload_image(url, image_path):
    with open(image_path, 'rb') as image_file:
        files = {'file': image_file}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            print("Image uploaded successfully.")
        else:
            print("Error uploading image. Status code:", response.status_code)

# Example usage
website_url = "https://imgbb.com/upload"  
image_filepath = r"C:\Users\CODED\Desktop\cardata\image\room-5.jpg"  

upload_image(website_url, image_filepath)
