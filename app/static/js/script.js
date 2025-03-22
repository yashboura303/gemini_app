document.addEventListener("DOMContentLoaded", function () {
  const chatForm = document.getElementById("chat-form");
  const promptInput = document.getElementById("prompt-input");
  const chatMessages = document.getElementById("chat-messages");
  const cancelBtn = document.getElementById("cancel-btn");

  // Function to add a message to the chat
  function addMessage(content, type) {
    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${type}`;

    const messageContent = document.createElement("p");
    messageContent.textContent = content;

    messageDiv.appendChild(messageContent);
    chatMessages.appendChild(messageDiv);

    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Function to show loading animation
  function showLoading() {
    const loadingDiv = document.createElement("div");
    loadingDiv.className = "loading";
    loadingDiv.id = "loading-indicator";

    for (let i = 0; i < 3; i++) {
      const dot = document.createElement("div");
      dot.className = "loading-dot";
      loadingDiv.appendChild(dot);
    }

    chatMessages.appendChild(loadingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Function to hide loading animation
  function hideLoading() {
    const loadingIndicator = document.getElementById("loading-indicator");
    if (loadingIndicator) {
      loadingIndicator.remove();
    }
  }

  // Handle form submission
  chatForm.addEventListener("submit", async function (e) {
    e.preventDefault();

    const userPrompt = promptInput.value.trim();
    if (!userPrompt) return;

    // Add user message to chat
    addMessage(userPrompt, "user");

    // Clear input
    promptInput.value = "";

    // Show loading animation
    showLoading();

    try {
      // Send request to backend
      const response = await fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: userPrompt }),
      });

      const data = await response.json();

      // Hide loading animation
      hideLoading();

      if (response.ok) {
        // Add AI response to chat
        addMessage(data.response, "ai");
      } else {
        // Add error message to chat
        addMessage(`Error: ${data.error || "Something went wrong"}`, "system");
      }
    } catch (error) {
      // Hide loading animation
      hideLoading();

      // Add error message to chat
      addMessage(`Error: ${error.message}`, "system");
    }
  });

  // Handle cancel button
  cancelBtn.addEventListener("click", function () {
    promptInput.value = "";
    promptInput.focus();
  });

  // Focus on input when page loads
  promptInput.focus();
});
