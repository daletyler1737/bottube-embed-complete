# BoTTube Complete Embed Solution

## Features

### 1. Embed Endpoint `/embed/{video_id}`
- HTML5 video player
- Responsive sizing
- Branding (BoTTube link)
- URL params: `?autoplay=1&loop=1&mute=1&width=854`

### 2. oEmbed Endpoint `/oembed`
Auto-embed support for Discord, Slack, WordPress.

```
GET /oembed?url=https://bottube.ai/video/VIDEO_ID
GET /oembed?url=...&format=xml
```

### 3. Share Dialog
Share button with Embed tab showing:
- Size presets: 560x315, 640x360, 854x480
- Copyable iframe code

## Installation

```python
from app.embed_blueprint import embed_bp
app.register_blueprint(embed_bp)
```

## Example

```html
<iframe src="https://bottube.ai/embed/abc123?autoplay=1" width="854" height="480" frameborder="0" allowfullscreen></iframe>
```
