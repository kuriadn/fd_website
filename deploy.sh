#!/bin/bash
# deploy.sh

echo "🚀 Starting deployment process..."

# Check if there are changes
if [ -z "$(git status --porcelain)" ]; then
    echo "No changes to commit"
    exit 0
fi

# Add all changes
git add .

# Commit with timestamp or custom message
if [ -z "$1" ]; then
    COMMIT_MSG="Auto-update: $(date '+%Y-%m-%d %H:%M:%S')"
else
    COMMIT_MSG="$1"
fi

git commit -m "$COMMIT_MSG"

# Push to GitHub
git push origin main

echo "✅ Successfully pushed to GitHub!"
echo "🔄 Deploying to server..."

# SSH to server and pull changes
ssh fayvad@167.86.95.242 << 'EOF'
cd ~/projects/fd_website
git pull origin main
docker-compose down
docker-compose up -d --build
echo "✅ Deployment complete!"
EOF