from pyodide.http import pyfetch
from pyodide.ffi import create_proxy

import asyncio

from js import console
from js import window
from js import document
from js import localStorage

window.scroll(0, 0)

exercisedb_headers = {'X-RapidAPI-Key': 'bf431ea5cfmsha2be49757f2b182p1c71a3jsn9e36cee07f95',
                      'X-RapidAPI-Host': 'exercisedb.p.rapidapi.com'}


def toggleGender(gender):
    male = document.getElementById('male-body-layout')
    female = document.getElementById('female-body-layout')

    if (gender == "male"):
        male.style.display = "flex"
        female.style.display = "none"

    elif (gender == "female"):
        male.style.display = "none"
        female.style.display = "flex"





@staticmethod
def setExerciseId(event):
    window.location.href = "new-doc.htm"
    localStorage.setItem("exercise_id", event.target.id)


def getValue():
    val = "name/"+document.getElementById("search-bar").value
    document.getElementById("search-bar").textContent = " "
    asyncio.create_task(call(val))


async def call(muscle):
    document.body.style.overflow = "auto"
    document.body.style.padding = "0 0 1000px 0"
    window.scroll(0, 700)

    response = await pyfetch(url="https://exercisedb.p.rapidapi.com/exercises/{}".format(muscle), method="GET", headers=exercisedb_headers)

    output = await response.json()

    print(output)

    cardContainer = document.getElementById("card-container")
    cardContainer.innerHTML = " "

    for i in range(0, len(output)):
        card = document.createElement('div')
        card.classList.add('card')
        card.setAttribute("id", output[i]["id"])
        card.innerHTML = f'<p class="ex-name" id={output[i]["id"]} >{output[i]["name"]}</p><img src={output[i]["gifUrl"]} class="ex-img" id={output[i]["id"]}><div class="info-muscles" id={output[i]["id"]}><div class="bodyPart" id={output[i]["id"]}>{output[i]["bodyPart"]}</div><div class="targetMuscles" id={output[i]["id"]}>{output[i]["target"]} </div> </div>'
        card.addEventListener("click", create_proxy(setExerciseId))
        cardContainer.appendChild(card)

    document.body.style.padding = "0 0 30px 0"
