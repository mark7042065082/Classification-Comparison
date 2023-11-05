{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "50cceda6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2eb1d78",
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install scikit-learn"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9e510fa7",
   "metadata": {},
   "source": [
    "### About Data \n",
    " \n",
    " \n",
    " \n",
    "1. survival\t (Survival\t    0 = No, 1 = Yes)\n",
    "2. pclass\t (Ticket class\t1 = 1st, 2 = 2nd, 3 = 3rd)\n",
    "3. sex\t     (Sex\t)\n",
    "4. Age\t     (Age in years\t)\n",
    "5. sibsp\t(# of siblings / spouses aboard the Titanic\t)\n",
    "6. parch\t(# of parents / children aboard the Titanic\t)\n",
    "7. ticket\t(Ticket number\t)\n",
    "8. fare\t    (Passenger fare\t)\n",
    "9. cabin\t(Cabin number\t)\n",
    "19. embarked\t(Port of Embarkation\tC = Cherbourg, Q = Queenstown, S = Southampton)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "13fa11a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv(r'C:\\Users\\brago\\Desktop\\New folder\\\\dataset_titanic.csv')\n",
    "#df2=df.copy()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7c09051",
   "metadata": {},
   "source": [
    "### Data Preprocessing"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "34b3d967",
   "metadata": {},
   "source": [
    "The head() method in pandas is used to view the first few rows of a DataFrame or Series\n",
    "The tail() method in pandas is used to view the last few rows of a DataFrame or Series \n",
    "The sample() method in pandas is used to randomly sample rows from a DataFrame or Series"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "66a30f3d",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>887</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Montvila, Rev. Juozas</td>\n",
       "      <td>male</td>\n",
       "      <td>27.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>211536</td>\n",
       "      <td>13.0000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>888</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Graham, Miss. Margaret Edith</td>\n",
       "      <td>female</td>\n",
       "      <td>19.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>112053</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>B42</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>889</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Johnston, Miss. Catherine Helen \"Carrie\"</td>\n",
       "      <td>female</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>W./C. 6607</td>\n",
       "      <td>23.4500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>890</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Behr, Mr. Karl Howell</td>\n",
       "      <td>male</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>111369</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>C148</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>891</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Dooley, Mr. Patrick</td>\n",
       "      <td>male</td>\n",
       "      <td>32.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>370376</td>\n",
       "      <td>7.7500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Q</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass  \\\n",
       "0              1         0       3   \n",
       "1              2         1       1   \n",
       "2              3         1       3   \n",
       "3              4         1       1   \n",
       "4              5         0       3   \n",
       "..           ...       ...     ...   \n",
       "886          887         0       2   \n",
       "887          888         1       1   \n",
       "888          889         0       3   \n",
       "889          890         1       1   \n",
       "890          891         0       3   \n",
       "\n",
       "                                                  Name     Sex   Age  SibSp  \\\n",
       "0                              Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1    Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                               Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3         Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                             Allen, Mr. William Henry    male  35.0      0   \n",
       "..                                                 ...     ...   ...    ...   \n",
       "886                              Montvila, Rev. Juozas    male  27.0      0   \n",
       "887                       Graham, Miss. Margaret Edith  female  19.0      0   \n",
       "888           Johnston, Miss. Catherine Helen \"Carrie\"  female   NaN      1   \n",
       "889                              Behr, Mr. Karl Howell    male  26.0      0   \n",
       "890                                Dooley, Mr. Patrick    male  32.0      0   \n",
       "\n",
       "     Parch            Ticket     Fare Cabin Embarked  \n",
       "0        0         A/5 21171   7.2500   NaN        S  \n",
       "1        0          PC 17599  71.2833   C85        C  \n",
       "2        0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3        0            113803  53.1000  C123        S  \n",
       "4        0            373450   8.0500   NaN        S  \n",
       "..     ...               ...      ...   ...      ...  \n",
       "886      0            211536  13.0000   NaN        S  \n",
       "887      0            112053  30.0000   B42        S  \n",
       "888      2        W./C. 6607  23.4500   NaN        S  \n",
       "889      0            111369  30.0000  C148        C  \n",
       "890      0            370376   7.7500   NaN        Q  \n",
       "\n",
       "[891 rows x 12 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df\n",
    "# df.head()    \n",
    "# df.tail()     \n",
    "# df.sample()   "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c6b1ed7e",
   "metadata": {},
   "source": [
    "# Description of basic methods\n",
    "\n",
    "\n",
    "\n",
    "1. The shape attribute in pandas is used to determine the dimensions (number of rows and columns) of a DataFrame or a\n",
    "NumPy array.\n",
    "\n",
    "2. The info() method in pandas is used to retrieve a concise summary of the DataFrame's information, including data types, \n",
    "non-null values, and memory usage\n",
    "\n",
    "3. The describe() method in pandas is used to generate descriptive statistics of a DataFrame or Series.\n",
    "4. The isnull() method in pandas is used to check for missing or null values in a DataFrame or Series.\n",
    "5. The nunique() method in pandas is used to count the number of unique values in a Series (a single column of a DataFrame)\n",
    "6. The unique() method in pandas is used to retrieve the unique values from a Series (a single column of a DataFrame)\n",
    "7. The value_counts() method in pandas is used to count the frequency of each unique value in a Series (a single column of    a DataFrame).\n",
    "8. By default, dropna() removes any row that contains at least one null value.\n",
    "9. The fillna() method in pandas is used to fill missing or null (NaN) values in a DataFrame or Series with specified    values or using various filling strategies."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0909ad43",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(891, 12)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8f445b8e",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 891 entries, 0 to 890\n",
      "Data columns (total 12 columns):\n",
      " #   Column       Non-Null Count  Dtype  \n",
      "---  ------       --------------  -----  \n",
      " 0   PassengerId  891 non-null    int64  \n",
      " 1   Survived     891 non-null    int64  \n",
      " 2   Pclass       891 non-null    int64  \n",
      " 3   Name         891 non-null    object \n",
      " 4   Sex          891 non-null    object \n",
      " 5   Age          714 non-null    float64\n",
      " 6   SibSp        891 non-null    int64  \n",
      " 7   Parch        891 non-null    int64  \n",
      " 8   Ticket       891 non-null    object \n",
      " 9   Fare         891 non-null    float64\n",
      " 10  Cabin        204 non-null    object \n",
      " 11  Embarked     889 non-null    object \n",
      "dtypes: float64(2), int64(5), object(5)\n",
      "memory usage: 83.7+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c94c6935",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>714.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.383838</td>\n",
       "      <td>2.308642</td>\n",
       "      <td>29.699118</td>\n",
       "      <td>0.523008</td>\n",
       "      <td>0.381594</td>\n",
       "      <td>32.204208</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>257.353842</td>\n",
       "      <td>0.486592</td>\n",
       "      <td>0.836071</td>\n",
       "      <td>14.526497</td>\n",
       "      <td>1.102743</td>\n",
       "      <td>0.806057</td>\n",
       "      <td>49.693429</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.420000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>223.500000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>20.125000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.910400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>28.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>14.454200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>668.500000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>31.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>512.329200</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       PassengerId    Survived      Pclass         Age       SibSp  \\\n",
       "count   891.000000  891.000000  891.000000  714.000000  891.000000   \n",
       "mean    446.000000    0.383838    2.308642   29.699118    0.523008   \n",
       "std     257.353842    0.486592    0.836071   14.526497    1.102743   \n",
       "min       1.000000    0.000000    1.000000    0.420000    0.000000   \n",
       "25%     223.500000    0.000000    2.000000   20.125000    0.000000   \n",
       "50%     446.000000    0.000000    3.000000   28.000000    0.000000   \n",
       "75%     668.500000    1.000000    3.000000   38.000000    1.000000   \n",
       "max     891.000000    1.000000    3.000000   80.000000    8.000000   \n",
       "\n",
       "            Parch        Fare  \n",
       "count  891.000000  891.000000  \n",
       "mean     0.381594   32.204208  \n",
       "std      0.806057   49.693429  \n",
       "min      0.000000    0.000000  \n",
       "25%      0.000000    7.910400  \n",
       "50%      0.000000   14.454200  \n",
       "75%      0.000000   31.000000  \n",
       "max      6.000000  512.329200  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5d854765",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "147"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Cabin'].unique()\n",
    "df['Cabin'].nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e0cfcbca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Pclass'].nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "cc1d5c5f",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Embarked\n",
       "S    644\n",
       "C    168\n",
       "Q     77\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Embarked'].value_counts()\n",
    "df['Cabin'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c63c8836",
   "metadata": {},
   "source": [
    "### What to do if your dataset has null values?\n",
    "1. You can drop all the rows that has null value\n",
    "2. You can fill the null values with mean,median, mode."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8ef32105",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Cabin          687\n",
       "Age            177\n",
       "Embarked         2\n",
       "PassengerId      0\n",
       "Survived         0\n",
       "Pclass           0\n",
       "Name             0\n",
       "Sex              0\n",
       "SibSp            0\n",
       "Parch            0\n",
       "Ticket           0\n",
       "Fare             0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull()\n",
    "df.isnull().sum()\n",
    "df.isnull().sum().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a90230a4",
   "metadata": {},
   "outputs": [],
   "source": [
    " df['Age']=df['Age'].fillna(df['Age'].mean())\n",
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c7308ebb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "77.10437710437711"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(df['Cabin'].isnull().sum()/df.shape[0])*100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e9aac87e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# df=df.dropna()\n",
    "df=df.dropna(subset=['Fare'])   #it will drop row that contains null value in Embarked column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "afe15b4d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    S\n",
       "Name: Embarked, dtype: object"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()\n",
    "df.shape\n",
    "\n",
    "df['Embarked'].mode()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "9b4ce8b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Embarked\n",
       "S    644\n",
       "C    168\n",
       "Q     77\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Embarked'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "20368359",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Embarked']=df['Embarked'].fillna('S')\n",
    "df['Embarked'].isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "aa9b329f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# df['up']=df['Pclass'].replace(3,4)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b3562e19",
   "metadata": {},
   "source": [
    "A Label Encoder is a preprocessing technique used in machine learning and data analysis to convert categorical data into numerical form. Categorical data represents categories or labels, such as colors, cities, or types of fruits, and these labels need to be converted into numerical values for many machine learning algorithms to work effectively, as most algorithms require numerical input.\n",
    "\n",
    "One-Hot Encoding is a popular technique for representing categorical data in a format that is suitable for machine learning algorithms. It is used to convert categorical variables into a binary matrix (1s and 0s), where each category is transformed into a new column, and each column represents a category with a binary value indicating its presence or absence."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "7d25cfce",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: scikit-learn in c:\\users\\brago\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (1.3.0)\n",
      "Requirement already satisfied: numpy>=1.17.3 in c:\\users\\brago\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from scikit-learn) (1.24.3)\n",
      "Requirement already satisfied: scipy>=1.5.0 in c:\\users\\brago\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from scikit-learn) (1.11.1)\n",
      "Requirement already satisfied: joblib>=1.1.1 in c:\\users\\brago\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from scikit-learn) (1.3.1)\n",
      "Requirement already satisfied: threadpoolctl>=2.0.0 in c:\\users\\brago\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from scikit-learn) (3.2.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.HTTPSConnection object at 0x00000270A30259D0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed')': /simple/scikit-learn/\n",
      "WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.HTTPSConnection object at 0x00000270A64150D0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed')': /simple/scikit-learn/\n",
      "WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.HTTPSConnection object at 0x00000270A6415A50>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed')': /simple/scikit-learn/\n",
      "WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.HTTPSConnection object at 0x00000270A64163D0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed')': /simple/scikit-learn/\n",
      "WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.HTTPSConnection object at 0x00000270A6416D50>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed')': /simple/scikit-learn/\n"
     ]
    }
   ],
   "source": [
    "pip install scikit-learn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "9e805c53",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import LabelEncoder\n",
    "lr=LabelEncoder()\n",
    "df['Sex']=lr.fit_transform(df['Sex'])\n",
    "df['Embarked']=lr.fit_transform(df['Embarked'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "9610c7e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>1</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>0</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>0</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>1</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name  Sex   Age  SibSp  Parch  \\\n",
       "0                            Braund, Mr. Owen Harris    1  22.0      1      0   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...    0  38.0      1      0   \n",
       "2                             Heikkinen, Miss. Laina    0  26.0      0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)    0  35.0      1      0   \n",
       "4                           Allen, Mr. William Henry    1  35.0      0      0   \n",
       "\n",
       "             Ticket     Fare Cabin  Embarked  \n",
       "0         A/5 21171   7.2500   NaN         2  \n",
       "1          PC 17599  71.2833   C85         0  \n",
       "2  STON/O2. 3101282   7.9250   NaN         2  \n",
       "3            113803  53.1000  C123         2  \n",
       "4            373450   8.0500   NaN         2  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "1ae450b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "encoded_df = pd.get_dummies(df, columns=['Embarked'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "2e90f9df",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked_0</th>\n",
       "      <th>Embarked_1</th>\n",
       "      <th>Embarked_2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>1</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>0</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>0</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>1</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name  Sex   Age  SibSp  Parch  \\\n",
       "0                            Braund, Mr. Owen Harris    1  22.0      1      0   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...    0  38.0      1      0   \n",
       "2                             Heikkinen, Miss. Laina    0  26.0      0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)    0  35.0      1      0   \n",
       "4                           Allen, Mr. William Henry    1  35.0      0      0   \n",
       "\n",
       "             Ticket     Fare Cabin  Embarked_0  Embarked_1  Embarked_2  \n",
       "0         A/5 21171   7.2500   NaN       False       False        True  \n",
       "1          PC 17599  71.2833   C85        True       False       False  \n",
       "2  STON/O2. 3101282   7.9250   NaN       False       False        True  \n",
       "3            113803  53.1000  C123       False       False        True  \n",
       "4            373450   8.0500   NaN       False       False        True  "
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "encoded_df.head()\n",
    "encoded_df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "395427aa",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(df['Age'])\n",
    "plt.plot()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb3a67c9",
   "metadata": {},
   "source": [
    "### Feature Generation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "0ceb8f7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "age_bin=[0,18,30,40,50,60,100]\n",
    "age_labels = ['0-17', '18-29', '30-39', '40-49', '50-59', '60-100']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "da6307a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Age_Grp']=pd.cut(df['Age'],bins=age_bin,labels=age_labels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "a31d2df6",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "      <th>Age_Grp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>1</td>\n",
       "      <td>22.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>0</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>0</td>\n",
       "      <td>30-39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>0</td>\n",
       "      <td>26.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>0</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>2</td>\n",
       "      <td>30-39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>1</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>30-39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>887</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Montvila, Rev. Juozas</td>\n",
       "      <td>1</td>\n",
       "      <td>27.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>211536</td>\n",
       "      <td>13.0000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>888</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Graham, Miss. Margaret Edith</td>\n",
       "      <td>0</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>112053</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>B42</td>\n",
       "      <td>2</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>889</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Johnston, Miss. Catherine Helen \"Carrie\"</td>\n",
       "      <td>0</td>\n",
       "      <td>29.699118</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>W./C. 6607</td>\n",
       "      <td>23.4500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>890</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Behr, Mr. Karl Howell</td>\n",
       "      <td>1</td>\n",
       "      <td>26.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>111369</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>C148</td>\n",
       "      <td>0</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>891</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Dooley, Mr. Patrick</td>\n",
       "      <td>1</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>370376</td>\n",
       "      <td>7.7500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "      <td>30-39</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 13 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass  \\\n",
       "0              1         0       3   \n",
       "1              2         1       1   \n",
       "2              3         1       3   \n",
       "3              4         1       1   \n",
       "4              5         0       3   \n",
       "..           ...       ...     ...   \n",
       "886          887         0       2   \n",
       "887          888         1       1   \n",
       "888          889         0       3   \n",
       "889          890         1       1   \n",
       "890          891         0       3   \n",
       "\n",
       "                                                  Name  Sex        Age  SibSp  \\\n",
       "0                              Braund, Mr. Owen Harris    1  22.000000      1   \n",
       "1    Cumings, Mrs. John Bradley (Florence Briggs Th...    0  38.000000      1   \n",
       "2                               Heikkinen, Miss. Laina    0  26.000000      0   \n",
       "3         Futrelle, Mrs. Jacques Heath (Lily May Peel)    0  35.000000      1   \n",
       "4                             Allen, Mr. William Henry    1  35.000000      0   \n",
       "..                                                 ...  ...        ...    ...   \n",
       "886                              Montvila, Rev. Juozas    1  27.000000      0   \n",
       "887                       Graham, Miss. Margaret Edith    0  19.000000      0   \n",
       "888           Johnston, Miss. Catherine Helen \"Carrie\"    0  29.699118      1   \n",
       "889                              Behr, Mr. Karl Howell    1  26.000000      0   \n",
       "890                                Dooley, Mr. Patrick    1  32.000000      0   \n",
       "\n",
       "     Parch            Ticket     Fare Cabin  Embarked Age_Grp  \n",
       "0        0         A/5 21171   7.2500   NaN         2   18-29  \n",
       "1        0          PC 17599  71.2833   C85         0   30-39  \n",
       "2        0  STON/O2. 3101282   7.9250   NaN         2   18-29  \n",
       "3        0            113803  53.1000  C123         2   30-39  \n",
       "4        0            373450   8.0500   NaN         2   30-39  \n",
       "..     ...               ...      ...   ...       ...     ...  \n",
       "886      0            211536  13.0000   NaN         2   18-29  \n",
       "887      0            112053  30.0000   B42         2   18-29  \n",
       "888      2        W./C. 6607  23.4500   NaN         2   18-29  \n",
       "889      0            111369  30.0000  C148         0   18-29  \n",
       "890      0            370376   7.7500   NaN         1   30-39  \n",
       "\n",
       "[891 rows x 13 columns]"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "6ba5c2b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#The drop() method in pandas is used to remove specified rows or columns from a DataFrame.\n",
    "ndf=df.drop(['Name','Sex','Ticket','Cabin','Embarked','Age_Grp'],axis=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "358c5a48",
   "metadata": {},
   "source": [
    "### Correlation Matrix\n",
    "A correlation matrix is a table or matrix that displays the correlation coefficients between many variables. It is a common tool in statistics and data analysis to understand the relationships between variables, especially in multivariate datasets. Correlation coefficients quantify the strength and direction of a linear relationship between two variables, and they typically range from -1 to 1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "ad96f1e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>PassengerId</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.005007</td>\n",
       "      <td>-0.035144</td>\n",
       "      <td>0.033207</td>\n",
       "      <td>-0.057527</td>\n",
       "      <td>-0.001652</td>\n",
       "      <td>0.012658</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Survived</th>\n",
       "      <td>-0.005007</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.338481</td>\n",
       "      <td>-0.069809</td>\n",
       "      <td>-0.035322</td>\n",
       "      <td>0.081629</td>\n",
       "      <td>0.257307</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Pclass</th>\n",
       "      <td>-0.035144</td>\n",
       "      <td>-0.338481</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.331339</td>\n",
       "      <td>0.083081</td>\n",
       "      <td>0.018443</td>\n",
       "      <td>-0.549500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Age</th>\n",
       "      <td>0.033207</td>\n",
       "      <td>-0.069809</td>\n",
       "      <td>-0.331339</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.232625</td>\n",
       "      <td>-0.179191</td>\n",
       "      <td>0.091566</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SibSp</th>\n",
       "      <td>-0.057527</td>\n",
       "      <td>-0.035322</td>\n",
       "      <td>0.083081</td>\n",
       "      <td>-0.232625</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.414838</td>\n",
       "      <td>0.159651</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Parch</th>\n",
       "      <td>-0.001652</td>\n",
       "      <td>0.081629</td>\n",
       "      <td>0.018443</td>\n",
       "      <td>-0.179191</td>\n",
       "      <td>0.414838</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.216225</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fare</th>\n",
       "      <td>0.012658</td>\n",
       "      <td>0.257307</td>\n",
       "      <td>-0.549500</td>\n",
       "      <td>0.091566</td>\n",
       "      <td>0.159651</td>\n",
       "      <td>0.216225</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             PassengerId  Survived    Pclass       Age     SibSp     Parch  \\\n",
       "PassengerId     1.000000 -0.005007 -0.035144  0.033207 -0.057527 -0.001652   \n",
       "Survived       -0.005007  1.000000 -0.338481 -0.069809 -0.035322  0.081629   \n",
       "Pclass         -0.035144 -0.338481  1.000000 -0.331339  0.083081  0.018443   \n",
       "Age             0.033207 -0.069809 -0.331339  1.000000 -0.232625 -0.179191   \n",
       "SibSp          -0.057527 -0.035322  0.083081 -0.232625  1.000000  0.414838   \n",
       "Parch          -0.001652  0.081629  0.018443 -0.179191  0.414838  1.000000   \n",
       "Fare            0.012658  0.257307 -0.549500  0.091566  0.159651  0.216225   \n",
       "\n",
       "                 Fare  \n",
       "PassengerId  0.012658  \n",
       "Survived     0.257307  \n",
       "Pclass      -0.549500  \n",
       "Age          0.091566  \n",
       "SibSp        0.159651  \n",
       "Parch        0.216225  \n",
       "Fare         1.000000  "
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corrM=ndf.corr()\n",
    "corrM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "5d5d97f6",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "sns.heatmap(corrM,cmap='PiYG',annot=True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f0d3e87d",
   "metadata": {},
   "source": [
    "### Outlier\n",
    "An outlier is an observation or data point that significantly deviates from the majority of other data points in a dataset. In other words, it is a data point that lies far outside the typical range of values in a dataset. Outliers can occur in various types of data, including numerical and categorical data, and they can have a significant impact on statistical analyses and machine learning models."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "f7823e97",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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NHnyZH311Vd677339PTTT3t02u7sTCv6aOiq3JkW1Fue6TscDudFgZ4SFhZWrg9tu91+1uWQlZXlsadWetrcuXN10UUXldp+Pq83d1T2yaflGbYqn1Ba1evtuuuuK/Oo8nXXXae0tLRS26tyvVX1vP3000/Ky8srsS0vL0/ffvutLrnkklKHr8p5c+cicne+COXk5KhPnz6SznzpLu+1PO58ETrbON1Zb9L5vT8p4JXwcurUKaWkpDgv8JLOPPwnNjZWycnJxfrPzc112dAqu1IqujN150O2Knem1fHYa0+5kB97zXqzpupeby+//HKVjets6626523s2LFVNq6zzZs7F5GfPHmyQl+aCkJMefAZ8D+e2J94Jbz88ccfys/PV0REhEv3iIgIbd++vVj/48aNOy/OfaM4K5/rtXLt1ak834jLe3SlrGkAuHD4GC/cYJ6enq6LL75Yq1atUkxMjLP70KFDtXz5cq1evdql/5KOvDRs2FBZWVkKCwtze/runDYqfHjR3cOAnDYq/2Hs8jjXrnmp7kP0leXtw7xlycjI0B133FFq+6effqrIyMhqqcUT6y0hIaHUtpkzZ5Y57Ll82qis+SpQ1vx5a5s8nz8DpHN7f5Kdna3w8PAKf34X8MqRlzp16sjPz0+ZmZku3TMzM0vcQdlstir9luvuMyq8ff99Qb3lrbl27doerqjqWG1duON8Xm9VLTIyUr6+vs7fkCnM19e32oKL5Jn19v3336tTp04ldq9OVT1vpc1X4fZzkdX2O+6uN+n835945VaJwMBAXXnllVq8eLGzm8Ph0OLFi12OxAC4cJR1O/H5oHHjxmW+t6rSAsq5GlxwfvDafZ6PPfaYpk6dqpkzZyo1NVUDBw7U8ePHnXcfAbjwdO7cucz3VvbBBx+U+R5A+XnlmpcCb7zxhl5++WVlZGSobdu2mjRpktq3b3/W4arqnBmAc0/h0xB8e7cO1hvKo6o+v70aXiqK8AIAgPVU1ec3jwcFAACWQngBAACWQngBAACWQngBAACWQngBAACWQngBAACWQngBAACWQngBAACWQngBAACW4pVfla6sgocCe/onvwEAQNUp+Nyu7MP9LRlejh49Kklq2LChlysBAADuOnr0qMLDwys8vCV/28jhcCg9PV01atSQj4+Px6eXnZ2thg0bau/evefdbykxb9bEvFkT82ZN5/O8SdU7f8YYHT16VFFRUfL1rfiVK5Y88uLr66sGDRpU+3TDwsLOyw1XYt6sinmzJubNms7neZOqb/4qc8SlABfsAgAASyG8AAAASyG8lIPNZtOoUaNks9m8XUqVY96siXmzJubNms7neZOsOX+WvGAXAABcuDjyAgAALIXwAgAALIXwAgAALIXwYnHXX3+9hgwZUunxLFu2TD4+Pjpy5Eilx1WWe+65R7169fLIuKtqWQAV5ePjozlz5kiSdu/eLR8fH23cuNGrNZ2rqmufcyEaPXq02rZt65Fxe2K9VeR/5ZwIL/fcc498fHzk4+OjwMBANW/eXM8995zy8vK8XVq1+/333zVw4EA1atRIfn5+stvtiouL08qVKz063Q4dOmj//v1V8vCgyrjQt4XC699msykyMrJa1n91SU5Olp+fn7p37+7tUirkbOtn//796tq1q1vjnD17tq655hqFh4erRo0auuyyy7wSwi+k/73C81r4tWvXrnOmli5dulR7LVZyzjxht0uXLpo+fbpyc3P19ddfKzExUQEBARo2bJi3S6tWvXv3Vm5urmbOnKk333xTv//+u66//nodPHiwQuMzxig/P1/+/mWv6sDAQEVGRlZoGlXtQt4WevfurVOnTmnmzJn605/+pMzMTC1evLjC6/9cM23aND300EOaNm2a0tPTFRUV5e2S3HK29ePu/9DixYvVp08fjR07Vrfeeqt8fHy0bds2LVq0yBPln1VV/e/l5+fLx8enUo9/97SCeS2sbt26bo2jquazpFrOxduWT58+7e0S/secAxISEkzPnj1dut10003mmmuuMRMmTDCXX365CQ4ONg0aNDADBw40R48edfa3e/du06NHD1OzZk0THBxsWrdubb766itjjDGHDh0yd955p6lTp46x2+2mefPm5r333nMOu2fPHnP77beb8PBwc9FFF5lbb73VpKWlFavr5ZdfNpGRkaZWrVpm0KBB5tSpU85+0tPTTbdu3YzdbjdNmjQxSUlJpnHjxubVV1919nP48GHTv39/U6dOHVOjRg1zww03mI0bNzrbR40aZf785z+bf/3rX0aSKVgtRZfL1q1bjSRjt9tNZGSkeeWVV0zHjh2NJLN06VJjjDFLly41kszXX39toqOjTUBAgJkyZYqRZFJTU12W8cSJE82f/vQnl+EOHz5ssrKyjN1uN19//bVL/1988YUJDQ01x48fL9fyy8vLM48++qgJDw83tWrVMk8++aTp169fsXVdWFnbgjHGrFixwlx33XUmKCjI1KxZ09x8883m0KFDxhhjrrvuOvPII484h3v//ffNlVdeaUJDQ01ERIT5xz/+YTIzM53tZW0fubm5JjEx0URGRhqbzWYaNWpkXnjhhVLrrgqHDx82ksyyZcvK7Ke0benAgQMmIiLCjB071tn/ypUrTUBAgPnuu+88Wnt5HD161ISGhprt27ebPn36uNRpjDFz5841zZs3NzabzVx//fVmxowZzm2ywA8//GCuvfZaY7fbTYMGDcxDDz1kjh07Vi31l2f9SDKzZ882xhiTlpZmJJmPPvrIxMTEGJvNZi677DKX4R955BFz/fXXlzndgv3D5MmTTYMGDUxQUJC5/fbbzZEjR6pkvgpUZj88ffp0Ex4ebubOnWsuvfRS4+fnZ9LS0kxOTo4ZOnSoadCggQkMDDTNmjUz7777rjHmf/uc7777zlx55ZUmKCjIxMTEmO3bt1fpfJV3Xo0xlZrPxx9/3ERFRZng4GBz9dVXO/fJFa2lgCQzefJk0717dxMUFGRatWplVq1aZXbu3Gmuu+46ExwcbGJiYsyuXbucw5Rnm1mzZo2JjY01tWvXNmFhYaZTp04mJSWl2LTfeustc8stt5jg4GAzatQol88KY4w5fvy46dKli+nQoYOz29SpU02rVq2MzWYzLVu2NG+++abLeFevXm3atm1rbDabufLKK80XX3xhJJkNGzaUa5kZY8w5G4uDgoJ06tQp+fr6atKkSdq6datmzpypJUuWaOjQoc7+EhMTlZubq++//15btmzRSy+9pNDQUEnSM888o23btmnBggVKTU3V22+/rTp16kg6kyDj4uJUo0YN/fDDD1q5cqVCQ0PVpUsXnTp1yjn+pUuX6ueff9bSpUs1c+ZMzZgxQzNmzHC29+vXT+np6Vq2bJk+//xzvfPOOzpw4IDLvNx+++06cOCAFixYoJSUFEVHR6tz5846dOiQs59du3bpq6++UnBwsO666y7l5uYWWyYvvPCCJOm1117Tt99+q2XLlmnTpk0lLr+nn35aL774olJTU3XbbbepXbt2SkpKcuknKSlJd955Z7Fhw8LC1KNHD82aNatY/7169VJwcHC5lt+ECRM0Y8YMvffee1qx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kpJy1jpL2hakM98+Fi9eXK553b59uw4ePKgXX3xRf/3rX9WqVasSv82Vtn1IZ6796dOnj6ZOnapPPvlEn3/+uct1StWldevWOn78eLm2pVOnTumuu+5Snz59NGbMGN1///3V8i22LHl5eXr//fc1YcIEl2+WmzZtUlRUlD766CO1bNlS69atcxlu7dq1Lu+jo6O1bdu2YvPevHlz5zc/byhYP6UpONop/e9/4NJLLy21/yZNmig4ONhlnHv27HHZ9/3444/y9fVVy5YtK1m9q8rsh4tq06aNHA6Hli9fXqU1ekpF5/Mvf/mL8vPzdeDAgWLbpTfv4DzbNrNy5Uo9/PDD6tatmy677DLZbDb98ccf5R7/iy++qISEBHXu3Fnbtm2TdOYIUFRUlH755Zdiy6Jp06aSpEsvvVSbN29WTk6OS23uOmfCS0maN2+u06dP6/XXX9cvv/yiDz74wOUIhCQNGTJECxcuVFpamtavX6+lS5c6dwwjR47U3LlztWvXLm3dulXz5893tsXHx6tOnTrq2bOnfvjhB6WlpWnZsmV6+OGHtW/fvnLV16pVK8XGxmrAgAFas2aNNmzYoAEDBrgk89jYWMXExKhXr1769ttvtXv3bq1atUrDhw8vtrM+ePCgbrzxRn344YfavHmzjh49qt9++03jx49Xr169dP/99yswMFBPP/205s2bpx49erh169rf//53HT16VAMHDtQNN9xw1ttUO3XqpMjISMXHx6tp06YuSbo8y++RRx7Riy++qDlz5mj79u0aNGhQpR5sNGzYMK1du1aDBg3S5s2btX37dr399tsl/sM1atRIgYGBzm1n3rx5GjNmjEs/ZW0fEydO1EcffaTt27frp59+0meffabIyEiXIxxVrej6T0tL02effabx48erZ8+e5dqWhg8frqysLE2aNElPPfWULrnkEq9eACmdORVx+PBh9e/fX5dffrnLq3fv3po2bZoefPBBbd++XU899ZR++uknffrpp85TMQX/S0899ZRWrVqlwYMHa+PGjdq5c6fmzp1bbRfsnm39lObNN9/U7NmztX37diUmJurw4cPOdTJ69GgNHTpUy5YtU1pamjZs2KD77rtPp0+f1k033eQch91uV0JCgjZt2qQffvhBDz/8sO64445q+XAsz364JE2aNFFCQoLuu+8+zZkzx7mP+PTTTz1ec0VUdD4vueQSxcfHq1+/fvriiy+UlpamNWvWaNy4cfrqq6/KNe3c3FxlZGS4vNwJEiU52zbTokULffDBB0pNTdXq1asVHx/v1tFt6cwp6vj4eN14443avn27JOnZZ5/VuHHjNGnSJP3000/asmWLpk+frokTJ0qS7rzzTvn4+OiBBx7Qtm3b9PXXX+uVV15xfwbLfXWMB5V1q9jEiRNN/fr1TVBQkImLizPvv/++y0V8gwcPNs2aNTM2m83UrVvX3H333eaPP/4wxpy5SOjSSy81QUFBplatWqZnz57ml19+cY57//79pl+/fqZOnTrGZrOZP/3pT+aBBx4wWVlZpdb1yCOPmOuuu875Pj093XTt2tXYbDbTuHFjM2vWLFOvXj0zefJkZz/Z2dnmoYceMlFRUSYgIMA0bNjQxMfHmz179hhj/ndbW05Ojnn66adNdHS0CQ8PN/7+/iY0NNSMGDHCnDhxwhw9etTccsstxtfX10gyUVFRpk2bNiVesFv49tLC7rjjDiPJ5ZbxsoYbOnSokWRGjhxZbFxnW36nT582jzzyiAkLCzM1a9Y0jz32WIVulS5s2bJlpkOHDsZms5maNWuauLg4Z81FL9idNWuWadKkibHZbCYmJsbMmzfP5aKwsraPd955x7Rt29aEhISYsLAw07lzZ7N+/fpS66oKRdd/cHCwadmypXP9G1P2trR06VLj7+9vfvjhB+c409LSTFhYmHnrrbc8WntZevToYbp161Zi2+rVq40ks2nTpmK3ShdcxFf4wr41a9aYm266yYSGhpqQkBBzxRVXFLvl2lPKs35UwgW7s2bNMldffbUJDAw0rVu3NkuWLHGOc8mSJaZ3796mYcOGJjAw0ERERJguXbq4rMOC/cNbb71loqKijN1uN7fddpvzEQFVpTL74YJbiIs6efKkefTRR039+vVNYGCgy+MIStrnbNiwwUhyeeSCJ5Q2rxWdz1OnTpmRI0eaJk2amICAAFO/fn3zt7/9zWzevLlctei/j8go/GrZsqUxxnWbMuZ/21Xhi1uLLsvybDPr16837dq1M3a73bRo0cJ89tlnxR7zUXTaJU3LmDM3ONSvX9/s2LHDGGNMUlKSadu2rQkMDDQXXXSR6dSpk/niiy+c/ScnJ5s///nPJjAw0LRt29Z8/vnnbl+w6/PfAlFF9u3bp4YNGzov/AJQMWPHjtXkyZO1d+9eb5fiVaNHj9acOXP4mQGgkHPmgl2rWrJkiY4dO6Y2bdpo//79Gjp0qJo0aaJOnTp5uzTAUt566y1dddVVql27tlauXKmXX3652k4JAbAWwkslnT59Wv/3f/+nX375RTVq1FCHDh2UlJRU7C4lAGXbuXOnnn/+eR06dEiNGjXS448/fkH8JAQA93HaCAAAWMo5fbcRAABAUYQXAABgKYQXAABgKYQXAABgKYQXAABgKYQXAABgKYQXAABgKYQXAABgKYQXAABgKf8PHD4iqJpXSl4AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Outlier Detection using boxplot\n",
    "sns.boxplot(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "32630cde",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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ElVVVZ3bRwUAAIa0AV8HxQSugwIAwNAzKNdBAQAAOF8IFAAAYB0CBQAAWIdAAQAA1iFQAACAdQgUAABgHQIFAABYh0ABAADWIVAAAIB1CBQAAGAdAgUAAFiHQAEAANaJ69OMAeB8mzdvng4dOqQLLrhAb775pulxABjCERQA1ti3b58OHTokSTp06JD27dtneCIAphAoAKyxdOnS094HMHwQKACssGbNGkUikZhtkUhEa9asMTQRAJMIFADG9fT06J133ul37Z133lFPT88gTwTANAIFgHHV1dUDWgeQeAgUAMZVVFQMaB1A4iFQABiXkpKioqKiftduueUWpaSkDPJEAEwjUABYYfny5XI4HDHbHA6HHnzwQUMTATCJQAFgjeeff/609wEMHwQKAGtMnjxZ6enpkqT09HRNnjzZ8EQATCFQAFijq6tLwWBQkhQMBtXV1WV2IADGECgArPHYY48pHA5LksLhsCorKw1PBMAUAgWAFZqamtTS0hKz7aOPPlJTU5OhiQCYRKAAMC4cDquqqqrftaqqquhRFQDDB4ECwLjGxkYFAoF+1wKBgBobGwd5IgCmESgAjMvPz5fL5ep3ze12Kz8/f5AnAmAagQLAOKfTecoTYleuXCmnk3+qgOGG33oAVsjLy9OUKVNitk2dOlXXXHONoYkAmESgALDGr371q+jREqfTecoTZwEkPgIFgDUyMjK0cOFCOZ1OLVy4UBkZGaZHAmCIIxKJREwPEa9AICC32y2/33/KE+sAAIBd4nn+5ggKAACwDoECwCplZWWaNWuWysrKTI8CwCACBYA1WltbtW/fPknSvn371NraangiAKYQKACscd999532PoDhg0ABYIVNmzbp2LFjMduOHTumTZs2GZoIgEkECgDj+vr6tH79+n7X1q9fr76+vkGeCIBpBAoA41555ZUBrQNIPAQKAOPuvPPOAa0DSDwECgDjkpOTdccdd/S7tmDBAiUnJw/yRABMI1AAGBeJRPT555/3u/bZZ59pCF7wGsAAESgAjGttbdWePXv6XduzZw/XQwGGIQIFgHE5OTmaMWOGkpKSYrYnJSXp2muvVU5OjqHJAJhCoAAwzuFw6P777z/ldofDYWAqACYRKACscPHFF+vmm2+O2XbzzTfroosuMjQRAJMIFADW+Mtf/nLa+wCGDwIFgBU2bdqk//73vzHb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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df['Fare'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "34d907db",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjIAAAHHCAYAAACle7JuAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAABxxklEQVR4nO3de1xUdf4/8NcMDsNFuYk4YAjkNaQyUZTUruAl1zLdbtZm5q+r7pa222Zbirqt2e43rTTdyrTNJa3tnubmLU0FMYySMFNDaRPwgoCCDOPM+f1BMzLM7ZyZc+bMwOv5ePhIzpzzOZ/5DMabc97n/dYIgiCAiIiIKAhp1Z4AERERkbcYyBAREVHQYiBDREREQYuBDBEREQUtBjJEREQUtBjIEBERUdBiIENERERBi4EMERERBS0GMkRERBS0GMgQEUlw9OhRaDQarF69Wu2pEBEYyBDRr/bv34/f/va3SElJQVhYGHr06IHc3Fy88sorip0zPz8fS5Yscdh+/Phx5OXloaSkRLFzt/Xll19Co9HY/uh0Olx66aW499578dNPP8lyjt27dyMvLw+1tbWyjEdEDGSICC0/YAcPHoxvv/0WDzzwAJYuXYr/9//+H7RaLV566SXFzusukJk3b55fAxmrP/zhD3j77bfx2muvYdy4cVi3bh2GDBmC48eP+zz27t27MW/ePAYyRDLqpPYEiEh9zz33HKKjo7F3717ExMTYvXbixAl1JqWAhoYGREZGut1n5MiR+O1vfwsAmDp1Kvr27Ys//OEPeOuttzB79mx/TJOIJOAVGSLCkSNHMGDAAIcgBgASEhIctq1ZswZZWVmIiIhAbGwsrrnmGnzxxRe21z/++GOMGzcOSUlJ0Ov16NWrFxYsWACz2Wzb57rrrsP69etx7Ngx2+2c1NRUfPnllxgyZAiAlkDC+lrrnJQ9e/ZgzJgxiI6ORkREBK699lrs2rXLbo55eXnQaDQoKyvD5MmTERsbixEjRkhemxtuuAEAUF5e7na/rVu3YuTIkYiMjERMTAxuueUWHDhwwG4+f/rTnwAAaWlptvd19OhRyXMioot4RYaIkJKSgoKCApSWliIjI8PtvvPmzUNeXh6uvvpqzJ8/H6GhodizZw+2bt2KUaNGAQBWr16Nzp07Y9asWejcuTO2bt2KOXPmoL6+Hn//+98BAH/5y19QV1eH//3vf1i8eDEAoHPnzrjsssswf/58zJkzBw8++CBGjhwJALj66qsBtAQMY8eORWZmJubOnQutVotVq1bhhhtuwFdffYWsrCy7+d52223o06cP/va3v0EQBMlrc+TIEQBA165dXe6zefNmjB07Fpdeeiny8vJw/vx5vPLKKxg+fDj27duH1NRUTJw4ET/++CPeeecdLF68GPHx8QCAbt26SZ4TEbUiEFGH98UXXwghISFCSEiIkJ2dLTz55JPCf//7X6G5udluv0OHDglarVa49dZbBbPZbPeaxWKx/b2xsdHhHA899JAQEREhNDU12baNGzdOSElJcdh37969AgBh1apVDufo06ePMHr0aIfzpaWlCbm5ubZtc+fOFQAId911l6g12LZtmwBAePPNN4WTJ08Kx48fF9avXy+kpqYKGo1G2Lt3ryAIglBeXu4wt4EDBwoJCQnC6dOnbdu+/fZbQavVCvfee69t29///ncBgFBeXi5qTkTkGW8tERFyc3NRUFCAm2++Gd9++y1eeOEFjB49Gj169MAnn3xi2++jjz6CxWLBnDlzoNXa/+9Do9HY/h4eHm77+9mzZ3Hq1CmMHDkSjY2N+OGHH7yeZ0lJCQ4dOoTJkyfj9OnTOHXqFE6dOoWGhgbceOON2LFjBywWi90xDz/8sKRz3H///ejWrRuSkpIwbtw4NDQ04K233sLgwYOd7l9ZWYmSkhLcd999iIuLs22/4oorkJubiw0bNkh/o0QkGm8tEREAYMiQIfjggw/Q3NyMb7/9Fh9++CEWL16M3/72tygpKUF6ejqOHDkCrVaL9PR0t2N9//33eOaZZ7B161bU19fbvVZXV+f1HA8dOgQAmDJlist96urqEBsba/s6LS1N0jnmzJmDkSNHIiQkBPHx8bjsssvQqZPr/1UeO3YMANCvXz+H1y677DL897//FZVkTETeYSBDRHZCQ0MxZMgQDBkyBH379sXUqVPx3nvvYe7cuaKOr62txbXXXouoqCjMnz8fvXr1QlhYGPbt24c///nPDldMpLAe+/e//x0DBw50uk/nzp3tvm59dUiMyy+/HDk5OV7Nj4j8j4EMEblkvZ1SWVkJAOjVqxcsFgvKyspcBhJffvklTp8+jQ8++ADXXHONbbuzp35a344Ss71Xr14AgKioqIAJNlJSUgAABw8edHjthx9+QHx8vO1q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27E5OTnIysrC3/72Nz+8IyJSGnNkiCigXH/99Vi+fLnt68jISGzevBkLFy7EDz/8gPr6ely4cAFNTU1obGxEREQEACA0NBRXXHGF7bj9+/fDbDajb9++duMbjUZ07drVP2+GiBTHQIaIAkpkZCR69+5t+/ro0aP4zW9+g0ceeQTPPfcc4uLisHPnTkybNg3Nzc22QCY8PBwajcZ23Llz5xASEoLi4mKEhITYnaNz587+eTNEpDgGMkQU0IqLi2GxWPB///d/tqeQ3n33XY/HXXXVVTCbzThx4gRGjhyp9DSJSCVM9iWigNa7d2+YTCa88sor+Omnn/D2229jxYoVHo/r27cv7r77btx777344IMPUF5ejqKiIixcuBDr16/3w8yJyB8YyBBRQLvyyivx4osvYtGiRcjIyMC///1vLFy4UNSxq1atwr333osnnngC/fr1w4QJE7B371707NlT4VkTkb/wqSUiIiIKWrwiQ0REREGLgQwREREFLQYyREREFLQYyBAREVHQYiBDREREQYuBDBEREQUtBjJEREQUtBjIEBERUdBiIENERERBi4EMERERBS0GMkRERBS0GMgQERFR0Pr/hXZBRyWEYhAAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x=df['Fare']\n",
    "y=df['Age']\n",
    "plt.scatter(x,y)\n",
    "plt.xlabel(\"Fare\")\n",
    "plt.ylabel(\"Age\")\n",
    "plt.grid()\n",
    "plt.title(\"Scatter Plot\")\n",
    "plt.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "986bb4cb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "10746a0c",
   "metadata": {},
   "source": [
    "### Outlier Removal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "cc02a9db",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.383838</td>\n",
       "      <td>2.308642</td>\n",
       "      <td>0.647587</td>\n",
       "      <td>29.699118</td>\n",
       "      <td>0.523008</td>\n",
       "      <td>0.381594</td>\n",
       "      <td>32.204208</td>\n",
       "      <td>1.536476</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>257.353842</td>\n",
       "      <td>0.486592</td>\n",
       "      <td>0.836071</td>\n",
       "      <td>0.477990</td>\n",
       "      <td>13.002015</td>\n",
       "      <td>1.102743</td>\n",
       "      <td>0.806057</td>\n",
       "      <td>49.693429</td>\n",
       "      <td>0.791503</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.420000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>223.500000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>22.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.910400</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>29.699118</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>14.454200</td>\n",
       "      <td>2.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>668.500000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>31.000000</td>\n",
       "      <td>2.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>512.329200</td>\n",
       "      <td>2.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       PassengerId    Survived      Pclass         Sex         Age  \\\n",
       "count   891.000000  891.000000  891.000000  891.000000  891.000000   \n",
       "mean    446.000000    0.383838    2.308642    0.647587   29.699118   \n",
       "std     257.353842    0.486592    0.836071    0.477990   13.002015   \n",
       "min       1.000000    0.000000    1.000000    0.000000    0.420000   \n",
       "25%     223.500000    0.000000    2.000000    0.000000   22.000000   \n",
       "50%     446.000000    0.000000    3.000000    1.000000   29.699118   \n",
       "75%     668.500000    1.000000    3.000000    1.000000   35.000000   \n",
       "max     891.000000    1.000000    3.000000    1.000000   80.000000   \n",
       "\n",
       "            SibSp       Parch        Fare    Embarked  \n",
       "count  891.000000  891.000000  891.000000  891.000000  \n",
       "mean     0.523008    0.381594   32.204208    1.536476  \n",
       "std      1.102743    0.806057   49.693429    0.791503  \n",
       "min      0.000000    0.000000    0.000000    0.000000  \n",
       "25%      0.000000    0.000000    7.910400    1.000000  \n",
       "50%      0.000000    0.000000   14.454200    2.000000  \n",
       "75%      1.000000    0.000000   31.000000    2.000000  \n",
       "max      8.000000    6.000000  512.329200    2.000000  "
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "37bcdb05",
   "metadata": {},
   "outputs": [],
   "source": [
    "percentile25 = df['Fare'].quantile(0.25)\n",
    "percentile75 = df['Fare'].quantile(0.75)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "27a2bd18",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7.9104"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "percentile25"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "c5d1d5e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "31.0"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "percentile75"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "4d02dcfb",
   "metadata": {},
   "outputs": [],
   "source": [
    "iqr=percentile75-percentile25"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "db9e8d3f",
   "metadata": {},
   "outputs": [],
   "source": [
    "upper_limit = percentile75 + 1.5 * iqr\n",
    "lower_limit = percentile25 - 1.5 * iqr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "daa6e92d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(-26.724, 65.6344)"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lower_limit,upper_limit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5d813ea",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "42a0f09d",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_df = df[(df['Fare'] <= 100) & (df['Fare'] >= 0)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "c3036a2b",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "      <th>Age_Grp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>1</td>\n",
       "      <td>22.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>0</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>0</td>\n",
       "      <td>30-39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>0</td>\n",
       "      <td>26.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>0</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>2</td>\n",
       "      <td>30-39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>1</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>30-39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>887</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Montvila, Rev. Juozas</td>\n",
       "      <td>1</td>\n",
       "      <td>27.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>211536</td>\n",
       "      <td>13.0000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>888</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Graham, Miss. Margaret Edith</td>\n",
       "      <td>0</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>112053</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>B42</td>\n",
       "      <td>2</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>889</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Johnston, Miss. Catherine Helen \"Carrie\"</td>\n",
       "      <td>0</td>\n",
       "      <td>29.699118</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>W./C. 6607</td>\n",
       "      <td>23.4500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>890</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Behr, Mr. Karl Howell</td>\n",
       "      <td>1</td>\n",
       "      <td>26.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>111369</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>C148</td>\n",
       "      <td>0</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>891</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Dooley, Mr. Patrick</td>\n",
       "      <td>1</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>370376</td>\n",
       "      <td>7.7500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "      <td>30-39</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>838 rows × 13 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass  \\\n",
       "0              1         0       3   \n",
       "1              2         1       1   \n",
       "2              3         1       3   \n",
       "3              4         1       1   \n",
       "4              5         0       3   \n",
       "..           ...       ...     ...   \n",
       "886          887         0       2   \n",
       "887          888         1       1   \n",
       "888          889         0       3   \n",
       "889          890         1       1   \n",
       "890          891         0       3   \n",
       "\n",
       "                                                  Name  Sex        Age  SibSp  \\\n",
       "0                              Braund, Mr. Owen Harris    1  22.000000      1   \n",
       "1    Cumings, Mrs. John Bradley (Florence Briggs Th...    0  38.000000      1   \n",
       "2                               Heikkinen, Miss. Laina    0  26.000000      0   \n",
       "3         Futrelle, Mrs. Jacques Heath (Lily May Peel)    0  35.000000      1   \n",
       "4                             Allen, Mr. William Henry    1  35.000000      0   \n",
       "..                                                 ...  ...        ...    ...   \n",
       "886                              Montvila, Rev. Juozas    1  27.000000      0   \n",
       "887                       Graham, Miss. Margaret Edith    0  19.000000      0   \n",
       "888           Johnston, Miss. Catherine Helen \"Carrie\"    0  29.699118      1   \n",
       "889                              Behr, Mr. Karl Howell    1  26.000000      0   \n",
       "890                                Dooley, Mr. Patrick    1  32.000000      0   \n",
       "\n",
       "     Parch            Ticket     Fare Cabin  Embarked Age_Grp  \n",
       "0        0         A/5 21171   7.2500   NaN         2   18-29  \n",
       "1        0          PC 17599  71.2833   C85         0   30-39  \n",
       "2        0  STON/O2. 3101282   7.9250   NaN         2   18-29  \n",
       "3        0            113803  53.1000  C123         2   30-39  \n",
       "4        0            373450   8.0500   NaN         2   30-39  \n",
       "..     ...               ...      ...   ...       ...     ...  \n",
       "886      0            211536  13.0000   NaN         2   18-29  \n",
       "887      0            112053  30.0000   B42         2   18-29  \n",
       "888      2        W./C. 6607  23.4500   NaN         2   18-29  \n",
       "889      0            111369  30.0000  C148         0   18-29  \n",
       "890      0            370376   7.7500   NaN         1   30-39  \n",
       "\n",
       "[838 rows x 13 columns]"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "fa08bf85",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x=new_df['Fare']\n",
    "y=new_df['Age']\n",
    "plt.scatter(x,y)\n",
    "plt.xlabel(\"Fare\")\n",
    "plt.ylabel(\"Age\")\n",
    "plt.grid()\n",
    "plt.title(\"Scatter Plot\")\n",
    "plt.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "af3a2153",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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kJT4AACSEh8AQFLiAwBISnwAAEmJDwAgKfEBACQlPgCApMQHAJCU+AAAkhIfAEBS4gMASEp8AABJiQ8AICnxAQAkJT4AgKTEBwCQlPgAAJISHwBAUuIDAEhKfAAASYkPACAp8QEAJCU+AICkxAcAkJT4AACSEh8AQFLiAwBISnwAAEmJDwAgKfEBACQlPgCApMQHAJCU+AAAkjqt+PjSl74UhUIhVq5cObStv78/li5dGueff35MmTIllixZEr29vac7JwAwTpxyfOzevTv+8i//MubNm1e1/fbbb4/vf//78cQTT8SOHTvi4MGD8bGPfey0BwUAxodTio9XX301br755vjGN74R73nPe4a29/X1xcMPPxz33ntvXHPNNXHppZfGI488Es8880zs2rVr1IYGAM5cpxQfS5cujY985CPR3t5etX3Pnj1x7Nixqu1z5syJmTNnxs6dO4d9roGBgSiVSlU3AGD8qhnpD2zdujWee+652L179wlrPT09cdZZZ8W5555btb2pqSl6enqGfb6NGzfGn/7pn450DADgDDWiPR/79++PFStWxJYtW6Kurm5UBlizZk309fUN3fbv3z8qzwsAjE0jio89e/bEoUOHYv78+VFTUxM1NTWxY8eOuO+++6Kmpiaampri6NGjcfjw4aqf6+3tjebm5mGfs7a2NhoaGqpuAMD4NaKPXX71V381Xnjhhaptt9xyS8yZMye+8IUvREtLS0yePDk6OjpiyZIlERGxd+/e6O7ujoULF47e1ADAGWtE8TF16tS46KKLqradc845cf755w9t/8xnPhOrVq2K8847LxoaGmL58uWxcOHCuPzyy0dvagDgjDXiA05/nq9+9atRLBZjyZIlMTAwEIsWLYqvf/3ro/1rAIAzVKFSqVTyHuLtSqVSNDY2Rl9fn+M/YBx5/fXXY/HixRERsW3btqivr895ImA0jeT927VdAICkxAcAkJT4AACSEh8AQFLiAwBISnwAAEmJDwAgKfEBACQlPgCApMQHAJCU+AAAkhIfAEBS4gMASEp8AABJiQ8AICnxAQAkJT4AgKTEBwCQlPgAAJISHwBAUuIDAEhKfAAASYkPACAp8QEAJCU+AICkxAcAkJT4AACSEh8AQFLiAwBISnwAAEmJDwAgKfEBACQlPgCApMQHAJCU+AAAkqrJe4DxqFKpRH9/f95j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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(new_df['Fare'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "a2b5557e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "      <th>Age_Grp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>1</td>\n",
       "      <td>22.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>0</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>0</td>\n",
       "      <td>30-39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>0</td>\n",
       "      <td>26.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>0</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>2</td>\n",
       "      <td>30-39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>1</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>30-39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>887</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Montvila, Rev. Juozas</td>\n",
       "      <td>1</td>\n",
       "      <td>27.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>211536</td>\n",
       "      <td>13.0000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>888</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Graham, Miss. Margaret Edith</td>\n",
       "      <td>0</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>112053</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>B42</td>\n",
       "      <td>2</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>889</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Johnston, Miss. Catherine Helen \"Carrie\"</td>\n",
       "      <td>0</td>\n",
       "      <td>29.699118</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>W./C. 6607</td>\n",
       "      <td>23.4500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>890</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Behr, Mr. Karl Howell</td>\n",
       "      <td>1</td>\n",
       "      <td>26.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>111369</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>C148</td>\n",
       "      <td>0</td>\n",
       "      <td>18-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>891</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Dooley, Mr. Patrick</td>\n",
       "      <td>1</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>370376</td>\n",
       "      <td>7.7500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "      <td>30-39</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>838 rows × 13 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass  \\\n",
       "0              1         0       3   \n",
       "1              2         1       1   \n",
       "2              3         1       3   \n",
       "3              4         1       1   \n",
       "4              5         0       3   \n",
       "..           ...       ...     ...   \n",
       "886          887         0       2   \n",
       "887          888         1       1   \n",
       "888          889         0       3   \n",
       "889          890         1       1   \n",
       "890          891         0       3   \n",
       "\n",
       "                                                  Name  Sex        Age  SibSp  \\\n",
       "0                              Braund, Mr. Owen Harris    1  22.000000      1   \n",
       "1    Cumings, Mrs. John Bradley (Florence Briggs Th...    0  38.000000      1   \n",
       "2                               Heikkinen, Miss. Laina    0  26.000000      0   \n",
       "3         Futrelle, Mrs. Jacques Heath (Lily May Peel)    0  35.000000      1   \n",
       "4                             Allen, Mr. William Henry    1  35.000000      0   \n",
       "..                                                 ...  ...        ...    ...   \n",
       "886                              Montvila, Rev. Juozas    1  27.000000      0   \n",
       "887                       Graham, Miss. Margaret Edith    0  19.000000      0   \n",
       "888           Johnston, Miss. Catherine Helen \"Carrie\"    0  29.699118      1   \n",
       "889                              Behr, Mr. Karl Howell    1  26.000000      0   \n",
       "890                                Dooley, Mr. Patrick    1  32.000000      0   \n",
       "\n",
       "     Parch            Ticket     Fare Cabin  Embarked Age_Grp  \n",
       "0        0         A/5 21171   7.2500   NaN         2   18-29  \n",
       "1        0          PC 17599  71.2833   C85         0   30-39  \n",
       "2        0  STON/O2. 3101282   7.9250   NaN         2   18-29  \n",
       "3        0            113803  53.1000  C123         2   30-39  \n",
       "4        0            373450   8.0500   NaN         2   30-39  \n",
       "..     ...               ...      ...   ...       ...     ...  \n",
       "886      0            211536  13.0000   NaN         2   18-29  \n",
       "887      0            112053  30.0000   B42         2   18-29  \n",
       "888      2        W./C. 6607  23.4500   NaN         2   18-29  \n",
       "889      0            111369  30.0000  C148         0   18-29  \n",
       "890      0            370376   7.7500   NaN         1   30-39  \n",
       "\n",
       "[838 rows x 13 columns]"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "e0f4ffcc",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_df=new_df.drop(['PassengerId','Name','Ticket','Cabin','Age_Grp'],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "7fa66672",
   "metadata": {},
   "outputs": [],
   "source": [
    "corrM=new_df.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "28b8ba3f",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(corrM,annot=True,cmap='PiYG')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "7ea64dc6",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=new_df.drop(['Survived'],axis=1)\n",
    "y=new_df['Survived']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "e294c748",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>22.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>26.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>27.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>13.0000</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>29.699118</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>23.4500</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>26.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>7.7500</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>838 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Pclass  Sex        Age  SibSp  Parch     Fare  Embarked\n",
       "0         3    1  22.000000      1      0   7.2500         2\n",
       "1         1    0  38.000000      1      0  71.2833         0\n",
       "2         3    0  26.000000      0      0   7.9250         2\n",
       "3         1    0  35.000000      1      0  53.1000         2\n",
       "4         3    1  35.000000      0      0   8.0500         2\n",
       "..      ...  ...        ...    ...    ...      ...       ...\n",
       "886       2    1  27.000000      0      0  13.0000         2\n",
       "887       1    0  19.000000      0      0  30.0000         2\n",
       "888       3    0  29.699118      1      2  23.4500         2\n",
       "889       1    1  26.000000      0      0  30.0000         0\n",
       "890       3    1  32.000000      0      0   7.7500         1\n",
       "\n",
       "[838 rows x 7 columns]"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "6b82c805",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      0\n",
       "1      1\n",
       "2      1\n",
       "3      1\n",
       "4      0\n",
       "      ..\n",
       "886    0\n",
       "887    1\n",
       "888    0\n",
       "889    1\n",
       "890    0\n",
       "Name: Survived, Length: 838, dtype: int64"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "daf769fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "89d70a97",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=21)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "9f1a4ecc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((670, 7), (670,), (168, 7), (168,))"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train.shape,y_train.shape,x_test.shape,y_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "5c9e1911",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import confusion_matrix,classification_report"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "df995411",
   "metadata": {},
   "source": [
    "### LogisticRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "3d05a4c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "lr=LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "da0b68c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LogisticRegression()"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lr.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "1d46eb2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training Accuracy\n",
      "0.7985074626865671\n",
      "Testing Accuracy\n",
      "0.8035714285714286\n"
     ]
    }
   ],
   "source": [
    "print(\"Training Accuracy\")\n",
    "print(lr.score(x_train,y_train))\n",
    "print(\"Testing Accuracy\")\n",
    "print(lr.score(x_test,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "da3e6fc5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], dtype=int64)"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pred=lr.predict(x_test)\n",
    "pred[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "f4ac582f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "631    0\n",
       "262    0\n",
       "464    0\n",
       "285    0\n",
       "538    0\n",
       "733    0\n",
       "809    1\n",
       "782    0\n",
       "450    0\n",
       "292    0\n",
       "Name: Survived, dtype: int64"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "bcf2da89",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[96, 20],\n",
       "       [13, 39]], dtype=int64)"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cm=confusion_matrix(pred,y_test)\n",
    "cm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "f875e778",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(cm,annot=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "4e4475fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.88      0.83      0.85       116\n",
      "           1       0.66      0.75      0.70        52\n",
      "\n",
      "    accuracy                           0.80       168\n",
      "   macro avg       0.77      0.79      0.78       168\n",
      "weighted avg       0.81      0.80      0.81       168\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(classification_report(pred,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "3be7a377",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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O+Hi4qIenVWpUiVUqlTpleMhIiKisk1yctOhQ4ci+5H89ttvktbn6+uLe/fuwd/fHykpKWjVqhVCQkLUnYyTk5NhYvK/C0zr1q2DUqlEv379NNYTEBCAefPmSdo2ERERGR/JyU2rVq003ufm5iI6OhqXL1+Gn59fsYIYP348xo8fr3VZWFiYxvukpKRibYOIiIjKB8nJzTfffKO1fN68ecjMzHzlgIiIiIhehd4mzvz444+xZcsWfa2OiIiIqFj0ltxEREQU+qwZIiIiopIi+bZU3759Nd4LIXD37l2cP38ec+fO1VtgRERERMUhObmxtbXVeG9iYoKGDRtiwYIFeO+99/QWGBEREVFxSEpu8vLyMGzYMDRv3hxVqlQxVExERERExSapz42pqSnee+89ybN/ExEREZUUyR2KmzVrhuvXrxsiFiIiIqJXJjm5+eKLLzB16lT88ssvuHv3LjIyMjReRERERKVJ5z43CxYswGeffYZu3boBAHr27KkxDYMQAjKZDHl5efqPkoiIiEhHOic38+fPx+jRo3HixAlDxkNERET0SnROboQQAID27dsbLBgiIiKiVyWpz01Rs4ETERERvQ4kPeemQYMGL01w7t+//0oBEREREb0KScnN/PnzCzyhmIiIiOh1Iim5GTBgAOzt7Q0VCxEREdEr07nPDfvbEBERUVmgc3KTP1qKiIiI6HWm820plUplyDiIiIiI9ELy9AtERERErzMmN0RERGRUmNwQERGRUWFyQ0REREaFyQ0REREZFSY3REREZFSY3BAREZFRYXJDRERERoXJDRERERkVJjdERERkVJjcEBERkVFhckNERERGhckNERERGRUmN0RERGRUmNwQERGRUWFyQ0REREaFyQ0REREZFSY3REREZFSY3BAREZFRYXJDRERERoXJDRERERkVJjdERERkVJjcEBERkVFhckNERERGhckNERERGZUKpR0AERkXIQSePn2KvLy80g6FiMoYMzMzmJqavvJ6mNwQkd4olUrcvXsXWVlZpR0KEZVBMpkMNWrUQKVKlV5pPUxuiEgvVCoVEhMTYWpqCicnJ8jlcshkstIOi4jKCCEE7t27h1u3bqF+/fqvdAWHyQ0R6YVSqYRKpYJCoYCVlVVph0NEZVC1atWQlJSE3NzcV0pu2KGYiPTKxIT/VoioePR1tZf/hYiIiMioMLkhIiIio8LkhojIwFxcXLBixYpit9+2bRsqV66st3jKqrCwMMhkMjx8+NDg2/r3339hb2+PpKQkg2+rvBgwYACWLVtWIttickNE5drQoUPRu3dvg27j3LlzGDVqlE51tSVCvr6+iI+P13l77777LmQyGWQyGSwsLNCgQQMEBgZCCCEl7NeOl5cX7t69C1tbW4Nva9GiRejVqxdcXFwKLPPx8YGpqSnOnTtXYNm7776LTz/9tEC5tgQ1IyMDs2fPRqNGjWBhYQEHBwd4e3tj//79Bv1dhYWFoXXr1jA3N0e9evWwbdu2l7Y5cuQI3nrrLVhbW6NatWr44IMPNBK//fv3o3PnzqhWrRpsbGzg6emJI0eOaKxjzpw5WLRoEdLT0/W8RwUxuSEiMrBq1aq90ggyS0tL2NvbS2ozcuRI3L17F3FxcZg5cyb8/f2xfv36YsegC6VSadD1y+VyODg4GPwRA1lZWdi8eTOGDx9eYFlycjLOnDmD8ePHY8uWLcXexsOHD+Hl5YWgoCDMnDkTUVFROHnyJHx9ffH5558bLAFITExE9+7d0aFDB0RHR+PTTz/FiBEjCiQiL7bp1asXOnbsiOjoaBw5cgRpaWno27evus7JkyfRuXNnHD58GJGRkejQoQN69OiBCxcuqOs0a9YMdevWxQ8//GCQfdMgypn09HQBQKSnp+t1vY9zckWt6b+IWtN/EY9zcvW6bqKyIDs7W8TExIjs7Gx1mUqlEo9zckv8pVKpdI7bz89P9OrVq9DlYWFh4s033xRyuVw4ODiI6dOni9zc//2NZ2RkiIEDBworKyvh4OAgli9fLtq3by8mTZqkrlOrVi3xzTffqI9JQECAUCgUQi6XC0dHRzFhwgQhhBDt27cXADReQgixdetWYWtrqxHXwYMHhZubmzA3NxdvvPGG6N27t3rZi9sXQojWrVuLPn36qN8/efJEfPbZZ8LJyUlYWVkJd3d3ceLECY02GzZsEDVq1BCWlpaid+/eYtmyZRpxBAQEiJYtW4qNGzcKFxcXIZPJhBBCPHjwQAwfPlzY2dkJa2tr0aFDBxEdHa1uFx0dLd59911RqVIlYW1tLVq3bi3OnTsnhBAiKSlJvP/++6Jy5crCyspKNGnSRBw6dEgIIcSJEycEAPHgwQP1uvbt2yeaNGki5HK5qFWrlvj666819qFWrVpi0aJFYtiwYaJSpUpCoVCI7777ThRl7969olq1alqXzZs3TwwYMEDExsYKW1tbkZWVpbFc27EXouDvcMyYMaJixYri9u3bBeo+evRI4zOmT59//rlo2rSpRpmvr6/w8fEptM3evXtFhQoVRF5enrrs4MGDQiaTCaVSWWi7Jk2aiPnz52uUzZ8/X7z99tuFttH2fySflPM3n3NDRAaTnZuHJv6FfyM0lJgFPrCSv/q/t9u3b6Nbt24YOnQogoKCcPXqVYwcORIWFhaYN28eAGDKlCkIDw/HwYMHUb16dfj7+yMqKgqtWrXSus4ff/wR33zzDYKDg9G0aVOkpKTg4sWLAJ5d2m/ZsiVGjRqFkSNHFhrXoUOH0KdPH8yePRtBQUFQKpU4fPiw1rpCCJw+fRpXr15F/fr11eXjx49HTEwMgoOD4eTkhAMHDqBLly64dOkS6tevj/DwcIwePRpffvklevbsiePHj2Pu3LkF1n/t2jX8+OOP2L9/v/q5JB9++CEsLS3x66+/wtbWFt999x06deqE+Ph4VK1aFYMGDYKrqyvWrVsHU1NTREdHw8zMDAAwbtw4KJVKnDx5EhUrVkRMTEyhT6uNjIxE//79MW/ePPj6+uLMmTMYO3Ys3njjDQwdOlRdb9myZVi4cCFmzZqFffv2YcyYMWjfvj0aNmyodb2nTp1CmzZttB7LrVu3Ys2aNWjUqBHq1auHffv2YfDgwdp/UYVQqVQIDg7GoEGD4OTkVGB5UU/nPXXqFLp27Vrk+r/77jsMGjRI67KIiAh4e3trlPn4+Gi9lZavTZs2MDExwdatWzF06FBkZmbi+++/h7e3t/r39iKVSoVHjx6hatWqGuXu7u5YtGgRcnJyYG5uXuR+vIrXIrlZs2YNli5dipSUFLRs2RKrVq2Cu7t7ofX37t2LuXPnIikpCfXr18eXX36Jbt26lWDERFQerF27FgqFAqtXr4ZMJkOjRo1w584dTJ8+Hf7+/nj8+DG2b9+OnTt3olOnTgCArVu3aj1h5UtOTlb3rTAzM0PNmjXV/++qVq0KU1NTWFtbw8HBodB1LFq0CAMGDMD8+fPVZS1btiwQ+6ZNm6BUKpGbmwsLCwtMnDhRHcPWrVuRnJysjnXq1KkICQnB1q1bsXjxYqxatQpdu3bF1KlTAQANGjTAmTNn8Msvv2hsR6lUIigoCNWqVQMAnD59GmfPnsU///yjPnl9/fXX+Omnn7Bv3z6MGjUKycnJmDZtGho1agQAGklXcnIyPvjgAzRv3hwAUKdOnUKPw/Lly9GpUyd10tWgQQPExMRg6dKlGslNt27dMHbsWADA9OnT8c033+DEiROFJjc3btzQ+js8fvw4srKy4OPjAwD4+OOPsXnzZsnJTVpaGh48eKDefync3NwQHR1dZJ3q1asXuiwlJaXA8urVqyMjIwPZ2dmwtLQs0KZ27do4evQo+vfvj08++QR5eXnw9PQsNKEGnv3OMzMz0b9/f41yJycnKJVKpKSkoFatWkXux6so9eRm9+7dmDJlCtavXw8PDw+sWLECPj4+iIuL03qP+cyZM/joo48QGBiI999/Hzt37kTv3r0RFRWFZs2alcIeEFFhLM1MEbPAp1S2qw+xsbHw9PTU6OPRtm1bZGZm4tatW3jw4AFyc3M1vozZ2toWetIEnl3VWLFiBerUqYMuXbqgW7du6NGjBypU0P3fcXR0dJFXdgBg0KBBmD17Nh48eICAgAB4eXnBy8sLAHDp0iXk5eWhQYMGGm1ycnLwxhtvAADi4uLQp08fjeXu7u4FkptatWqpExsAuHjxIjIzM9XryZednY2EhAQAz652jRgxQv3t/8MPP0TdunUBABMnTsSYMWNw9OhReHt744MPPkCLFi207mNsbCx69eqlUda2bVusWLECeXl56itJz7eXyWRwcHDAP//8U+ixy87OhoWFRYHyLVu2wNfXV/27+uijjzBt2jQkJCSo49eFeIXOwpaWlqhXr16x2xdHSkoKRo4cCT8/P3z00Ud49OgR/P390a9fPxw7dqxAH6idO3di/vz5+Pnnnwucx/OTJ0PPP1fqHYqXL1+OkSNHYtiwYWjSpAnWr18PKyurQjtqrVy5El26dMG0adPQuHFjLFy4EK1bt8bq1atLOHIiehmZTAYreYUSf73Oc1opFArExcVh7dq1sLS0xNixY9GuXTvk5ubqvA5t365fZGtri3r16uHNN9/Enj17sHr1ahw/fhwAkJmZCVNTU0RGRiI6Olr9io2NxcqVKyXtT8WKFTXeZ2ZmwtHRUWO90dHRiIuLw7Rp0wAA8+bNw5UrV9C9e3f89ttvaNKkCQ4cOAAAGDFiBK5fv47Bgwfj0qVLcHNzw6pVqyTF9KIXb53IZDKoVKpC69vZ2eHBgwcaZffv38eBAwewdu1aVKhQARUqVICzszOePn2qcb6ysbHR2hn44cOH6lFe1apVQ+XKlXH16lXJ+3Lq1ClUqlSpyNeOHTsKbe/g4IDU1FSNstTUVNjY2BT6uVqzZg1sbW3x1VdfwdXVFe3atcMPP/yA0NBQ/Pnnnxp1g4ODMWLECOzZs6fA7S/g2XEEoJEQG0KpJjdKpRKRkZEaB8DExATe3t6IiIjQ2qaw+4WF1c/JyUFGRobGi4hIF40bN0ZERITGN+3w8HBYW1ujRo0aqFOnDszMzDSGBKenp7902LalpSV69OiBb7/9FmFhYYiIiMClS5cAPBsRlJeXV2T7Fi1aIDQ0VOf9qFSpEiZNmoSpU6dCCAFXV1fk5eXhn3/+Qb169TRe+bfDGjZsWGCos7ahzy9q3bo1UlJSUKFChQLrtrOzU9dr0KABJk+ejKNHj6Jv377YunWreplCocDo0aOxf/9+fPbZZ9i4caPWbTVu3Bjh4eEaZeHh4WjQoMErzUvk6uqKmJgYjbIdO3agRo0auHjxokbStmzZMmzbtk39O2vYsCGioqIKrDMqKkp9pczExAQDBgzAjh07cOfOnQJ1MzMz8fTpU62x5d+WKurVs2fPQvfN09OzwGfn2LFj8PT0LLRNVlZWgWlV8o/v80nirl27MGzYMOzatQvdu3fXuq7Lly+jRo0aGp8FQyjV5CYtLQ15eXla7/+lpKRobVPY/cLC6gcGBsLW1lb9UigU+gmeiIxGenp6gRPEzZs3MXbsWNy8eRMTJkzA1atX8fPPPyMgIABTpkyBiYkJrK2t4efnh2nTpuHEiRO4cuUKhg8fDhMTk0KvHm3btg2bN2/G5cuXcf36dfzwww+wtLRU9z9wcXHByZMncfv2baSlpWldR0BAAHbt2oWAgADExsbi0qVL+PLLL4vcx08++QTx8fH48ccf0aBBAwwaNAhDhgzB/v37kZiYiLNnzyIwMBCHDh0CAEyYMAGHDx/G8uXL8ffff+O7777Dr7/++tKrYt7e3vD09ETv3r1x9OhRJCUl4cyZM5g9ezbOnz+P7OxsjB8/HmFhYbhx4wbCw8Nx7tw5NG7cGADw6aef4siRI0hMTERUVBROnDihXvaizz77DKGhoVi4cCHi4+Oxfft2rF69Wt1PqLh8fHxw5coVjas3mzdvRr9+/dCsWTON1/Dhw5GWloaQkBAAwJgxYxAfH4+JEyfir7/+QlxcHJYvX45du3bhs88+U69v0aJFUCgU8PDwQFBQEGJiYvD3339jy5YtcHV1RWZmptbY8m9LFfWytrYudN9Gjx6N69ev4/PPP8fVq1exdu1a7NmzB5MnT1bXWb16tboPGQB0794d586dw4IFC/D3338jKioKw4YNQ61ateDq6grg2a2oIUOGYNmyZfDw8EBKSgpSUlIKXMU6deoU3nvvPQm/jWJ66XgqA7p9+7YAIM6cOaNRPm3aNOHu7q61jZmZmdi5c6dG2Zo1a4S9vb3W+k+ePBHp6enq182bNw0yFPz5Ia9ShqESGYuihnC+zvz8/AoMvwYghg8fLoQo3lBwd3d3MWPGDHWd54eCHzhwQHh4eAgbGxtRsWJF8dZbb4njx4+r60ZERIgWLVoIc3PzIoeC//jjj6JVq1ZCLpcLOzs70bdvX/WywoYjf/LJJ6Jp06YiLy9PKJVK4e/vL1xcXISZmZlwdHQUffr0EX/99Ze6/oYNG4Szs7N6KPgXX3whHBwc1Mvzh4K/KCMjQ0yYMEE4OTkJMzMzoVAoxKBBg0RycrLIyckRAwYMUA+Fd3JyEuPHj1d/bsaPHy/q1q0rzM3NRbVq1cTgwYNFWlqaEKLooeBmZmaiZs2aYunSpRqxPH/s87Vs2VIEBAQUiPt57u7uYv369UIIIc6fPy8AiLNnz2qt27VrV41h9mfPnhWdO3cW1apVE7a2tsLDw0McOHCgQLuHDx+KGTNmiPr16wu5XC6qV68uvL29xYEDBwx6Hjlx4oT6s1OnTh2xdetWjeUBAQGiVq1aGmW7du0Srq6uomLFiqJatWqiZ8+eIjY2Vr1c22MMAAg/Pz91nezsbGFraysiIiIKjU1fQ8FLNbnJyckRpqamBX7pQ4YMET179tTaRqFQFPig+vv7ixYtWui0TUM954aovCuryY2+ZWZmCltbW7Fp06bSDkXvRowYUeQzSozJL7/8Iho3bqzxbBd6NWvXrhWdO3cuso6+kptSvS0ll8vRpk0bjft/KpUKoaGhhd7/K879QiIiQ7lw4QJ27dqFhIQEREVFqZ8v8uIonrLo66+/xsWLF3Ht2jWsWrUK27dvh5+fX2mHVSK6d++OUaNG4fbt26UditEwMzN75c7huir1oeBTpkyBn58f3Nzc4O7ujhUrVuDx48cYNmwYAGDIkCFwdnZGYGAgAGDSpElo3749li1bhu7duyM4OBjnz5/Hhg0bSnM3iKgc+/rrrxEXF6f+wnbq1CmDd5gsCWfPnsVXX32FR48eoU6dOvj2228xYsSI0g6rxBT1YDuSriQ/O6We3Pj6+uLevXvw9/dHSkoKWrVqhZCQEHWn4eTkZI1e2l5eXti5cyfmzJmDWbNmoX79+vjpp5/4jBsiKhWurq6IjIws7TAMYs+ePaUdAlGxyIQo49PESpSRkQFbW1ukp6fDxsamtMMhMhpPnjxBYmIiateurfUBaEREL1PU/xEp5+9Sf4gfERmXcvZ9iYj0SF//P5jcEJFe5D8F1tCPVSci46VUKgHglR7CCLwGfW6IyDiYmpqicuXK6jl7rKysXutpEIjo9aJSqXDv3j1YWVlJmmtNGyY3RKQ3+Y/uL2pSQiKiwpiYmKBmzZqv/MWIyQ0R6Y1MJoOjoyPs7e0lTQRJRAQ8e/7di/NYFQeTGyLSO1NT01e+Z05EVFzsUExERERGhckNERERGRUmN0RERGRUyl2fm/wHBGVkZJRyJERERKSr/PO2Lg/6K3fJzaNHjwAACoWilCMhIiIiqR49egRbW9si65S7uaVUKhXu3LkDa2trvT9gLCMjAwqFAjdv3uS8VQbE41wyeJxLBo9zyeGxLhmGOs5CCDx69AhOTk4vHS5e7q7cmJiYoEaNGgbdho2NDf9wSgCPc8ngcS4ZPM4lh8e6ZBjiOL/sik0+digmIiIio8LkhoiIiIwKkxs9Mjc3R0BAAMzNzUs7FKPG41wyeJxLBo9zyeGxLhmvw3Eudx2KiYiIyLjxyg0REREZFSY3REREZFSY3BAREZFRYXJDRERERoXJjURr1qyBi4sLLCws4OHhgbNnzxZZf+/evWjUqBEsLCzQvHlzHD58uIQiLdukHOeNGzfinXfeQZUqVVClShV4e3u/9PdCz0j9POcLDg6GTCZD7969DRugkZB6nB8+fIhx48bB0dER5ubmaNCgAf936EDqcV6xYgUaNmwIS0tLKBQKTJ48GU+ePCmhaMumkydPokePHnBycoJMJsNPP/300jZhYWFo3bo1zM3NUa9ePWzbts3gcUKQzoKDg4VcLhdbtmwRV65cESNHjhSVK1cWqampWuuHh4cLU1NT8dVXX4mYmBgxZ84cYWZmJi5dulTCkZctUo/zwIEDxZo1a8SFCxdEbGysGDp0qLC1tRW3bt0q4cjLFqnHOV9iYqJwdnYW77zzjujVq1fJBFuGST3OOTk5ws3NTXTr1k2cPn1aJCYmirCwMBEdHV3CkZctUo/zjh07hLm5udixY4dITEwUR44cEY6OjmLy5MklHHnZcvjwYTF79myxf/9+AUAcOHCgyPrXr18XVlZWYsqUKSImJkasWrVKmJqaipCQEIPGyeRGAnd3dzFu3Dj1+7y8POHk5CQCAwO11u/fv7/o3r27RpmHh4f45JNPDBpnWSf1OL/o6dOnwtraWmzfvt1QIRqF4hznp0+fCi8vL7Fp0ybh5+fH5EYHUo/zunXrRJ06dYRSqSypEI2C1OM8btw40bFjR42yKVOmiLZt2xo0TmOiS3Lz+eefi6ZNm2qU+fr6Ch8fHwNGJgRvS+lIqVQiMjIS3t7e6jITExN4e3sjIiJCa5uIiAiN+gDg4+NTaH0q3nF+UVZWFnJzc1G1alVDhVnmFfc4L1iwAPb29hg+fHhJhFnmFec4Hzx4EJ6enhg3bhyqV6+OZs2aYfHixcjLyyupsMuc4hxnLy8vREZGqm9dXb9+HYcPH0a3bt1KJObyorTOg+Vu4sziSktLQ15eHqpXr65RXr16dVy9elVrm5SUFK31U1JSDBZnWVec4/yi6dOnw8nJqcAfFP1PcY7z6dOnsXnzZkRHR5dAhMahOMf5+vXr+O233zBo0CAcPnwY165dw9ixY5Gbm4uAgICSCLvMKc5xHjhwINLS0vD2229DCIGnT59i9OjRmDVrVkmEXG4Udh7MyMhAdnY2LC0tDbJdXrkho7JkyRIEBwfjwIEDsLCwKO1wjMajR48wePBgbNy4EXZ2dqUdjlFTqVSwt7fHhg0b0KZNG/j6+mL27NlYv359aYdmVMLCwrB48WKsXbsWUVFR2L9/Pw4dOoSFCxeWdmikB7xyoyM7OzuYmpoiNTVVozw1NRUODg5a2zg4OEiqT8U7zvm+/vprLFmyBMePH0eLFi0MGWaZJ/U4JyQkICkpCT169FCXqVQqAECFChUQFxeHunXrGjboMqg4n2dHR0eYmZnB1NRUXda4cWOkpKRAqVRCLpcbNOayqDjHee7cuRg8eDBGjBgBAGjevDkeP36MUaNGYfbs2TAx4Xd/fSjsPGhjY2OwqzYAr9zoTC6Xo02bNggNDVWXqVQqhIaGwtPTU2sbT09PjfoAcOzYsULrU/GOMwB89dVXWLhwIUJCQuDm5lYSoZZpUo9zo0aNcOnSJURHR6tfPXv2RIcOHRAdHQ2FQlGS4ZcZxfk8t23bFteuXVMnjwAQHx8PR0dHJjaFKM5xzsrKKpDA5CeUglMu6k2pnQcN2l3ZyAQHBwtzc3Oxbds2ERMTI0aNGiUqV64sUlJShBBCDB48WMyYMUNdPzw8XFSoUEF8/fXXIjY2VgQEBHAouA6kHuclS5YIuVwu9u3bJ+7evat+PXr0qLR2oUyQepxfxNFSupF6nJOTk4W1tbUYP368iIuLE7/88ouwt7cXX3zxRWntQpkg9TgHBAQIa2trsWvXLnH9+nVx9OhRUbduXdG/f//S2oUy4dGjR+LChQviwoULAoBYvny5uHDhgrhx44YQQogZM2aIwYMHq+vnDwWfNm2aiI2NFWvWrOFQ8NfRqlWrRM2aNYVcLhfu7u7ijz/+UC9r37698PPz06i/Z88e0aBBAyGXy0XTpk3FoUOHSjjisknKca5Vq5YAUOAVEBBQ8oGXMVI/z89jcqM7qcf5zJkzwsPDQ5ibm4s6deqIRYsWiadPn5Zw1GWPlOOcm5sr5s2bJ+rWrSssLCyEQqEQY8eOFQ8ePCj5wMuQEydOaP1/m39s/fz8RPv27Qu0adWqlZDL5aJOnTpi69atBo9TJgSvvxEREZHxYJ8bIiIiMipMboiIiMioMLkhIiIio8LkhoiIiIwKkxsiIiIyKkxuiIiIyKgwuSEiIiKjwuSGiIiIjAqTGyIttm3bhsqVK5d2GMUmk8nw008/FVln6NCh6N27d4nE87qZO3cuRo0aVSLbCgsLg0wmw8OHD4us5+LighUrVhg0Fqnb0NffgS6fR6liYmJQo0YNPH78WK/rJePA5IaM1tChQyGTyQq8rl27VtqhYdu2bep4TExMUKNGDQwbNgz//POPXtZ/9+5ddO3aFQCQlJQEmUyG6OhojTorV67Etm3b9LK9wsybN0+9n6amplAoFBg1ahTu378vaT36TMRSUlKwcuVKzJ49W2P9+XHK5XLUq1cPCxYswNOnT195e15eXrh79y5sbW0BFJ4wnDt3rsQSrrJg0aJF8PLygpWVldbj1aRJE7z11ltYvnx5yQdHrz0mN2TUunTpgrt372q8ateuXdphAQBsbGxw9+5d3Lp1Cxs3bsSvv/6KwYMH62XdDg4OMDc3L7KOra1tiVydatq0Ke7evYvk5GRs3boVISEhGDNmjMG3W5hNmzbBy8sLtWrV0ijP/6z8/fff+OyzzzBv3jwsXbr0lbcnl8vh4OAAmUxWZL1q1arBysrqlbdnLJRKJT788MMiPyvDhg3DunXr9JKEknFhckNGzdzcHA4ODhovU1NTLF++HM2bN0fFihWhUCgwduxYZGZmFrqeixcvokOHDrC2toaNjQ3atGmD8+fPq5efPn0a77zzDiwtLaFQKDBx4sSXXi6XyWRwcHCAk5MTunbtiokTJ+L48ePIzs6GSqXCggULUKNGDZibm6NVq1YICQlRt1UqlRg/fjwcHR1hYWGBWrVqITAwUGPd+bcB8pM5V1dXyGQyvPvuuwA0r4Zs2LABTk5OUKlUGjH26tUL//nPf9Tvf/75Z7Ru3RoWFhaoU6cO5s+f/9ITS4UKFeDg4ABnZ2d4e3vjww8/xLFjx9TL8/LyMHz4cNSuXRuWlpZo2LAhVq5cqV4+b948bN++HT///LP66kpYWBgA4ObNm+jfvz8qV66MqlWrolevXkhKSioynuDgYPTo0aNAef5npVatWhgzZgy8vb1x8OBBAMCDBw8wZMgQVKlSBVZWVujatSv+/vtvddsbN26gR48eqFKlCipWrIimTZvi8OHDADRvS4WFhWHYsGFIT09X78u8efMAaN4yGjhwIHx9fTXiy83NhZ2dHYKCggAAKpUKgYGB6uPWsmVL7Nu3r8h9f5Gufwc//fQT6tevDwsLC/j4+ODmzZsay4vzuXiZ+fPnY/LkyWjevHmhdTp37oz79+/j999/f6VtkfFhckPlkomJCb799ltcuXIF27dvx2+//YbPP/+80PqDBg1CjRo1cO7cOURGRmLGjBkwMzMDACQkJKBLly744IMP8Ndff2H37t04ffo0xo8fLykmS0tLqFQqPH36FCtXrsSyZcvw9ddf46+//oKPjw969uypPqF+++23OHjwIPbs2YO4uDjs2LEDLi4uWtd79uxZAMDx48dx9+5d7N+/v0CdDz/8EP/++y9OnDihLrt//z5CQkIwaNAgAMCpU6cwZMgQTJo0CTExMfjuu++wbds2LFq0SOd9TEpKwpEjRyCXy9VlKpUKNWrUwN69exETEwN/f3/MmjULe/bsAQBMnToV/fv317gK5+XlhdzcXPj4+MDa2hqnTp1CeHg4KlWqhC5dukCpVGrd/v379xETEwM3N7eXxmppaalez9ChQ3H+/HkcPHgQEREREEKgW7duyM3NBQCMGzcOOTk5OHnyJC5duoQvv/wSlSpVKrBOLy8vrFixQn3V7u7du5g6dWqBeoMGDcJ///tfjUTjyJEjyMrKQp8+fQAAgYGBCAoKwvr163HlyhVMnjwZH3/8saQTvS5/B1lZWVi0aBGCgoIQHh6Ohw8fYsCAAerlxflcvPvuuxg6dKjOcRZGLpejVatWOHXq1Cuvi4yMwecdJyolfn5+wtTUVFSsWFH96tevn9a6e/fuFW+88Yb6/datW4Wtra36vbW1tdi2bZvWtsOHDxejRo3SKDt16pQwMTER2dnZWtu8uP74+HjRoEED4ebmJoQQwsnJSSxatEijzZtvvinGjh0rhBBiwoQJomPHjkKlUmldPwBx4MABIYQQiYmJAoC4cOGCRh0/Pz/Rq1cv9ftevXqJ//znP+r33333nXBychJ5eXlCCCE6deokFi9erLGO77//Xjg6OmqNQQghAgIChImJiahYsaKwsLAQAAQAsXz58kLbCCHEuHHjxAcffFBorPnbbtiwocYxyMnJEZaWluLIkSNa13vhwgUBQCQnJ2uUP79+lUoljh07JszNzcXUqVNFfHy8ACDCw8PV9dPS0oSlpaXYs2ePEEKI5s2bi3nz5mnd5okTJwQA8eDBAyFEwd99vlq1aolvvvlGCCFEbm6usLOzE0FBQerlH330kfD19RVCCPHkyRNhZWUlzpw5o7GO4cOHi48++khrHC9uQxttfwcAxB9//KEui42NFQDEn3/+KYTQ7XPx/OdRCCEGDx4sZsyYUWgczyvseOXr06ePGDp0qE7rovKjQmklVUQloUOHDli3bp36fcWKFQE8u4oRGBiIq1evIiMjA0+fPsWTJ0+QlZWltd/DlClTMGLECHz//ffqWyt169YF8OyW1V9//YUdO3ao6wshoFKpkJiYiMaNG2uNLT09HZUqVYJKpcKTJ0/w9ttvY9OmTcjIyMCdO3fQtm1bjfpt27bFxYsXATy7ktC5c2c0bNgQXbp0wfvvv4/33nvvlY7VoEGDMHLkSKxduxbm5ubYsWMHBgwYABMTE/V+hoeHa3wjz8vLK/K4AUDDhg1x8OBBPHnyBD/88AOio6MxYcIEjTpr1qzBli1bkJycjOzsbCiVSrRq1arIeC9evIhr167B2tpao/zJkydISEjQ2iY7OxsAYGFhUWDZL7/8gkqVKiE3NxcqlQoDBw7EvHnzEBoaigoVKsDDw0Nd94033kDDhg0RGxsLAJg4cSLGjBmDo0ePwtvbGx988AFatGhRZPxFqVChAvr3748dO3Zg8ODBePz4MX7++WcEBwcDAK5du4asrCx07txZo51SqYSrq6vO29Hl76BChQp488031W0aNWqEypUrIzY2Fu7u7sX6XOTfWtMHS0tLZGVl6W19ZByY3JBRq1ixIurVq6dRlpSUhPfffx9jxozBokWLULVqVZw+fRrDhw+HUqnU+s943rx5GDhwIA4dOoRff/0VAQEBCA4ORp8+fZCZmYlPPvkEEydOLNCuZs2ahcZmbW2NqKgomJiYwNHREZaWlgCAjIyMl+5X69atkZiYiF9//RXHjx9H//794e3tLbnPxfN69OgBIQQOHTqEN998E6dOncI333yjXp6ZmYn58+ejb9++BdpqSxby5Y8+AoAlS5age/fumD9/PhYuXAjgWR+YqVOnYtmyZfD09IS1tTWWLl2KP//8s8h4MzMz0aZNG42kMl+1atW0trGzswPwrA/Ni3XyE2G5XA4nJydUqKD7v8cRI0bAx8cHhw4dwtGjRxEYGIhly5YVSOKkGDRoENq3b49//vkHx44dg6WlJbp06QIA6ttVhw4dgrOzs0a7l3Ukz1ecvwNtivu50Jf79++rv2gQ5WNyQ+VOZGQkVCoVli1bpr4qkd+/oygNGjRAgwYNMHnyZHz00UfYunUr+vTpg9atWyMmJqZAEvUyJiYmWtvY2NjAyckJ4eHhaN++vbo8PDwc7u7uGvV8fX3h6+uLfv36oUuXLrh//z6qVq2qsb78/i15eXlFxmNhYYG+fftix44duHbtGho2bIjWrVurl7du3RpxcXGS9/NFc+bMQceOHTFmzBj1fnp5eWHs2LHqOi9eeZHL5QXib926NXbv3g17e3vY2NjotO26devCxsYGMTExaNCggcYybYkwADRu3BhPnz7Fn3/+CS8vLwDAv//+i7i4ODRp0kRdT6FQYPTo0Rg9ejRmzpyJjRs3ak1utO2LNl5eXlAoFNi9ezd+/fVXfPjhh+p+Xk2aNIG5uTmSk5M1PiNS6Pp38PTpU5w/f1792YuLi8PDhw/VVyT19bkorsuXL6Nfv36lsm16fbFDMZU79erVQ25uLlatWoXr16/j+++/x/r16wutn52djfHjxyMsLAw3btxAeHg4zp07p/7nPn36dJw5cwbjx49HdHQ0/v77b/z888+SOxQ/b9q0afjyyy+xe/duxMXFYcaMGYiOjsakSZMAPBvlsmvXLly9ehXx8fHYu3cvHBwctA7ttre3h6WlJUJCQpCamor09PRCtzto0CAcOnQIW7ZsUXckzufv74+goCDMnz8fV65cQWxsLIKDgzFnzhxJ++bp6YkWLVpg8eLFAID69evj/PnzOHLkCOLj4zF37lycO3dOo42Liwv++usvxMXFIS0tDbm5uRg0aBDs7OzQq1cvnDp1ComJiQgLC8PEiRNx69Ytrds2MTGBt7c3Tp8+rXO89evXR69evTBy5EicPn0aFy9exMcffwxnZ2f06tULAPDpp5/iyJEjSExMRFRUFE6cOFHo7UgXFxdkZmYiNDQUaWlpRd5SGThwINavX49jx45p/D6sra0xdepUTJ48Gdu3b0dCQgKioqKwatUqbN++Xaf90vXvwMzMDBMmTMCff/6JyMhIDB06FG+99ZY62SnO52LIkCGYOXNmkfElJycjOjoaycnJyMvLQ3R0NKKjozU6WSclJeH27dvw9vbWaZ+pHCntTj9EhqKtE2q+5cuXC0dHR2FpaSl8fHxEUFBQoZ0+c3JyxIABA4RCoRByuVw4OTmJ8ePHa3QWPnv2rOjcubOoVKmSqFixomjRokWBDsHPe1knyby8PDFv3jzh7OwszMzMRMuWLcWvv/6qXr5hwwbRqlUrUbFiRWFjYyM6deokoqKi1MvxQgfOjRs3CoVCIUxMTET79u0LPT55eXnC0dFRABAJCQkF4goJCRFeXl7C0tJS2NjYCHd3d7Fhw4ZC9yMgIEC0bNmyQPmuXbuEubm5SE5OFk+ePBFDhw4Vtra2onLlymLMmDFixowZGu3++ecf9fEFIE6cOCGEEOLu3btiyJAhws7OTpibm4s6deqIkSNHivT09EJjOnz4sHB2dlZ3lC7sWDzv/v37YvDgwcLW1lb9mYmPj1cvHz9+vKhbt64wNzcX1apVE4MHDxZpaWlCiIIdioUQYvTo0eKNN94QAERAQIAQQntn35iYGAFA1KpVq0DncZVKJVasWCEaNmwozMzMRLVq1YSPj4/4/fffC92PF7eh69/Bjz/+KOrUqSPMzc2Ft7e3uHHjhsZ6X/a5ePHz2L59e+Hn51donEI8+53g/zugP//K/90LIcTixYuFj49Pkeuh8kkmhBClkVQREZUGIQQ8PDzUtxepbFIqlahfvz527txZoPM9EW9LEVG5IpPJsGHDBj7VtoxLTk7GrFmzmNiQVrxyQ0REREaFV26IiIjIqDC5ISIiIqPC5IaIiIiMCpMbIiIiMipMboiIiMioMLkhIiIio8LkhoiIiIwKkxsiIiIyKkxuiIiIyKj8H6+3GIKCZzebAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.metrics import RocCurveDisplay\n",
    "rfc_disp = RocCurveDisplay.from_estimator(lr, x_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "9983d95d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7887931034482759"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn .metrics import roc_auc_score\n",
    "roc_auc_score(pred,y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd4918c4",
   "metadata": {},
   "source": [
    "### Decision Tree Classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "5526ea00",
   "metadata": {},
   "outputs": [],
   "source": [
    "dt=DecisionTreeClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "5d2e2449",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-2 {color: black;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>DecisionTreeClassifier()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">DecisionTreeClassifier</label><div class=\"sk-toggleable__content\"><pre>DecisionTreeClassifier()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "DecisionTreeClassifier()"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dt.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "4b8ea187",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training Accuracy\n",
      "0.982089552238806\n",
      "Testing Accuracy\n",
      "0.7678571428571429\n"
     ]
    }
   ],
   "source": [
    "print(\"Training Accuracy\")\n",
    "print(dt.score(x_train,y_train))\n",
    "print(\"Testing Accuracy\")\n",
    "print(dt.score(x_test,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "cca0b609",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, 0, 0], dtype=int64)"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pred=lr.predict(x_test)\n",
    "pred[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "e7a8a664",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "631    0\n",
       "262    0\n",
       "464    0\n",
       "285    0\n",
       "538    0\n",
       "Name: Survived, dtype: int64"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "55f3894e",
   "metadata": {},
   "outputs": [],
   "source": [
    "cm=confusion_matrix(pred,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "072b82ac",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(cm,annot=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "8e636bf3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.88      0.83      0.85       116\n",
      "           1       0.66      0.75      0.70        52\n",
      "\n",
      "    accuracy                           0.80       168\n",
      "   macro avg       0.77      0.79      0.78       168\n",
      "weighted avg       0.81      0.80      0.81       168\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(classification_report(pred,y_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3403d6a",
   "metadata": {},
   "source": [
    "### RandomForestClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "37c98e15",
   "metadata": {},
   "outputs": [],
   "source": [
    "rf=RandomForestClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "dfc843d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-3 {color: black;}#sk-container-id-3 pre{padding: 0;}#sk-container-id-3 div.sk-toggleable {background-color: white;}#sk-container-id-3 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-3 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-3 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-3 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-3 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-3 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-3 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-3 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-3 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-3 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-3 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-3 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-3 div.sk-item {position: relative;z-index: 1;}#sk-container-id-3 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-3 div.sk-item::before, #sk-container-id-3 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-3 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-3 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-3 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-3 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-3 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-3 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-3 div.sk-label-container {text-align: center;}#sk-container-id-3 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-3 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-3\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>RandomForestClassifier()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-3\" type=\"checkbox\" checked><label for=\"sk-estimator-id-3\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomForestClassifier</label><div class=\"sk-toggleable__content\"><pre>RandomForestClassifier()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "RandomForestClassifier()"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "c36f821b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training Accuracy\n",
      "0.982089552238806\n",
      "Testing Accuracy\n",
      "0.7857142857142857\n"
     ]
    }
   ],
   "source": [
    "print(\"Training Accuracy\")\n",
    "print(rf.score(x_train,y_train))\n",
    "print(\"Testing Accuracy\")\n",
    "print(rf.score(x_test,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "ba0373d2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, 0, 0], dtype=int64)"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pred=lr.predict(x_test)\n",
    "pred[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "bf97e734",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "631    0\n",
       "262    0\n",
       "464    0\n",
       "285    0\n",
       "538    0\n",
       "Name: Survived, dtype: int64"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "6a04dc15",
   "metadata": {},
   "outputs": [],
   "source": [
    "cm=confusion_matrix(pred,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "39b4d61d",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(cm,annot=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "95fb857f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.88      0.83      0.85       116\n",
      "           1       0.66      0.75      0.70        52\n",
      "\n",
      "    accuracy                           0.80       168\n",
      "   macro avg       0.77      0.79      0.78       168\n",
      "weighted avg       0.81      0.80      0.81       168\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(classification_report(pred,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "fd203154",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.metrics import RocCurveDisplay\n",
    "# rfc_disp = RocCurveDisplay.from_estimator(lr, x_test, y_test)\n",
    "rfc_disp = RocCurveDisplay.from_estimator(rf, x_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "def439b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import cross_val_score\n",
    "score=cross_val_score(rf, x_train,y_train,cv=5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "954beec0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8358208955223881"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "score.sum()/5"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "566793aa",
   "metadata": {},
   "source": [
    "### Hyperparameter Tuning"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "543e4b87",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import GridSearchCV ,RandomizedSearchCV\n",
    "import random"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b0d3aef5",
   "metadata": {},
   "source": [
    "#### Hyperparameter Tuning on Tree"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "6b2a9c37",
   "metadata": {},
   "outputs": [],
   "source": [
    "param_dist = {\"max_depth\": [3, 5,7],\n",
    "              \"max_features\": [3,5,7],\n",
    "              \"min_samples_leaf\": [2,4,7],\n",
    "              \"criterion\": [\"gini\", \"entropy\"]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "5950695c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# tree_cv = RandomizedSearchCV(dt, param_dist, cv = 5)\n",
    "tree_cv = GridSearchCV(dt, param_dist, cv = 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "ce8bbab7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-5 {color: black;}#sk-container-id-5 pre{padding: 0;}#sk-container-id-5 div.sk-toggleable {background-color: white;}#sk-container-id-5 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-5 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-5 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-5 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-5 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-5 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-5 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-5 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-5 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-5 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-5 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-5 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-5 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-5 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-5 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-5 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-5 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-5 div.sk-item {position: relative;z-index: 1;}#sk-container-id-5 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-5 div.sk-item::before, #sk-container-id-5 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-5 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-5 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-5 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-5 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-5 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-5 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-5 div.sk-label-container {text-align: center;}#sk-container-id-5 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-5 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-5\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>GridSearchCV(cv=5, estimator=DecisionTreeClassifier(),\n",
       "             param_grid={&#x27;criterion&#x27;: [&#x27;gini&#x27;, &#x27;entropy&#x27;],\n",
       "                         &#x27;max_depth&#x27;: [3, 5, 7], &#x27;max_features&#x27;: [3, 5, 7],\n",
       "                         &#x27;min_samples_leaf&#x27;: [2, 4, 7]})</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-7\" type=\"checkbox\" ><label for=\"sk-estimator-id-7\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">GridSearchCV</label><div class=\"sk-toggleable__content\"><pre>GridSearchCV(cv=5, estimator=DecisionTreeClassifier(),\n",
       "             param_grid={&#x27;criterion&#x27;: [&#x27;gini&#x27;, &#x27;entropy&#x27;],\n",
       "                         &#x27;max_depth&#x27;: [3, 5, 7], &#x27;max_features&#x27;: [3, 5, 7],\n",
       "                         &#x27;min_samples_leaf&#x27;: [2, 4, 7]})</pre></div></div></div><div class=\"sk-parallel\"><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-8\" type=\"checkbox\" ><label for=\"sk-estimator-id-8\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">estimator: DecisionTreeClassifier</label><div class=\"sk-toggleable__content\"><pre>DecisionTreeClassifier()</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-9\" type=\"checkbox\" ><label for=\"sk-estimator-id-9\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">DecisionTreeClassifier</label><div class=\"sk-toggleable__content\"><pre>DecisionTreeClassifier()</pre></div></div></div></div></div></div></div></div></div></div>"
      ],
      "text/plain": [
       "GridSearchCV(cv=5, estimator=DecisionTreeClassifier(),\n",
       "             param_grid={'criterion': ['gini', 'entropy'],\n",
       "                         'max_depth': [3, 5, 7], 'max_features': [3, 5, 7],\n",
       "                         'min_samples_leaf': [2, 4, 7]})"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tree_cv.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "ca9fcee8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0.8641791044776119, 0.7797619047619048)"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tree_cv.score(x_train,y_train),tree_cv.score(x_test,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "14f5bceb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'criterion': 'entropy',\n",
       " 'max_depth': 7,\n",
       " 'max_features': 3,\n",
       " 'min_samples_leaf': 2}"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tree_cv.best_params_"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "99d4ba94",
   "metadata": {},
   "source": [
    "#### Hyperparameter Tuning on Random Forest Classifier \n",
    "\n",
    "1. max_features{“sqrt”, “log2”, None}, int or float, default=”sqrt”\n",
    "The number of features to consider when looking for the best split:\n",
    "If “sqrt”, then max_features=sqrt(n_features).\n",
    "If “log2”, then max_features=log2(n_features).\n",
    "If None, then max_features=n_features.\n",
    "\n",
    "2. max_leaf_nodes, int, default=None\n",
    "Grow trees with max_leaf_nodes in best-first fashion. Best nodes are defined as relative reduction in impurity. If None then unlimited number of leaf nodes.\n",
    "\n",
    "3. max_depth int, default=None\n",
    "The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples.\n",
    "\n",
    "4. n_estimators int, default=100\n",
    "The number of trees in the forest."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "001564a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "param_grid = {\n",
    "    'n_estimators': [25, 50, 100, 150],\n",
    "    'max_features': ['sqrt', 'log2', None],\n",
    "    'max_depth': [3, 6, 9],\n",
    "    'max_leaf_nodes': [3, 6, 9],\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "70b3d260",
   "metadata": {},
   "outputs": [],
   "source": [
    "# rf_cv = RandomizedSearchCV(dt, param_dist, cv = 5)\n",
    "rf_cv = GridSearchCV(rf, param_dist, cv = 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "45ac5cc1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-6 {color: black;}#sk-container-id-6 pre{padding: 0;}#sk-container-id-6 div.sk-toggleable {background-color: white;}#sk-container-id-6 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-6 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-6 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-6 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-6 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-6 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-6 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-6 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-6 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-6 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-6 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-6 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-6 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-6 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-6 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-6 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-6 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-6 div.sk-item {position: relative;z-index: 1;}#sk-container-id-6 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-6 div.sk-item::before, #sk-container-id-6 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-6 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-6 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-6 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-6 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-6 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-6 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-6 div.sk-label-container {text-align: center;}#sk-container-id-6 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-6 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-6\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>GridSearchCV(cv=5, estimator=RandomForestClassifier(),\n",
       "             param_grid={&#x27;criterion&#x27;: [&#x27;gini&#x27;, &#x27;entropy&#x27;],\n",
       "                         &#x27;max_depth&#x27;: [3, 5, 7], &#x27;max_features&#x27;: [3, 5, 7],\n",
       "                         &#x27;min_samples_leaf&#x27;: [2, 4, 7]})</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-10\" type=\"checkbox\" ><label for=\"sk-estimator-id-10\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">GridSearchCV</label><div class=\"sk-toggleable__content\"><pre>GridSearchCV(cv=5, estimator=RandomForestClassifier(),\n",
       "             param_grid={&#x27;criterion&#x27;: [&#x27;gini&#x27;, &#x27;entropy&#x27;],\n",
       "                         &#x27;max_depth&#x27;: [3, 5, 7], &#x27;max_features&#x27;: [3, 5, 7],\n",
       "                         &#x27;min_samples_leaf&#x27;: [2, 4, 7]})</pre></div></div></div><div class=\"sk-parallel\"><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-11\" type=\"checkbox\" ><label for=\"sk-estimator-id-11\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">estimator: RandomForestClassifier</label><div class=\"sk-toggleable__content\"><pre>RandomForestClassifier()</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-12\" type=\"checkbox\" ><label for=\"sk-estimator-id-12\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomForestClassifier</label><div class=\"sk-toggleable__content\"><pre>RandomForestClassifier()</pre></div></div></div></div></div></div></div></div></div></div>"
      ],
      "text/plain": [
       "GridSearchCV(cv=5, estimator=RandomForestClassifier(),\n",
       "             param_grid={'criterion': ['gini', 'entropy'],\n",
       "                         'max_depth': [3, 5, 7], 'max_features': [3, 5, 7],\n",
       "                         'min_samples_leaf': [2, 4, 7]})"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf_cv.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "c7ce4cb2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0.8671641791044776, 0.8035714285714286)"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf_cv.score(x_train,y_train),rf_cv.score(x_test,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "2ab00d39",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'criterion': 'gini', 'max_depth': 5, 'max_features': 5, 'min_samples_leaf': 2}"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf_cv.best_params_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "221e6172",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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/okmTZrk20+pVEKpVErKRURERGWX5JEbmUyGmTNnIiEhATdv3sTFixfx9OlTLFiwQPLGFQoFWrZsqTUZOGdycLt27fJdbtmyZViwYAECAgLQqlUrydslIiIi4yV55CaHQqGAm5tbkQP4+PjA29sbrVq1Qps2bbBq1SqkpqZi+PDhAIChQ4fC2dkZixcvBgAsXboUc+bMwa5du+Dq6qqZm2NpaQlLS8si5yEiIqKyTXJx06lTJ8hksnxfP3HihKT1eXl54enTp5gzZw5iY2PRrFkzBAQEaCYZR0dHQy7/3wDT+vXrkZmZiY8++khrPb6+vpg7d66kbRMREZHxkVzcNGvWTOt5VlYWQkJCcPPmTXh7excqxPjx4zF+/Pg8Xzt16pTW86ioqEJtg4iIiN4Mkoub7777Ls/2uXPnIiUlpciBiIiIiIpCbzfOHDx4cL5XFX5TZKnUSEzLRGJaJpJeZhk6DhER0Rup0BOK/+vChQv5XmvmTZCUloUuK08jPiXD0FGIiIjeaJKLm759+2o9F0IgJiYGV65cwezZs/UWrKyJiE/Js7DpUt/eAGmIiIjeXJKLGxsbG63ncrkc9erVw/z589GtWze9BSurXCqa4+SX72qelzPR25E/IiIi0oGk4kalUmH48OFo3LgxKlSoUFyZyjQZZCxoiIiIDEjSt7CJiQm6desm+e7fRERERCVF8hBDo0aNcO/eveLIQkRERFRkkoubb775BlOmTMGhQ4cQExOD5ORkrQcRERGRIek852b+/Pn48ssv0aNHDwDAhx9+qHUbBiEEZDIZVCqV/lMSERER6Ujn4mbevHkYPXo0Tp48WZx5iIiIiIpE5+JGCAEA6NixY7GFISIiIioqSXNuCrobOBEREVFpIOk6N3Xr1n1tgZOQkFCkQERERERFIam4mTdvXq4rFBMRERGVJpKKm48//hj29rxXEhEREZVeOs+54XwbIiIiKgt0Lm5yzpYiIiIiKs10PiylVquLMwcRERGRXvD21URERGRUWNwQERGRUWFxQ0REREaFxQ0REREZFRY3REREZFRY3BAREZFRYXFDRERERoXFDRERERkVFjdERERkVFjcEBERkVFhcUNERERGhcUNERERGRUWN0RERGRUWNwQERGRUWFxQ0REREaFxQ0REREZFRY3REREZFRY3BAREZFRYXFDRERERoXFDRER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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "rfc_disp = RocCurveDisplay.from_estimator(rf_cv, x_test, y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f55d9c6",
   "metadata": {},
   "source": [
    "### Feature Selectiona and Feature Importance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "dbd1a2ff",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-7 {color: black;}#sk-container-id-7 pre{padding: 0;}#sk-container-id-7 div.sk-toggleable {background-color: white;}#sk-container-id-7 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-7 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-7 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-7 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-7 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-7 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-7 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-7 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-7 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-7 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-7 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-7 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-7 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-7 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-7 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-7 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-7 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-7 div.sk-item {position: relative;z-index: 1;}#sk-container-id-7 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-7 div.sk-item::before, #sk-container-id-7 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-7 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-7 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-7 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-7 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-7 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-7 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-7 div.sk-label-container {text-align: center;}#sk-container-id-7 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-7 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-7\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>SelectFromModel(estimator=RandomForestClassifier())</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-13\" type=\"checkbox\" ><label for=\"sk-estimator-id-13\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">SelectFromModel</label><div class=\"sk-toggleable__content\"><pre>SelectFromModel(estimator=RandomForestClassifier())</pre></div></div></div><div class=\"sk-parallel\"><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-14\" type=\"checkbox\" ><label for=\"sk-estimator-id-14\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">estimator: RandomForestClassifier</label><div class=\"sk-toggleable__content\"><pre>RandomForestClassifier()</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-15\" type=\"checkbox\" ><label for=\"sk-estimator-id-15\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomForestClassifier</label><div class=\"sk-toggleable__content\"><pre>RandomForestClassifier()</pre></div></div></div></div></div></div></div></div></div></div>"
      ],
      "text/plain": [
       "SelectFromModel(estimator=RandomForestClassifier())"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.feature_selection import SelectFromModel\n",
    "sel = SelectFromModel(rf)\n",
    "sel.fit(x_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "2a9ab92d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "selected_feat= x_train.columns[(sel.get_support())]\n",
    "len(selected_feat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "a92ea85d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Sex', 'Age', 'Fare'], dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(selected_feat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "b3ae3744",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "importances = sel.estimator_.feature_importances_\n",
    "indices = np.argsort(importances)[::-1]\n",
    "# X is the train data used to fit the model \n",
    "plt.figure()\n",
    "plt.title(\"Feature importances\")\n",
    "plt.bar(range(x.shape[1]), importances[indices],\n",
    "       color=\"r\", align=\"center\")\n",
    "plt.xticks(range(x.shape[1]), indices)\n",
    "plt.xlim([-1, x.shape[1]])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "id": "a25a515f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "with open('trained_model.pkl', 'wb') as model_file:\n",
    "    pickle.dump(rf, model_file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "e813bb35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter value for Age: 32\n",
      "Enter value for Sex: 0\n",
      "Enter value for Fare: 23\n",
      "Enter value for Embarked: 1\n",
      "Enter value for Pclass: 2\n",
      "Enter value for SibSp: 0\n",
      "Enter value for Parch: 0\n",
      "Predicted class: 1\n"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# Load the trained model\n",
    "with open('trained_model.pkl', 'rb') as model_file:\n",
    "    trained_model = pickle.load(model_file)\n",
    "\n",
    "# Get input features from the user\n",
    "input_features = []\n",
    "\n",
    "# Assuming you have a list of feature names\n",
    "feature_names = ['Age', 'Sex', 'Fare', 'Embarked','Pclass','SibSp','Parch']\n",
    "\n",
    "for feature_name in feature_names:\n",
    "    value = float(input(f\"Enter value for {feature_name}: \"))\n",
    "    input_features.append(value)\n",
    "\n",
    "# Convert input features to a NumPy array\n",
    "input_features_array = np.array(input_features).reshape(1, -1)\n",
    "\n",
    "# Make predictions using the loaded model\n",
    "predicted_class = trained_model.predict(input_features_array)\n",
    "\n",
    "print(f\"Predicted class: {predicted_class[0]}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "id": "8b2cb3df",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Survived  Pclass  Sex   Age  SibSp  Parch     Fare  Embarked\n",
       "0         0       3    1  22.0      1      0   7.2500         2\n",
       "1         1       1    0  38.0      1      0  71.2833         0\n",
       "2         1       3    0  26.0      0      0   7.9250         2\n",
       "3         1       1    0  35.0      1      0  53.1000         2\n",
       "4         0       3    1  35.0      0      0   8.0500         2"
      ]
     },
     "execution_count": 188,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a37736ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "streamlit cloud\n",
    "\n",
    "github"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
