pipeline {
    agent any

    parameters {
        choice(
            name: 'ENV',
            choices: ['qa', 'uat', 'prod'],
            description: 'Select Environment'
        )
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Execute Tests') {
            steps {
                sh """
                    . venv/bin/activate
                    pytest -v \
                    --env=${params.ENV} \
                    --alluredir=reports/allure-reports \
                    tests/
                """
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'reports/allure-reports']]
                ])
            }
        }
    }

    post {

        always {
            archiveArtifacts(
                artifacts: 'reports/**/*',
                allowEmptyArchive: true
            )

            junit(
                testResults: 'reports/junit.xml',
                allowEmptyResults: true
            )
        }

        success {
            echo 'Automation execution completed successfully.'
        }

        failure {
            echo 'Automation execution failed.'
        }
    }
}