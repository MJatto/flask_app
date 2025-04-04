pipeline {
    agent {label 'node1'}
    environment{
        ARCHIVE_NAME="${env.BUILD_TAG}.tar.gz"
        BUCKET_NAME ="s3://flask-app-proj"
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
                sh '''
                aws s3 cp ${ARCHIVE_NAME} ${BUCKET_NAME}
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                cd deployment
                
                ansible-playbook -i aws_ec2.yml  playbook.yml
                '''
            }
        }
    }
}