```
# AIAssist Connect

AIAssist Connect is a web platform that serves as an intermediation platform between experts in Artificial Intelligence (AI) tools and small business entrepreneurs or individuals on a small scale. It aims to provide practical assistance in the design, implementation, and administration of projects through the application of technology and innovation.

## Features

- **AI Virtual Assistant**: An artificial intelligence-based virtual assistant provides initial guidance to users, answers frequently asked questions, and directs visitors to appropriate resources.
- **Automated Notifications**: Email or SMS notifications are automatically sent to users about important updates such as scheduling changes, new services, etc.
- **Automatic Consultancy Scheduling**: Integrate an automatic scheduling system so that entrepreneurs can schedule consultations with AI experts according to their availability.
- **User Management**: Allows user administration, including adding, editing, and removing users.
- **Social Media Integration**: A section in the admin panel to manage and schedule social media posts, promoting events, webinars, or sharing success stories.
- **Content Management**: Provides an easy-to-use interface for adding, editing, and removing content from the website.

## Project Structure

```
AIAssist_Connect_Project/
├── aiassist_connect/                 # Django project directory
├── core/                             # Core Django app for common functionalities
├── users/                            # Django app for user management
├── chatbot/                          # Django app for Dialogflow integration
├── notifications/                    # Django app for Twilio integration
├── admin_panel/                      # Django app for admin panel functionalities
├── static/                           # Directory for static files (CSS, JS, images)
├── templates/                        # Directory for HTML templates
├── media/                            # Directory for user-uploaded media files
├── manage.py                         # Django's command-line utility for administrative tasks
└── requirements.txt                  # List of Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.x
- Django

### Installation

1. Clone the repository:

```
git clone <repository-url>
cd AIAssist_Connect_Project
```

2. Create and activate a virtual environment:

```
python3 -m venv env
source env/bin/activate   # On Windows, use env\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Apply database migrations:

```
python manage.py migrate
```

### Running the Server

Start the Django development server:

```
python manage.py runserver
```

The server will start running at `http://localhost:8000`.

Create a new account
To access the admin dashboard use:
username - admin
password - Mchafuziarts189

## Modifying AI Codes

To modify the AI codes and train the Assistant:

1. Navigate to the `chatbot` app directory:

```
cd chatbot
```

2. Modify the logic for generating bot responses in the `views.py` file:

```python
# Modify the generate_bot_response function to train the assistant with desired logic
```

3. Test the changes by sending messages through the chat interface and observing the bot's responses.

## Issues

For any issues or questions, please contact amukoahdavid@gmail.com.

--- 
```