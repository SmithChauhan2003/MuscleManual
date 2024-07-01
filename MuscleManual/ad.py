from js import XMLHttpRequest

from pyodide.http import pyfetch
import asyncio
  
async def main():

 print("Executing code...")
 muscle = 'biceps'
 response = await pyfetch(url="https://api.api-ninjas.com/v1/exercises?muscle={}".format(muscle), method="GET", headers={'X-Api-Key': 'g9dDgyoIEDawyQA/Uu2nxA==PjZkTHFnN8ESNkeV'})
 
 response_dict = await response.json()

 status = f"Request status: {response.status}"
 text = f"Text: {response_dict['text']}"

 print(response_dict[1])


  
asyncio.create_task(main())