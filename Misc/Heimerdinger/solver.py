def transform_file(input_image_path, output_image_path):
    with open(input_image_path, 'rb') as input_file:
        data = input_file.read()
    modified_data = bytearray((15 - byte) % 256 for byte in data)
    with open(output_image_path, 'wb') as output_file:
        output_file.write(modified_data)
        print("Modified image saved to:", output_image_path)

# Usage
input_image_path = "C:\\Users\\Khalil\\Desktop\\corrupted.jpg"
output_image_path = "C:\\Users\\Khalil\\Desktop\\heimer.jpg"
transform_file(input_image_path, output_image_path)
