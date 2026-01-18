#!/usr/bin/env python3
"""
Test script for Startup Radar Bot Mock API
Usage: python test_mock_api.py
"""

import requests
import json
from datetime import datetime

# Configuration
BASE_URL = "http://localhost:8000/api/scan"
API_KEY = "test-key"

def print_header(text):
    """Print formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def print_result(success, message):
    """Print test result"""
    icon = "✅" if success else "❌"
    print(f"{icon} {message}")

def test_health_check():
    """Test GET /api/scan (health check)"""
    print_header("TEST 1: Health Check")

    try:
        response = requests.get(BASE_URL, timeout=5)
        data = response.json()

        if response.status_code == 200:
            print_result(True, f"Health check successful")
            print(f"   Service: {data.get('service')}")
            print(f"   Version: {data.get('version')}")
            print(f"   Status: {data.get('status')}")
            print(f"   Current Group: {data.get('current_group')}")
            return True
        else:
            print_result(False, f"Unexpected status code: {response.status_code}")
            return False

    except requests.exceptions.ConnectionError:
        print_result(False, "Connection failed - Is the mock server running?")
        print("   Start it with: python api/mock_scan.py")
        return False
    except Exception as e:
        print_result(False, f"Error: {e}")
        return False

def test_scan_basic():
    """Test POST /api/scan with basic parameters"""
    print_header("TEST 2: Basic Scan")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "days_back": 60,
        "max_results": 10,
        "min_score": 20
    }

    try:
        response = requests.post(BASE_URL, headers=headers, json=payload, timeout=10)
        data = response.json()

        if response.status_code == 200 and data.get('success'):
            count = data.get('count', 0)
            print_result(True, f"Scan successful - Found {count} startups")

            if count > 0:
                print("\n   Top 3 Results:")
                for i, startup in enumerate(data['results'][:3], 1):
                    print(f"   {i}. {startup['startup_name']}")
                    print(f"      City: {startup['city']} | Score: {startup['relevance_score']} | Tags: {startup['tags']}")

            return True
        else:
            print_result(False, f"Scan failed: {data.get('error', 'Unknown error')}")
            return False

    except Exception as e:
        print_result(False, f"Error: {e}")
        return False

def test_scan_high_score():
    """Test with high score filter"""
    print_header("TEST 3: High Score Filter (min_score=60)")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "days_back": 90,
        "max_results": 20,
        "min_score": 60
    }

    try:
        response = requests.post(BASE_URL, headers=headers, json=payload, timeout=10)
        data = response.json()

        if response.status_code == 200:
            count = data.get('count', 0)
            print_result(True, f"Found {count} high-score startups")

            if count > 0:
                scores = [s['relevance_score'] for s in data['results']]
                avg_score = sum(scores) / len(scores)
                print(f"   Average Score: {avg_score:.1f}")
                print(f"   Highest Score: {max(scores)}")
                print(f"   Lowest Score: {min(scores)}")

            return True
        else:
            print_result(False, f"Test failed")
            return False

    except Exception as e:
        print_result(False, f"Error: {e}")
        return False

def test_scan_recent():
    """Test with recent startups only"""
    print_header("TEST 4: Recent Startups (last 30 days)")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "days_back": 30,
        "max_results": 15,
        "min_score": 30
    }

    try:
        response = requests.post(BASE_URL, headers=headers, json=payload, timeout=10)
        data = response.json()

        if response.status_code == 200:
            count = data.get('count', 0)
            print_result(True, f"Found {count} recent startups")

            if count > 0:
                cities = {}
                for startup in data['results']:
                    city = startup['city']
                    cities[city] = cities.get(city, 0) + 1

                print("\n   Distribution by City:")
                for city, cnt in sorted(cities.items(), key=lambda x: x[1], reverse=True):
                    print(f"   - {city}: {cnt}")

            return True
        else:
            print_result(False, f"Test failed")
            return False

    except Exception as e:
        print_result(False, f"Error: {e}")
        return False

def test_unauthorized():
    """Test without authorization header"""
    print_header("TEST 5: Authentication Test")

    # Test without Bearer token
    try:
        response = requests.post(BASE_URL, json={}, timeout=5)

        if response.status_code == 401:
            print_result(True, "Unauthorized request correctly rejected")
            return True
        else:
            print_result(False, f"Expected 401, got {response.status_code}")
            return False

    except Exception as e:
        print_result(False, f"Error: {e}")
        return False

def test_data_structure():
    """Test response data structure"""
    print_header("TEST 6: Data Structure Validation")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "days_back": 60,
        "max_results": 1,
        "min_score": 20
    }

    required_fields = [
        'startup_id', 'startup_name', 'city', 'relevance_score',
        'tags', 'industry', 'founded_year', 'handelsregister_id',
        'short_description', 'country', 'created_at'
    ]

    try:
        response = requests.post(BASE_URL, headers=headers, json=payload, timeout=10)
        data = response.json()

        if response.status_code == 200 and data.get('count', 0) > 0:
            startup = data['results'][0]
            missing_fields = [field for field in required_fields if field not in startup]

            if not missing_fields:
                print_result(True, "All required fields present")
                print(f"   Total fields: {len(startup)}")
                return True
            else:
                print_result(False, f"Missing fields: {missing_fields}")
                return False
        else:
            print_result(False, "No results to validate")
            return False

    except Exception as e:
        print_result(False, f"Error: {e}")
        return False

def run_all_tests():
    """Run all tests and print summary"""
    print("\n" + "🧪" * 30)
    print("   STARTUP RADAR BOT - MOCK API TEST SUITE")
    print("🧪" * 30)

    tests = [
        ("Health Check", test_health_check),
        ("Basic Scan", test_scan_basic),
        ("High Score Filter", test_scan_high_score),
        ("Recent Startups", test_scan_recent),
        ("Authentication", test_unauthorized),
        ("Data Structure", test_data_structure),
    ]

    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print_result(False, f"{name} crashed: {e}")
            results.append((name, False))

    # Print summary
    print_header("TEST SUMMARY")

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        icon = "✅" if result else "❌"
        print(f"{icon} {name}")

    print("\n" + "-" * 60)
    print(f"   PASSED: {passed}/{total}")
    print(f"   FAILED: {total - passed}/{total}")
    print(f"   SUCCESS RATE: {(passed/total)*100:.1f}%")
    print("-" * 60)

    if passed == total:
        print("\n🎉 All tests passed! Mock API is working correctly.")
    else:
        print("\n⚠️  Some tests failed. Check the output above for details.")

    return passed == total

if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
