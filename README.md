\documentclass{article}
\usepackage{graphicx} % Required for inserting images

\title{International Debt Analysis}
\author{Basil Osman}
\date{December 2023}

\begin{document}

\maketitle

\section{Introduction}

This is a project that uses the IDS dataset on Kaggle from the world bank to compare the how LEDC's (Less Economically Developed Countries) are affected by different types of debt statistics from 2000 to 2020, such as IMF credit and external debt etc. The goal of this project was to show how debt can negatively affect LEDC's and how more powerful countries are using international aid/loans to take advantage of these countries.

\section{Project overlay}
The first part of the project is located in the \textit{main.py} file, where I extract the data from the json and clean it up so that statistics with less data are removed and only necessary data is kept, which is determined by finding out how many missing values are in each category. Then I reformatted the data into a JSON file for ease in manipulation. \\

The second part - the analysis - is located in \textit{debt_analysis_jup-notebook.ipynb} and contains 3 main parts of analysis: a correlation graph between the economic indicators and the debt statistics; some bar charts on the debt statistics and comparison between different countries; a clustering graph that can compare two values (categories of debt) in a given year to see how these LEDC's match up together.

\section{Analysis Technique}
The correlation graph is gained from getting all the values of the LEDC's of the indicators and the categories of debt and finding the correlation matrix in each year and summing these values then finding the average correlation. This is displayed in two graph, the original correlation matrix between the indicators and the debt categories through a heat-map, furthermore a secondary graph with the data normalised (the standard deviation of the data is set to 1 and the mean is 0) for better readability of the graph, however some of the data is skewed due to a larger number of positive values leading to more of the data becoming positive, which may cause misinterpretation of the data. \\

The bar charts are for comparison between countries of their year by year data, to see how different LEDC's debt and performance have trended from 2000 to 2020. The '\textit{barchart}' function takes in the selected countries of comparison and either some selected categories it can show all 26 debt categories chosen. It then gives a graph showing all this data in different bar charts for the countries which can they be used to observe patterns over the years. \\

The final part of the analysis techniques used is a clustering algorithm that shows how all the different countries \textit{cluster} given the data. It displays how these countries cluster through the comparison of two categories of debt in a given years data. This is done by using the K-Means algorithm, provided by the scikit-learn library on python. First the data from the given it get cleans empty values by using means and then it standardised for ease of comparison. The number of clusters is then determined using the elbow method, however I have automated it to choose the cluster number where its inertia is a quarter of the original inertia. Then the k-means algorithm is applied and the result is displayed in a scatter-graph.

\section{Analysis Findings}
The observed data suggests a leaning towards the notion that Less Economically Developed Countries (LEDCs) do not experience significant benefits from incurring debt. In fact, the prevailing trend indicates a detrimental impact on their current economic levels. The analysis focused on correlations, particularly with GDP per capita and various debt statistics. \\

Among the debt-related variables, there were notable positive correlations with interest payments on external debt, short-term debt, and total debt service, all expressed as percentages. These findings imply that higher levels of these debt-related components coincide with increased GDP per capita in LEDCs. On the flip side, external debt exhibited larger negative correlations, indicating a potentially more adverse effect on economic performance when it comes to indebtedness to foreign entities. \\

Interestingly, when considering the other two indicators, there was less correlation, suggesting that the impact of debt might be more pronounced in the short term rather than having a sustained effect over the long term. This observation gains support from the year-on-year data, where correlations were weaker, implying that the influence of debt on economic levels might be more immediate and less enduring over successive years. \\

\newpage
In summary, the data implies that, for LEDCs, the nature of the correlation between debt and economic indicators is nuanced. While certain forms of debt, such as interest payments, short-term debt, and total debt service, may have positive associations with GDP per capita, external debt appears to have a more consistently negative impact. Moreover, the weaker correlations over successive years suggest that the influence of debt on LEDC economies might be more transitory in nature, with short-term effects overshadowing long-term trends.

\section{Packages used}

In my Python project, I utilized a diverse set of packages within the context of a Jupyter Notebook for comprehensive data analysis and visualization. The \textbf{json} package facilitated efficient encoding and decoding of JSON data, while the powerful data manipulation and analysis capabilities of \textbf{pandas} were harnessed through DataFrames. Numerical operations and array handling were streamlined using \textbf{numpy}. Visualization, a crucial aspect of my analysis, was achieved using \textbf{matplotlib.pyplot} and \textbf{seaborn} for creating various types of plots and charts. The \textbf{os} module facilitated seamless interaction with the operating system for file and directory manipulation. The integration of external data sources was made possible through the \textbf{wbgapi} package, likely dedicated to fetching economic and financial data from the World Bank. The \textbf{notion_client} package enabled programmatic interaction with Notion databases and pages, offering a collaborative workspace aspect to the project. For machine learning tasks, the scikit-learn library played a key role, with the \textbf{StandardScaler} class ensuring proper scaling of numerical features, and the \textbf{KMeans} class facilitating k-means clustering. The entire workflow was executed within the Python ecosystem, leveraging the capabilities of Jupyter Notebooks for a seamless and interactive development environment.

\end{document}
