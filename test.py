from bs4 import BeautifulSoup

def format_html(input_file, output_file):
    # Read the input HTML file
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Prettify the HTML
    formatted_html = soup.prettify()

    # Write the formatted HTML to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(formatted_html)

# Example usage
input_file = 'hehe.html'
output_file = 'chuong1.html'
format_html(input_file, output_file)
