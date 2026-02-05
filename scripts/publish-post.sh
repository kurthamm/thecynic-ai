#!/bin/bash

# Exit on any error
set -e

# Change to the project directory
cd ~/thecynic.ai

echo "Building the site..."
npm run build

if [ $? -ne 0 ]; then
    echo "Build failed! Aborting deployment."
    exit 1
fi

echo "Build successful. Deploying to Cloudflare Pages..."

# Deploy to Cloudflare Pages
CLOUDFLARE_API_TOKEN=yiQ_vBDqABDzFYH2Uu8og3hsLtcGnaCQ9Nl5yOsL \
CLOUDFLARE_ACCOUNT_ID=29ac8fc102d8ebb2d8e080914e407a2d \
wrangler pages deploy dist --project-name thecynic-ai --branch main --commit-dirty=true

if [ $? -ne 0 ]; then
    echo "Deployment failed!"
    exit 1
fi

echo "Deployment successful! Committing and pushing changes..."

# Git commit and push
git add .
git commit -m "Automated blog post publish - $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main

echo "All done! Site updated and changes pushed to git."