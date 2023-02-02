import io
from flask import Flask, request, send_file
from PIL import Image
import moviepy.editor as mp
import imageio

app = Flask(__name__)

@ app.route("/gif", methods = ["POST"])
def overlay_gif(): #Get the uploaded PNG and GIF files
    png_file = request.files.get("png_file")
    gif_file = request.files.get("gif_file")

    # Save the PNG and GIF files to the same directory
    png_file.save("gif/nimage.png")
    gif_file.save("gif/start.gif")

    # Convert GIF To video(mp4)
    clip = mp.VideoFileClip("gif/start.gif")

    clip.write_videofile("input.mp4")

    # Load the video clip
    video = mp.VideoFileClip("input.mp4")

    # Load the overlay image
    overlay = mp.ImageClip("gif/nimage.png")

    # Resize the overlay to 250 x250
    overlay = overlay.resize((250, 250))

    # Calculate the position of the overlay
    x = (video.w - overlay.w) / 2
    y = (video.h - overlay.h) / 2

    # Add the overlay to the video
    final = mp.CompositeVideoClip([video, overlay.set_pos((x, y))])

    # Set the duration of the final clip to the duration of the video
    # Set the duration of the final clip to the duration of the video
    final = final.set_duration(video.duration)

    # Write the output video
    final.write_videofile("output.mp4")

    filename = "output.mp4"
    output_filename = "output.gif"

    with imageio.get_reader(filename, 'ffmpeg') as reader:
        fps = reader.get_meta_data()['fps']
        frames = []
        for i, im in enumerate(reader):
            if i > fps * video.duration: # only keep the same number of frames as the original GIF
                break
            frames.append(im)
        imageio.mimsave(output_filename, frames, 'GIF', fps = fps)

    return send_file("output.gif",
        mimetype = "image/gif",
       )
if __name__ == '__main__':
        app.run(debug = True)