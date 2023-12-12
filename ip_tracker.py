#coded By Stark-404©
#Allright Reserved
#Github : github.com/STARK-404
#Instagram : la1uuuuu







import requests,rich
from rich import print




print(""" [bold magenta]

[bold pink]   __  ___       __            
 [bold pink] /  |/  /_ __  / /__ _  _____ 
[bold pink] / /|_/ / // / / / _ \ |/ / -_)
[bold pink]/_/  /_/\_, / /_/\___/___/\__/ 
       /___/ 
                         
[italic magenta]Coded By Stark-404
Insta : la1uuuuu
Github : github.com/STARK-404
""")
ip = input(f"\033[1m\033[92m[\033[0m+\033[92m] Enter The Ip Address To Track : ")

def ur_dady():
	try:
		response  = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
		data = response.json()
		print("\n")
		
		print(f"[bold green][✓]IP :{data['query']}")
		print(f"[bold green][✓]Status : {data['status']}")
		print(f"[bold green][+]Country : {data['country']}")
		print(f"[bold green][+]Region : {data['region']}")
		print(f"[bold green][+]RegionName : {data['regionName']}")
		
		print(f"[bold green][+]City : {data['city']}")
		print(f"[bold green][+]Latitude : {data['lat']}")
		print(f"[bold green][+]Longitude :[bold yellow] {data['lon']}")
		print(f"[bold green][+]Continent :[bold yellow] {data['continent']}")
		print(f"[bold green][+]Continent Code : {data['continentCode']}")
		print(f"[bold green][+]Offset : {data['offset']}")
		print(f"[bold green][+]Currency : {data['currency']}")
		print(f"[bold green][+]Isp : {data['isp']}")
		
		print(f"[bold green][+]Zipcode : {data['zip']}")
		print(f"[bold green][+]Org : {data['org']}")
		print(f"[bold green][+]TimeZone : {data['timezone']}")
		print(f"[bold green][+]As : {data['as']}")
		print(f"[bold green][+]AsName : {data['asname']}")
		print(f"[bold green][+]Reverse :[bold yellow] {data['reverse']}")
		print(f"[bold green][+]Mobile? :[bold blue] {data['mobile']}")
		print(f"[bold green][+]Proxy? :[bold blue] {data['proxy']}")
		print(f"[bold green][+]Hosting :[bold blue] {data['hosting']}")
		
	except Exception as e:
		print (f"Error: {e}")
		
		
ur_dady();
