document.getElementById("convertBtn").addEventListener("click", function () {
  const cCode = document.getElementById("cCode").value.trim();
  const pythonCodeArea = document.getElementById("pythonCode");

  if (!cCode) {
    pythonCodeArea.value = "Please enter C code to convert.";
    return;
  }

  fetch("http://localhost:5000/convert", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ code: cCode })
  })
    .then(response => response.json())
    .then(data => {
      typeEffect(pythonCodeArea, data.result || "Conversion failed.");
    })
    .catch(error => {
      pythonCodeArea.value = "Error: " + error.message;
    });
});

// Typing effect function
function typeEffect(element, text, speed = 20) {
  element.value = "";
  let i = 0;
  function typing() {
    if (i < text.length) {
      element.value += text.charAt(i);
      i++;
      setTimeout(typing, speed);
    }
  }
  typing();
}

// Copy to clipboard
document.getElementById("copyBtn").addEventListener("click", function () {
  const pythonCode = document.getElementById("pythonCode");
  pythonCode.select();
  document.execCommand("copy");
  alert("Copied to clipboard!");
});

// Dark mode toggle
document.getElementById("themeToggle").addEventListener("change", function () {
  document.body.classList.toggle("dark");
});
