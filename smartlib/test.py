import smarthttp

response = smarthttp.post("localhost:8000","/polls/register","this is body",{})

print response.read()