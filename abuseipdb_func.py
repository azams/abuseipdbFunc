import requests,re,sys,pprint

def abuseipdb(ip):
    resp = requests.get("https://www.abuseipdb.com/check/"+ip)
    info = re.findall('(<span class="([.*?]+)" aria\-hidden=true title="(.+)" data\-toggle=tooltip><\/span>)?\n<img class="flag flag\-([a-z]+)" src="\/img\/blank\.gif" title=([A-Za-z\-_]+) data\-toggle=tooltip \/>\n<a href="https:\/\/www\.abuseipdb\.com\/user\/([0-9]+)">(.+)<\/a>', resp.text)
    comm = re.findall('<td data\-title=Date>\n<time datetime=(.*?)>(.*?)<\/time>\n<\/td>\n<td data\-title=Comment>\s(.*?)<\/td>', resp.text, re.DOTALL)
    cats = re.findall('<td class=text\-right data\-title=Categories>\s(.*?)<\/td>', resp.text, re.DOTALL)
    ipinfo = re.findall('<img src="\/img\/blank\.gif" class="flag flag\-([a-z]+)"\/>\n([a-zA-Z]+)\n<\/td>', resp.text)
    js = {}
    js['findings'] = {}
    js['infos'] = {"ip_address":ip, "ip_country_code":ipinfo[0][0], "ip_country_name":ipinfo[0][1]}
    for i in range(len(info)):
        name = info[i][6]
        country = info[i][4]
        country_code = info[i][3]
        date = comm[0][0]
        category = re.findall('<span class="label label\-default" data\-toggle=tooltip data\-placement=top title="(.*?)">(.*?)<\/span>', cats[i])
        cat = {}
        for c in range(len(category)):
            cat[c] = {'category_name':category[c][1],'category_value':category[c][0]}
        comment = comm[i][2].replace('<div style="max-width:400px!important">', '').replace('</div>', '').replace('\n', '')
        js['findings'][i] = {"reporter_name":name, "reporter_date":date, "reporter_country":country, "reporter_country_code":country_code, "reporter_comment":comment, "category":cat}
    return js
