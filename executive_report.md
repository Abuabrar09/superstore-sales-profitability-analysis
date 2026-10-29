# Executive Summary — Superstore Sales & Profitability

## Objective
Demonstrate an end-to-end analysis workflow for a Business Data & Financial Analyst: data quality, financial KPIs, category/region performance, discount analysis, and management recommendations.

## Data and method
The project uses the Kaggle Sample Superstore transaction dataset. The analysis notebook calculates total sales, profit, profit margin, distinct orders/customers, units sold, category and regional results, subcategory profit, discount bands, and monthly trends. The exact results should be taken from a run of the notebook against the CSV version you download.

## Questions for management
- Are high-sales categories also delivering strong profit?
- Which subcategories have negative profit and need pricing/cost review?
- Are higher discount bands associated with lower profit margin?
- Which regions contribute the most absolute profit and which have the strongest margins?
- Are there seasonal patterns that should influence inventory and forecasting?

## Recommendations
1. Track profit and margin alongside revenue in every sales review.
2. Investigate loss-making subcategories at SKU level, including discount, shipping, cost, and return drivers where available.
3. Create discount approval thresholds tied to expected margin, not revenue alone.
4. Compare regions using both absolute profit and profit margin to distinguish scale from efficiency.
5. Monitor monthly KPIs and investigate material deviations from prior periods.

## Deliverables
- `analysis_notebook.py`: reproducible analysis script.
- `images/superstore_dashboard.png`: dashboard-style visual for portfolio presentation; verify figures against your exact source file before publishing.
- `README.md`: setup guide and LinkedIn project description.
