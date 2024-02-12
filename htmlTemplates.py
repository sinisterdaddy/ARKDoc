css = '''
<style>
  body {
    font-family: 'Roboto', Arial, sans-serif;
    background-color: #f7f7f7;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }

  .chat-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
  }

  .chat-message {
    max-width: 70%;
    border-radius: 1rem;
    margin-bottom: 1.5rem;
    overflow: hidden;
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  }

  .chat-message.user {
    background-color: #4caf50;
    color: #fff;
  }

  .chat-message.bot {
    background-color: #2196f3;
    color: #fff;
  }

  .chat-message .avatar {
    width: 20%;
  }

  .chat-message .avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
  }

  .chat-message .message {
    padding: 1.5rem;
    color: #333;
  }

'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://github.com/sinisterdaddy/WeChat/assets/113205807/da5198ff-9c24-4bbb-b615-fa2cf40c8d37">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
