from flask import Flask, request, send_file, redirect
import pyvibe as pv
from ytmp3 import YouTube, download_video
from urllib.parse import unquote

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    page = pv.Page(title="Youtube to mp4", 
                   navbar= pv.Navbar(title="", components=[], logo="https://www.youtube.com/s/desktop/339bae71/img/favicon_144x144.png"),
                   footer= pv.Footer(title="", components=[], logo="" ),)

    with page.add_card() as card:
        card.add_header("Youtube to mp4")
        with card.add_form(action="/", method='POST') as form:
            form.add_formtext(name="url", label="Video URL", placeholder="Enter the URL of the video")
            form.add_formsubmit(label="Download")
    if request.method == 'POST':
        if request.form['url']:
            url = unquote(str(request.form['url']))
            mp4 = download_video(url)
            if mp4 == None:
                return redirect('/')
            print(mp4)
            page.add_card().add_header("Downloaded")

            return send_file(f'{mp4}', as_attachment=True)
    return page.to_html()


if __name__ == '__main__':
    app.run(debug=True)
