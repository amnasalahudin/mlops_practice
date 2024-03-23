pipeline {
    agent any

    triggers {
        githubPush()
    }
    
    environment {
        // Use Jenkins Credentials to store Docker Hub login
        DOCKERHUB_CREDENTIALS_ID = 'dockerhub-credentials'
        IMAGE_NAME = 'amnasalahudin/flask-app-test' // Include Docker Hub username here
        TAG = 'latest' // Define your Docker image tag here
        DOCKER_HOST = 'tcp://localhost:2375' // Define Docker daemon endpoint here
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checks out the Git repository
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                script {
                    // Building the Docker image from the Dockerfile in the current directory
                    docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }
        
        stage('Push') {
            steps {
                script {
                    // Logging in to Docker Hub and pushing the image
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS_ID) {
                        docker.image("${IMAGE_NAME}:${TAG}").push()
                    }
                }
            }
        }
    }
    
    post {
        success {
            // Notifying the administrator via email
            mail to: 'amnasalahudin123@gmail.com',
                 subject: "Successful Docker Image Build",
                 body: "The Docker image ${IMAGE_NAME}:${TAG} has been built and pushed successfully."
        }
        failure {
            // Optionally, notify if the pipeline fails
            mail to: 'amnasalahudin123@gmail.com',
                 subject: "Docker Image Build Failed",
                 body: "There was a problem building or pushing the Docker image ${IMAGE_NAME}:${TAG}."
        }
    }
}
