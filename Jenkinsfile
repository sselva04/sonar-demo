pipeline {
  agent any
  stages {
    stage('Sonar scan') {
      steps {
        withSonarQubeEnv('sonarqube') {
          script {
            def scannerHome = tool 'sonar-scanner'
            sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=demo-project -Dsonar.sources=. -Dsonar.qualitygate.wait=true -Dsonar.token=\$SONAR_AUTH_TOKEN"
          }
        }
      }
    }
  }
}
