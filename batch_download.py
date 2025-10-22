"""
Instagram Batch Image Downloader

Downloads images from a list of Instagram post URLs.

Usage:
    python batch_download.py

Requirements:
    pip install requests beautifulsoup4
"""

import requests
import re
import os
import time
from urllib.parse import urlparse

def extract_shortcode(url):
    """Extract shortcode from Instagram URL"""
    match = re.search(r'/p/([A-Za-z0-9_-]+)', url)
    if match:
        return match.group(1)
    return None

def get_image_url_from_post(shortcode):
    """
    Fetch the image URL from an Instagram post

    This tries multiple methods to extract the image URL
    """
    methods = [
        lambda: method_oembed(shortcode),
        lambda: method_page_scrape(shortcode),
        lambda: method_direct_url(shortcode),
    ]

    for method in methods:
        try:
            image_url = method()
            if image_url:
                return image_url
        except Exception as e:
            print(f"  Method failed: {e}")
            continue

    return None

def method_oembed(shortcode):
    """Try Instagram oEmbed API (public posts only)"""
    url = f"https://api.instagram.com/oembed/?url=https://www.instagram.com/p/{shortcode}/"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # oEmbed doesn't give direct image URL, but we can try thumbnail
            thumbnail = data.get('thumbnail_url')
            if thumbnail:
                # Convert thumbnail to full size
                return thumbnail.replace('/150x150/', '/1080x1080/')
    except:
        pass

    return None

def method_page_scrape(shortcode):
    """Scrape the Instagram page for image URL"""
    url = f"https://www.instagram.com/p/{shortcode}/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            # Look for image URLs in the page
            image_pattern = r'https://[^"\']*\.(?:jpg|jpeg)[^"\']*'
            matches = re.findall(image_pattern, response.text)

            # Filter for Instagram CDN URLs
            cdn_images = [m for m in matches if 'cdninstagram' in m or 'fbcdn' in m]

            if cdn_images:
                # Get the largest/best quality
                largest = max(cdn_images, key=len)
                return largest
    except Exception as e:
        print(f"  Page scrape error: {e}")

    return None

def method_direct_url(shortcode):
    """Try direct media URL patterns"""
    possible_urls = [
        f"https://www.instagram.com/p/{shortcode}/media/?size=l",
        f"https://instagram.com/p/{shortcode}/media/",
    ]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    for url in possible_urls:
        try:
            response = requests.head(url, headers=headers, allow_redirects=True, timeout=5)
            if response.status_code == 200:
                return response.url
        except:
            continue

    return None

def download_image(image_url, output_path):
    """Download image from URL to file"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://www.instagram.com/',
    }

    try:
        response = requests.get(image_url, headers=headers, timeout=30, stream=True)
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
        else:
            print(f"  Error: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"  Download error: {e}")
        return False

def process_url_list(url_file, output_dir='downloaded_images'):
    """Process a list of URLs from a text file"""

    # Read URLs from file
    if not os.path.exists(url_file):
        print(f"Error: File '{url_file}' not found")
        return

    with open(url_file, 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip() and 'instagram.com' in line]

    if not urls:
        print("No Instagram URLs found in file")
        return

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    print(f"Found {len(urls)} URLs to process")
    print(f"Output directory: {output_dir}")
    print("=" * 70)

    successful = 0
    failed = 0

    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] Processing: {url}")

        # Extract shortcode
        shortcode = extract_shortcode(url)
        if not shortcode:
            print("  ✗ Invalid URL format")
            failed += 1
            continue

        print(f"  Shortcode: {shortcode}")

        # Get image URL
        print("  Fetching image URL...")
        image_url = get_image_url_from_post(shortcode)

        if not image_url:
            print("  ✗ Could not extract image URL")
            failed += 1
            continue

        print(f"  ✓ Found image URL")

        # Download image
        output_path = os.path.join(output_dir, f"instagram_{shortcode}.jpg")
        print(f"  Downloading to: {output_path}")

        if download_image(image_url, output_path):
            print(f"  ✓ Successfully downloaded!")
            successful += 1
        else:
            print(f"  ✗ Download failed")
            failed += 1

        # Be nice to Instagram servers
        if i < len(urls):
            time.sleep(2)

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total URLs: {len(urls)}")
    print(f"✓ Successful: {successful}")
    print(f"✗ Failed: {failed}")
    print(f"\nImages saved to: {os.path.abspath(output_dir)}")
    print("=" * 70)

def interactive_mode():
    """Interactive mode for entering URLs"""
    print("=" * 70)
    print("Instagram Batch Downloader - Interactive Mode")
    print("=" * 70)
    print("\nEnter Instagram post URLs (one per line)")
    print("Press Enter twice when done, or type 'done'")
    print("=" * 70 + "\n")

    urls = []
    while True:
        url = input().strip()
        if not url or url.lower() == 'done':
            if not urls:
                print("\nNo URLs entered. Exiting...")
                return
            break
        if 'instagram.com/p/' in url:
            urls.append(url)
            print(f"  ✓ Added ({len(urls)} total)")
        else:
            print("  ✗ Invalid Instagram URL")

    # Save to temp file
    temp_file = 'temp_urls.txt'
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(urls))

    print(f"\n✓ Collected {len(urls)} URLs")

    # Process
    process_url_list(temp_file)

    # Clean up
    os.remove(temp_file)

if __name__ == "__main__":
    print("=" * 70)
    print("Instagram Batch Image Downloader")
    print("=" * 70)
    print("\nOptions:")
    print("1. Load URLs from file (urls.txt)")
    print("2. Enter URLs interactively")
    print("=" * 70 + "\n")

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == '1':
        filename = input("Enter filename (default: urls.txt): ").strip() or 'urls.txt'
        process_url_list(filename)
    elif choice == '2':
        interactive_mode()
    else:
        print("Invalid choice. Exiting...")
