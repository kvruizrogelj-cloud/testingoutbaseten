# Baseten Enterprise Sales Intelligence Tool

Strategic analysis tool built with Baseten's Model APIs to generate competitive intelligence and positioning frameworks for selling AI infrastructure to traditional enterprises.

## What It Does

- Analyzes pain points of non-AI-native enterprise customers
- Generates competitive positioning vs AWS, Google, Azure for conservative buyers  
- Creates enterprise-focused value propositions and business cases
- Develops risk mitigation messaging for traditional IT leadership

## Built For

Product marketing teams selling to traditional enterprises who are early in their AI journey (vs AI-native startups). Focuses on companies with legacy infrastructure, procurement processes, and limited AI experience.

## Requirements

- Python 3.7+
- Baseten API key from [app.baseten.co](https://app.baseten.co)
- `requests` library: `pip install requests`

## Setup & Usage

1. Get your Baseten API key and set environment variable:
```bash
   export BASETEN_API_KEY="your_key_here"

2. Install dependencies

  pip install -r requirements.txt

3. Run the tool:

   python3 baseten_enterprise_intelligence.py

4. Choose from analysis options:
- Enterprise competitive analysis
- Non-AI-native enterprise pain points

