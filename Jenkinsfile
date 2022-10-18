pipeline {
    agent any

    stages{
        stage('Docker Build') {
            steps {
                sh 'docker build -t lenvendo_tests . < Dockerfile'
            }
        }
        stage('Tests') {
            steps {
                catchError {
                    sh """docker run --name lenvendo_tests --network selenoid lenvendo_tests --browser_name=${BROWSER_NAME} --browser_version=${BROWSER_VERSION} --hub=${HUB} --hub_port=${HUB_PORT} --enable_vnc=${ENABLE_VNC} --url=${URL} --api=${API} --search=${SEARCH} --sort_field=${SEARCH_FIELD}"""
                }
            }
        }
        stage('Copy Artefact') {
            steps {
                sh 'docker cp lenvendo_tests:/app/allure-results .'
            }
        }
        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
    post {
        always {
            sh 'docker rm lenvendo_tests'
        }
    }
}
