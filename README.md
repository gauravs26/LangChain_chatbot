# LangChain_chatbot
System to scrape a given web URL, analyze the content, and answer queries based on the information from the scraped data so that user can get precise and relevant responses without manually reading through the website.

<img width="951" alt="Demo" src="https://github.com/user-attachments/assets/c3be51b7-a540-4f19-8266-aa2c56c474b3">

### Containerize the Application
Containerization involves packaging your application and its dependencies to ensure it runs consistently across different environments. 
Requirements
•	Docker installed locally.
•	Optimized code for model inference (fast loading, minimal overhead).
Steps
1.	Create a requirements.txt file listing dependencies
2.	Create a Dockerfile for your Python application.
3.	Build the Docker image: docker build -t genai-microservice:latest .
4.	Test locally:  docker run -p 8000:8000 genai-microservice:latest

### Optimize the Model Loading
Optimize the AI model to reduce initialization time and memory usage. You can use techniques such as:
•	Pre-loading the model in memory.
•	Quantization to reduce model size and inference time.

### Monitoring and Logging
Add logging for better visibility into requests and errors.
4. Testing the Dockerized Application
Run Locally
docker run -p 8000:8000 genai-microservice:latest
Test the Endpoint
Use tools like curl or Postman:
curl -X POST "http://localhost:8000/summarize/" -H "Content-Type: application/json" -d '{"input_text": "The quick brown fox jumps over the lazy dog."}'

Requirements for Deployment
1.	Docker:
o	Ensure Docker is installed on your local system.
o	Push the Docker image to a container registry (e.g., Docker Hub).


### Cloud Deployment Overview
Cloud deployment involves:
1.	Hosting your microservice on a cloud platform (AWS, Azure, or GCP).
2.	Using Kubernetes for orchestration.
3.	Automating the deployment with CI/CD pipelines.

#### Requirements
Infrastructure Requirements:
1.	Cloud Account: 
o	AWS, Azure, or Google Cloud account.
2.	Kubernetes Cluster: 
o	Use a managed Kubernetes service like: 
	AWS EKS (Elastic Kubernetes Service).
	Azure AKS (Azure Kubernetes Service).
	GKE (Google Kubernetes Engine).
Tools Required:
•	kubectl: For managing Kubernetes clusters.
•	Docker: To build and push container images.
•	CI/CD Tool: GitHub Actions, Jenkins, or GitLab CI/CD.
•	Container Registry: Docker Hub, AWS ECR, or Google Container Registry.

#### Steps for Deployment
Step 1: Push Docker Image to a Container Registry
1.	Build and tag the Docker image: 
2.	docker build -t genai-microservice:latest .
3.	docker tag genai-microservice:latest <YOUR_REGISTRY>/genai-microservice:latest
4.	Log in to your container registry: 
5.	docker login
6.	Push the image:  docker push <YOUR_REGISTRY>/genai-microservice:latest
7.	
Step 2: Write Kubernetes Manifests
Create the required YAML files for Kubernetes deployment.

Step 3: Deploy to Kubernetes
1.	Connect to your Kubernetes cluster: 
2.	kubectl config use-context <YOUR_CLUSTER_CONTEXT>
3.	Apply the YAML files: 
4.	kubectl apply -f deployment.yaml
5.	kubectl apply -f service.yaml
6.	Verify deployment: 
7.	kubectl get pods
8.	kubectl get services

Step 4: Automate Deployment with CI/CD
Set up a CI/CD pipeline to automate the build, test, and deployment process.

Step 5: Expose the Application
After deploying, Kubernetes assigns an external IP to the service.
1.	Check the external IP: 
2.	kubectl get service genai-service
3.	Test the application using the external IP: 
4.	curl -X POST "http://<EXTERNAL_IP>/summarize/" -H "Content-Type: application/json" -d '{"input_text": "The quick brown fox jumps over the lazy dog."}'

#### Testing the Cloud Deployment
1.	Postman or cURL: 
o	Send API requests to verify the service functionality.
2.	Load Testing: 
o	Use tools like Apache JMeter or Locust for testing scalability.
Final Deliverables
1.	Push all YAML files and pipeline configurations to your GitHub repository.
2.	Add deployment steps to the README.md file: 
o	Steps to connect to the Kubernetes cluster.
o	Commands to apply YAML files.
o	Instructions to test the service.

