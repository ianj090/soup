#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests, sys, csv, json
from os.path import isfile as file_exist
import re

# url variables
url1 = "http://ufm.edu/Portal"
url2 = "http://ufm.edu/Estudios"
url3 = "https://fce.ufm.edu/carrera/cs/"
url4 = "http://ufm.edu/Directorio"

# print if needed, gets too noisy
# print(soup.prettify())

print("<Ian Jenatz>")

#if output > 30 lines:
#    print("Output exceeds 30 lines, sending output to <logfile>")
#    saber

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
        for data in soup.find_all("div", {"class": "container"}):
            phone = "missing phone"
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
        for link in soup.find_all("a"):
            print("\n-", link.get("href"))
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
        for link in soup.find_all("img"):
            print("\n-", link.get("src"))
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
        # for item in soup.find_all("div", {"class": "menu-key"}):
        #     print("\n-", item.get("data-menu"))
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
        for link in soup.find_all("a"):
            print("\n-", link.get("href"))
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
        for tr in soup.find_all("table", {"class": "tabla ancho100"}):
            match = re.findall(r"[\w\.-]+@[\w\.-]+", tr.text)
            #match.sort()
            for word in match:
                if word[0] in ["a","e","i","o","u","A","E","I","O","U"]:
                    count += 1
        print("Sort emails alphabetically:", match)
        print("------------------------------------------------------------------")
        print("count all emails:", count)
        print("------------------------------------------------------------------")
        # tables = soup.findChildren("table")
        # my_table = tables[1]
        # rows = my_table.findChildren(["th", "tr"])
        # for row in rows:
        #     cells = row.findChildren("td")
        #     for cell in cells:
        #         value = cell.text
        #         print("The value in this cell is %s" % value)
        
        
        #print(soup.findChildren("table"))
        print("==================================================================")
        return 0
    # def excedes_30_lines(self):
    #     a = Soup()
    #     a.part3()
    #     with open(filename="log.txt",mode=-"w") as f:
    #         f.write() #ccomo parametro mandale todo 
    #         pass

run = Soup()
#if argument == 1:
#    run.part1()
#elif argument == 2:
#    run.part2()
#elif argument == 3:
#    run.part3()
#elif argument == 4:
#    run.part4()
#else:
#    run.part1()
#    run.part2()
#    run.part3()
#    run.part4()
run.part4()