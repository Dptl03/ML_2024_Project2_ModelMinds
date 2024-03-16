import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt



# Load dataset from CSV
df = pd.read_csv('object_info_all.csv')

X = df.drop(columns=['X-cm','Y-cm'])

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initialize PCA
pca = PCA(n_components=5)  # Choose the number of principal components

# Fit and transform the scaled features
principal_components = pca.fit_transform(X_scaled)
print(pca.explained_variance_ratio_)

# Plot the principal components
plt.scatter(principal_components[:, 0], principal_components[:, 1])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

