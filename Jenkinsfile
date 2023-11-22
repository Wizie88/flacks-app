pipeline {
    agent any
    
    environment {
        FLASK_APP = 'app.py'
        TEST_SCRIPT = 'test.py'
        ANSIBLE_PLAYBOOK = 'deploy.yml'
    }
    
    stages {
        stage('clone repo') {
            steps {
               git branch: 'main' , url: 'https://github.com/Wizie88/flacks-app.git'
            }
        }

        stage('install Packages needed') {
            steps{
                sh 'pip install virtualenv'
                sh 'virtualenv venv'
                sh 'source venv/bin/activate && pip install flask'
                sh 'chmod -R 755 venv'
            }
        }

        stage('Build') {
            steps {
                script {
                    // Set up virtual environment and install dependencies
                    sh 'echo "building will be done and deployed momentarity"'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh 'source venv/bin/activate && python $TEST_SCRIPT'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Running Ansible playbook for deployment
                    ansiblePlaybook credentialsId: 'f4', disableHostKeyChecking: true, installation: 'project2-1', inventory: 'hosts.ini', playbook: 'deploy.yml', vaultTmpPath: ''
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
