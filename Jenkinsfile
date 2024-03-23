pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS_ID = 'dockerhub-credentials'
    }
    stages {
        stage('Build') {
            steps {
                script {
                    docker.build('flask-app-test')
                }
            }
        }
        stage('Push') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS_ID) {
                        docker.image('flask-app-test').push('latest')
                    }
                }
            }
        }
    }
    post {
        success {
            // Notify the administrator via email
            mail to: 'amnasalahudin123@gmail.com',
                 subject: "Successful Docker Image Build",
                 body: "The Docker image has been built and pushed successfully."
        }
    }
}
