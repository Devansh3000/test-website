pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the project...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat 'pip install selenium'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Running Selenium test cases...'
                bat 'python tests/test_form.py'
            }
        }
    }

    post {
        success {
            echo '✅ All tests passed! Build successful.'
        }
        failure {
            echo '❌ Some tests failed. Check the console output for details.'
        }
    }
}
