# App Engine Blog

## Getting started

1. Install gcloud SDK

    ```
    curl https://sdk.cloud.google.com | bash
    ```

2. Run server

    ```
    dev_appserver.py .
    ```

3. Open 

    ```
    localhost:8080
    ```


## Deploy

1. Login with your gcloud account

    ```
    gcloud auth login
    ```

2. Set gcloud project

    ```
    gcloud config set project <your_project>
    ```

3. Deploy

    ```
    gcloud app deploy
    ```

4. View results

    ```
    gcloud app browse
    ```