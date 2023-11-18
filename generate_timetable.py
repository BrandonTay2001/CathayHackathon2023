import os
import openai
import json
openai.api_type = "azure"
openai.api_base = "https://team-21.openai.azure.com/"
openai.api_version = "2023-09-15-preview"
openai.api_key = "f9d497ddba0e4f698c4064664785cd54"

timetablePrompt = "You are a trip planner AI. Given a user-given pacing, prompt, destination, start date and end date, generate a detailed itinerary in the form of a list of JSON objects with the following fields: startTime, endTime, name\n\nResponse should be in this form:\n[{startTime: 2023-12-11T00:00:00.000Z, endTime: 2023-12-14T00:00:00.000Z, name: 'Kyoto shrine'}, {startTime: 2023-12-25T00:00:00.000Z, endTime: 2023-12-28T00:00:00.000Z, name: 'Kyoto museum'}]\n\nName fields should be specific and mention actual locations. For example, do not mention 'breakfast at local cafe' but instead 'Restaurant ABC'.\n\nRequest:\n"

def generate(inputStr):
  try:
    response = openai.Completion.create(
      engine="generate-timetable",
      prompt=timetablePrompt + inputStr,
      temperature=0.9,
      max_tokens=4000,
      top_p=0,
      frequency_penalty=0,
      presence_penalty=0,
      best_of=1,
      stop=None
    )
  except Exception as e:
    print(e)
    return None

  jsonText = response['choices'][0]['text']
  # convert to json
  try:
    jsonData = json.loads(jsonText)
    return jsonData
  except Exception as e:
    print(e)
    return None
  