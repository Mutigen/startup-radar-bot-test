"""
Startup Radar Bot - Vercel Serverless Function
Echte Integration mit Handelsregister.ai API
Version 2.2 - Rotation System (5 Städte pro Run)
"""

from http.server import BaseHTTPRequestHandler
import json
import os
from datetime import datetime, timedelta
import requests
import time

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        """Health Check Endpoint"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        week = datetime.now().isocalendar()[1]
        group = "A" if week % 2 == 0 else "B"
        
        response = {
            'status': 'online',
            'service': 'Startup Radar Bot',
            'version': '2.2.0 (Rotation)',
            'coverage': '5 cities per run',
            'current_week': week,
            'current_group': group,
            'timestamp': datetime.now().isoformat()
        }
        
        self.wfile.write(json.dumps(response).encode())
        return
    
    def do_POST(self):
        """Scan Endpoint"""
        try:
            # Auth
            api_key = os.getenv('API_KEY', '')
            auth_header = self.headers.get('Authorization', '')
            
            if not auth_header.startswith('Bearer ') or auth_header.split(' ')[1] != api_key:
                self.send_error(401, 'Unauthorized')
                return
            
            # Body
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else '{}'
            params = json.loads(body) if body else {}
            
            # HR API Key
            hr_api_key = os.getenv('HANDELSREGISTER_API_KEY', '')
            if not hr_api_key:
                self.send_error(500, 'HR API Key fehlt')
                return
            
            # Scan
            results = self.scan_startups(hr_api_key, params)
            
            # Response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                'success': True,
                'timestamp': datetime.now().isoformat(),
                'results': results,
                'count': len(results)
            }
            
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode())
    
    def get_cities_today(self):
        """Rotation: Gerade KW = Gruppe A, Ungerade KW = Gruppe B"""
        
        group_a = {
            'Berlin': '10115',
            'München': '80331',
            'Hamburg': '20095',
            'Frankfurt': '60306',
            'Darmstadt': '64283'
        }
        
        group_b = {
            'Köln': '50667',
            'Stuttgart': '70173',
            'Düsseldorf': '40210',
            'Leipzig': '04103',
            'Karlsruhe': '76131'
        }
        
        week = datetime.now().isocalendar()[1]
        
        if week % 2 == 0:
            return group_a, "A"
        else:
            return group_b, "B"
    
    def scan_startups(self, api_key, params):
        """Scannt 5 Städte"""
        
        days_back = params.get('days_back', 30)
        max_results = params.get('max_results', 30)
        min_score = params.get('min_score', 20)
        
        cities, group = self.get_cities_today()
        
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
        
        cutoff_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
        
        headers = {
            'x-api-key': api_key,
            'Content-Type': 'application/json'
        }
        
        all_startups = []
        
        print(f"Group {group}: {list(cities.keys())}")
        
        for city, plz in cities.items():
            try:
                print(f"Scanning {city}...")
                
                response = requests.get(
                    'https://handelsregister.ai/api/v1/search-organizations',
                    headers=headers,
                    params={
                        'q': 'GmbH',
                        'limit': 20,
                        'filters': json.dumps({'postal_code': plz})
                    },
                    timeout=10
                )
                
                if response.status_code == 200:
                    companies = response.json().get('results', [])
                    
                    for company in companies:
                        reg_date = company.get('registration_date', '')
                        if reg_date and reg_date >= cutoff_date:
                            
                            score = self.calc_score(company, keywords, city, city_scores)
                            
                            if score >= min_score:
                                startup = self.format_startup(company, score, city)
                                all_startups.append(startup)
                
                time.sleep(1.5)  # Rate limit
                
            except Exception as e:
                print(f"{city} error: {e}")
        
        all_startups.sort(key=lambda x: x['relevance_score'], reverse=True)
        return all_startups[:max_results]
    
    def calc_score(self, company, keywords, city, city_scores):
        """Score 0-100"""
        score = 0
        
        # Aktualität (30)
        reg_date_str = company.get('registration_date', '')
        if reg_date_str:
            try:
                days = (datetime.now() - datetime.fromisoformat(reg_date_str.replace('Z', '+00:00'))).days
                if days <= 30: score += 30
                elif days <= 90: score += 25
                elif days <= 180: score += 15
                elif days <= 365: score += 10
            except: pass
        
        # Keywords (25)
        text = f"{company.get('name', '')} {company.get('purpose', '')}".lower()
        score += min(25, sum(2 for kw in keywords if kw in text))
        
        # Stadt (20)
        score += city_scores.get(city, 10)
        
        # Rechtsform (10)
        legal = company.get('legal_form', '')
        if legal in ['GmbH', 'UG']: score += 10
        elif legal == 'AG': score += 8
        
        # Purpose (15)
        purpose = company.get('purpose', '')
        if len(purpose) > 50: score += 15
        elif len(purpose) > 20: score += 10
        
        return min(score, 100)
    
    def format_startup(self, company, score, city):
        """Format für Sheets"""
        
        priority = 'High' if score >= 70 else ('Medium' if score >= 40 else 'Low')
        
        tags = [city]
        purpose = company.get('purpose', '').lower()
        
        if any(k in purpose for k in ['software', 'app']): tags.append('Software')
        if any(k in purpose for k in ['ki', 'ai']): tags.append('KI/AI')
        if 'saas' in purpose: tags.append('SaaS')
        if 'fintech' in purpose: tags.append('FinTech')
        
        reg = company.get('registration', {})
        
        return {
            'startup_id': company.get('entity_id', f"t{int(datetime.now().timestamp())}"),
            'created_at': datetime.now().isoformat(),
            'processed': False,
            'relevance_score': score,
            'tags': ','.join(tags),
            'startup_name': company.get('name', ''),
            'legal_name': company.get('name', ''),
            'website': company.get('contact_data', {}).get('website', '') if company.get('contact_data') else '',
            'linkedin_company_url': '',
            'country': 'DE',
            'city': company.get('address', {}).get('city', city),
            'industry': 'Tech',
            'sub_industry': ', '.join(tags[1:]) if len(tags) > 1 else 'Software',
            'founded_year': company.get('registration_date', '')[:4] if company.get('registration_date') else '',
            'stage': 'Pre-Seed',
            'handelsregister_source': 'handelsregister.ai',
            'handelsregister_id': f"{reg.get('register_type', '')}{reg.get('register_number', '')}",
            'short_description': company.get('purpose', '')[:200],
            'source': 'RadarBot v2.2',
            'notes': f'Priority: {priority}, Score: {score}',
            'founder_name': '',
            'founder_linkedin_url': ''
        }
