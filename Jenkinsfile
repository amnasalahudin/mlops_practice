pipeline {
    agent any
    
    // Trigger the pipeline on GitHub push events
    triggers {
        githubPush()
    }
    
    environment {
        // Use Jenkins Credentials to store Docker Hub login
        DOCKERHUB_CREDENTIALS_ID = 'dockerhub-credentials'
        IMAGE_NAME = 'flask-app-test' // Define your Docker image name here
        TAG = 'latest' // Define your Docker image tag here
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
            // Note: Make sure Jenkins is configured to send emails. If not, use plugins or configure SMTP settings.
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
