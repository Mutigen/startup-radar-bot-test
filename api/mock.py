"""
Startup Radar Bot - Mock API for Vercel Deployment
Version: 2.2 - Demo version for testing without API credits
UPDATED: January 2026 - Current dates
"""

from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime, timedelta

# Sample realistic startup data - UPDATED FOR 2026
MOCK_STARTUPS = [
    {
        'name': 'TechVision AI GmbH',
        'city': 'Berlin',
        'purpose': 'Development of AI-powered enterprise software solutions for process automation and data analytics in the manufacturing sector',
        'registration_date': '2026-01-05',
        'legal_form': 'GmbH',
        'postal_code': '10115',
        'register_type': 'HRB',
        'register_number': '234567'
    },
    {
        'name': 'CloudFlow Solutions UG',
        'city': 'München',
        'purpose': 'Cloud-based SaaS platform for workflow automation and project management for small and medium enterprises',
        'registration_date': '2025-12-20',
        'legal_form': 'UG',
        'postal_code': '80331',
        'register_type': 'HRB',
        'register_number': '345678'
    },
    {
        'name': 'DataMind Analytics GmbH',
        'city': 'Hamburg',
        'purpose': 'Big data analytics and machine learning solutions for retail and e-commerce businesses',
        'registration_date': '2026-01-10',
        'legal_form': 'GmbH',
        'postal_code': '20095',
        'register_type': 'HRB',
        'register_number': '456789'
    },
    {
        'name': 'FinTech Innovations AG',
        'city': 'Frankfurt',
        'purpose': 'Development of blockchain-based payment solutions and digital banking platforms for the European market',
        'registration_date': '2025-12-15',
        'legal_form': 'AG',
        'postal_code': '60306',
        'register_type': 'HRB',
        'register_number': '567890'
    },
    {
        'name': 'SmartLogistics Pro GmbH',
        'city': 'Darmstadt',
        'purpose': 'IoT and AI-driven logistics optimization software for supply chain management and warehouse automation',
        'registration_date': '2026-01-08',
        'legal_form': 'GmbH',
        'postal_code': '64283',
        'register_type': 'HRB',
        'register_number': '678901'
    },
    {
        'name': 'HealthTech Solutions UG',
        'city': 'Köln',
        'purpose': 'Digital health platform for telemedicine and patient data management with AI-supported diagnostics',
        'registration_date': '2025-12-28',
        'legal_form': 'UG',
        'postal_code': '50667',
        'register_type': 'HRB',
        'register_number': '789012'
    },
    {
        'name': 'EcoMobility GmbH',
        'city': 'Stuttgart',
        'purpose': 'Software solutions for electric vehicle fleet management and charging infrastructure optimization',
        'registration_date': '2026-01-03',
        'legal_form': 'GmbH',
        'postal_code': '70173',
        'register_type': 'HRB',
        'register_number': '890123'
    },
    {
        'name': 'CyberShield Security UG',
        'city': 'Düsseldorf',
        'purpose': 'Cybersecurity software and services for SMEs, including threat detection and data protection solutions',
        'registration_date': '2025-12-22',
        'legal_form': 'UG',
        'postal_code': '40210',
        'register_type': 'HRB',
        'register_number': '901234'
    },
    {
        'name': 'PropTech Ventures GmbH',
        'city': 'Leipzig',
        'purpose': 'Digital real estate platform connecting property owners with tenants using AI-powered matching algorithms',
        'registration_date': '2026-01-12',
        'legal_form': 'GmbH',
        'postal_code': '04103',
        'register_type': 'HRB',
        'register_number': '012345'
    },
    {
        'name': 'EdTech Learning Solutions UG',
        'city': 'Karlsruhe',
        'purpose': 'E-learning platform with adaptive learning technology and gamification for corporate training',
        'registration_date': '2025-12-18',
        'legal_form': 'UG',
        'postal_code': '76131',
        'register_type': 'HRB',
        'register_number': '123450'
    },
    {
        'name': 'RoboTech Automation GmbH',
        'city': 'Berlin',
        'purpose': 'Robotics and automation solutions for industrial manufacturing processes',
        'registration_date': '2025-11-25',
        'legal_form': 'GmbH',
        'postal_code': '10115',
        'register_type': 'HRB',
        'register_number': '234561'
    },
    {
        'name': 'GreenEnergy Digital UG',
        'city': 'München',
        'purpose': 'Software for renewable energy management and smart grid optimization',
        'registration_date': '2025-11-30',
        'legal_form': 'UG',
        'postal_code': '80331',
        'register_type': 'HRB',
        'register_number': '345672'
    },
    {
        'name': 'FoodTech Innovations GmbH',
        'city': 'Hamburg',
        'purpose': 'Online marketplace platform connecting local food producers with restaurants and consumers',
        'registration_date': '2025-11-15',
        'legal_form': 'GmbH',
        'postal_code': '20095',
        'register_type': 'HRB',
        'register_number': '456783'
    },
    {
        'name': 'InsurTech Connect AG',
        'city': 'Frankfurt',
        'purpose': 'Digital insurance brokerage platform with AI-powered risk assessment and personalized policy recommendations',
        'registration_date': '2025-10-28',
        'legal_form': 'AG',
        'postal_code': '60306',
        'register_type': 'HRB',
        'register_number': '567894'
    },
    {
        'name': 'SmartCity Solutions GmbH',
        'city': 'Darmstadt',
        'purpose': 'IoT platform for smart city infrastructure management and urban planning',
        'registration_date': '2025-11-05',
        'legal_form': 'GmbH',
        'postal_code': '64283',
        'register_type': 'HRB',
        'register_number': '678905'
    }
]


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Health Check Endpoint"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        week = datetime.now().isocalendar()[1]
        group = "A" if week % 2 == 0 else "B"

        response = {
            'status': 'online',
            'service': 'Startup Radar Bot (MOCK DEMO)',
            'version': '2.2.0 (Mock)',
            'coverage': '5 cities per run',
            'current_week': week,
            'current_group': group,
            'timestamp': datetime.now().isoformat(),
            'note': 'This is a DEMO API with sample data. No real API calls are made.',
            'github': 'https://github.com/Mutigen/startup-radar-bot-test',
            'demo_usage': {
                'method': 'POST',
                'headers': {
                    'Authorization': 'Bearer demo-key',
                    'Content-Type': 'application/json'
                },
                'body': {
                    'days_back': 30,
                    'max_results': 5,
                    'min_score': 40
                }
            }
        }

        self.wfile.write(json.dumps(response, ensure_ascii=False, indent=2).encode('utf-8'))
        return

    def do_POST(self):
        """Mock Scan Endpoint"""
        try:
            # Auth check (relaxed for demo - accepts any Bearer token)
            auth_header = self.headers.get('Authorization', '')
            if not auth_header.startswith('Bearer '):
                self.send_error(401, 'Unauthorized - Missing Bearer token')
                return

            # Read request body
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else '{}'
            params = json.loads(body) if body else {}

            # Extract parameters
            days_back = params.get('days_back', 30)
            max_results = params.get('max_results', 30)
            min_score = params.get('min_score', 20)

            # Filter startups based on days_back
            cutoff_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
            filtered = [s for s in MOCK_STARTUPS if s['registration_date'] >= cutoff_date]

            # Generate mock results
            results = []
            for startup in filtered:
                score = self.calculate_score(startup, days_back)

                if score >= min_score:
                    formatted = self.format_startup(startup, score)
                    results.append(formatted)

            # Sort by score and limit results
            results.sort(key=lambda x: x['relevance_score'], reverse=True)
            results = results[:max_results]

            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            response = {
                'success': True,
                'timestamp': datetime.now().isoformat(),
                'results': results,
                'count': len(results),
                'mock': True,
                'note': 'This is DEMO data for testing purposes. Real API uses Handelsregister.ai',
                'parameters_used': {
                    'days_back': days_back,
                    'max_results': max_results,
                    'min_score': min_score
                }
            }

            self.wfile.write(json.dumps(response, ensure_ascii=False, indent=2).encode('utf-8'))

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {
                'success': False,
                'error': str(e),
                'mock': True
            }
            self.wfile.write(json.dumps(error_response).encode())

    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Authorization, Content-Type')
        self.end_headers()

    def calculate_score(self, startup, days_back):
        """Calculate relevance score"""
        score = 0

        keywords = [
            'software', 'ki', 'ai', 'saas', 'deep tech', 'engineering',
            'logistik', 'cloud', 'data', 'analytics', 'app', 'plattform',
            'digital', 'innovation', 'tech', 'fintech', 'healthtech',
            'proptech', 'edtech', 'mobility', 'robotics', 'automation',
            'blockchain', 'iot', 'cybersecurity', 'machine learning'
        ]

        city_scores = {
            'Berlin': 20, 'München': 19, 'Hamburg': 18,
            'Frankfurt': 17, 'Darmstadt': 17, 'Köln': 16,
            'Stuttgart': 15, 'Düsseldorf': 14, 'Leipzig': 13, 'Karlsruhe': 14
        }

        # Company Age (30 points)
        reg_date = datetime.strptime(startup['registration_date'], '%Y-%m-%d')
        age_days = (datetime.now() - reg_date).days

        if age_days <= 30:
            score += 30
        elif age_days <= 90:
            score += 25
        elif age_days <= 180:
            score += 15
        elif age_days <= 365:
            score += 10

        # Tech Keywords (25 points)
        text = f"{startup['name']} {startup['purpose']}".lower()
        keyword_score = sum(2 for kw in keywords if kw in text)
        score += min(25, keyword_score)

        # City (20 points)
        score += city_scores.get(startup['city'], 10)

        # Legal Form (10 points)
        if startup['legal_form'] in ['GmbH', 'UG']:
            score += 10
        elif startup['legal_form'] == 'AG':
            score += 8

        # Purpose Length (15 points)
        if len(startup['purpose']) > 50:
            score += 15
        elif len(startup['purpose']) > 20:
            score += 10

        return min(score, 100)

    def format_startup(self, startup, score):
        """Format startup data"""
        priority = 'High' if score >= 70 else ('Medium' if score >= 40 else 'Low')

        tags = [startup['city']]
        purpose_lower = startup['purpose'].lower()

        if any(k in purpose_lower for k in ['software', 'app']):
            tags.append('Software')
        if any(k in purpose_lower for k in ['ki', 'ai', 'machine learning']):
            tags.append('KI/AI')
        if 'saas' in purpose_lower:
            tags.append('SaaS')
        if 'fintech' in purpose_lower:
            tags.append('FinTech')
        if 'healthtech' in purpose_lower or 'health' in purpose_lower:
            tags.append('HealthTech')
        if 'proptech' in purpose_lower or 'real estate' in purpose_lower:
            tags.append('PropTech')
        if 'edtech' in purpose_lower or 'learning' in purpose_lower:
            tags.append('EdTech')
        if 'logistik' in purpose_lower or 'logistics' in purpose_lower:
            tags.append('Logistics')

        entity_id = f"mock_{startup['register_type']}{startup['register_number']}"

        return {
            'startup_id': entity_id,
            'created_at': datetime.now().isoformat(),
            'processed': False,
            'relevance_score': score,
            'tags': ','.join(tags),
            'startup_name': startup['name'],
            'legal_name': startup['name'],
            'website': '',
            'linkedin_company_url': '',
            'country': 'DE',
            'city': startup['city'],
            'industry': 'Tech',
            'sub_industry': ', '.join(tags[1:]) if len(tags) > 1 else 'Software',
            'founded_year': startup['registration_date'][:4],
            'stage': 'Pre-Seed',
            'handelsregister_source': 'handelsregister.ai (DEMO)',
            'handelsregister_id': f"{startup['register_type']}{startup['register_number']}",
            'short_description': startup['purpose'][:200],
            'source': 'RadarBot v2.2 (DEMO)',
            'notes': f'Priority: {priority}, Score: {score}, DEMO DATA',
            'founder_name': '',
            'founder_linkedin_url': ''
        }
