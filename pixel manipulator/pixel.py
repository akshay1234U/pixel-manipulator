from PIL import Image

def encrypt_image(input_image_path, output_image_path, key):
    try:
      
        image = Image.open(input_image_path)

       
        if image.mode != 'RGB':
            image = image.convert('RGB')

        
        pixels = image.load()

        
        width, height = image.size

       
        for x in range(width):
            for y in range(height):
               
                r, g, b = pixels[x, y]

               
                encrypted_r = (r + key) % 256
                encrypted_g = (g + key) % 256
                encrypted_b = (b + key) % 256

                
                pixels[x, y] = (encrypted_r, encrypted_g, encrypted_b)

       
        image.save(output_image_path)
        print(f"Image encrypted and saved as {output_image_path}")

    except Exception as e:
        print(f"Error during encryption: {e}")


def decrypt_image(input_image_path, output_image_path, key):
    try:
       
        image = Image.open(input_image_path)

     
        if image.mode != 'RGB':
            image = image.convert('RGB')

        
        pixels = image.load()

       
        width, height = image.size

        
        for x in range(width):
            for y in range(height):
               
                r, g, b = pixels[x, y]

                
                decrypted_r = (r - key) % 256
                decrypted_g = (g - key) % 256
                decrypted_b = (b - key) % 256

               
                pixels[x, y] = (decrypted_r, decrypted_g, decrypted_b)

        
        image.save(output_image_path)
        print(f"Image decrypted and saved as {output_image_path}")

    except Exception as e:
        print(f"Error during decryption: {e}")


if __name__ == "__main__":
    
    input_image_path = "input_image.jpg"  
    encrypted_image_path = "encrypted_image.jpg"
    decrypted_image_path = "decrypted_image.jpg"

    
    key = 50 

  
    encrypt_image(input_image_path, encrypted_image_path, key)

 
    decrypt_image(encrypted_image_path, decrypted_image_path, key)

