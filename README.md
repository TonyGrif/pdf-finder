# PDF-Finder
A Python program to locate links to PDFs found within a webpage from the command line.

## Requirements
* [Python 3.8+](https://www.python.org/)
* [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)

## Running Instructions
Ensure required packages are available first through pip.
```
pip install -r requirements.txt
```

The program can then be run following the syntax below.
```
./main.py [URI]
```

## Sample Execution
When run with `./main.py https://www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html` the first
two PDFs will output:
```
URI: http://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-jones-archiveit.pdf
Final URI: https://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-jones-archiveit.pdf
Content Length: 2639215 Bytes

URI: http://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-jones-off-topic.pdf
Final URI: https://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-jones-off-topic.pdf
Content Length: 3119205 Bytes
```
