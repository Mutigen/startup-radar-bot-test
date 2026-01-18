#!/bin/bash

# Test Script for Deployed Mock API
# Usage: ./test_deployment.sh https://your-app.vercel.app

set -e

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get URL from argument or prompt
if [ -z "$1" ]; then
    echo -e "${YELLOW}Enter your Vercel deployment URL:${NC}"
    read -p "URL: " DEPLOYMENT_URL
else
    DEPLOYMENT_URL=$1
fi

# Remove trailing slash
DEPLOYMENT_URL=${DEPLOYMENT_URL%/}

echo ""
echo "=========================================="
echo "  Testing Mock API Deployment"
echo "=========================================="
echo "URL: $DEPLOYMENT_URL"
echo ""

# Test 1: Health Check
echo -e "${YELLOW}Test 1: Health Check (GET /api/mock)${NC}"
RESPONSE=$(curl -s -w "\n%{http_code}" "$DEPLOYMENT_URL/api/mock")
HTTP_CODE=$(echo "$RESPONSE" | tail -1)
BODY=$(echo "$RESPONSE" | head -n -1)

if [ "$HTTP_CODE" -eq 200 ]; then
    echo -e "${GREEN}✓ Health check passed${NC}"
    echo "$BODY" | jq -r '.service, .version, .status' 2>/dev/null || echo "$BODY"
else
    echo -e "${RED}✗ Health check failed (HTTP $HTTP_CODE)${NC}"
    exit 1
fi

echo ""

# Test 2: Basic Scan
echo -e "${YELLOW}Test 2: Basic Scan (POST /api/mock)${NC}"
RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "$DEPLOYMENT_URL/api/mock" \
  -H "Authorization: Bearer demo-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":30,"max_results":5,"min_score":40}')

HTTP_CODE=$(echo "$RESPONSE" | tail -1)
BODY=$(echo "$RESPONSE" | head -n -1)

if [ "$HTTP_CODE" -eq 200 ]; then
    COUNT=$(echo "$BODY" | jq -r '.count' 2>/dev/null)
    echo -e "${GREEN}✓ Scan successful - Found $COUNT startups${NC}"

    # Show first result
    FIRST=$(echo "$BODY" | jq -r '.results[0].startup_name' 2>/dev/null)
    SCORE=$(echo "$BODY" | jq -r '.results[0].relevance_score' 2>/dev/null)
    echo "  Example: $FIRST (Score: $SCORE)"
else
    echo -e "${RED}✗ Scan failed (HTTP $HTTP_CODE)${NC}"
    echo "$BODY"
    exit 1
fi

echo ""

# Test 3: High Score Filter
echo -e "${YELLOW}Test 3: High Score Filter (min_score=60)${NC}"
RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "$DEPLOYMENT_URL/api/mock" \
  -H "Authorization: Bearer demo-key" \
  -H "Content-Type: application/json" \
  -d '{"days_back":90,"max_results":10,"min_score":60}')

HTTP_CODE=$(echo "$RESPONSE" | tail -1)
BODY=$(echo "$RESPONSE" | head -n -1)

if [ "$HTTP_CODE" -eq 200 ]; then
    COUNT=$(echo "$BODY" | jq -r '.count' 2>/dev/null)
    echo -e "${GREEN}✓ Filter test passed - Found $COUNT high-score startups${NC}"
else
    echo -e "${RED}✗ Filter test failed (HTTP $HTTP_CODE)${NC}"
    exit 1
fi

echo ""

# Test 4: Authentication Test
echo -e "${YELLOW}Test 4: Authentication Test (no token)${NC}"
RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "$DEPLOYMENT_URL/api/mock" \
  -H "Content-Type: application/json" \
  -d '{"days_back":30}')

HTTP_CODE=$(echo "$RESPONSE" | tail -1)

if [ "$HTTP_CODE" -eq 401 ]; then
    echo -e "${GREEN}✓ Authentication working - Unauthorized request rejected${NC}"
else
    echo -e "${RED}✗ Authentication test failed (Expected 401, got $HTTP_CODE)${NC}"
fi

echo ""
echo "=========================================="
echo -e "${GREEN}  All Tests Passed! ✓${NC}"
echo "=========================================="
echo ""
echo "Your mock API is working correctly!"
echo ""
echo "Share this with employers:"
echo "  URL: $DEPLOYMENT_URL/api/mock"
echo ""
echo "Test command:"
echo "  curl -X POST $DEPLOYMENT_URL/api/mock \\"
echo "    -H \"Authorization: Bearer demo-key\" \\"
echo "    -H \"Content-Type: application/json\" \\"
echo "    -d '{\"days_back\":30,\"max_results\":5,\"min_score\":40}'"
echo ""
