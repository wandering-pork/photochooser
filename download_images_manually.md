# How to Download Instagram Images Manually

Since automated scraping is blocked, here's the easiest manual approach:

## Method 1: Browser Extension (Fastest)
1. Install "DownloadGram" or "Instagram Downloader" extension for Chrome/Firefox
2. Visit https://www.instagram.com/heartlands.studio/
3. Click the download button on each post (appears when you hover)
4. Save 40 images to a folder like `E:\code\photo chooser\images\account_a\`

## Method 2: Online Tool
1. Go to https://downloadgram.com/ or https://inflact.com/downloader/instagram/photo/
2. For each photo:
   - Copy the Instagram post URL
   - Paste into the downloader
   - Download the image
3. Save to `E:\code\photo chooser\images\account_a\`

## Method 3: Browser Developer Tools (Most Control)
1. Open Instagram profile
2. Press F12 → Network tab → Filter by "Img"
3. Scroll to load photos
4. Right-click on image requests → "Open in new tab"
5. Right-click image → "Save image as..."

## After Downloading
Once you have ~40 images saved locally, the web app will reference them like:
```
images/account_a/photo1.jpg
images/account_a/photo2.jpg
...
```

I can modify the web app to use local file paths instead of URLs.
