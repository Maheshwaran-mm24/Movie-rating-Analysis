import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Movie Ratings.csv')
# Top 10 highest-rated movies
df.nlargest(10, 'Rating')[['MovieId', 'Rating']]