#!/usr/bin/env python3
"""
Generate a new blog post for thecynic.ai

Usage:
    python3 generate-post.py "Post Title" "Description"
    python3 generate-post.py --auto-generate
"""

import sys
import os
import re
from datetime import date
from pathlib import Path

def slugify(title):
    """Convert a title to a URL-friendly slug"""
    # Convert to lowercase and replace spaces/special chars with hyphens
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')

def create_post(title, description, tags=None):
    """Create a new markdown blog post file"""
    
    if tags is None:
        tags = []
    
    slug = slugify(title)
    today = date.today()
    
    # Create the blog content directory
    blog_dir = Path.home() / 'thecynic.ai' / 'src' / 'content' / 'blog'
    blog_dir.mkdir(parents=True, exist_ok=True)
    
    # Create the filename
    filename = f"{slug}.md"
    filepath = blog_dir / filename
    
    # Check if file already exists
    if filepath.exists():
        print(f"Error: File {filename} already exists!")
        return False
    
    # Create the frontmatter and content template
    frontmatter = f"""---
title: "{title}"
description: "{description}"
date: {today}
tags: {tags}
draft: false
---

# {title}

[Write your post content here...]

🏮
"""
    
    # Write the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter)
    
    print(f"Created new blog post: {filepath}")
    print(f"Slug: {slug}")
    print(f"URL: /blog/{slug}")
    
    return True

def auto_generate_topic():
    """Generate a topic automatically (for cron job use)"""
    # This is where a cron job could call out to an AI service
    # For now, just return a placeholder
    topics = [
        ("The Pattern That Connects Everything", "How the same architectural failures repeat across every domain, from Roman aqueducts to modern APIs."),
        ("Enterprise Entropy: Why Systems Die", "The thermodynamics of business software: complexity always increases until maintenance becomes impossible."),
        ("The Honest Architecture Diagram", "What if we drew systems the way they actually work instead of how we wished they worked?"),
        ("Digital Cynicism in Practice", "Real-world lessons from applying ancient philosophy to modern technology problems."),
    ]
    
    import random
    return random.choice(topics)

def main():
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']):
        print(__doc__)
        return
    
    if len(sys.argv) == 2 and sys.argv[1] == '--auto-generate':
        title, description = auto_generate_topic()
        tags = ["patterns", "enterprise", "philosophy"]
        print(f"Auto-generating post: {title}")
        create_post(title, description, tags)
        return
    
    if len(sys.argv) < 3:
        print("Error: Please provide both title and description")
        print(__doc__)
        return
    
    title = sys.argv[1]
    description = sys.argv[2]
    
    # Optional tags
    tags = []
    if len(sys.argv) > 3:
        tags = sys.argv[3].split(',')
        tags = [tag.strip() for tag in tags]
    
    create_post(title, description, tags)

if __name__ == "__main__":
    main()