# GitHub Webhook Receiver

This project demonstrates handling GitHub repository events using webhooks, storing minimal event data in MongoDB, and displaying recent activity via a polling UI.

## 🚀 Features

- Receives GitHub webhook events
- Handles:
  - Push events
  - Pull Request events
  - Merge events (via merged pull requests)
- Stores minimal required data in MongoDB
- Displays latest repository activity in a simple UI
- UI polls backend every 15 seconds
- Dockerized for easy setup

## 🛠 Tech Stack

- **Backend:** Python, Flask
- **Database:** MongoDB (Atlas)
- **Integration:** GitHub Webhooks
- **DevOps:** Docker
- **Tunneling:** ngrok (for local webhook testing)
