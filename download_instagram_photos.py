"""
Instagram Photo Downloader using Instaloader

This script downloads photos from Instagram profiles using Instaloader library.

Installation:
    pip install instaloader

Usage:
    python download_instagram_photos.py
"""

import instaloader
import os
import json

def download_instagram_photos(username, max_posts=40):
    """
    Download photos from an Instagram profile

    Args:
        username: Instagram username
        max_posts: Maximum number of posts to download
    """
    # Create an Instaloader instance
    loader = instaloader.Instaloader(
        download_videos=False,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False,
        compress_json=False,
        post_metadata_txt_pattern=''
    )

    print(f"Downloading photos from @{username}...")
    print(f"Target: {max_posts} posts\n")

    try:
        # Load the profile
        profile = instaloader.Profile.from_username(loader.context, username)

        # Create directory for photos
        photo_dir = f"photos_{username}"
        os.makedirs(photo_dir, exist_ok=True)

        # Download posts
        photo_urls = []
        count = 0

        for post in profile.get_posts():
            if count >= max_posts:
                break

            if not post.is_video:
                # Download the post
                loader.download_post(post, target=photo_dir)

                # Get the image URL
                photo_urls.append(post.url)
                count += 1
                print(f"Downloaded {count}/{max_posts}: {post.shortcode}")

        print(f"\n✓ Successfully downloaded {count} photos to '{photo_dir}' folder")

        # Save URLs to file
        save_urls(photo_urls, username)

        # Generate JavaScript code
        generate_js_code(photo_urls, username)

        return photo_urls

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Error: Profile @{username} does not exist")
        return []
    except instaloader.exceptions.ConnectionException:
        print("Error: Connection failed. Check your internet connection.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


def save_urls(urls, username):
    """Save URLs to a text file"""
    filename = f"urls_{username}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        for url in urls:
            f.write(f"{url}\n")
    print(f"✓ URLs saved to {filename}")


def generate_js_code(urls, username):
    """Generate JavaScript array for the web app"""
    filename = f"urls_{username}.js"

    js_code = f"// Photo URLs for @{username}\n"
    js_code += f"const ACCOUNT_PHOTOS = [\n"
    for url in urls:
        js_code += f"    '{url}',\n"
    js_code += "];\n"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(js_code)

    print(f"✓ JavaScript array saved to {filename}")
    print("\nCopy the array from this file and paste it into script.js")


def generate_local_references(username, max_posts=40):
    """Generate file paths for locally downloaded images"""
    photo_dir = f"photos_{username}"

    if not os.path.exists(photo_dir):
        print(f"Error: Directory '{photo_dir}' not found")
        return []

    # Get all jpg files
    image_files = [f for f in os.listdir(photo_dir) if f.endswith('.jpg')][:max_posts]

    # Generate relative paths
    local_paths = [f"photos_{username}/{filename}" for filename in image_files]

    # Generate JavaScript code
    js_code = f"// Local photo paths for @{username}\n"
    js_code += f"const ACCOUNT_PHOTOS = [\n"
    for path in local_paths:
        js_code += f"    '{path}',\n"
    js_code += "];\n"

    filename = f"local_paths_{username}.js"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(js_code)

    print(f"✓ Local paths saved to {filename}")
    return local_paths


if __name__ == "__main__":
    print("=" * 70)
    print("Instagram Photo Downloader")
    print("=" * 70)

    # Configuration
    USERNAME = "heartlands.studio"
    MAX_POSTS = 40

    print(f"\nProfile: @{USERNAME}")
    print(f"Max posts: {MAX_POSTS}")
    print("\nNote: This will download photos to your computer.")
    print("Instagram may rate-limit requests if you download too many.\n")
    print("=" * 70 + "\n")

    # Download photos
    urls = download_instagram_photos(USERNAME, MAX_POSTS)

    if urls:
        print("\n" + "=" * 70)
        print("SUCCESS!")
        print("=" * 70)
        print("\nNext steps:")
        print(f"1. Check the 'photos_{USERNAME}' folder for downloaded images")
        print(f"2. Open 'urls_{USERNAME}.js' to see the photo URLs")
        print("3. Copy the array and replace ACCOUNT_A_PHOTOS in script.js")
        print("\nOR use local files:")
        print(f"- Move the photos_{USERNAME} folder to your web app directory")
        print("- Use the local file paths instead of URLs")
        print("=" * 70)
