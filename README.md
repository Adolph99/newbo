# Heroku Deploy


## Deploy With Github Workflow

1. Go to Repository Settings -> Secrets 

2. Add the below Mandatory Variables one by one (clicking New Repository Secret)

    - HEROKU_EMAIL: Heroku Account Email 
    - HEROKU_API_KEY: Your Heroku API key
    - HEROKU_APP_NAME: Your Heroku app name (unique)
    - CONFIG_FILE_URL: Copy the sample_config.env content and paste in any text editor. Go to https://gist.github.com and paste your config data and fill mandatory variables. Rename the file to config.env and then create secret gist. Click on Raw, copy the link: this link will be your CONFIG_FILE_URL.

3. After that go to Github Actions tab in your repository. Select Manually Deploy to Heroku workflow.

4. Choose heroku branch then click on Run workflow



  


