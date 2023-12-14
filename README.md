![](America.gif.gif)
# Capstone Team 22 - War What Is It Good For?
Erica Huerta & Julien Szarata

## Project Overview
‘War, What Is It Good For?’ is a macroeconomic analysis of war and its impact to the United States. As the Israel-Hamas war advances and the United States is furthering its engagement in the war, it’s crucial that consumers understand the economic ramifications of war beyond human cost. While the broader implications of war may not be directly evident by a populace, consumers endure economic and financial consequences as a result of war that extends beyond when war conflict ceases, such as an increase in grocery prices, increase in the unemployment rate, and a decrease in personal savings. 

Our project analyzes multiple U.S. economic indicators, e.g. Gross Domestic Product, and attempts to model a counterfactual, i.e. if the United States was not engaged in war, what behaviors would we witness for those same economic indicators? Our project experiments with multiple machine learning models including ARMA, ARIMA, XGBOOST, and CNN, to predict a non-war counterfactual and compares the predicted versus actual economic data in an attempt to conclude war economic effects. In an effort to reduce the scope of our project to a manageable workload, we shifted the focus of our analysis to key-in on a primary macroeconomic indicator, Gross Domestic Product (GDP), which is widely sourced as the main indicator of the economic health and performance of a country. We further refined our scope to analyze two major U.S. wars over the last century, the Vietnam War and the Afghanistan War. Provided the complexity and pitfalls of the counterfactual analysis, we also included an independent country to act as a baseline for economic behavioral comparisons to enhance our findings. 

## Economic Indicators & Datasets

### 1. Gross Domestic Product (GDP)
Gross Domestic Product (GDP) a comprehensive measurement of economic activity and is, therefore, a widely used indicator when discussing the health of a national or global economy. GDP measures the monetary value of all final goods and services produced by the country over a given time period, including consumer spending, government spending, economic output, national income, standard of living, amongst many others. 

In the U.S., GDP is calculated on a quarterly and annual basis by the Bureau of Economic Analysis (BEAU), a division of the U.S. Department of Commerce. The frequency of calculation and publication will vary dependent on the country. 

$Gross\ Domestic\ Product\ (GDP)\ =\ Consumption\ +\ Investment\ +\ Government\ Spending\ +\ (Exports-Imports)$

### 2. Inflation
Inflation measures the rate in which the general level of prices for goods and services is changing over a given time period and signifies a consumer’s purchasing power, i.e. the amount of goods and services that a unit of currency can buy. For example, when inflation increases, consumer’s purchasing power decreases as they can afford less when prices increase, assuming the same amount of currency. 
Inflation rate is calculated from either the Consumer Price Index (CPI) or Personal Consumption Expenditures (PCE) economic measurement, further defined below. The inflation rate calculation requires a base period for comparison; the United States commonly uses a year-over-year comparison when calculating and publishing inflation. 

$`Inflation\ Rate\ =\ (\frac{Current\ CPI\ or\ PCE\\- \\Base\ CPI\ or\ PCE}{CPI\ or\ PCE} )\ x\ 100`$

### 3. Consumer Price Index (CPI)
The Consumer Price Index (CPI) quantifies the average change of prices for a pre-determined basket of goods and services paid by consumers over a given time period. CPI represents the cost of living for the average consumer and is one of two metrics used to calculate inflation rate. The selection of goods and services used as part of the CPI calculation is intended to represent typical consumptions items such as food, clothing, housing, healthcare, transportation, entertainment, and other goods and services. 

In the U.S., CPI is calculated by the Bureau of Labor Statistics (BLS) on a monthly basis. 

$`Consumer\ Price\ Index\ CPI\ =\ (\frac{Current\ Year\ Price\ of\ Basket\ (Goods\ and\ Services)}{Base\ Year\ Price\ of\ Basket\ (Goods\ and\ Services)} )\ x\ 100`$

### 4. Federal Debt
Federal Debt is the total amount of money the federal government has borrowed from external creditors and its own bondholders during a given period of time. Financial Debt is the accumulation of budget deficits, as defined when government expenditures exceed its revenues, i.e. collection of taxes, Treasure bonds, bills, and other means of revenue, during a fiscal year and is one of the many economic indicators analyzed when determining the financial health of a government. 

In the U.S., federal debt is managed by the U.S. Department of Treasury and is reported by the Congressional Budget Office (CBO), amongst other agencies, on quarterly basis.

$Federal\ Debt\ =\ Cumulative\ Budget\ Deficits\\ -\\ Cumulative\ Budget\ Surpluses$

### 5. Federal Debt-to-GDP Ratio
Federal Debt-to-GDP ratio is a comparison of federal debt to the country’s gross domestic product at a given period in time. A higher Debt-to-GDP ratio indicates a larger debt burden relative to the size of the economy’s productive output, GDP, and can be a cause for concern when the ratio is either extremely high or increasing rapidly, potentially acting as a precursor to a fiscal crisis.

In the U.S. and globally, central banks, e.g. Federal Reserve, European Central Bank (ECB), and international organizations, e.g. United Nations, monitors the Federal Debt-to-GDP ratio to assess the overall health of a country’s economy and to provide recommendations for sustainable fiscal policies. 


$`Federal\ Debt-to-GDP\ Ratio\ =\ (\frac{Federal\ Debt}{Gross\ Domestic\ Product\ (GDP)} ) x 100`$


### 6. Federal Tax Rates & Revenues
U.S. federal taxes include the various types of taxes imposed by the federal government to fund its operations and programs, as collected from individuals, businesses, and other entities. Federal taxes are the primary source of revenue for the government and its ability to fund activities, such as XX. During economic periods of growth, federal tax revenues naturally increase as individuals and businesses earn more income. During an economic downturn, federal tax revenues commonly decline, however, federal tax rates may increase due to inflationary pressure to offset total federal revenues collected to fund its operations or offset a federal deficit. We may also witness an inverse, wherein during periods of economic downturn, the federal government may decrease the federal tax rate to stimulate the economy and consumer expenditures.

Federal tax revenue is further defined to include the collection of individual income tax, i.e. what is paid as part of our wages and salary, corporate income tax, payroll tax, excise tax, estate tax, gift tax, customs duties, and other miscellaneous taxes and fees. Additionally, given the changes and revisions to tax laws over any given period in history, the composition of federal tax revenue may not be consistent when comparing two time periods. 

$Federal\ Tax\ Revenue\ = Income\ Tax\ +\ Corporate\ Income\ Tax\ +\ Payroll\ Tax\ +\ Excise\ Tax\ +\ Estate\ Tax\ +\ Customs\ Duties\ Tariffs\ +\ Other\ Taxes\ and\ Fees$

### 7. Personal Savings Rate
Personal Savings Rate is the percentage of personals savings relative to total personal income, less any personal outlays and taxes, thereafter, referred to as total disposable income. Personal Savings Rate is the portion of personal income saved as opposed to spent or consumed, e.g. taxes, and signifies saving behavior of a population. 

In the U.S., Personal Savings Rate is calculated by the Bureau of Labor Statistics (BLS) on a monthly basis. 

$`Personal Savings Rate = (\frac{Personal Saving}{Disposable Personal Income} ) x 100`$

### 8. Revolving Consumer Credit Outstanding
Revolving credit is either secured or unsecured credit plans that allow a consumer to borrow up to a prearranged limit and repay the debt in one or more installments, e.g. credit cards. Revolving Consumer Credit Outstanding is the amount owed, or otherwise referred to as the account balance, for any revolving credit plan. Revolving Consumer Credit Outstanding provides insights into consumer spending habits, financial health, and economic trends. 

In the U.S., Revolving Consumer Credit Outstanding is calculated by the Board of Governors of the Federal Reserve System on a monthly basis. 

$Revolving\ Consumer\ Credit\ Outstanding = Total\ Credit\ Limit-Total\ (Re)Payments$

### 9. Unemployment Rate
Unemployment Rate is the number of unemployed individuals relative to the total labor force, wherein unemployed individuals is further defined as individuals who are without a job and are actively seeking employment. Total labor force is defined as employed and unemployed individuals who are willing and able to work, but does not include individuals who are not actively seeking employment, e.g. discouraged individuals.

In the U.S., Unemployment Rate is calculated by the Bureau of Labor Statistics (BLS) on a monthly basis. 

$`Unemployment\ Rate\ =\ (\frac{Unemployed\ Individuals}{Total\ Labor\ Force} )\ x\ 100`$

### 10. Baseline Country Gross Domestic Product (Switzerland)
Switzerland adopted the international standard for measuring Gross Domestic Product (GDP), which is determined by the System of National Accounts (SNA) and is widely used by countries around the world for consistency in measurement. 

Switzerland’s Federal Statistical Office (FSO) is responsible for calculating Switzerland’s GDP, and does so on a quarterly basis much like the U.S. 

A critical note, Switzerland did not adopt the use of Gross Domestic Product until 1960; as such, our dataset only contains data from 1960 to present, presenting a gap in data when analyzing the economic counterfactual for any time period prior. 

We selected Switzerland as our baseline country for GDP comparison for the following reasons: 1. Switzerland’s GDP per capita was the second most similar to the U.S. GDP per capita, with its GDP per capita slightly above the U.S. as of 2022, 2. Switzerland historically does not engage in war, either directly or as a proxy, meaning Switzerland acts as a good counterfactual dataset for baseline comparisons. Following this same logic, our alternative baseline country was Denmark when analyzing GDP per capita, however Switzerland has a longer history and commitment of neutrality. Switzerland also has a larger population than Denmark, but this is inconsequential relatively. 
