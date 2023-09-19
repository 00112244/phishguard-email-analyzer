import os
import re
import argparse
from prettytable import PrettyTable
import pyfiglet
from colorama import Fore, Style

# List of phishing keywords to detect in email content and links
phishing_keywords = ['verify', 'account', 'password', 'compromised', 'urgent']

# Function to analyze email content for phishing keywords
def analyze_email_content(content):
    for keyword in phishing_keywords:
        if re.search(rf'\b{keyword}\b', content, re.I):
            return "Phishing"
    return "Legitimate"

# Function to analyze email links for phishing keywords
def analyze_email_links(link):
    for keyword in phishing_keywords:
        if re.search(rf'\b{keyword}\b', link, re.I):
            return "Potentially phishing link"
    return "Legitimate link"

# Function to read email content and links from a text file
def read_email_content_and_links(file_path):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Check if the file has a .txt extension
        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() != '.txt':
            raise ValueError("Invalid file format. Please provide a .txt file.")

        with open(file_path, 'r') as file:
            content = file.read()
            if not content.strip():
                raise ValueError("File is empty.")
        return content
    except PermissionError:
        raise PermissionError(f"Permission denied to open file: {file_path}")
    except ValueError as ve:
        raise ValueError(f"Error: {ve}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

# Function to print the analysis results
def print_analysis_results(email_content_analysis, link_analysis):
    content_table = PrettyTable()
    content_table.field_names = ["Analysis", "Reason"]
    content_table.add_row([email_content_analysis, "Phishing keyword found in email content." if email_content_analysis == "Phishing" else "No phishing keyword found in email content."])

    link_table = PrettyTable()
    link_table.field_names = ["Analysis", "Reason"]
    link_table.add_row([link_analysis, "Phishing keyword found in the link." if link_analysis == "Potentially phishing link" else "No phishing keyword found in the link."])

    print("Email Content Analysis:")
    print(content_table)

    print("\nLink Analysis:")
    print(link_table)

# Function to print a styled name
def print_name(text, font="standard", color="white", style=""):
    try:
        custom_text = pyfiglet.Figlet(font=font).renderText(text)
        style_code = {"bold": 1, "italic": 3, "underline": 4}.get(style, 0)
        colored_text = f"\033[{style_code};{30 + ['black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white'].index(color)}m{custom_text}\033[0m"
        print(colored_text)
    except pyfiglet.FontNotFound:
        print(f"Font '{font}' not found. Available fonts: {pyfiglet.FigletFont.getFonts()}")

# Function to print a welcome message inside a rectangle
def print_welcome_message():
    welcome_message = "Welcome to the Email Analysis Tool!\nThis tool allows you to analyze email for phishing and spoof mails."
    print_text_in_rectangle(welcome_message, text_color=Fore.GREEN)
    print("                                 A tool for email phishing and spoofing analyzer")
    print("                                                      By: Hariharan (00112244)\n")


# Function to print text inside a rectangle
def print_text_in_rectangle(text, text_color=Fore.WHITE):
    box_width, box_height = 80, 5
    border_horizontal = f"{Fore.WHITE}+{'-' * (box_width - 2)}+{Style.RESET_ALL}"
    empty_line = f"{Fore.WHITE}|{' ' * (box_width - 2)}|{Style.RESET_ALL}"

    boxed_text = [border_horizontal]
    boxed_text.extend(f"{Fore.WHITE}| {text_color}{Style.BRIGHT}{line.center(box_width - 4)}{Style.RESET_ALL} |{Style.RESET_ALL}" for line in text.splitlines())
    boxed_text.extend([empty_line] * (box_height - len(text.splitlines()) - 1) + [border_horizontal])

    print("\n".join(boxed_text))

# Main function to handle command line arguments and initiate the analysis
def main():
    parser = argparse.ArgumentParser(description="Analyze email content and links for phishing and spoof mails.")
    parser.add_argument("file_path", nargs='?', help="Path to the text file containing email content and links.")
    
    args = parser.parse_args()

    if args.file_path:
        # Print a name using the print_name function
        print_name("PhishGuard Email Anlayzer", font="standard", color="green", style="bold")

        try:
            email_content_and_links = read_email_content_and_links(args.file_path)
        except (FileNotFoundError, PermissionError, ValueError, Exception) as e:
            print(f"Error: {e}")
            exit(1)

        if email_content_and_links is not None:
            email_content_analysis = analyze_email_content(email_content_and_links)
            link_analysis = analyze_email_links(email_content_and_links)
            print_analysis_results(email_content_analysis, link_analysis)
    else:
        # Print a name using the print_name function
        print_name("PhishGuard Email Anlayzer", font="standard", color="green", style="bold")

        # Display boxed welcome message
        print_welcome_message()

if __name__ == "__main__":
    main()
