# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 02:41:32 2025

@author: dtabo
"""

#CRISP-DM Data Analytics Proposals PDF Generator
#Generates a professional PDF report from the three business proposals

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.platypus import Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib import colors
from datetime import datetime

def create_pdf_report(filename=CRISP_DM_Analytics_Proposals.PDF):

#Creates a professional PDF report with CRISP-DM proposals

# Create the PDF document
doc = SimpleDocTemplate(
filename,
pagesize=letter,
rightMargin=72,
leftMargin=72,
topMargin=72,
bottomMargin=18,
)

# Container for the 'Flowable' objects
elements = []

# Define styles
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
'CustomTitle',
parent=styles['Heading1'],
fontSize=24,
textColor=colors.HexColor('#1a1a1a'),
spaceAfter=30,
alignment=TA_CENTER,
fontName='Helvetica-Bold'
)

subtitle_style = ParagraphStyle(
'CustomSubtitle',
parent=styles['Heading2'],
fontSize=16,
textColor=colors.HexColor('#444444'),
spaceAfter=12,
alignment=TA_CENTER,
)

h1_style = ParagraphStyle(
'CustomH1',
parent=styles['Heading1'],
fontSize=18,
textColor=colors.HexColor('#2c3e50'),
spaceAfter=12,
spaceBefore=12,
fontName='Helvetica-Bold'
)

h2_style = ParagraphStyle(
'CustomH2',
parent=styles['Heading2'],
fontSize=14,
textColor=colors.HexColor('#34495e'),
spaceAfter=10,
spaceBefore=10,
fontName='Helvetica-Bold'
)

h3_style = ParagraphStyle(
'CustomH3',
parent=styles['Heading3'],
fontSize=12,
textColor=colors.HexColor('#7f8c8d'),
spaceAfter=8,
spaceBefore=8,
fontName='Helvetica-Bold'
)

body_style = ParagraphStyle(
'CustomBody',
parent=styles['BodyText'],
fontSize=10,
textColor=colors.HexColor('#2c3e50'),
alignment=TA_JUSTIFY,
spaceAfter=6,
)

bullet_style = ParagraphStyle(
'CustomBullet',
parent=styles['BodyText'],
fontSize=10,
textColor=colors.HexColor('#2c3e50'),
leftIndent=20,
spaceAfter=4,
)

# Cover Page
elements.append(Spacer(1, 2*inch))
elements.append(Paragraph("DATA ANALYTICS STUDY PROPOSALS", title_style))
elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph("Using the CRISP-DM Framework", subtitle_style))
elements.append(Spacer(1, 0.5*inch))

# Cover page details
cover_data = [
["Prepared for:", "Three Strategic Business Initiatives"],
["Date:", datetime.now().strftime("%B %d, %Y")],
["Framework:", "CRISP-DM (Cross-Industry Standard Process for Data Mining)"],
]

cover_table = Table(cover_data, colWidths=[2*inch, 4*inch])
cover_table.setStyle(TableStyle([
('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
('FONTSIZE', (0, 0), (-1, -1), 11),
('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2c3e50')),
('ALIGN', (0, 0), (-1, -1), 'LEFT'),
('VALIGN', (0, 0), (-1, -1), 'TOP'),
('TOPPADDING', (0, 0), (-1, -1), 8),
('BOTTOMPADDING', (0, 0), (-1, -1), 8),
]))

elements.append(cover_table)
elements.append(PageBreak())

# Table of Contents
elements.append(Paragraph("TABLE OF CONTENTS", h1_style))
elements.append(Spacer(1, 0.2*inch))

toc_items = [
"1. Executive Summary",
"2. Proposal 1: 22nd Special Tactics Squadron",
"3. Proposal 2: Doorley Orchard Homes (DOH)",
"4. Proposal 3: MDMW - High-Alpine Training Center",
"5. Cross-Cutting Recommendations",
]

for item in toc_items:
elements.append(Paragraph(item, body_style))

elements.append(PageBreak())

# Executive Summary
elements.append(Paragraph("EXECUTIVE SUMMARY", h1_style))
elements.append(Spacer(1, 0.1*inch))

exec_summary = """
This report presents comprehensive data analytics study proposals for three distinct business 
initiatives, each utilizing the CRISP-DM (Cross-Industry Standard Process for Data Mining) 
framework. The CRISP-DM methodology provides a structured approach to data mining projects 
through six iterative phases: Business Understanding, Data Understanding, Data Preparation, 
Modeling, Evaluation, and Deployment.
"""

elements.append(Paragraph(exec_summary, body_style))
elements.append(Spacer(1, 0.2*inch))

# Business summaries
summaries = [
("<b>22nd Special Tactics Squadron:</b> Focuses on operational efficiency optimization within "
"budgetary constraints ($3.6M annual), utilizing predictive maintenance, resource allocation "
"models, and process mining to enhance mission readiness while navigating USAF bureaucracy."),

("<b>Doorley Orchard Homes:</b> Emphasizes rental price optimization, predictive maintenance, "
"and portfolio expansion strategy for a small property management business managing properties "
"in N. Las Vegas and University Place, WA."),

("<b>MDMW Training Center:</b> Requires extensive market feasibility analysis for a $27M investment "
"in a high-alpine training facility in Leadville, Colorado, with phased deployment across civilian "
"recreation, military training, and R&D operations.")
]

for summary in summaries:
elements.append(Paragraph(summary, body_style))
elements.append(Spacer(1, 0.1*inch))

elements.append(PageBreak())

# PROPOSAL 1: 22nd Special Tactics Squadron
elements.append(Paragraph("PROPOSAL 1: 22nd SPECIAL TACTICS SQUADRON", h1_style))
elements.append(Paragraph("Operational Efficiency & Resource Optimization", h2_style))
elements.append(Spacer(1, 0.1*inch))

# Business Understanding
elements.append(Paragraph("1. BUSINESS UNDERSTANDING", h2_style))

elements.append(Paragraph("<b>Business Objectives:</b>", h3_style))
objectives_sq = [
"Optimize resource allocation within $3.6M annual budget constraints",
"Identify process inefficiencies in deployment readiness and training cycles",
"Predict maintenance and equipment lifecycle costs",
"Reduce bureaucratic delays in procurement and operations",
"Enhance mission readiness through data-driven decision making"
]
for obj in objectives_sq:
elements.append(Paragraph(f"• {obj}", bullet_style))

elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("<b>Data Mining Goals:</b>", h3_style))
dm_goals_sq = [
"Develop predictive models for equipment failure and maintenance scheduling",
"Create resource allocation optimization models for personnel and equipment deployment",
"Identify patterns in bureaucratic bottlenecks and approval delays",
"Forecast budget utilization and identify cost-saving opportunities"
]
for goal in dm_goals_sq:
elements.append(Paragraph(f"• {goal}", bullet_style))

elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("<b>Success Criteria:</b>", h3_style))
success_sq = [
"15-20% reduction in equipment downtime",
"10% improvement in budget efficiency",
"25% reduction in procurement processing time",
"Improved mission readiness scores"
]
for criterion in success_sq:
elements.append(Paragraph(f"• {criterion}", bullet_style))

# Data Understanding
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("2. DATA UNDERSTANDING", h2_style))

elements.append(Paragraph("<b>Data Sources:</b>", h3_style))
data_sources_sq = [
"Mission logs and deployment records (frequency, duration, location, personnel)",
"Equipment maintenance records and failure logs",
"Training schedules, completion rates, and certification tracking",
"Budget expenditure data (procurement, maintenance, training, personnel)",
"Supply chain and logistics data",
"Personnel readiness and availability records",
"Procurement request timelines and approval chains",
"Equipment utilization rates"
]
for source in data_sources_sq:
elements.append(Paragraph(f"• {source}", bullet_style))

elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("<b>Initial Data Collection:</b>", h3_style))
collection_sq = [
"Extract 3-5 years of historical operational data",
"Gather equipment manufacturer specifications and warranty data",
"Collect training performance metrics",
"Document bureaucratic approval workflows"
]
for item in collection_sq:
elements.append(Paragraph(f"• {item}", bullet_style))

# Data Preparation
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("3. DATA PREPARATION", h2_style))

elements.append(Paragraph("<b>Data Cleaning:</b>", h3_style))
cleaning_sq = [
"Standardize mission classification codes",
"Remove duplicate maintenance entries",
"Handle missing values in equipment usage logs",
"Correct inconsistent date/time formats across systems"
]
for item in cleaning_sq:
elements.append(Paragraph(f"• {item}", bullet_style))

elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("<b>Feature Engineering:</b>", h3_style))
features_sq = [
"Equipment age and usage intensity scores",
"Personnel experience levels and specialization indices",
"Seasonal deployment patterns",
"Geographic combatant command demand metrics"
]
for item in features_sq:
elements.append(Paragraph(f"• {item}", bullet_style))

# Modeling
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("4. MODELING", h2_style))

elements.append(Paragraph("<b>Predictive Maintenance Models:</b>", h3_style))
models_sq = [
"Random Forest or Gradient Boosting for equipment failure prediction",
"Survival analysis for lifecycle modeling",
"Time series forecasting for spare parts demand"
]
for item in models_sq:
elements.append(Paragraph(f"• {item}", bullet_style))

elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("<b>Resource Optimization:</b>", h3_style))
optimization_sq = [
"Linear programming for budget allocation",
"Constraint satisfaction for personnel scheduling",
"Multi-objective optimization for deployment planning"
]
for item in optimization_sq:
elements.append(Paragraph(f"• {item}", bullet_style))

# Evaluation
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("5. EVALUATION", h2_style))

eval_text_sq = """
Model performance will be assessed against historical data with validation periods. 
Predictive maintenance models will be evaluated using precision, recall, and F1-scores. 
Optimization models will be tested against current performance baselines to calculate 
ROI and cost savings from implementation.
"""
elements.append(Paragraph(eval_text_sq, body_style))

# Deployment
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("6. DEPLOYMENT", h2_style))

elements.append(Paragraph("<b>Implementation Plan:</b>", h3_style))
deployment_sq = [
"Phase 1: Deploy predictive maintenance dashboard for critical equipment",
"Phase 2: Implement resource allocation optimization tool for quarterly planning",
"Phase 3: Rollout process monitoring system for procurement tracking"
]
for item in deployment_sq:
elements.append(Paragraph(f"• {item}", bullet_style))

elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("<b>Monitoring:</b>", h3_style))
monitoring_sq = [
"Monthly model performance reviews",
"Quarterly retraining with new operational data",
"Annual comprehensive model updates"
]
for item in monitoring_sq:
elements.append(Paragraph(f"• {item}", bullet_style))

elements.append(PageBreak())

# PROPOSAL 2: Doorley Orchard Homes
elements.append(Paragraph("PROPOSAL 2: DOORLEY ORCHARD HOMES", h1_style))
elements.append(Paragraph("Property Performance & Investment Strategy Analytics", h2_style))
elements.append(Spacer(1, 0.1*inch))

# Business Understanding
elements.append(Paragraph("1. BUSINESS UNDERSTANDING", h2_style))

elements.append(Paragraph("<b>Business Objectives:</b>", h3_style))
objectives_doh = [
"Maximize rental income and occupancy rates across portfolio",
"Optimize property maintenance costs and prevent major repairs",
"Identify optimal rental pricing strategy for University Place property",
"Evaluate expansion opportunities and ROI forecasting",
"Minimize vacancy periods and tenant turnover",
"Balance owner's military deployment schedule with property management demands"
]
for obj in objectives_doh:
elements.append(Paragraph(f"• {obj}", bullet_style))

elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("<b>Success Criteria:</b>", h3_style))
success_doh = [
"Achieve 95%+ occupancy rate",
"Reduce maintenance costs by 15%",
"Optimize University Place rental price within 5% of market maximum",
"Reduce tenant turnover by 20%",
"Identify 2-3 viable expansion opportunities within 18 months"
]
for criterion in success_doh:
elements.append(Paragraph(f"• {criterion}", bullet_style))

# Data Understanding
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("2. DATA UNDERSTANDING", h2_style))

elements.append(Paragraph("<b>Data Sources:</b>", h3_style))
data_sources_doh = [
"Rental income and payment history (N. Las Vegas property)",
"Maintenance and repair records with costs",
"Utility costs and consumption patterns",
"Local market rental listings (Zillow, Realtor.com, Apartments.com)",
"Neighborhood demographic and economic data (Census, local MLS)",
"Renovation costs and timeline for University Place property",
"Comparable property sales and rental data"
]
for source in data_sources_doh:
elements.append(Paragraph(f"• {source}", bullet_style))

# Data Preparation
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("3. DATA PREPARATION", h2_style))

elements.append(Paragraph("<b>Feature Engineering:</b>", h3_style))
features_doh = [
"Property age and condition indices",
"Distance to military bases (JBLM for University Place, Nellis for N. Las Vegas)",
"Neighborhood quality scores (schools, crime, amenities)",
"Seasonal demand indicators",
"Rental price momentum (market trend indicators)"
]
for item in features_doh:
elements.append(Paragraph(f"• {item}", bullet_style))

# Modeling
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("4. MODELING", h2_style))

elements.append(Paragraph("<b>Rental Price Optimization:</b>", h3_style))
models_doh = [
"Hedonic pricing models (regression) for University Place property",
"Competitive analysis using clustering of comparable properties",
"Time series forecasting for seasonal pricing adjustments"
]
for item in models_doh:
elements.append(Paragraph(f"• {item}", bullet_style))

elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("<b>Maintenance Prediction:</b>", h3_style))
maintenance_doh = [
"Survival analysis for major system replacements (HVAC, roof, appliances)",
"Regression models for monthly maintenance cost forecasting",
"Anomaly detection for unusual expense patterns"
]
for item in maintenance_doh:
elements.append(Paragraph(f"• {item}", bullet_style))

elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("<b>Investment Analysis:</b>", h3_style))
investment_doh = [
"Monte Carlo simulation for cash flow scenarios",
"Portfolio optimization for expansion strategy",
"Sensitivity analysis for key variables (vacancy rate, maintenance costs, appreciation)"
]
for item in investment_doh:
elements.append(Paragraph(f"• {item}", bullet_style))

# Evaluation & Deployment
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("5. EVALUATION", h2_style))

eval_text_doh = """
Models will be validated against actual market transactions and historical property performance. 
The business value will be quantified through increased revenue from optimized pricing, maintenance 
cost savings, and reduced vacancy rates. Scenario planning will assess the impact of owner deployments 
and various expansion strategies.
"""
elements.append(Paragraph(eval_text_doh, body_style))

elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("6. DEPLOYMENT", h2_style))

elements.append(Paragraph("<b>Implementation Timeline:</b>", h3_style))
deployment_doh = [
"Phase 1: Deploy rental pricing dashboard for University Place property (Q1 2025)",
"Phase 2: Implement predictive maintenance calendar (Q2 2025)",
"Phase 3: Launch tenant screening scorecard (Q3 2025)",
"Phase 4: Develop portfolio expansion evaluation tool (Q4 2025)"
]
for item in deployment_doh:
elements.append(Paragraph(f"• {item}", bullet_style))

elements.append(PageBreak())

# PROPOSAL 3: MDMW
elements.append(Paragraph("PROPOSAL 3: MDMW TRAINING CENTER", h1_style))
elements.append(Paragraph("High-Alpine Training Center Market Feasibility & Operations Analytics", h2_style))
elements.append(Spacer(1, 0.1*inch))

# Business Understanding
elements.append(Paragraph("1. BUSINESS UNDERSTANDING", h2_style))

elements.append(Paragraph("<b>Business Objectives:</b>", h3_style))
objectives_mdmw = [
"Validate market demand and revenue potential for $27M investment",
"Optimize pricing strategy across civilian and military service lines",
"Forecast cash flow and break-even timeline",
"Identify optimal launch sequence (civilian → military → R&D)",
"Maximize facility utilization across seasonal variations",
"Support fundraising and investor presentations with data-driven projections"
]
for obj in objectives_mdmw:
elements.append(Paragraph(f"• {obj}", bullet_style))

elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("<b>Success Criteria:</b>", h3_style))
success_mdmw = [
"Validate $27M investment with 7-10 year ROI projection",
"Achieve 70%+ facility utilization in peak season (Year 3)",
"Secure 2-3 military training contracts within first 24 months",
"Generate $500K+ in civilian revenue by Year 2",
"Establish 3+ R&D partnerships within 36 months"
]
for criterion in success_mdmw:
elements.append(Paragraph(f"• {criterion}", bullet_style))

# Data Understanding
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("2. DATA UNDERSTANDING", h2_style))

elements.append(Paragraph("<b>Market Data Sources:</b>", h3_style))
market_data_mdmw = [
"Competitor analysis (Silverton Mountain, CMH Heli-Skiing, AMGA guide services)",
"Tourism statistics for Leadville and Summit County",
"Heli-skiing market size and pricing data",
"Avalanche course enrollment trends (AIARE, AAA)",
"Military training expenditure data (DoD budget documents)"
]
for source in market_data_mdmw:
elements.append(Paragraph(f"• {source}", bullet_style))

elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("<b>Operational Data Sources:</b>", h3_style))
operational_data_mdmw = [
"Weather patterns and snow conditions (NOAA, CAIC)",
"Property listings and acquisition costs in Leadville area",
"Construction and renovation cost estimates",
"Staffing requirements and salary data (guides, pilots, instructors)",
"Equipment costs (helicopters, snowcats, avalanche safety gear)"
]
for source in operational_data_mdmw:
elements.append(Paragraph(f"• {source}", bullet_style))

# Data Preparation
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("3. DATA PREPARATION", h2_style))

elements.append(Paragraph("<b>Feature Engineering:</b>", h3_style))
features_mdmw = [
"Competitive positioning scores (price, quality, accessibility)",
"Seasonality multipliers for demand forecasting",
"Customer acquisition cost by channel (digital, referral, partnerships)",
"Equipment utilization efficiency ratios",
"Military contract probability scores based on relationship factors"
]
for item in features_mdmw:
elements.append(Paragraph(f"• {item}", bullet_style))

# Modeling
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("4. MODELING", h2_style))

elements.append(Paragraph("<b>Market Feasibility Models:</b>", h3_style))
feasibility_mdmw = [
"Demand forecasting using time series analysis (seasonal ARIMA)",
"Market sizing using top-down and bottom-up approaches",
"Customer segmentation using clustering (civilian vs military profiles)",
"Competitive positioning using perceptual mapping"
]
for item in feasibility_mdmw:
elements.append(Paragraph(f"• {item}", bullet_style))

elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("<b>Financial Projection Models:</b>", h3_style))
financial_mdmw = [
"Monte Carlo simulation for revenue and cost scenarios",
"Discounted cash flow (DCF) analysis for ROI calculation",
"Break-even analysis with sensitivity testing",
"Scenario planning (best case, base case, worst case)"
]
for item in financial_mdmw:
elements.append(Paragraph(f"• {item}", bullet_style))

elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("<b>Risk Assessment:</b>", h3_style))
risk_mdmw = [
"Decision tree analysis for launch sequence timing",
"Logistic regression for success probability factors",
"Survival analysis for business sustainability"
]
for item in risk_mdmw:
elements.append(Paragraph(f"• {item}", bullet_style))

# Evaluation
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("5. EVALUATION", h2_style))

eval_text_mdmw = """
The evaluation phase will focus on validating market size estimates through customer surveys 
and comparing projections to comparable businesses. Risk evaluation will identify and quantify 
the top 10 risk factors including weather variability, military budget cuts, competition, and 
regulatory challenges. A clear go/no-go decision framework will be established with success 
criteria for each business phase.
"""
elements.append(Paragraph(eval_text_mdmw, body_style))

# Deployment
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("6. DEPLOYMENT", h2_style))

elements.append(Paragraph("<b>Phased Implementation:</b>", h3_style))
deployment_mdmw = [
"Phase 1: Pre-Launch Analytics (Months 1-6) - Market intelligence dashboard and demand validation",
"Phase 2: Civilian Operations (Year 1-2) - Booking system and dynamic pricing model",
"Phase 3: Military Expansion (Year 2-3) - Contract pipeline tracker and training outcome measurement",
"Phase 4: R&D Operations (Year 3+) - Product development and partner relationship management"
]
for item in deployment_mdmw:
elements.append(Paragraph(f"• {item}", bullet_style))

elements.append(PageBreak())

# Cross-Cutting Recommendations
elements.append(Paragraph("CROSS-CUTTING RECOMMENDATIONS", h1_style))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph("Data Governance", h2_style))
governance = [
"Establish data collection protocols from day one",
"Implement consistent naming conventions and storage",
"Create data dictionaries and documentation",
"Ensure data security and compliance (especially for Squadron)"
]
for item in governance:
elements.append(Paragraph(f"• {item}", bullet_style))

elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("Analytical Capability Building", h2_style))
capability = [
"Start simple with descriptive analytics, evolve to predictive",
"Invest in training or hire analytical talent where budget allows",
"Leverage free/low-cost tools initially (Google Analytics, Excel, R, Python)",
"Build feedback loops to continuously improve models"
]
for item in capability:
elements.append(Paragraph(f"• {item}", bullet_style))

elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("Integration Opportunities", h2_style))
integration = [
"Squadron: Share best practices in operational efficiency with MDMW military training",
"DOH: Test MDMW property as potential expansion or partnership",
"MDMW: Leverage Squadron connections for military contracts",
"Cross-pollinate analytical approaches across all three ventures"
]
for item in integration:
elements.append(Paragraph(f"• {item}", bullet_style))

elements.append(Spacer(1, 0.3*inch))

# Conclusion
elements.append(Paragraph("CONCLUSION", h2_style))
conclusion_text = """
These CRISP-DM-based proposals provide structured frameworks for data-driven decision making 
across three diverse business contexts. Each proposal balances analytical rigor with practical 
implementation constraints, recognizing budget limitations, operational realities, and strategic 
priorities. The iterative nature of CRISP-DM ensures that insights from later phases can inform 
earlier decisions, creating a continuous improvement cycle that maximizes the value of data 
analytics investments.
"""
elements.append(Paragraph(conclusion_text, body_style))

# Build PDF
doc.build(elements)
print(f"PDF report generated successfully: {filename}")
return filename
```

if **name** == **main**:
# Generate the PDF
pdf_file = create_pdf_report()
print(f\nYour professional PDF report has been created: {pdf_file}”)
print(\nThe report includes:”)
print(” - Professional cover page”)
print(” - Table of contents”)
print(” - Executive summary”)
print(” - All three CRISP-DM proposals”)
print(” - Cross-cutting recommendations”)