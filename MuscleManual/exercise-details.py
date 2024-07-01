from js import document
from js import localStorage
from js import window
from js import console
from pyodide.ffi import create_proxy
from pyodide.http import pyfetch
import asyncio

out = document.getElementById('card-container')
msg = localStorage.getItem("exercise_id")
name = ""


exercisedb_headers = {'X-RapidAPI-Key': 'bf431ea5cfmsha2be49757f2b182p1c71a3jsn9e36cee07f95',
                      'X-RapidAPI-Host': 'exercisedb.p.rapidapi.com'}

yt_headers = {'X-RapidAPI-Key': 'bf431ea5cfmsha2be49757f2b182p1c71a3jsn9e36cee07f95',
              'X-RapidAPI-Host': 'youtube-search6.p.rapidapi.com'}


def func():
    window.location.href = "Untitled-1.htm"





async def exDetails():

    response = await pyfetch(url="https://exercisedb.p.rapidapi.com/exercises/exercise/"+msg, method="GET", headers=exercisedb_headers)
    output = await response.json()

    name = output['name'].replace(" ", "+")

    response_yt = await pyfetch(url="https://youtube-search6.p.rapidapi.com/search/?query="+name, method="GET", headers=yt_headers)
    yt_output = await response_yt.json()

    document.getElementById(
        "gif-ex-details").setAttribute("src", output['gifUrl'])

    document.getElementById("exercise-name-txt").innerText = output['name']
    document.getElementById("muscle").innerText = output['bodyPart']
    document.getElementById("target-muscle").innerText = output['target']
    document.getElementById("equipment").innerText = output['equipment']
    document.getElementById("vmjckl").innerText = output['name']

    vid_container = document.getElementById("vid-container")
    vid_container.innerHTML = " "

    for i in range(0, len(yt_output['videos'])):
        vid_container.innerHTML += f'<iframe allow="fullscreen;" class="vid" src="https://www.youtube.com/embed/{yt_output["videos"][i]["video_id"]}"></iframe>'
        console.log(
            f'https://www.youtube.com/embed/{yt_output["videos"][i]["video_id"]}')

exDetails()
