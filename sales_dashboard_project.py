# =============================================
# SALES DASHBOARD - BEGINNER VERSION
# By: Ayushi Sahu
# Tools: Python, Pandas, Matplotlib
# =============================================

# STEP 1: Import libraries (tools we need)
import pandas as pd
import matplotlib.pyplot as plt

# STEP 2: Create our sales data (fake but realistic)


data = {
    'Month':    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Revenue':  [45000, 52000, 48000, 61000, 55000, 67000,
                 72000, 69000, 74000, 80000, 95000, 110000],
    'Profit':   [18000, 21000, 19000, 25000, 22000, 27000,
                 29000, 28000, 30000, 33000, 40000, 47000],
    'Orders':   [120, 140, 130, 165, 150, 180,
                 195, 185, 200, 215, 260, 300]
}

df = pd.DataFrame(data)

# STEP 3: Create the dashboard (4 charts)


fig, axes = plt.subplots(2, 2, figsize=(14, 9))
fig.suptitle('Business Sales Dashboard 2024', fontsize=18, fontweight='bold', y=0.98)
fig.patch.set_facecolor('#f8f8f8')

# --- Chart 1: Revenue Over the Year (top-left) ---
ax1 = axes[0, 0]
ax1.plot(df['Month'], df['Revenue'], color='#2563EB', linewidth=2.5, marker='o', markersize=6)
ax1.fill_between(df['Month'], df['Revenue'], alpha=0.1, color='#2563EB')
ax1.set_title('Monthly Revenue (₹)', fontweight='bold')
ax1.set_ylabel('Revenue (₹)')
ax1.grid(axis='y', linestyle='--', alpha=0.4)
ax1.set_facecolor('white')
# Add value labels on key months
for i in [0, 5, 11]:
    ax1.annotate(f"₹{df['Revenue'][i]//1000}K",
                 (df['Month'][i], df['Revenue'][i]),
                 textcoords="offset points", xytext=(0, 10), fontsize=8, color='#2563EB')

# --- Chart 2: Profit Bar Chart (top-right) ---
ax2 = axes[0, 1]
colors = ['#16A34A' if p > 25000 else '#F59E0B' for p in df['Profit']]
bars = ax2.bar(df['Month'], df['Profit'], color=colors, edgecolor='none')
ax2.set_title('Monthly Profit (₹)  [Green = High, Yellow = Average]', fontweight='bold')
ax2.set_ylabel('Profit (₹)')
ax2.grid(axis='y', linestyle='--', alpha=0.4)
ax2.set_facecolor('white')

# --- Chart 3: Category Revenue Pie (bottom-left) ---
ax3 = axes[1, 0]
categories     = ['Electronics', 'Clothing', 'Groceries', 'Furniture', 'Sports']
category_sales = [38, 25, 20, 10, 7]
pie_colors     = ['#2563EB', '#E8739A', '#F59E0B', '#16A34A', '#7C3AED']
ax3.pie(category_sales, labels=categories, autopct='%1.0f%%',
        colors=pie_colors, startangle=90,
        wedgeprops={'edgecolor': 'white', 'linewidth': 2})
ax3.set_title('Sales by Category', fontweight='bold')

# --- Chart 4: Orders per Month (bottom-right) ---
ax4 = axes[1, 1]
ax4.bar(df['Month'], df['Orders'], color='#7C3AED', alpha=0.8, edgecolor='none')
ax4.set_title('Orders Per Month', fontweight='bold')
ax4.set_ylabel('Number of Orders')
ax4.grid(axis='y', linestyle='--', alpha=0.4)
ax4.set_facecolor('white')
# Highlight best month
best = df['Orders'].idxmax()
ax4.bar(df['Month'][best], df['Orders'][best], color='#E8739A', alpha=1)
ax4.annotate('Best Month!', (df['Month'][best], df['Orders'][best]),
             textcoords="offset points", xytext=(0, 8), fontsize=8,
             color='#E8739A', fontweight='bold', ha='center')

plt.tight_layout()
plt.savefig('sales_dashboard.png', dpi=150, bbox_inches='tight')
plt.show()

print("Dashboard saved as sales_dashboard.png")
print(f"\nQuick Stats:")
print(f"  Total Revenue : ₹{df['Revenue'].sum():,}")
print(f"  Total Profit  : ₹{df['Profit'].sum():,}")
print(f"  Total Orders  : {df['Orders'].sum()}")
print(f"  Best Month    : {df.loc[df['Revenue'].idxmax(), 'Month']}")