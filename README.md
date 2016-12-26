# App Engine Blog

## Getting started

1. Install gcloud SDK

    ```
    curl https://sdk.cloud.google.com | bash
    ```

2. Login with your gcloud account

    ```
    gcloud auth login
    ```

3. Set gcloud project

    ```
    gcloud config set project <your_project>
    ```

4. Run server

    ```
    dev_appserver.py .
    ```

## Deploy

```
gcloud app deploy
```