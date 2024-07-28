# ABOUT DATA (from Kaggle)

When a consumer places an order on DoorDash, we show the expected time of delivery. It is very important for DoorDash to get this right, as it has a big impact on consumer experience. In this exercise, you will build a model to predict the estimated time taken for a delivery.

Concretely, for a given delivery you must predict the total delivery duration seconds , i.e., the time taken from

Start: the time consumer submits the order (created_at) to
End: when the order will be delivered to the consumer (actual_delivery_time)

Data Description
The attached file historical_data.csv contains a subset of deliveries received at DoorDash in early 2015 in a subset of the cities. Each row in this file corresponds to one unique delivery. We have added noise to the dataset to obfuscate certain business details. Each column corresponds to a feature as explained below. Note all money (dollar) values given in the data are in cents and all time duration values given are in seconds

The target value to predict here is the total seconds value between created_at and actual_delivery_time.

Columns in historical_data.csv

Time features
market_id: A city/region in which DoorDash operates, e.g., Los Angeles, given in the data as an id

created_at: Timestamp in UTC when the order was submitted by the consumer to DoorDash. (Note this timestamp is in UTC, but in case you need it, the actual timezone of the region was US/Pacific)

actual_delivery_time: Timestamp in UTC when the order was delivered to the consumer

Store features
store_id: an id representing the restaurant the order was submitted for

store_primary_category: cuisine category of the restaurant, e.g., italian, asian

order_protocol: a store can receive orders from DoorDash through many modes. This field represents an id denoting the protocol

Order features
total_items: total number of items in the order

subtotal: total value of the order submitted (in cents)

num_distinct_items: number of distinct items included in the order

min_item_price: price of the item with the least cost in the order (in cents)

max_item_price: price of the item with the highest cost in the order (in cents)

Market features
DoorDash being a marketplace, we have information on the state of marketplace when the order is placed, that can be used to estimate delivery time. The following features are values at the time of created_at (order submission time):

total_onshift_dashers: Number of available dashers who are within 10 miles of the store at the time of order creation

total_busy_dashers: Subset of above total_onshift_dashers who are currently working on an order

total_outstanding_orders: Number of orders within 10 miles of this order that are currently being processed.

Predictions from other models
We have predictions from other models for various stages of delivery process that we can use:
estimated_order_place_duration: Estimated time for the restaurant to receive the order from DoorDash (in seconds)

estimated_store_to_consumer_driving_duration: Estimated travel time between store and consumer (in seconds)

"""

# the created_at and actual_delivery_time are dates;  let's convert them
df['created_at'] = pd.to_datetime(df['created_at'])
df['actual_delivery_time'] = pd.to_datetime(df['actual_delivery_time'])

# our target is actual duration
df['actual_duration'] = (df['actual_delivery_time'] - df['created_at']).dt.total_seconds()


numerical = ['max_item_price', 'min_item_price', 'subtotal', 'total_items', 'num_distinct_items', 'max_item_price', 'min_item_price', 'total_onshift_dashers', 'total_busy_dashers', 'total_outstanding_orders']

categorical = ['market_id', 'store_id', 'store_primary_category', 'order_protocol']

"""## Validation Framework"""

from sklearn.model_selection import train_test_split

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

len(df_train), len(df_val), len(df_test)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.actual_duration.values
y_val = df_val.actual_duration.values
y_test = df_test.actual_duration.values

del df_train['actual_duration']
del df_val['actual_duration']
del df_test['actual_duration']

df_train.shape, df_val.shape, df_test.shape

"""## One-Hot Encoding"""

from sklearn.feature_extraction import DictVectorizer

dv = DictVectorizer(sparse=False)

train_dict = df_train[categorical + numerical].to_dict(orient='records')
X_train = dv.fit_transform(train_dict)

val_dict = df_val[categorical + numerical].to_dict(orient='records')
X_val = dv.transform(val_dict)

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

from sklearn.metrics import mean_squared_error


with mlflow.start_run():
    
    mlflow.set_tag("developer", "clewis")

    mlflow.log_param("train-data-path", "data/historical_data_csv")   
        
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    y_pred = lr.predict(X_train)

    mean_squared_error(y_train, y_pred, squared=False)
    mlflow.log_metric("rmse", rmse)



import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(y_pred, label='prediction', bins=50)
sns.histplot(y_train, label='actual', bins=50)

plt.legend()

with open('models/lin_reg.bin', 'wb') as f_out:
    pickle.dump((dv, lr), f_out)

# try lasso
alpha = 0.01
mlflow.log_param("alpha", alpha)
lasso = Lasso(alpha)
lasso.fit(X_train, y_train)

y_pred = lasso.predict(X_train)

mean_squared_error(y_train, y_pred, squared=False)

# try ridge
ridge = Ridge(alpha=0.01)
ridge.fit(X_train, y_train)

y_pred = ridge.predict(X_train)

mean_squared_error(y_train, y_pred, squared=False)

