pipeline {
    agent {label 'node1'}
    environment{
        ARCHIVE_NAME="${env.BUILD_TAG}.tar.gz"
    }

    stages {
        stage('Build') {
            steps {
                script{
                    sh '''
                    python3 -m venv venv

                    source venv/bin/activate

                    pip install -r requirements.txt

                    touch ${ARCHIVE_NAME}
                    tar --exclude=${ARCHIVE_NAME} -czvf ${ARCHIVE_NAME} .
                    '''
                }
                
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