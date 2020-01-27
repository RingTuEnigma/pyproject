import json

def test_function(body):
  #Prints the content of the HTTP POST Request Body
  print(body)
  #The JSON encoded content is decoded
  data_list = json.loads(body)
  print(data_list)
  #Shows that the content is a list and not just a string
  print(data_list[0])
  data_JSON = json.dumps(data_list)
  return data_JSON
  