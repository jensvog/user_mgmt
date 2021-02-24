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