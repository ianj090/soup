#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests, sys, csv, json, re, os, urllib.request

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
        print("Get hrefs of all <img>:")
        # Print all <img> hrefs
        if len(soup.find_all("img")) < 31:
            for link in soup.find_all("img"):
                print("-", link.get("src"))
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
        print("Count all <a>:", count)
        print("------------------------------------------------------------------")
        # Extra point, create a csv file from all a.
        print("Created a csv file from all <a>, dumping to logs/extra_as.csv")
        # Creats lists.
        text = []
        href = []
        # Parses page for all a and appends text and hrefs to the list
        for data in soup.find_all("a"):
            texts = data.text
            hrefs = data.get("href")
            texts = texts.replace("\t", "").replace("\r", "").replace("\n", "")
            texts = texts.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
            texts = ' '.join(texts.split())
            text.append(texts)
            href.append(hrefs)

        # Creates csv file and dumps result
        n = 0
        filename = "../p3soup/logs/extra_as.csv"
        with open(filename, mode='w+') as f:          
            f_writer = csv.writer(f)

            columnTitleRow = ["Text", " href"]
            f_writer.writerow(columnTitleRow)
            for i in href:
                f_writer.writerow([text[n], href[n]])
                n += 1
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
        print("Display all items from \"topmenu\" (8 in total): ")
        n = 0
        for item in soup.find_all("div", {"id": "topmenu"}):
            nav_menu = item.text
            nav_menu = nav_menu.replace("\t", "").replace("\r", "").replace("\n", ", ")
            nav_menu = " ".join(nav_menu.split())
            nav_menu = nav_menu.split(", ")
            nav_menu = filter(None, nav_menu)
            for i in nav_menu:
                if n < 8:
                    print("-", i)
                    n += 1           
        print("------------------------------------------------------------------")
        # Print all Estudios
        print("Display ALL \"Estudios\" (Doctorados/Maestrias/Posgrados/Licenciaturas/Baccalaureus): ")
        for item in soup.find_all("div", {"class": "estudios"}):
            print("-", item.text)
        print("------------------------------------------------------------------")
        # Print all li leftbar items
        print("Display from \"leftbar\" all <li> items (4 in total): ")
        for item in soup.find_all("div", {"class": "leftbar"}):
            unwanted = item.find("div", {"class": "hidden-phone"})
            unwanted.extract()
            item = str(item.text.strip())
            item = item.replace("\n", ",")
            item = item.split(",")
            for i in item:
                print("-", i)
        print("------------------------------------------------------------------")
        # Print all social media with its links
        print("Get and display all available social media with its links (href) \"class=social pull-right\": ")
        for link in soup.find_all("div", {"class": "social pull-right"}):
            for item in link.find_all("a", {"target": "_blank"}):
                print("-", item.get("href"))
        print("------------------------------------------------------------------")
        count = 0
        for i in soup.find_all("a"):
            i
            count+=1
        print("Count all <a>:", count)
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
        # Downlodea la imagen pero por alguna razón hay un problema al abrirlo. (Abre la imagen pero desaparece)
        for img in soup.find_all("img", {"class": "fl-photo-img wp-image-500 size-full"}):
            imgUrl = img.get("src")
            urllib.request.urlretrieve(imgUrl, os.path.basename(imgUrl))
        print("Downloading the \"FACULTAD de CIENCIAS ECONOMICAS\" logo: ", imgUrl)
        print("------------------------------------------------------------------")
        print("GET following <meta>: \"title\", \"description\" (\"og\"): ")
        for link in soup.find_all("meta", {"property": "og:title"}):
            print("\n-", link.get("content"))
        for link in soup.find_all("meta", {"property": "og:description"}):
            print("-", link.get("content"))
        print("------------------------------------------------------------------")
        # Print the count of all <a>
        count = 0
        for i in soup.find_all("a"):
            i
            count+=1
        print("Count all <a>:", count)
        print("------------------------------------------------------------------")
        # Print the count of all <div>
        count = 0
        for i in soup.find_all("div"):
            i
            count+=1
        print("Count all <div>:", count)
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
        print("Count all emails that start with a vowel:", count)
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
                var3 = cells[0].text
                var4 = cells[4].find(text = True).replace("\n", "").replace(",", "")
                var3 = " ".join(var3.split())
                var4 = " ".join(var4.split())
                # Replaces tildes to delete hex codes later on.
                var3 = var3.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                var4 = var4.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                # Adds results to lists
                page.append(var3)
                location.append(var4)
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
        print("Correlated Faculty Dean and Directors into JSON, dumping to logs/4directorio_deans.json")
        # Parse both tables.
        table3 = soup.find_all("table", {"class": "tabla ancho100 col3"})[1]
        # Create empty lists 
        dean = []
        faculty = []
        email = []
        phone = []
        # Checks data in table3
        for row in table3.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) == 3: # Not really necessary
                var5 = cells[0].text
                var6 = cells[1].find(text = True).replace("\n", "")
                var7 = cells[2].text
                var5 = " ".join(var5.split())
                var6 = " ".join(var6.split())
                var7 = " ".join(var7.split())
                # Replaces tildes to delete hex codes later on.
                var5 = var5.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                var6 = var6.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace(", decano", "")
                var7 = var7.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                var6 = "Dean/Director: " + var6
                var7 = "E-mail: " + var7
                if "Facultad" in var5:
                    faculty.append(var5)
                    dean.append(var6)
                    email.append(var7)

        # Compares the faculty with rows in first table, if they are found, gets the phone number for that row.
        faculty_var = str(faculty).replace("Facultad de", "").replace("[", "").replace("\'", "").replace("]", "")
        faculty_var = ' '.join(faculty_var.split())
        faculty_var = list(faculty_var.split(", "))
        table1 = soup.find("table", {"class": "tabla ancho100"})
        for i in faculty_var:
            for row in table1.find_all("tr"):
                cells = row.find_all("td")
                if len(cells) == 5: # Not really necessary
                    var9 = cells[2].text
                    var8 = cells[0].text
                    var9 = " ".join(var9.split())
                    var8 = " ".join(var8.split())
                    # Replaces tildes to delete hex codes later on.
                    var9 = var9.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                    var8 = var8.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                    # Adds results to lists
                    if i.replace("\n", "") == var8:
                        var9 = "Phone Number: " + var9
                        phone.append(var9)
        dictionary2 = dict((z[0], list(z[1:])) for z in zip(faculty, dean, email, phone))
        
        # Creates json and dumps result.
        json_string = json.dumps(dictionary2)
        datastore = json.loads(json_string)
        filename = "../p3soup/logs/4directorio_deans.json"
        if filename:
            with open(filename, mode = "w") as f:
                json.dump(datastore, f, indent = 4)   
        print("------------------------------------------------------------------")
        print("Generated CSV file with directories of all 3 column tables, dumping to logs/4directorio_3column_tables.csv")
        table1 = soup.find_all("table", {"class": "tabla ancho100 col3"})[0]
        table2 = soup.find_all("table", {"class": "tabla ancho100 col3"})[1]
        table3 = soup.find_all("table", {"class": "tabla ancho100 col3"})[2]
        # Create empty lists 
        entity = []
        fullname = []
        emails = []
        # Checks data in table1
        for row in table1.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) == 3: # Not really necessary
                var10 = cells[0].text
                var11 = cells[1].find(text = True).replace("\n", "").replace(",", "")
                var12 = cells[2].text
                var10 = " ".join(var10.split())
                var11 = " ".join(var11.split())
                var12 = " ".join(var12.split())
                if var11 is not "":
                    # Replaces tildes to delete hex codes later on.
                    var10 = var10.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                    var11 = var11.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                    var12 = var12.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                    # Adds results to lists
                    entity.append(var10)
                    fullname.append(var11)
                    emails.append(var12)
        # Checks data in table2
        for row in table2.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) == 3: # Not really necessary
                var10 = cells[0].text
                var11 = cells[1].find(text = True).replace("\n", "").replace(",", "")
                var12 = cells[2].text
                var10 = " ".join(var10.split())
                var11 = " ".join(var11.split())
                var12 = " ".join(var12.split())
                if var11 is not "":
                    # Replaces tildes to delete hex codes later on.
                    var10 = var10.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                    var11 = var11.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                    var12 = var12.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                    # Adds results to lists
                    entity.append(var10)
                    fullname.append(var11)
                    emails.append(var12)
        # Checks data in table3
        for row in table3.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) == 3: # Not really necessary
                var10 = cells[0].text
                var11 = cells[1].find(text = True).replace("\n", "").replace(",", "")
                var12 = cells[2].text
                var10 = " ".join(var10.split())
                var11 = " ".join(var11.split())
                var12 = " ".join(var12.split())
                if var11 is not "":
                    # Replaces tildes to delete hex codes later on.
                    var10 = var10.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                    var11 = var11.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                    var12 = var12.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                    # Adds results to lists
                    entity.append(var10)
                    fullname.append(var11)
                    emails.append(var12)

        # Creates csv file and dumps result
        n = 0
        filename = "../p3soup/logs/4directorio_3column_tables.csv"
        with open(filename, mode='w+') as f:          
            f_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            columnTitleRow = ["Entity", " Fullname", " Email"]
            f_writer.writerow(columnTitleRow)
            for i in entity:
                f_writer.writerow([entity[n], fullname[n], emails[n]])
                n += 1
        print("==================================================================")
        return 0

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
        print("Error in command line, please specify which part to run with 1 to 4 or leave blank to run all parts")
else:
    run.part1()
    run.part2()
    run.part3()
    run.part4()
