import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rest=pd.read_csv('/Users/msyzdykova/Downloads/restaurants.csv')
#top 10 categories
rest['category'].value_counts()
cat=pd.DataFrame(rest['category'].value_counts())
cat.head()
cat=cat.reset_index(drop=False)
cat.columns=['Category', 'Count']
cat.head()
#bar chart
plt.figure(figsize=(40,9))
plt.bar(cat['Category'][:10], cat['Count'][:10])
plt.title('Top 10 categories')
#pie chart
plt.figure()
plt.pie(cat['Count'][:10])
plt.legend(cat['Category'][:10], loc='upper center', bbox_to_anchor=(-1,1))
plt.title('Top 10 restaurant categories')
#top 100 rated restaurants
rest.sort_values(by=['ratings', 'score'], ascending=False)[['name', 'ratings']][:100]
#relationship b/n position-score (plt)
clean=rest.dropna()
plt.figure()
plt.scatter(clean['position'], clean['score'])
plt.xlabel('Position')
plt.ylabel('Score')
#relationship b/n position-ratings (sns)
sns.scatterplot(clean['position'], clean['ratings'])
#pie chart of restaurant types by price range
sign={'$': 'Inexpensive', '$$': 'Moderately expensive', '$$$': 'Expensive', '$$$$': 'Very expensive'}
clean['price_range']=clean['price_range'].replace(sign)
clean['price_range'].head()
price=pd.DataFrame(clean['price_range'].value_counts())
price=price.reset_index(drop=False)
price.columns=['Price', 'Count']
price.head()
plt.figure()
plt.pie(price['Count'])
plt.legend(price['Price'], loc='upper center', bbox_to_anchor=(-1,1))
plt.title('Restaurant types')
#relationship b/n price and score
plt.figure()
sns.scatterplot(clean['score'], clean['price_range'])
#top 10 menu items
menu=pd.read_csv('/Users/msyzdykova/Downloads/restaurant-menus.csv')
best_menu=pd.DataFrame(menu['name'].value_counts()[:10])
best_menu=best_menu.reset_index(drop=False)
best_menu.columns=['Menu item', 'Count']
plt.figure()
sns.barplot(x=best_menu['Count'][:10], y=best_menu['Menu item'][:10], orient='h')
#top 10 menu categories
best_cat=pd.DataFrame(menu['category'].value_counts()[:10])
best_cat=best_cat.reset_index(drop=False)
best_cat.columns=['Category', 'Count']
plt.figure()
sns.barplot(x=best_cat['Count'], y=best_cat['Category'], orient='h')
#merge rest and rest_menu
merged=pd.merge(rest, menu, left_on='id', right_on='restaurant_id')
merged.columns.values.tolist()
merged.rename(columns={'name_x': 'rest_name', 'category_x': 'rest_cat', 'category_y': 'menu_cat', 'name_y': 'menu_item'}, inplace=True)
merged.columns.values.tolist()
merged.head()





