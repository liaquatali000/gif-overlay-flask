Description: A Flask application that overlays a PNG image on a GIF and outputs the result as a new GIF.

Short Documentation:

This repository contains a Flask application that takes two inputs: a PNG image file and a GIF file. The application overlays the PNG image on the GIF and outputs the result as a new GIF.

To run the application, you need to have Flask installed on your computer. You can install Flask using pip:

Copy code
pip install Flask
The application also uses moviepy and imageio to manipulate the video and images. You can install these dependencies using pip as well:

Copy code
pip install moviepy
pip install imageio
To start the application, run the following command in the project directory:

Copy code
python app.py
This will start the Flask development server. You can access the application at http://127.0.0.1:5000/. The application has a single endpoint "/gif" that accepts POST requests with the PNG and GIF files. The response is a GIF file containing the overlayed image.
