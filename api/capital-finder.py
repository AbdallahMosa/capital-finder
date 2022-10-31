from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s=self.path
        url = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url.query)
        dictionary=dict(query_string_list)
        if "capital" in dictionary:
            city=dictionary["capital"]
            new_url="https://restcountries.com/v3.1/capital/"
            r=requests.get(new_url+city)
            data=r.json()
            country  =data[0]["name"]['common']
            mss= f"{city} is the capital of {country}"

        elif "country" in dictionary:
            #"https://restcountries.com/v3.1/name/"
            name=dictionary["country"]
            new_url="https://restcountries.com/v3.1/name/"
            r=requests.get(new_url+name)
            data=r.json()
            capital=data[0]["capital"][0]
            mss= f"the capital of {name} is {capital}"
        else : 
            mss='''
            welcome to our website 
            find your lovely capital or country 
            '''





        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        # message = 'Hello from Python from a Serverless Function!'
        self.wfile.write(mss.encode())
        return