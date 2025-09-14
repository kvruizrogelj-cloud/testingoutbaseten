#!/usr/bin/env python3
"""
Baseten Enterprise Sales Intelligence Tool
Generate competitive analysis, positioning, and sales enablement materials
building on Baseten's core messaging of "ML infrastructure that just works"
for enterprises scaling their AI workloads.
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
        """Analyze pain points for enterprises scaling AI workloads"""
        industry_context = f" in the {industry} industry" if industry else ""
        
        prompt = f"""
        Building on Baseten's core value proposition of "Machine learning infrastructure that just works" and "provide all the infrastructure you need to deploy and serve ML models performantly, scalably, and cost-efficiently," analyze pain points that enterprises{industry_context} face when scaling AI workloads:

        CONTEXT: Baseten currently serves dynamic AI companies like Abridge, OpenEvidence, Clay, Mirage, Zed, Gamma, Sourcegraph, Writer, and Bland who "use Baseten to power applications that reach hundreds of millions of users." The messaging is "we let them take performance and reliability for granted, so they can focus on what makes them unique."

        1. SCALING AND INFRASTRUCTURE PAIN POINTS:
        - Complex deployment processes that slow down AI initiatives
        - Performance bottlenecks with current cloud infrastructure
        - Unpredictable costs as AI workloads scale beyond pilot phase
        - DevOps overhead preventing teams from focusing on core product
        - Reliability concerns for mission-critical AI applications

        2. COMPETITIVE INFRASTRUCTURE CHALLENGES:
        - Hyperscaler complexity (AWS SageMaker, Google Vertex, Azure ML) vs "infrastructure that just works"
        - Token-based pricing creating budget uncertainty vs cost-efficient scaling
        - Vendor lock-in concerns vs flexible, optimized serving
        - Performance optimization requiring specialized expertise vs automated optimization

        3. ENTERPRISE-SPECIFIC REQUIREMENTS:
        - Need for enterprise-grade security and compliance
        - Integration with existing enterprise systems and workflows
        - Professional support and SLAs for production workloads
        - Risk management and vendor evaluation processes

        For each area, provide:
        - How Baseten's "infrastructure that just works" messaging addresses these challenges
        - Extensions of their current value proposition for enterprise buyers
        - Competitive positioning leveraging their performance and cost advantages
        - Business case frameworks building on their existing customer success stories

        Focus on how enterprises can achieve the same "focus on what makes them unique" benefit that current customers experience.
        """
        
        return self._call_api(prompt, max_tokens=1000)
    
    def competitive_analysis(self):
        """Generate enterprise-focused competitive analysis building on current Baseten positioning"""
        prompt = """
        Analyze the competitive landscape for Baseten's enterprise expansion, focusing on concrete technical advantages that translate to executive value:

        BASETEN'S ACTUAL TECHNICAL DIFFERENTIATORS:
        - 225% better cost-performance than hyperscalers (proven with Google Cloud A4 + NVIDIA Blackwell)
        - 2x higher throughput + 10% lower latency than any other solution (Baseten Embeddings Inference)
        - 6x better GPU usage + 50% latency reduction (Baseten Chains for compound AI)
        - 30-60x faster cold starts: 5-10 seconds vs 5 minutes industry standard
        - 60% performance improvement for custom LLMs (proven with Writer's Palmyra models)
        - Sub-400ms end-to-end latency for complex multi-model workflows (AI phone calls)
        - 99.99% uptime with multi-cloud deployment across regions

        EXECUTIVE IMPACT ANALYSIS:

        **AWS SageMaker vs Baseten:**
        - Technical Gap: AWS cold starts take 5 minutes, Baseten takes 10 seconds
        - CEO Impact: 30x faster deployment = faster market entry and competitive advantage
        - CTO Impact: Engineering team productivity, superior user experience delivery
        - CIO Impact: Reduced operational complexity vs AWS requiring specialized expertise
        - CFO Impact: 225% better cost-performance = significant budget optimization

        **Google Vertex AI vs Baseten:**
        - Technical Gap: Google lacks multi-cloud resilience, Baseten runs across all clouds
        - CEO Impact: Strategic flexibility vs vendor dependency that limits business options
        - CTO Impact: Technology independence while maintaining cutting-edge performance
        - CIO Impact: Business continuity protection vs catastrophic single-cloud failure risk
        - CFO Impact: Better vendor negotiation position vs Google Cloud lock-in pricing

        **Azure ML vs Baseten:**
        - Technical Gap: Azure legacy architecture vs Baseten's next-generation optimization
        - CEO Impact: Market-leading AI performance = differentiated customer experience
        - CTO Impact: Competitive product capabilities vs legacy technical constraints
        - CIO Impact: Modern infrastructure investment vs technical debt accumulation
        - CFO Impact: Performance improvements drive measurable user engagement and revenue

        STAKEHOLDER-SPECIFIC VALUE PROPOSITIONS:

        **CEO Value (Strategic Business Impact):**
        - Market advantage: Sub-400ms AI responses = industry-leading user experience
        - Competitive differentiation: 60% better AI performance vs competitors using standard solutions
        - Strategic flexibility: Multi-cloud deployment = avoid vendor dependency risks
        - Growth enablement: Proven scale (hundreds of millions of users) = confidence in expansion plans
        - Innovation speed: 30x faster deployment = capture market opportunities before competitors

        **CTO Value (Technology Strategy & Performance):**
        - Product competitive advantage through superior AI performance
        - Engineering team focus on innovation vs infrastructure maintenance
        - Technology risk mitigation through multi-cloud architecture
        - Proven reliability (99.99% uptime) protecting product reputation

        **CIO Value (Operations & Risk Management):**
        - Enterprise-proven scale and reliability
        - Business continuity through redundant multi-cloud deployment
        - Operational risk reduction with professional SLAs and support
        - Compliance and security for regulated industries

        **CFO Value (Financial Impact & ROI):**
        - 225% better cost-performance = quantifiable budget optimization
        - Faster time-to-market = accelerated revenue realization
        - Engineering cost efficiency = improved team ROI and resource allocation
        - Predictable pricing model vs consumption-based budget uncertainty

        ENTERPRISE PROOF POINTS:
        - Writer: 60% custom LLM performance improvement = competitive product advantage
        - Bland AI: Sub-400ms phone calls = breakthrough user experience capabilities
        - Scale validation: Hundreds of millions of users served = enterprise-grade reliability
        - Market leadership: Top performance rankings = technical credibility and market position

        Format this as executive briefing material with role-specific value propositions focused on strategic business outcomes.
        """
        
        return self._call_api(prompt, max_tokens=1200)

def main():
    """Interactive sales intelligence generator"""
    print("🎯 Baseten Enterprise Sales Intelligence Tool")
    print('Building on "ML infrastructure that just works"')
    print("=" * 60)
    
    try:
        analyzer = BasetenSalesIntelligence()
        
        print("\nCurrent Baseten messaging:")
        print("• Machine learning infrastructure that just works")
        print("• Fastest, most reliable model delivery network") 
        print("• Deploy and serve ML models performantly, scalably, cost-efficiently")
        print("• Let teams focus on what makes them unique")
        
        print("\nSelect enterprise expansion analysis:")
        print("1. Enterprise Competitive Analysis for AI Scaling")
        print("2. Pain Points for Enterprises Scaling AI Workloads")
        
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "1":
            print("\n📊 ENTERPRISE COMPETITIVE ANALYSIS")
            print("Building on current Baseten positioning")
            print("=" * 50)
            result = analyzer.competitive_analysis()
            print(result)
            
        elif choice == "2":
            industry = input("Enter specific industry (optional): ").strip()
            print(f"\n💼 ENTERPRISE PAIN POINTS ANALYSIS")
            print("Extending 'infrastructure that just works' messaging")
            if industry:
                print(f"Industry Focus: {industry}")
            print("=" * 50)
            result = analyzer.enterprise_pain_points_analysis(industry)
            print(result)
            
        else:
            print("Please choose option 1 or 2")
            
        print(f"\n✅ Analysis complete!")
        print("\n💡 This demonstrates:")
        print("   • Understanding of current Baseten messaging and positioning")
        print("   • Strategic thinking for enterprise market expansion")
        print("   • Evolution (not replacement) of existing value propositions")
        print("   • Baseten API capabilities for business intelligence")
        
    except ValueError as e:
        print(f"❌ Setup Error: {e}")
        print("Please make sure your BASETEN_API_KEY environment variable is set.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
