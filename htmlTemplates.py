css = """
<style>
.chat-message {
    display: flex;
    align-items: flex-start;
    margin: 8px 0;
    position: relative;
}

.chat-message.user {
    justify-content: flex-end;
}

.chat-message.bot {
    justify-content: flex-start;
}

.avatar {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    margin: 0 8px;
}

.message-box {
    max-width: 70%;
    background-color: #2f2f3f;
    padding: 12px 16px;
    border-radius: 12px;
    color: white;
    font-size: 15px;
    position: relative;
    word-wrap: break-word;
}

.chat-message.user .message-box {
    background-color: #4f4f61;
    border-bottom-right-radius: 0;
}

.chat-message.bot .message-box {
    background-color: #2f2f3f;
    border-bottom-left-radius: 0;
}

/* Copy and like buttons */
.action-buttons {
    position: absolute;
    top: 4px;
    right: 6px;
    display: flex;
    gap: 6px;
}

.copy-btn,
.like-btn {
    font-size: 13px;
    background: none;
    border: none;
    color: #ccc;
    cursor: pointer;
    display: none;
}

.message-box:hover .copy-btn,
.message-box:hover .like-btn {
    display: inline;
}

.copy-btn:hover,
.like-btn:hover {
    color: white;
}
</style>
"""

user_template = """
<div class="chat-message user">
    <div class="message-box">
        {{MSG}}
    </div>
    <img class="avatar" src="https://i.ibb.co/0jqHpnp/user-icon.png" />
</div>
"""

bot_template = """
<div class="chat-message bot">
    <img class="avatar" src="https://i.ibb.co/vX5V1cG/robot-icon.png" />
    <div class="message-box">
        {{MSG}}
    </div>
</div>
"""

# layout_css = """
# <style>
# /* Fix header to top */
# header[data-testid="stHeader"] {
#     position: fixed;
#     top: 0;
#     width: 100%;
#     background-color: #0e1117;
#     z-index: 999;
#     border-bottom: 1px solid #444;
# }
#
# /* Push content down so it's not hidden under fixed header */
# main[data-testid="stAppViewContainer"] > section {
#     padding-top: 4rem;
# }
#
# /* Widen central content */
# section.main {
#     max-width: 90%;
#     margin: 0 auto;
# }
#
# /* Optional: remove Streamlit's default padding */
# .block-container {
#     padding-left: 1rem;
#     padding-right: 1rem;
# }
# </style>
# """


# scroll_and_copy_js = """
# <script>
# function copyText(btn) {
#     const text = btn.parentElement.parentElement.innerText
#         .replace("📋", "")
#         .replace("👍", "").trim();
#     navigator.clipboard.writeText(text);
#     btn.innerText = "✅";
#     setTimeout(() => { btn.innerText = "📋"; }, 1200);
# }
#
# function likeText(btn) {
#     btn.innerText = "❤️";
#     setTimeout(() => { btn.innerText = "👍"; }, 1500);
# }
#
# // Scroll to bottom
# window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
# </script>
# """
