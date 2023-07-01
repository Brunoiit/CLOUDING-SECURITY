with open('urls.txt', 'r') as file:
    urls = file.readlines()
    
for url in urls:
    # Assuming process(url) is the function which handles the URL analysis
    # It will contain your XSS analysis code by XSSScrapy
    process(url.strip())
