#!/bin/bash
# setup-env.sh - Set up environment variables for a child agent
# Usage: ./setup-env.sh <child-name> <provider>

set -e

CHILD_NAME=$1
PROVIDER=$2

if [ -z "$CHILD_NAME" ] || [ -z "$PROVIDER" ]; then
    echo "Usage: ./setup-env.sh <child-name> <provider>"
    echo "Example: ./setup-env.sh mercury zai"
    exit 1
fi

# Convert to uppercase for env var
ENV_VAR_NAME="${CHILD_NAME^^}_API_KEY"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Setting up environment for $CHILD_NAME with $PROVIDER"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Determine shell config file
SHELL_CONFIG="$HOME/.bashrc"
if [ -n "$ZSH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
fi

# Check if already exists
if grep -q "export $ENV_VAR_NAME=" "$SHELL_CONFIG" 2>/dev/null; then
    echo "⚠️  $ENV_VAR_NAME already exists in $SHELL_CONFIG"
    echo "   To update, manually edit the file or remove the old entry first."
    exit 1
fi

# Prompt for API key
echo "Please provide your API key for $PROVIDER."
echo ""
read -s -p "API Key: " API_KEY
echo ""

if [ -z "$API_KEY" ]; then
    echo "❌ No API key provided. Aborting."
    exit 1
fi

# Add to shell config
echo "" >> "$SHELL_CONFIG"
echo "# $CHILD_NAME agent API key (added by family-birth-skill on $(date +%Y-%m-%d))" >> "$SHELL_CONFIG"
echo "export $ENV_VAR_NAME=\"$API_KEY\"" >> "$SHELL_CONFIG"

# Export for current session
export "$ENV_VAR_NAME"="$API_KEY"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Environment variable set: $ENV_VAR_NAME"
echo "✅ Added to $SHELL_CONFIG"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "To use in current terminal:"
echo "    source $SHELL_CONFIG"
echo ""
echo "Or start a new terminal session."
