import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

class Plots:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def save_and_display_plot(self, plot_func, output_path):
        plt.figure(figsize=(10, 6))  
        plot_func()  
        plt.savefig(output_path) 
        plt.show()  
        plt.close()  
        #print(f"Plot saved to {output_path}.")

    def sales_trends(self, output_path: str):
        self.save_and_display_plot(
            lambda: sns.lineplot(x='Date', y='Revenue', data=self.data),
            output_path
        )

    def revenue_profit_by_product_category(self, output_path: str):
        revenue_data = self.data.groupby('Product_Category').agg({'Revenue': 'sum', 'Profit': 'sum'}).reset_index()
        
        revenue_profit_data = revenue_data.melt(id_vars='Product_Category', value_vars=['Revenue', 'Profit'],
                                                var_name='Metric', value_name='Amount')

        self.save_and_display_plot(
            lambda: sns.barplot(x='Product_Category', y='Amount', hue='Metric', data=revenue_profit_data),
            output_path
        )

    def price_vs_profit(self, output_path: str):
        self.save_and_display_plot(
            lambda: sns.scatterplot(x='Unit_Price', y='Profit', data=self.data),
            output_path
        )

    def barplot(self,col,output_path: str):
        self.save_and_display_plot(
            lambda: sns.barplot(x=col, y='median_house_value', data=self.data),
            output_path 
        )

    def correlation_heatmap(self, output_path: str):
        self.save_and_display_plot(
            lambda: sns.heatmap(self.data.corr(), annot=True, fmt=".2f", cmap="coolwarm"),
            output_path
        )