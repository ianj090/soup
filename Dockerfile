FROM python:3-alpine
ENV DEVELOPER="Ian Jenatz"
RUN pip install bs4
RUN pip install requests
RUN mkdir c:\documents\marro\computer_science_programs\p3soup
RUN mkdir /logs
RUN mkdir /images
COPY soup.py /documents/marro/computer_science_programs/p3soup/soup.py
CMD python /documents/marro/computer_science_programs/p3soup/soup.py