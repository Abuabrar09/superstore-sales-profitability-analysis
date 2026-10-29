# Superstore Sales & Profitability Analysis

## Project overview
A portfolio project for a Business Data & Financial Analyst role. It examines retail sales, profit, margin, product categories, regions, discounting, and monthly performance using the Kaggle Sample Superstore dataset.

## Dataset
- Source: [Kaggle — Sample Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- Common file name: `Sample - Superstore.csv`
- Common version: 9,994 transaction rows, 21 columns, covering 2014–2017.
- The dataset is commonly used for learning and portfolio analytics; verify the file version and license on Kaggle before redistribution.

## Tools
Python, pandas, NumPy, Matplotlib; the output tables can also be imported into Excel or Power BI.

## Questions answered
1. What are total sales, profit, margin, order count, and units sold?
2. Which categories and regions generate the most sales and profit?
3. Which subcategories lose money?
4. How does discount level relate to profitability?
5. How do sales and profit change month by month?

## How to run
1. Download the CSV from the Kaggle link above.
2. Put `Sample - Superstore.csv` beside `analysis_notebook.py`.
3. Install dependencies: `pip install pandas numpy matplotlib jupyter`
4. Run `python analysis_notebook.py` or copy the code into a Jupyter notebook.
5. Review the exported CSV tables in the `outputs/` folder.

## Initial hypotheses to validate against the downloaded file
- Technology is expected to be a major contributor to sales and profit.
- Furniture can show a gap between sales volume and profit contribution.
- Some product subcategories may be loss-making.
- Heavy discounts may be associated with weaker profit outcomes.

These are hypotheses, not conclusions to publish without running the notebook on the exact downloaded file. The notebook calculates all measures directly from the source data.

## Business recommendations framework
- Review pricing, supplier costs, and discount approvals for negative-profit subcategories.
- Use profit margin alongside sales when evaluating products and regions.
- Test discount policy changes with controlled comparisons instead of assuming discounts cause losses.
- Build a monthly reporting cadence with sales, profit, margin, orders, and exception flags.

## LinkedIn project description
**Superstore Sales & Profitability Analysis | Python, Excel/Power BI**
Analyzed the Kaggle Sample Superstore retail dataset to assess sales and profitability by product category, subcategory, region, and discount band. Built data-quality checks, KPI summaries, trend charts, and exportable performance tables using Python (pandas, NumPy, Matplotlib). The project demonstrates how financial and operational data can be translated into recommendations on pricing, discount controls, and profit-focused decision-making.

## Important
The included dashboard image is a portfolio-style mockup based on commonly reported summary figures for the standard Sample Superstore dataset. Re-run the notebook against your downloaded file and replace any dashboard values that differ before claiming results publicly.
