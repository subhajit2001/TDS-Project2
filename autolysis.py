# Importing the necessary libraries
import pandas as pd
import os
os.system("!pip install requests")
import requests
import sys
import shutil

# Change the current working directory
try:
    os.mkdir(sys.argv[1].split(".")[0])
    print(f"Directory '{sys.argv[1].split(".")[0]}' created successfully.")
except FileExistsError:
    print(f"Directory '{sys.argv[1].split(".")[0]}' already exists.")


# Importing the dataset
df = pd.read_csv(sys.argv[1],encoding='latin-1')
df.head()

# Initialization of proxy token along with the url
key = os.environ["AIPROXY_TOKEN"]
headers = {"Authorization": f"Bearer {key}"}
url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"

# Creation of an LLM response function
def llm_response(dataset_df, prompt):
	summary_dataset_csv = dataset_df.to_string()
	data = {
	    'model': 'gpt-4o-mini', 
	    'messages':[
		{"role":"system", "content":"You are a helpful assistant."},
		{"role":"user",  "content": prompt}
		]
	}

	data_response = requests.post(url, headers=headers, json=data).json()

	with open('file.txt', "a") as f:
		f.write(str(data_response))
		f.write("\n\n\n")

	return data_response['choices'][0]['message']['content']

# Creating the string for columns names to pass to the prompt
string_columns = ""
for i in df.columns:
	string_columns = string_columns+i+", "

# Creating the string for column datatypes to pass to the prompt 
string_dtypes = ""
for i in df.dtypes:
	string_dtypes = string_dtypes+str(i)+", "

# Summary of the dataset
summary_dataset = df.describe()

# Creation of the prompt for summarization of the dataset
prompt = f"Here is summary statistics data for a {sys.argv[1]} dataset file:\n{summary_dataset}\nPlease summarize it as a story. The summary statistics is obtained from the {sys.argv[1]} dataset containing multiple columns such as {string_columns}. The corresponding datatypes of the columns are {string_dtypes}. Please summarize the summary statistics as a story."

summarization_response = llm_response(summary_dataset, prompt=prompt)

print("Done with summarization")

# Correlation matrix of the dataset
corr_dataset = df.corr(numeric_only=True)

# Creation of the prompt for correlation of the dataset
prompt = f"Here is correlation statistics data across columns for a {sys.argv[1]} dataset file is \n{corr_dataset}\n. The correlation statistics data is obtained from the {sys.argv[1]} dataset containing multiple columns such as {string_columns}. The corresponding datatypes of the columns are {string_dtypes}. Please summarize the summary statistics as a story."

correlation_response = llm_response(corr_dataset, prompt=prompt)

print("Done with correlation")

# Changing the directory for saving the files
shutil.copy(sys.argv[1],'./'+sys.argv[1].split(".")[0])
os.chdir(sys.argv[1].split(".")[0])

# Creation of the prompt for generating the heatmap of the correlation matrix
prompt = f"Here is correlation statistics data across columns for a {sys.argv[1]} dataset file is \n{corr_dataset}\n. The statistics data is obtained from the {sys.argv[1]} dataset containing multiple columns such as {string_columns}. The corresponding datatypes of the columns are {string_dtypes}. Generate a python code to generate a heatmap for the correlation data provided as a png file."

# Cleaning out the response and getting the code
llm_res = llm_response(corr_dataset, prompt=prompt)

llm_res_actual = llm_res.split("```")

for i in range(len(llm_res_actual)):
	if llm_res_actual[i].count("python")>0:
		llm_res_final = llm_res_actual[i].replace("python","")

with open('corr_heatmap.py', 'w+') as f_heatmap:
	f_heatmap.write(llm_res_final)

# Changing the directory for saving the files
try:
	exec(open('corr_heatmap.py').read())
	print("Done with correlation heatmap generation")
except:
	print("Error doing correlation heatmap generation")

# Creation of the prompt for clustering analysis of the dataset
prompt = f"The dataset name is {sys.argv[1]}. The {sys.argv[1]} dataset is containing multiple columns such as {string_columns}. The corresponding datatypes of the columns are {string_dtypes}. Missing values have to be dealt with before any kind of analysis and should be done after selecting the features. Generate a python code to do a clustering analysis for the data. Save the images or plots as .png files.Use latin-1 as encoding while reading the csv file."

# Cleaning of the response and getting the code
llm_res = llm_response(corr_dataset, prompt=prompt)

llm_res_actual = llm_res.split("```")

for i in range(len(llm_res_actual)):
    if llm_res_actual[i].count("python")>0:
        llm_res_final = llm_res_actual[i].replace("python","")

with open('clustering.py', 'w+') as f_cluster:
    f_cluster.write(llm_res_final)

try:
	exec(open('clustering.py').read())
	print("Done with clustering")
except:
	print("Error doing clustering")

# Creation of the prompt for categorical analysis of the dataset
prompt = f"The dataset name is {sys.argv[1]}. The {sys.argv[1]} dataset is containing multiple columns such as {string_columns}. The corresponding datatypes of the columns are {string_dtypes}. Missing values have to be dealt with before any kind of analysis and should be done after selecting the features. Generate a python code to do a categorical columns data wise analysis for the data. The column names have to be used properly otherwise code returned might not run. Save the images or plots as .png files.Use latin-1 as encoding while reading the csv file."

# Cleaning of the response and getting the code
llm_res = llm_response(corr_dataset, prompt=prompt)

llm_res_actual = llm_res.split("```")

for i in range(len(llm_res_actual)):
    if llm_res_actual[i].count("python")>0:
        llm_res_final = llm_res_actual[i].replace("python","")

with open('categorical-wise.py', 'w+') as f_category:
    f_category.write(llm_res_final)
    
try:
	exec(open('categorical-wise.py').read())
	print("Done with categorical analysis")
except:
	print("Error doing categorical analysis")

# Generating a README.md file
os.chdir("..")
with open('README.md', 'w+') as f:
    f.write(summarization_response)
    f.write(correlation_response)
    
print("Done with README.md generation")
