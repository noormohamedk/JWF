# Image Setup Guide

## Overview
All image paths in `jwf.html` have been updated to use relative paths instead of local file paths. This allows the website to work properly when hosted online.

## Folder Structure Created
```
📁 jasoor-welfare-foundation.html/
  📁 assets/
    📁 images/
```

## Required Images
Add the following images to the `assets/images/` folder:

| Image Name | Expected Size | Project Type | Description |
|---|---|---|---|
| **education-scholarship.jpg** | 1200x800px | Education | Education & Scholarship Support program image |
| **youth-empowerment.jpg** | 1200x800px | Youth | Youth Empowerment Initiatives program image |
| **community-health.jpg** | 1200x800px | Health | Community Health Programs image |
| **social-impact-research.jpg** | 1200x800px | Research | Social Impact Research program image |
| **humanitarian-relief.jpg** | 1200x800px | Relief | Humanitarian Relief program image |

## Image Specifications

- **Format**: JPG or PNG (JPG recommended for photos, PNG for graphics)
- **Recommended Size**: 1200x800px (optimal for card layout)
- **File Size**: Keep under 300KB per image for fast loading
- **Quality**: High-resolution for crisp display across all devices

## How to Add Images

1. **Prepare your images** - Resize to 1200x800px if needed
2. **Copy images to folder** - Place them in `assets/images/`
3. **Verify filenames** - Ensure they match exactly:
   - `education-scholarship.jpg`
   - `youth-empowerment.jpg`
   - `community-health.jpg`
   - `social-impact-research.jpg`
   - `humanitarian-relief.jpg`

## CSS Responsive Settings

The CSS is already configured to handle images properly:
```css
.project-img {
  width: 100%;
  height: 240px;
  overflow: hidden;
  border-radius: 12px;
  background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
}

.project-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}
```

## Verification Checklist

✅ All 5 image files are in `assets/images/` folder
✅ Images are named exactly as specified above
✅ Images are 1200x800px or similar aspect ratio
✅ File sizes are optimized (under 300KB)
✅ Opening `jwf.html` in browser shows all images correctly
✅ Images load without broken link icons

## Optimization Tips

1. **Compress Images** - Use tools like TinyPNG or ImageOptim to reduce file size
2. **Consistent Style** - Try to maintain consistent visual style across all project images
3. **Alt Text** - Alt text is already set in HTML for accessibility
4. **Responsive Design** - Images will automatically scale on mobile and tablet devices

## Testing

After adding images:
1. Open `jwf.html` in your browser
2. Scroll to the "Featured Projects" section
3. Verify all 5 project cards display images
4. Check that images don't have broken link icons
5. Resize browser window to test responsiveness

## Browser Compatibility

The updated relative paths work in:
- ✅ All modern browsers (Chrome, Firefox, Safari, Edge)
- ✅ Local file system (file://)
- ✅ Web servers (http:/// or https://)
- ✅ Mobile browsers

## Next Steps

1. Add your images to `assets/images/` folder
2. Test in browser to verify all images load correctly
3. Deploy website to host - all relative paths will continue to work
