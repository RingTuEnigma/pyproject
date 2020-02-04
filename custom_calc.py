import json

def test_function(body):
  #Prints the content of the HTTP POST Request Body
  print(body)
  #The JSON encoded content is decoded
  data_list = json.loads(body)
  print(data_list)
  #Shows that the content is a list and not just a string
  print(data_list['num'])
  data_JSON = json.dumps(data_list)
  print(data_JSON)
  return data_JSON
  
