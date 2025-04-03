pipeline {
    agent {label 'node1'}

    stages {
        stage('Build') {
            steps {
                sh '''
                python3 -m venv venv

                source venv/bin/activate

                pip install -r requirements.txt 
                '''
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