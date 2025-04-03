pipeline {
    agent {label 'node1'}

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Upload Artifact') {
            steps {
                echo 'Uploading artifact..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}