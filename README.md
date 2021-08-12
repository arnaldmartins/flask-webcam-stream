# install opencv (OrangePi)
pip install python3-opencv

# install open cv (Windows)
pip install opencv-python

# instal Flask
pip install Flask

# run Flask app
# windows
$env:FLASK_APP = "<caminho-do-arquivo>/stream_video.py" 
python -m flask run --host 0.0.0.0
# orangepi
export FLASK_APP = "<caminho-do-arquivo>/stream_video.py" 
flask run --host 0.0.0.0
