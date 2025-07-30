PROJECT TITTLE: India Import and Export Analysis(1997-2022)

📽️Project Overview:
This project provides a comprehensive analysis of India's import and export data from 1997 to 2022. The data was sourced, cleaned, and transformed using Python (Pandas and NumPy), stored in an SQLite database, and finally visualized using Power BI for interactive insights. The entire project, including the data and scripts, is managed using Git and hosted on GitHub.


⚙️ Tools/technologies used:
Python: Pandas, NumPy, SQLite3
Database: SQLite
Business Intelligence: Microsoft Power BI
Version Control: Git, GitHub


LINE CHARTS:

📊 Power BI Line Chart – India Import vs Export (1997–2022)

🔹 1. Purpose
To analyze trade trends over 25 years.
Compare the growth and gaps between imports and exports.
Identify trade surplus or deficit patterns.

🔹 2. Data Setup
X-axis: Year (1997 to 2022).
Y-axis: Value in USD Billion (or INR Crore).
Legend: Import, Export (two lines).

🔹 3. Key Insights You Can Show
📈 Trend Analysis: How trade volume evolved.
🟥 Trade Deficit Periods: When imports > exports.
🟩 Trade Surplus/Improvement: Years when the gap reduced.


📌 Important Events Impacting Trade:
2008 Global Recession
2016 Demonetization
2020 COVID-19
2022 Russia-Ukraine war impact on oil import bills

🔹 4. Visual Features to Use
Dual-line chart: One for Exports, one for Imports.
Markers: Highlight major events (tooltip or annotation).
Data labels (optional): For peak values.
Custom tooltip: Show year-wise details on hover.


🔹 5. Customizations
Format Y-axis with currency (₹ or $).
Color Exports (e.g., green) and Imports (e.g., red).
Add slicer for filtering by decade or government era.


 LINE CHARTS SCREENSHOT LINK:https://postimg.cc/R3tTXY67 


TREEMAP CHARTS:

🧩 Treemap Chart – Power BI Overview (India Trade Data)

🔹 1. Purpose
Visualize hierarchical or categorical data.
Show proportions within a whole (e.g., top exporting sectors).
Quickly compare the size of each category.

🔹 2. Data Setup (India Trade Example)

         Use Case                                Treemap Setup Example
 📦 Top Export Commodities              Category: CommodityValues: Export Value
 🌍 Top Importing Countries              Category: CountryValues: Import Value
 📊 Sector-wise Trade Share              Group: SectorCategory: SubsectorValues:   Trade   value
                                        
                                        

🔹 3. Key Insights You Can Sho
🏭 Which sectors dominate India’s exports (e.g., Petroleum, Textiles, IT).
🌎 Which countries are India’s biggest trade partners.
🔄 Compare import vs export share by category.

🔹 4. Features
Size of rectangle = value (e.g., export amount).
Color can show:
Different categories (by default)
Conditional formatting (e.g., trade surplus in green, deficit in red).
Tooltips show detailed data on hover.

🔹 5. Best Practices
Use for relative comparison, not for trends.
Combine with slicers (e.g., Year, Type: Import/Export).
Limit the number of categories shown to avoid clutter.

🔹 6. Example Analysis Titles
✅ “Country-wise Share of India’s Imports (1997–2022)”
✅ “Sectoral Contribution to India's Export Growth”


TREEMAP CHARTS SCREENSHOT LINK :  https://postimg.cc/R69wGZzm



WATERFALL CHARTS:

🌊 Waterfall Chart – Power BI Overview (India Trade Data)

🔹 1. Purpose
Shows incremental changes in values over time or across categories.
Helps identify how a value increased or decreased step-by-step.
Great for showing contributions to a total (e.g., trade balance).

🔹 2. Structure
Start column: Beginning value (e.g., trade balance in 1997).
Rising bars: Positive changes (e.g., export growth).
Falling bars: Negative changes (e.g., import spikes).
End column: Final total (e.g., trade balance in 2022).

🔹 3. Use Cases for India’s Trade

                   Use Case                                  Description
         📈 Year-over-Year Trade Balance           Show how trade surplus/deficit changed yearly.
         🔄 Import Cost Change  Breakdown          Break total change into sectors (e.g., oil, gold, electronics).
         💰 Export Revenue Growth Breakdown        Identify which sectors contributed most to  export increase.


🔹 4. Key Features
Automatically calculates increases and decreases.
Breakdown field: Allows category-wise contribution (e.g., sector-wise).
Tooltips: Show exact values and deltas on hover.
Total bars: Can be toggled on/off.

🔹 5. Best Practices
Keep category names short for clarity.
Use distinct colors for increase (green) and decrease (red).
Highlight key categories or years with data labels.

🔹 6. Example Analysis Titles
✅ “How India’s Trade Deficit Widened from 1997 to 2022”
✅ “Contribution of Import Categories to Total Cost – 2022”
✅ “Year-wise Impact on Export Revenue Growth”

 WATERFALL CHARTS SCREENSHOT LINK : https://postimg.cc/xc7HhRSt


MATRIX CHARTS:
🧮 Matrix Chart – Power BI Overview (India Trade Data)

🔹 1. Purpose
Displays data in tabular format with the power of pivot tables.
Allows you to show hierarchies, row/column groups, and aggregates.
Ideal for detailed comparisons across multiple dimensions.

🔹 2. Structure
Rows: Typically a category like Year or Country.
Columns: Another category (e.g., Import/Export, Sector).
Values: Numerical data (e.g., trade amount, growth %, etc.).

                  Use Case                                  Setup Example
        📅Year-wise Export/Import Summary           YearColumns: Trade TypeValues: USD
        🌍 Country-wise Trade with India            CountryColumns: Import/ExportValues: Amount
        🏭 Sector Contribution to Exports(by year)  SectorColumns: YearValues: Export Value
        📊 Trade Balance Comparison                 YearColumns: Import vs ExportValues: Difference  (Calculated Measure)


🔹 4. Key Features
Drill-down: Expand/collapse rows or columns for hierarchy (e.g., Sector → Subsector).
Conditional Formatting: Add color scales or data bars.
Totals/Subtotals: Automatically displayed and customizable.
Sorting: By rows, columns, or values.
Tooltips: Show detailed info on hover.

🔹 5. Best Practices
Use column/row formatting to highlight key data.
Hide unnecessary totals for clarity.
Use hierarchical fields to reduce clutter.
Avoid overcrowding with too many columns—consider slicers or filters.

🔹 6. Example Titles
✅ “India’s Year-wise Import & Export Matrix (1997–2022)”
✅ “Country-Wise Trade with India: A Matrix View”
✅ “Sector-Wise Export Trends Over Time”

MATRIX  CHARTS SCREENSHOT LINK : https://postimg.cc/XBrqkRX3

