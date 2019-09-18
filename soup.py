#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests, sys, csv, json, re, os, urllib.request
# import rhinoscriptsyntax as rs
# from os.path import isfile as file_exist

# url variables
url1 = "http://ufm.edu/Portal"
url2 = "http://ufm.edu/Estudios"
url3 = "https://fce.ufm.edu/carrera/cs/"
url4 = "http://ufm.edu/Directorio"

# print if needed, gets too noisy
# print(soup.prettify())

print("<Ian Jenatz>")

class Soup:
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def part1(self):
        print("==================================================================")
        # Make a GET request to fetch the raw HTML content
        try:
            html_content = requests.get(url1).text
        except:
            print("unable to get {url1}")
            sys.exit(1)
        print("1. Portal")
        soup = BeautifulSoup(html_content, "html.parser")
        # Print Title
        title = soup.title.string
        print("GET the title and print it:", title)
        print("------------------------------------------------------------------")
        # Print the Complete Address of UFM
        for data in soup.find_all("meta", {"property": "og:url"}):
            address = data.get("content")
        print("GET the Complete Address of UFM:", address)
        print("------------------------------------------------------------------")
        # Print the phone number and info email
        for data in soup.find_all("a", {"href": "tel:+50223387700"}):
            phone = data.text
        for data in soup.find_all("a", {"href": "mailto:inf@ufm.edu"}):
            info_email = data.string
        print("GET the phone number and info email:", phone, info_email)
        print("------------------------------------------------------------------")
        # Print nav menu
        nav_menu = soup.find(id="menu-table").text
        nav_menu = nav_menu.replace("\t", "").replace("\r", "").replace("\n", "")
        nav_menu = " ".join(nav_menu.split())
        print("GET all item that are part of the upper nav menu (id: menu-table):", nav_menu)
        print("------------------------------------------------------------------")
        # Print all hrefs
        print("Find all properties that have href (link to somewhere):")
        if len(soup.find_all(href = True)) < 31:
            for link in soup.find_all(href = True):
                print("\n-", link)
        else:
            logfile = "../p3soup/logs/find_all_properties_that_have_href.txt"
            f = open(logfile, "w+")
            for link in soup.find_all(href = True):
                f.write("-" + str(link)+ "\n")
            f.close()
            print("Output exceeds 30 lines, sending output to:", logfile)
        print("------------------------------------------------------------------")
        # Print UFMail button href
        for link in soup.find_all("a", {"id": "ufmail_"}):
            UFMail = link.get("href")
        print("GET href of \"UFMail\" button:", UFMail)
        print("------------------------------------------------------------------")
        # Print MiU button href
        for link in soup.find_all("a", {"id": "miu_"}):
            MiU = link.get("href")
        print("GET href of \"MiU\" button:", MiU)
        print("------------------------------------------------------------------")
        print("get hrefs of all <img>:")
        # Print all <img> hrefs
        if len(soup.find_all("img")) < 31:
            for link in soup.find_all("img"):
                print("\n-", link.get("src"))
        else:
            logfile = "../p3soup/logs/get_hrefs_of_all_img.txt"
            f = open(logfile, "w+")
            for link in soup.find_all("img"):
                f.write("-" + str(link.get("src"))+ "\n")
            f.close()
            print("Output exceeds 30 lines, sending output to:", logfile)
        print("------------------------------------------------------------------")
        # Count all <a>
        count = 0
        for i in soup.find_all("a"):
            i
            count+=1
        print("count all <a>:", count)
        print("==================================================================")
        return 0
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def part2(self):
        print("==================================================================")
        try:
            html_content = requests.get(url2).text
        except:
            print("unable to get {url2}")
            sys.exit(1)
        soup = BeautifulSoup(html_content, "html.parser")
        print("2. Estudios")
        # Print topmenu items
        # Home button has no text to specify so nothing appears.
        for item in soup.find_all("div", {"class": "menu-key"}):
            nav_menu = item.text
            nav_menu = nav_menu.replace("\t", "").replace("\r", "").replace("\n", "")
            nav_menu = " ".join(nav_menu.split())
            print("-", nav_menu)
        print("------------------------------------------------------------------")
        # Print all Estudios
        for item in soup.find_all("div", {"class": "estudios"}):
            print(item.text)
        print("------------------------------------------------------------------")
        # Print all li leftbar items
        for item in soup.find_all("div", {"class": "leftbar"}):
            unwanted = item.find("div", {"class": "hidden-phone"})
            unwanted.extract()
            print(item.text.strip())
        print("------------------------------------------------------------------")
        # Print all social media with its links
        for link in soup.find_all("div", {"class": "social pull-right"}):
            for item in link.find_all("a", {"target": "_blank"}):
                print("\n-", item.get("href"))
        print("------------------------------------------------------------------")
        count = 0
        for i in soup.find_all("a"):
            i
            count+=1
        print("count all <a>:", count)
        print("==================================================================")
        return 0
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def part3(self):
        print("==================================================================")
        try:
            html_content = requests.get(url3).text
        except:
            print("unable to get {url3}")
            sys.exit(1)
        soup = BeautifulSoup(html_content, "html.parser")
        print("3. CS")
        # Print Title
        title = soup.title.string
        print("GET the title and print it:", title)
        print("------------------------------------------------------------------")
        # Print all hrefs
        print("GET and display the href:")
        if len(soup.find_all(href = True)) < 31:
            for link in soup.find_all(href = True):
                print("\n-", link.get("href"))
        else:
            logfile = "../p3soup/logs/get_and_display_the_href.txt"
            f = open(logfile, "w+")
            for link in soup.find_all(href = True):
                f.write("-" + str(link.get("href"))+ "\n")
            f.close()
            print("Output exceeds 30 lines, sending output to:", logfile)
        print("------------------------------------------------------------------")
        # Download the logo
        print("Download the \"FACULTAD de CIENCIAS ECONOMICAS\" logo.")
        # Downlodea la imagen pero por alguna razón hay un problema al abrirlo. (Abre la imagen pero desaparece)
        for img in soup.find_all("img", {"class": "fl-photo-img wp-image-500 size-full"}):
            imgUrl = img.get("src")
            print(imgUrl)
            urllib.request.urlretrieve(imgUrl, os.path.basename(imgUrl))
        print("------------------------------------------------------------------")
        # Print "title" "description" metadata
        for link in soup.find_all("meta", {"property": "og:title"}):
            print("\n-", link.get("content"))
        for link in soup.find_all("meta", {"property": "og:description"}):
            print("\n-", link.get("content"))
        print("------------------------------------------------------------------")
        # Print the count of all <a>
        count = 0
        for i in soup.find_all("a"):
            i
            count+=1
        print("count all <a>:", count)
        print("------------------------------------------------------------------")
        # Print the count of all <div>
        count = 0
        for i in soup.find_all("div"):
            i
            count+=1
        print("count all <div>:", count)
        print("==================================================================")
        return 0
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def part4(self):
        print("==================================================================")
        try:
            html_content = requests.get(url4).text
        except:
            print("unable to get {url4}")
            sys.exit(1)
        soup = BeautifulSoup(html_content, "html.parser")
        print("4. Directorio")
        # Count of emails with a vowel
        count = 0         
        for table in soup.find_all("table", {"class": ["tabla ancho100", "tabla ancho100 col3"]}):
            match = re.findall(r"[\w\.-]+@[\w\.-]+", table.text)
            match = match + match
            match.sort()
        # Count of emails that start with with a vowel
        for table in soup.find_all("table", {"class": ["tabla ancho100", "tabla ancho100 col3"]}):
            for word in re.findall(r"[\w\.-]+@[\w\.-]+", table.text):
                if word[0] in ["a","e","i","o","u","A","E","I","O","U"]:
                    count += 1
        logfile = "../p3soup/logs/4directorio_emails.txt"
        f = open(logfile, "w+")
        f.write(str(match))
        f.close()
        print("Sort emails alphabetically, sending output to", logfile)
        print("------------------------------------------------------------------")
        print("count all emails that start with a vowel:", count)
        print("------------------------------------------------------------------")
        # Group in a JSON rows that have same address and dump into logs
        # Had to replace á, é, í, ó, ú because json wasn't accepting the values and would place the hexcode. 
        print("Grouped all rows with Same Address, dumping to logs/4directorio_address.json")
        # Parse both tables.
        table1 = soup.find("table", {"class": "tabla ancho100"})
        table2 = soup.find_all("table", {"class": "tabla ancho100"})[1]
        # Create empty lists 
        location = []
        page = []
        # Checks data in table1
        for row in table1.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) == 5: # Not really necessary
                var2 = cells[4].find(text = True).replace("\n", "").replace(",", "")
                var1 = cells[0].text
                var2 = " ".join(var2.split())
                var1 = " ".join(var1.split())
                # Replaces tildes to delete hex codes later on.
                var2 = var2.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                var1 = var1.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                # Adds results to lists
                location.append(var2)
                page.append(var1)
        # Checks data in table1
        for row in table2.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) == 5: # Not really necessary
                var4 = cells[4].find(text = True).replace("\n", "").replace(",", "")
                var3 = cells[0].text
                var4 = " ".join(var4.split())
                var3 = " ".join(var3.split())
                # Replaces tildes to delete hex codes later on.
                var4 = var4.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                var3 = var3.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                # Adds results to lists
                location.append(var4)
                page.append(var3)
        dictionary = dict(zip(page, location))
        # Reverses the list (not necessary but I had an error doing it reversed since the beginning, would delete multiple values)
        ordered = {}
        for key, value in dictionary.items():
            if value not in ordered:
                ordered[value] = [key]
            else:
                ordered[value].append(key)

        # Creates json and dumps result.
        json_string = json.dumps(ordered)
        datastore = json.loads(json_string)
        filename = "../p3soup/logs/4directorio_address.json"
        if filename:
            with open(filename, "w+") as f:
                json.dump(datastore, f, indent = 4)
        print("------------------------------------------------------------------")
        
           
           
           
           
           
           
        
        print("==================================================================")
        return 0
    
    # for table in soup.find_all("table", {"class": ["tabla ancho100", "tabla ancho100 col3"]}):
        #     x = soup.find("Arquitectura")
        #     y = soup.find("Edificio Académico")
        # address = {
        #     x: y
        # }
        # print(x)
        # print(y)

    # count = 0
        # for table in soup.find_all("table", {"class": ["tabla ancho100", "tabla ancho100 col3"]}):
        #     table_rows = table.find_all("tr")
        #     for tr in table_rows:
        #         td = tr.find_all('td')
        #         row = [i.text for i in td]
        #         print(row)

    # group1 = re.search("Edificio Académico", table.text)
        # count += 1
        # print(group1.string)

        # soup.find_all(text = re.compile("Edificio Académico"))
        
        #print(soup.findChildren("table"))

    # Como dump a un log file, complements de David pero saber que significa
    # def log(self):
    #     run.part3()
    #     with open(filename="log.txt",mode=-"w") as f:
    #         f.write() #como parametro mandale todo 
    #         pass


# Checks the command line and runs program according to input.
run = Soup()
if len(sys.argv) > 1:
    if sys.argv[1] == "1":
        run.part1()
    elif sys.argv[1] == "2":
        run.part2()
    elif sys.argv[1] == "3":
        run.part3()
    elif sys.argv[1] == "4":
        run.part4()
    else:
        print("Error in command line, please specify which part to run with 1-4 or leave blank to run all parts")
else:
    run.part1()
    run.part2()
    run.part3()
    run.part4()
