#!/bin/bash
set -e

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

# Force push to overwrite remote
echo "📤 Force pushing to GitHub (overwriting remote)..."
if git push origin main --force; then
    echo "✅ Successfully force pushed to GitHub!"
else
    echo "❌ Failed to push to GitHub"
    exit 1
fi

echo "🔄 Restarting containers..."
docker-compose restart

echo "🎉 Deployment complete!"