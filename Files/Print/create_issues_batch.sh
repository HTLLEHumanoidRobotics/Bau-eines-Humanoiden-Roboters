#!/bin/bash
# Script to create GitHub issues in batch for all printing parts
# Requires: GitHub CLI (gh) to be installed and authenticated

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
JSON_FILE="${SCRIPT_DIR}/issue_templates/printing_issues.json"
REPO="HTLLEHumanoidRobotics/Bau-eines-Humanoiden-Roboters"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo -e "${RED}Error: GitHub CLI (gh) is not installed.${NC}"
    echo "Please install it from: https://cli.github.com/"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo -e "${RED}Error: Not authenticated with GitHub CLI.${NC}"
    echo "Please run: gh auth login"
    exit 1
fi

# Check if JSON file exists
if [ ! -f "$JSON_FILE" ]; then
    echo -e "${RED}Error: JSON file not found: $JSON_FILE${NC}"
    echo "Please run: python3 generate_print_issues.py"
    exit 1
fi

echo -e "${BLUE}╔════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Batch GitHub Issue Creator for Printing Parts    ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════╝${NC}"
echo ""

# Parse JSON and count issues
TOTAL_ISSUES=$(jq -r '.count' "$JSON_FILE")
echo -e "${YELLOW}Total issues to create: ${TOTAL_ISSUES}${NC}"
echo ""

# Ask for confirmation
echo -e "${YELLOW}This will create ${TOTAL_ISSUES} issues in the repository: ${REPO}${NC}"
read -p "Do you want to proceed? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    echo -e "${RED}Aborted.${NC}"
    exit 0
fi

echo ""
echo -e "${GREEN}Creating issues...${NC}"
echo ""

# Create issues
CREATED=0
FAILED=0

# Read issues from JSON and create them
jq -c '.issues[]' "$JSON_FILE" | while read -r issue; do
    TITLE=$(echo "$issue" | jq -r '.title')
    BODY=$(echo "$issue" | jq -r '.body')
    LABELS=$(echo "$issue" | jq -r '.labels | join(",")')
    
    echo -n "Creating issue: $TITLE ... "
    
    if gh issue create \
        --repo "$REPO" \
        --title "$TITLE" \
        --body "$BODY" \
        --label "$LABELS" &> /dev/null; then
        echo -e "${GREEN}✓${NC}"
        ((CREATED++))
    else
        echo -e "${RED}✗${NC}"
        ((FAILED++))
    fi
    
    # Small delay to avoid rate limiting
    sleep 0.5
done

echo ""
echo -e "${GREEN}╔════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║                    Summary                         ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════╝${NC}"
echo -e "Total issues: ${TOTAL_ISSUES}"
echo -e "${GREEN}Successfully created: ${CREATED}${NC}"
if [ $FAILED -gt 0 ]; then
    echo -e "${RED}Failed: ${FAILED}${NC}"
fi
echo ""
echo -e "${BLUE}View issues at: https://github.com/${REPO}/issues${NC}"
