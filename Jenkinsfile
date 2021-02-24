pipeline {
    agent {
        dockerfile true
    } 
    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }
        stage('Test') { 
            steps {
                sh 'pytest --junitxml unit_test_report.xml'
            }
        }
        stage('Create page') { 
            steps {
                sh 'python user_mgmt.py'
            }
        }
    }
    post {
        always {
            junit 'unit_test_report.xml'
        }
        success {
            archiveArtifacts artifacts: 'unit_test_report.xml,index.html', followSymlinks: false
        }
    }
}