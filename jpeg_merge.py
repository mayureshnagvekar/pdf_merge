from PIL import Image
from PIL import ExifTags
from reportlab.pdfgen import canvas
import os


def create_pdf_from_jpegs(jpeg_files, output_pdf):
    c = canvas.Canvas(output_pdf)
    for jpeg_file in jpeg_files:
        # Open the JPEG image and Auto-rotate the image based on EXIF data
        img = auto_rotate_image(Image.open(jpeg_file))
        # Get image dimensions
        width, height = img.size
        # Set the page size of the PDF to match the image
        c.setPageSize((width, height))
        # Save the rotated image to a temporary file
        temp_file = f"temp_{os.path.basename(jpeg_file)}"
        img.save(temp_file)
        # Draw the image on the PDF
        c.drawImage(temp_file, 0, 0, width, height)
        # Remove the temporary file
        os.remove(temp_file)
        # Move to the next page
        c.showPage()
    # Save the PDF
    c.save()


def auto_rotate_image(image):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = dict(image._getexif().items())
        if exif[orientation] == 3:
            image = image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image = image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image = image.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        # Cases: image doesn't have getexif
        pass
    return image


# List of JPEG files in the desired order
jpeg_files = [
    "pg1.jpeg",
    "pg2.jpeg",
    "pg3.jpeg"
]

# Output PDF file name
output_pdf = "combined_offer_documents.pdf"
# Create the PDF
create_pdf_from_jpegs(jpeg_files, output_pdf)
print(f"PDF created successfully: {output_pdf}")
