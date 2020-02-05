import json
from Heinrich_V1 import Call

def test_function(body):
  #Prints the content of the HTTP POST Request Body
  print(body)
  #The JSON encoded content is decoded
  data_list = json.loads(body)
  #response_data = call(classes,absolute,z)
  print(data_list)
  #Shows that the content is a list and not just a string
  data_JSON = json.dumps(data_list) #exchange data_list with response_data
  print(data_JSON)
  return data_JSON

def do_calculation(input_JSON):
  input_data = json.loads(input_JSON)
  output_data = Call(input_data['classes'], input_data['absolute'], input_data['z'])
  output_JSON = json.dumps(output_data)
  #print(output_data)
  #print(output_JSON)
  return output_JSON