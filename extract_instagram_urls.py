"""
Instagram Image URL Extractor

This script attempts to extract image URLs from an Instagram profile page.
Note: Instagram frequently changes their HTML structure and may require authentication.

Usage:
    python extract_instagram_urls.py

Requirements:
    pip install requests beautifulsoup4
"""

import requests
import json
import re

def extract_instagram_urls(username, num_posts=40):
    """
    Extract image URLs from an Instagram profile

    Args:
        username: Instagram username (e.g., 'heartlands.studio')
        num_posts: Number of posts to extract (default: 40)
    """
    url = f"https://www.instagram.com/{username}/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }

    try:
        print(f"Fetching Instagram profile: {username}")
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return []

        # Try to find JSON data embedded in the page
        image_urls = []

        # Method 1: Look for shared data in script tags
        pattern = r'window\._sharedData\s*=\s*({.*?});'
        match = re.search(pattern, response.text)

        if match:
            try:
                shared_data = json.loads(match.group(1))

                # Navigate through the JSON structure to find images
                # Note: Instagram's structure changes frequently
                if 'entry_data' in shared_data:
                    profile_page = shared_data.get('entry_data', {}).get('ProfilePage', [])
                    if profile_page:
                        user_data = profile_page[0].get('graphql', {}).get('user', {})
                        edges = user_data.get('edge_owner_to_timeline_media', {}).get('edges', [])

                        for edge in edges[:num_posts]:
                            node = edge.get('node', {})
                            display_url = node.get('display_url')
                            if display_url:
                                image_urls.append(display_url)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")

        # Method 2: Look for image URLs in meta tags and img tags
        if not image_urls:
            print("Trying alternative extraction method...")
            img_pattern = r'https://[^"\']*\.(?:jpg|jpeg|png|webp)[^"\']*'
            potential_urls = re.findall(img_pattern, response.text)

            # Filter for likely Instagram CDN URLs
            cdn_urls = [url for url in potential_urls if 'cdninstagram' in url or 'fbcdn' in url]

            # Remove duplicates and limit to num_posts
            image_urls = list(dict.fromkeys(cdn_urls))[:num_posts]

        if image_urls:
            print(f"\nSuccessfully extracted {len(image_urls)} image URLs!")
            return image_urls
        else:
            print("\nNo image URLs found. Instagram may require authentication or has changed its structure.")
            print("\nAlternative approaches:")
            print("1. Use Instagram's official API (requires registration)")
            print("2. Use third-party tools like Instaloader or instagram-scraper")
            print("3. Manually copy image URLs from the browser")
            return []

    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return []


def save_urls_to_file(urls, filename='instagram_urls.txt'):
    """Save URLs to a text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        for i, url in enumerate(urls, 1):
            f.write(f"{url}\n")
    print(f"\nURLs saved to {filename}")


def generate_js_array(urls, account_name='A'):
    """Generate JavaScript array code"""
    js_code = f"const ACCOUNT_{account_name}_PHOTOS = [\n"
    for url in urls:
        js_code += f"    '{url}',\n"
    js_code += "];\n"

    with open(f'account_{account_name}_urls.js', 'w', encoding='utf-8') as f:
        f.write(js_code)

    print(f"JavaScript array saved to account_{account_name}_urls.js")


if __name__ == "__main__":
    # Configuration
    USERNAME = "heartlands.studio"
    NUM_POSTS = 40

    print("=" * 60)
    print("Instagram Image URL Extractor")
    print("=" * 60)
    print("\nNote: Due to Instagram's restrictions, this may not work")
    print("without proper authentication. Consider using:")
    print("- Instaloader: pip install instaloader")
    print("- instagram-scraper: pip install instagram-scraper")
    print("=" * 60 + "\n")

    urls = extract_instagram_urls(USERNAME, NUM_POSTS)

    if urls:
        # Save to text file
        save_urls_to_file(urls)

        # Generate JavaScript array
        generate_js_array(urls, 'A')

        print("\n" + "=" * 60)
        print("Next steps:")
        print("1. Open account_A_urls.js")
        print("2. Copy the array code")
        print("3. Replace ACCOUNT_A_PHOTOS in script.js")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("RECOMMENDED ALTERNATIVE: Use Instaloader")
        print("=" * 60)
        print("\nInstall: pip install instaloader")
        print("\nUsage:")
        print("  instaloader --fast-update --no-videos heartlands.studio")
        print("\nThis will download images to a folder.")
        print("Then you can reference them locally in your web app.")
        print("=" * 60)
