function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div><b>You:</b> ${userInput}</div>`;
    document.getElementById("user-input").value = "";

    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({message: userInput}),
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<div><b>Bot:</b> ${data.answer}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => console.error('Error:', error));
}
