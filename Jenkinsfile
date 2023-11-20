pipeline {
    agent any
    
    environment {
        FLASK_APP = 'app.py'
        TEST_SCRIPT = 'test.py'
        ANSIBLE_PLAYBOOK = 'deploy.yml'
        NON_PRODUCTION_SERVER = '172.31.31.71'
    }

    stages {
        stage('Checkout') {
            steps {
               checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    // Set up virtual environment and install dependencies
                    sh 'python -m venv venv'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh "python $TEST_SCRIPT"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Run Ansible playbook for deployment
                    sh "ansible-playbook -i $NON_PRODUCTION_SERVER $ANSIBLE_PLAYBOOK"
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded. App deployed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}