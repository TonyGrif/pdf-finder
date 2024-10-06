# PDF-Finder
A Python program to locate links to PDFs found within a webpage from the command line.

## Running with Docker
First, build the image using `docker build -t pdf-finder`.
Upon completion, run `docker run pdf-finder [URI]`.

## Running with Poetry
Ensure required packages are available first through poetry using `poetry install`.
The program can then be run following the syntax: `poetry run python main.py [URI]`.

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
