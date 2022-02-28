# An rclone bot to upload and transfer to many cloud servers, made by @SamMax009

Contact: [Telegram](https://t.me/SamMax009)

    - Upload telegram files to cloud.
    - Transfer from cloud to cloud.
    - Renaming of files.
    - Menu to list clouds from rclone.conf and selection of folders and files.
    - Progress bar when downloading and uploading.

## Commands for bot(set through @BotFather) 
- upload - upload to selected cloud 
- copy - copy from cloud to cloud
- conf - config rclone and set upload folder 
- logs - get logs from server
- clean- clean downloads

    
## Deploy With Github Workflow

   1- Go to Repository Settings -> Secrets 

   2- Add the below Required Variables one by one by clicking New Repository Secret every time.

    HEROKU_EMAIL: Heroku Account Email 
    HEROKU_API_KEY: Your Heroku API key
    HEROKU_APP_NAME: Your Heroku app name (unique)
    CONFIG_FILE_URL: Copy This in any text editor. Go to https://gist.github.com and paste your config data. Rename the file to config.env and then create secret gist. Click on Raw, copy the link. This will be your CONFIG_FILE_URL.

   3- After adding all the above Required Variables go to Github Actions tab in your repository. Select Manually Deploy to Heroku workflow.

  


