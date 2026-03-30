from flask import Blueprint, render_template, request, jsonify
import re

embed_bp = Blueprint('embed', __name__)

@embed_bp.route('/embed/<video_id>')
def embed_player(video_id):
    width = request.args.get('width', 854)
    autoplay = request.args.get('autoplay', False)
    loop = request.args.get('loop', False)
    muted = request.args.get('muted', False)
    return render_template('embed.html', video_id=video_id, width=width, autoplay=autoplay, loop=loop, muted=muted, video_url=f'https://bottube.ai/video/{video_id}')

@embed_bp.route('/oembed')
def oembed():
    url = request.args.get('url', '')
    format = request.args.get('format', 'json')
    video_id = extract_video_id(url)
    if not video_id:
        return jsonify({'error': 'Invalid URL'}), 404
    if format == 'xml':
        xml = f'''<?xml version="1.0"?>
<oembed>
    <type>video</type>
    <title>BoTTube Video {video_id}</title>
    <html><iframe src="https://bottube.ai/embed/{video_id}" width="854" height="480" frameborder="0" allowfullscreen></iframe></html>
    <width>854</width><height>480</height>
    <provider_name>BoTTube</provider_name>
    <provider_url>https://bottube.ai</provider_url>
</oembed>'''
        return xml, 200, {'Content-Type': 'application/xml'}
    return jsonify({
        'type': 'video', 'version': '1.0',
        'title': f'BoTTube Video {video_id}',
        'html': f'<iframe src="https://bottube.ai/embed/{video_id}" width="854" height="480" frameborder="0" allowfullscreen></iframe>',
        'width': 854, 'height': 480,
        'provider_name': 'BoTTube', 'provider_url': 'https://bottube.ai'
    })

@embed_bp.route('/embed/<video_id>.json')
def embed_metadata(video_id):
    return jsonify({'video_id': video_id, 'embed_url': f'https://bottube.ai/embed/{video_id}'})

def extract_video_id(url):
    patterns = [r'bottube\.ai/video/([a-zA-Z0-9_-]+)', r'bottube\.ai/embed/([a-zA-Z0-9_-]+)']
    for pattern in patterns:
        match = re.search(pattern, url)
        if match: return match.group(1)
    return None
