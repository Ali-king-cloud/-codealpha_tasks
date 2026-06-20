import os
import shutil
import re
import requests
from pathlib import Path

def organize_images():
    """Move all .jpg files from a folder to a new folder."""
    print("\n📁 IMAGE ORGANIZER")
    print("-" * 30)
    
    source = input("Enter source folder path: ").strip()
    if not os.path.exists(source):
        print("❌ Source folder not found!")
        return
    
    dest = os.path.join(source, "JPG_Images")
    os.makedirs(dest, exist_ok=True)
    
    moved = 0
    for filename in os.listdir(source):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            src_path = os.path.join(source, filename)
            if os.path.isfile(src_path):
                shutil.move(src_path, os.path.join(dest, filename))
                moved += 1
                print(f"  ✅ Moved: {filename}")
    
    print(f"\n📊 Total files moved: {moved}")
    print(f"📂 Destination: {dest}")

def extract_emails():
    """Extract all email addresses from a .txt file."""
    print("\n📧 EMAIL EXTRACTOR")
    print("-" * 30)
    
    source_file = input("Enter path to .txt file: ").strip()
    if not os.path.exists(source_file):
        print("❌ File not found!")
        return
    
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Email regex pattern
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)
    emails = list(set(emails))  # Remove duplicates
    
    if not emails:
        print("📭 No email addresses found.")
        return
    
    # Save to output file
    output_file = os.path.splitext(source_file)[0] + "_emails.txt"
    with open(output_file, 'w') as f:
        f.write("Extracted Email Addresses\n")
        f.write("=" * 30 + "\n\n")
        for email in sorted(emails):
            f.write(email + "\n")
        f.write(f"\nTotal: {len(emails)} emails found.\n")
    
    print(f"✅ Found {len(emails)} unique email(s):")
    for email in sorted(emails):
        print(f"  📧 {email}")
    print(f"\n💾 Saved to: {output_file}")

def scrape_webpage():
    """Scrape the title of a webpage and save it."""
    print("\n🌐 WEBPAGE TITLE SCRAPER")
    print("-" * 30)
    
    url = input("Enter webpage URL: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Extract title using regex
        title_match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else "No title found"
        
        # Save to file
        domain = re.sub(r'[^\w]', '_', url.split('/')[2])
        filename = f"{domain}_title.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"URL: {url}\n")
            f.write(f"Title: {title}\n")
            f.write(f"Status: {response.status_code}\n")
        
        print(f"\n✅ Title: {title}")
        print(f"💾 Saved to: {filename}")
        
    except requests.RequestException as e:
        print(f"❌ Error fetching page: {e}")

def main():
    print("=" * 50)
    print("    🤖 PYTHON TASK AUTOMATION SUITE")
    print("=" * 50)
    print("\nChoose a task:")
    print("  1. 📁 Organize .jpg images into a folder")
    print("  2. 📧 Extract emails from a text file")
    print("  3. 🌐 Scrape webpage title")
    print("  4. 🚪 Exit")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        organize_images()
    elif choice == "2":
        extract_emails()
    elif choice == "3":
        scrape_webpage()
    elif choice == "4":
        print("👋 Goodbye!")
    else:
        print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
