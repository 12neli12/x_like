# X API Like Script

This script uses tweepy library to like a specific tweet. It handles authentication, API errors and rate limits.

## Necessities

Beforehand, you should have:
- Python 3 installed
- Twitter API credentials (Consumer Key, Consumer Secret, Access Token, and Access Token Secret)
- Necessary Python packages installed

## Installation

1. Clone or download this repo.
2. Navigate to the project folder:
   ```bash
   cd project_folder
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## X API Credentials

1. Go to https://developer.x.com.
2. Create a new project and generate API keys.
3. Copy the `consumer_key`, `consumer_secret`, `access_token`, and `access_token_secret` from the app details.
4. In the '.env' add the following:
   ```env
   CONSUMER_KEY=your_consumer_key_here
   CONSUMER_SECRET=your_consumer_secret_here
   ACCESS_TOKEN=your_access_token_here
   ACCESS_TOKEN_SECRET=your_access_token_secret_here
   TWEET_ID=your_tweet_id_here
   ```

## Running the Script

Run the script with:
```bash
py x_like.py
```

Modify the `.env` file to specify the `TWEET_ID` of the tweet you want to like.

## Error Handling

Exception handling for:
- Authentication failures
- Rate limits (automatically waits and retries)
- Permission errors
- Tweet not found errors

## Author
Ornel Mero

