"""
Extract Instagram Post URLs from a Profile

This script extracts the URLs of all posts from an Instagram profile
by accessing Instagram's public API endpoint.

Usage:
    python extract_post_urls.py
"""

import requests
import json
import time

def get_user_id(username):
    """Get Instagram user ID from username"""
    url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-IG-App-ID': '936619743392459',  # Public Instagram web app ID
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': f'https://www.instagram.com/{username}/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            user_data = data.get('data', {}).get('user', {})
            user_id = user_data.get('id')

            # Get post edges
            edges = user_data.get('edge_owner_to_timeline_media', {}).get('edges', [])

            return user_id, edges, user_data
        else:
            print(f"Error: Status code {response.status_code}")
            return None, [], None

    except Exception as e:
        print(f"Error: {e}")
        return None, [], None


def extract_post_urls(username, max_posts=40):
    """Extract post URLs and image URLs from Instagram profile"""
    print(f"Fetching posts from @{username}...")

    user_id, edges, user_data = get_user_id(username)

    if not user_id:
        print("Failed to get user data")
        return [], []

    print(f"✓ Found user: {user_data.get('full_name', username)}")
    print(f"✓ Total posts: {user_data.get('edge_owner_to_timeline_media', {}).get('count', 0)}")

    post_urls = []
    image_urls = []

    # Extract from initial data
    for edge in edges[:max_posts]:
        node = edge.get('node', {})
        shortcode = node.get('shortcode')
        display_url = node.get('display_url')

        if shortcode:
            post_url = f"https://www.instagram.com/p/{shortcode}/"
            post_urls.append(post_url)

        if display_url:
            image_urls.append(display_url)

    print(f"✓ Extracted {len(post_urls)} post URLs")
    print(f"✓ Extracted {len(image_urls)} image URLs")

    return post_urls, image_urls


def save_to_file(urls, filename):
    """Save URLs to file"""
    with open(filename, 'w', encoding='utf-8') as f:
        for url in urls:
            f.write(f"{url}\n")
    print(f"✓ Saved to {filename}")


def generate_js_array(urls, variable_name, filename):
    """Generate JavaScript array"""
    js_code = f"// Auto-generated from Instagram profile\n"
    js_code += f"const {variable_name} = [\n"
    for url in urls:
        js_code += f"    '{url}',\n"
    js_code += "];\n"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(js_code)
    print(f"✓ JavaScript array saved to {filename}")


def download_images_from_urls(image_urls, username):
    """Download images from URLs"""
    import os
    from urllib.request import urlretrieve

    folder = f"images_{username}"
    os.makedirs(folder, exist_ok=True)

    print(f"\nDownloading images to '{folder}'...")

    for i, url in enumerate(image_urls, 1):
        try:
            filename = f"{folder}/photo_{i:03d}.jpg"
            urlretrieve(url, filename)
            print(f"Downloaded {i}/{len(image_urls)}: photo_{i:03d}.jpg")
            time.sleep(0.5)  # Be nice to Instagram servers
        except Exception as e:
            print(f"Error downloading image {i}: {e}")

    print(f"✓ Downloaded {i} images to '{folder}'")


if __name__ == "__main__":
    print("=" * 70)
    print("Instagram Post & Image URL Extractor")
    print("=" * 70)

    # Configuration
    USERNAME = "heartlands.studio"
    MAX_POSTS = 40

    print(f"\nProfile: @{USERNAME}")
    print(f"Max posts: {MAX_POSTS}\n")
    print("=" * 70 + "\n")

    # Extract URLs
    post_urls, image_urls = extract_post_urls(USERNAME, MAX_POSTS)

    if post_urls:
        # Save post URLs
        save_to_file(post_urls, f"post_urls_{USERNAME}.txt")

        # Save image URLs
        if image_urls:
            save_to_file(image_urls, f"image_urls_{USERNAME}.txt")
            generate_js_array(image_urls, "ACCOUNT_A_PHOTOS", f"photos_{USERNAME}.js")

        print("\n" + "=" * 70)
        print("SUCCESS!")
        print("=" * 70)
        print(f"\nExtracted {len(post_urls)} post URLs")
        print(f"Extracted {len(image_urls)} image URLs")

        print("\nFiles created:")
        print(f"  - post_urls_{USERNAME}.txt (list of post URLs)")
        print(f"  - image_urls_{USERNAME}.txt (list of image URLs)")
        print(f"  - photos_{USERNAME}.js (JavaScript array for web app)")

        # Ask if user wants to download
        print("\n" + "=" * 70)
        print("Next steps:")
        print("=" * 70)
        print("1. Copy the array from photos_{USERNAME}.js into script.js")
        print("2. OR download images locally (type 'yes' below)")

        download = input("\nDownload images to local folder? (yes/no): ").strip().lower()

        if download == 'yes' and image_urls:
            download_images_from_urls(image_urls, USERNAME)
            print("\n✓ All done! Images are ready to use.")
        else:
            print("\n✓ URLs are ready! Check the generated files.")

        print("=" * 70)
    else:
        print("\n" + "=" * 70)
        print("ERROR: Could not extract URLs")
        print("=" * 70)
        print("\nInstagram may be blocking the request.")
        print("Try the browser console method instead:")
        print("  1. Open bookmarklet.html")
        print("  2. Follow the console instructions")
        print("=" * 70)
