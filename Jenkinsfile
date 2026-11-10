pipeline {
  agent any
  stages {
    stage('Test and coverage') {
      steps {
        sh '''
          python3 -m venv .venv
          . .venv/bin/activate
          pip install -q pytest pytest-cov
          pytest --cov=. --cov-report=xml
        '''
      }
    }
    stage('Sonar scan') {
      steps {
        withSonarQubeEnv('sonarqube') {
          script {
            def scannerHome = tool 'sonar-scanner'
            sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=demo-project -Dsonar.sources=. -Dsonar.exclusions=.venv/** -Dsonar.python.coverage.reportPaths=coverage.xml -Dsonar.qualitygate.wait=true -Dsonar.token=\$SONAR_AUTH_TOKEN"
          }
        }
      }
    }
  }
}
