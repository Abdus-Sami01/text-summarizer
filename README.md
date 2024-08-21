Text Summarization Project
Workflows:

Update config.yaml
Update params.yaml
Update entity
Update the configuration manager in src/config
Update the components
Update the pipeline
Update main.py
Update app.py
How to Run:

Clone the Repository:
https://github.com/Abdus-Sami01/text-summarizer.git

Create and Activate Conda Environment:
conda create -n summary python=3.8 -y
conda activate summary

STEP 02- install the requirements
pip install -r requirements.txt
run the following command
python app.py

open up you local host and port

AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment
   1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

Create ECR repo to store/save docker image  

Create EC2 machine (Ubuntu)

Open EC2 and Install docker in EC2 Machine

Configure EC2 as self-hosted runnerSetup github secrets

and you are done
