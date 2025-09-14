#!/usr/bin/env python3
"""
Baseten Enterprise Sales Intelligence Tool
Generate competitive analysis, positioning, and sales enablement materials
for selling to non-AI-native enterprise customers.
"""

import os
import requests
import json

class BasetenSalesIntelligence:
    def __init__(self):
        self.api_key = os.environ.get("BASETEN_API_KEY")
        if not self.api_key:
            raise ValueError("BASETEN_API_KEY environment variable not set")
        
        self.model = "deepseek-ai/DeepSeek-V3-0324"  # Using DeepSeek V3 for strategic analysis
    
    def _call_api(self, prompt, max_tokens=800, temperature=0.7):
        """Make API call to Baseten"""
        try:
            response = requests.post(
                "https://inference.baseten.co/v1/chat/completions",
                headers={
                    "Authorization": f"Api-Key {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": "You are a strategic business analyst specializing in AI infrastructure and enterprise sales. Provide detailed, actionable insights for B2B sales teams."},
                        {"role": "user", "content": prompt}
                    ],
                    "max_tokens": max_tokens,
                    "temperature": temperature
                }
            )
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
            else:
                return f"API Error: {response.text}"
                
        except Exception as e:
            return f"Error: {e}"
    
    def enterprise_pain_points_analysis(self, industry=""):
        """Analyze pain points for non-AI-native enterprises"""
        industry_context = f" in the {industry} industry" if industry else ""
        
        prompt = f"""
        Analyze the key pain points that traditional, non-AI-native enterprise customers{industry_context} face when considering AI adoption. These are companies with legacy infrastructure, traditional IT teams, and limited AI experience:

        1. AI ADOPTION BARRIERS:
        - "We don't know where to start with AI"
        - Fear of complex technical implementation
        - Uncertainty about which AI use cases to prioritize
        - Lack of internal AI talent and expertise
        - Concerns about disrupting existing business processes

        2. INFRASTRUCTURE CONCERNS:
        - Legacy systems integration challenges
        - Security and compliance requirements (SOC2, HIPAA, GDPR)
        - Existing vendor relationships and procurement processes
        - Budget approval processes for new technology categories
        - Risk aversion to "bleeding edge" technology

        3. BUSINESS JUSTIFICATION CHALLENGES:
        - Difficulty quantifying AI ROI
        - Unclear timeline for AI implementation and results
        - Competition priorities with other IT initiatives
        - Board/executive skepticism about AI hype
        - Pressure to show quick wins vs long-term transformation

        4. ORGANIZATIONAL READINESS:
        - IT teams without ML/AI experience
        - Resistance to change from existing teams
        - Skills gap and training requirements
        - Cross-departmental coordination for AI initiatives
        - Managing expectations across stakeholder groups

        For each area, provide:
        - How Baseten reduces complexity and risk for traditional enterprises
        - Positioning Baseten as "enterprise-grade" vs "startup technology"
        - Proof points that address conservative buyer concerns
        - Business case frameworks that resonate with traditional IT leadership

        Focus on positioning Baseten as the safe, enterprise-ready choice for companies taking their first serious steps into AI.
        """
        
        return self._call_api(prompt, max_tokens=1000)
    
    def competitive_analysis(self):
        """Generate enterprise-focused competitive analysis"""
        prompt = """
        Analyze the ML infrastructure competitive landscape for traditional enterprise IT teams evaluating AI solutions:

        1. ENTERPRISE EVALUATION CRITERIA:
        - Vendor stability and enterprise credibility
        - Security, compliance, and governance features
        - Integration with existing enterprise infrastructure
        - Support and professional services availability
        - Total cost of ownership vs complexity
        - Risk mitigation and business continuity

        2. COMPETITORS analyzed through enterprise IT lens:

        AWS SageMaker:
        - Strengths: Enterprise trust, comprehensive ecosystem, compliance certifications
        - Weaknesses: Complexity, steep learning curve, unpredictable costs, vendor lock-in

        Google Vertex AI:
        - Strengths: AI expertise, integrated platform, good documentation
        - Weaknesses: Limited enterprise sales support, complex pricing, newer in enterprise

        Azure ML:
        - Strengths: Microsoft relationship, enterprise integration, familiar tooling
        - Weaknesses: Performance concerns, limited model variety, Azure dependency

        Traditional vendors (IBM, Oracle, etc.):
        - Strengths: Enterprise relationships, professional services
        - Weaknesses: Legacy technology, high costs, slow innovation

        3. BASETEN'S ENTERPRISE POSITIONING:
        - "Enterprise-ready AI infrastructure without the complexity"
        - Faster deployment than cloud providers with enterprise security
        - Transparent, predictable pricing vs hyperscaler complexity
        - Proven reliability for companies deploying AI at scale
        - Professional support without vendor lock-in

        Format this for enterprise IT decision-makers and procurement teams.
        """
        
        return self._call_api(prompt, max_tokens=1000)

def main():
    """Interactive sales intelligence generator"""
    print("🎯 Baseten Enterprise Sales Intelligence Tool")
    print("=" * 60)
    
    try:
        analyzer = BasetenSalesIntelligence()
        
        print("\nSelect analysis type:")
        print("1. Enterprise Competitive Analysis")
        print("2. Non-AI-Native Enterprise Pain Points")
        
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "1":
            print("\n📊 ENTERPRISE COMPETITIVE ANALYSIS")
            print("=" * 50)
            result = analyzer.competitive_analysis()
            print(result)
            
        elif choice == "2":
            industry = input("Enter specific industry (optional): ").strip()
            print(f"\n💼 NON-AI-NATIVE ENTERPRISE PAIN POINTS")
            if industry:
                print(f"Industry Focus: {industry}")
            print("=" * 50)
            result = analyzer.enterprise_pain_points_analysis(industry)
            print(result)
            
        else:
            print("Please choose option 1 or 2")
            
        print(f"\n✅ Analysis complete!")
        print("\n💡 This tool demonstrates:")
        print("   • Strategic thinking for enterprise market expansion")
        print("   • Understanding of non-AI-native buyer concerns")
        print("   • Baseten API capabilities for business intelligence")
        
    except ValueError as e:
        print(f"❌ Setup Error: {e}")
        print("Please make sure your BASETEN_API_KEY environment variable is set.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
